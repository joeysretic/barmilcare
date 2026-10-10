"""Audit every marketing page from built HTML. Standard library only.

Keyword checks test the presence of topic words in each meaningful field,
allowing natural grammar and word order. They are not ranking predictions
or substitutes for the recorded manual intent/readability review.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
from collections import Counter
import argparse, gzip, hashlib, itertools, json, re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Node:
    def __init__(self, tag='', attrs=None, parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs or []), parent, []
    def nodes(self, tag=None):
        for n in self.children:
            if isinstance(n, Node):
                if tag is None or n.tag == tag: yield n
                yield from n.nodes(tag)
    def has_class(self, name): return name in self.attrs.get('class','').split()
    def text(self, exclude=()):
        if self.tag in {'script','style','svg'} or any(self.has_class(c) for c in exclude): return ''
        return ' '.join(' '.join(c.text(exclude) if isinstance(c,Node) else c for c in self.children).split())

class Document(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.root=Node('document'); self.current=self.root; self.feed(html)
    def handle_starttag(self, tag, attrs):
        n=Node(tag,attrs,self.current);self.current.children.append(n)
        if tag not in VOID:self.current=n
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag,attrs)
        if tag not in VOID:self.handle_endtag(tag)
    def handle_endtag(self, tag):
        p=self.current
        while p.parent:
            if p.tag==tag:self.current=p.parent;return
            p=p.parent
    def handle_data(self, data):self.current.children.append(data)

def tokens(text):
    words=re.findall(r'[a-z0-9]+',text.lower().replace('&',' and '))
    aliases={'services':'service','providers':'provider','skills':'skill','tasks':'task','activities':'activity','areas':'area','supports':'support'}
    return [aliases.get(w,w) for w in words if w not in {'in','and','for','the','of','with','our','your','to','about'}]

def has_topic(phrase, text):return set(tokens(phrase)).issubset(set(tokens(text)))

def audit(dist, targets, preview):
    pages={};results=[];errors=[];warnings=[];links_checked=0
    for target in targets:
        route=target['path'];file=dist/route.strip('/')/'index.html'
        html=file.read_text();doc=Document(html).root;main=next(doc.nodes('main'))
        nodes=list(doc.nodes()); mainnodes=list(main.nodes())
        title=next(doc.nodes('title')).text();meta={n.attrs.get('name',n.attrs.get('property')):n.attrs.get('content') for n in doc.nodes('meta')}
        canonical=[n.attrs.get('href') for n in doc.nodes('link') if n.attrs.get('rel')=='canonical']
        hs=[n for n in mainnodes if n.tag in ('h1','h2','h3','h4','h5','h6')]
        h1s=[n.text() for n in hs if n.tag=='h1'];last=0;skips=[]
        for h in hs:
            level=int(h.tag[1])
            if last and level>last+1:skips.append(f'{last} to {level}: {h.text()}')
            last=level
        intro=next((n.text() for n in mainnodes if n.tag=='p' and n.has_class('lead')),'')
        core=main.text(('breadcrumbs','sidebar','service-grid','actions','hero-caption'))
        body=main.text(('breadcrumbs','sidebar','service-grid','actions','hero','page-hero','hero-caption'))
        imgs=[n.attrs for n in doc.nodes('img')]
        schemas=[]
        for n in doc.nodes('script'):
            if n.attrs.get('type')=='application/ld+json':schemas.append(json.loads(''.join(c for c in n.children if isinstance(c,str))))
        graph=schemas[0].get('@graph',[]) if schemas else []
        schema_types=[n.get('@type') for n in graph]
        graph_ids=[n.get('@id') for n in graph if n.get('@id')]
        entity=next((n for n in graph if n.get('@type')=='Organization'),{})
        webpage=next((n for n in graph if n.get('@type')=='WebPage'),{})
        service_schema=next((n for n in graph if n.get('@type')=='Service'),{})
        expected='https://barmilcareservices.com.au'+route
        required=target['primary_check']
        checks={
            'primary_title':has_topic(required,title),'primary_h1':bool(h1s) and has_topic(required,h1s[0]),
            'primary_intro':has_topic(required,intro),'primary_body':has_topic(target.get('body_check',required),body),
            'one_h1':len(h1s)==1,'heading_order':not skips,
            'meta_description':bool(meta.get('description')),
            'canonical':canonical==[expected],
            'robots':('noindex' in meta.get('robots','')) if preview else ('noindex' not in meta.get('robots','') and 'index' in meta.get('robots','')),
            'image_alts':all('alt' in i and (i['alt'] or i.get('src','').endswith('barmil-logo.png')) and not i.get('alt','').startswith('Illustrative scene') for i in imgs),
            'image_dimensions':all(i.get('width') and i.get('height') for i in imgs),
            'canberra_in_main':'canberra' in core.lower(),
            'schema_json':bool(schemas) and {'Organization','WebSite','WebPage'}.issubset(set(schema_types)),
            'service_schema':not route.startswith('/services/') or 'Service' in schema_types,
            'schema_consistency':len(graph_ids)==len(set(graph_ids)) and webpage.get('url')==expected and entity.get('name')=='Barmil Care Services' and (not service_schema or (service_schema.get('url')==expected and service_schema.get('provider',{}).get('@id')==entity.get('@id'))),
            'cta':any(n.attrs.get('href','').startswith(('tel:','mailto:')) or n.attrs.get('href')=='/contact' for n in doc.nodes('a')),
        }
        for key,passed in checks.items():
            if not passed:errors.append({'path':route,'check':key})
        secondaries=[{'keyword':s['keyword'],'natural_form':s['natural_form'],'present':has_topic(s['check'],core),'note':s.get('note','')} for s in target['secondary']]
        for s in secondaries:
            if not s['present']:errors.append({'path':route,'check':'secondary','keyword':s['keyword']})
        internal=[n.attrs['href'] for n in main.nodes('a') if n.attrs.get('href','').startswith('/')]
        rec={**target,'title':title,'title_chars':len(title),'description':meta.get('description',''),'description_chars':len(meta.get('description','')),
             'h1':h1s[0] if h1s else '', 'intro':intro,'word_count':len(core.split()),'visible_main_words':len(main.text(('breadcrumbs',)).split()),'headings':[[h.tag,h.text()] for h in hs],
             'secondary_results':secondaries,'checks':checks,'heading_skips':skips,'internal_links':sorted(set(internal)),
             'images':imgs,'schema_types':schema_types,'canonical':canonical,'robots':meta.get('robots',''),
             'html_bytes':len(html.encode()),'html_gzip_bytes':len(gzip.compress(html.encode()))}
        results.append(rec);pages[route]={'doc':doc,'core':core,'ids':{n.attrs['id'] for n in nodes if 'id' in n.attrs}}
    duplicates={}
    for field in ['title','description','h1']:
        counts=Counter(r[field] for r in results);duplicates[field]=[k for k,v in counts.items() if v>1]
        if duplicates[field]:errors.append({'check':'duplicate_'+field,'values':duplicates[field]})
    for route,p in pages.items():
        for n in p['doc'].nodes():
            values=[]
            if n.tag=='a':values.append(n.attrs.get('href',''))
            if n.tag in ('script','img'):values.append(n.attrs.get('src',''))
            if n.tag=='link' and n.attrs.get('rel') in ('stylesheet','icon','preload','apple-touch-icon'):values.append(n.attrs.get('href',''))
            for value in values:
                u=urlparse(value)
                if not value or u.scheme or u.netloc:continue
                path=unquote(u.path) or route
                if path in pages:
                    if u.fragment and u.fragment not in pages[path]['ids']:errors.append({'path':route,'check':'anchor','target':value})
                elif not (dist/path.lstrip('/')).is_file() and not (dist/path.lstrip('/')/'index.html').is_file():errors.append({'path':route,'check':'broken_link','target':value})
                links_checked+=1
    sims=[]
    for (a,pa),(b,pb) in itertools.combinations(pages.items(),2):
        def shingles(t):
            w=tokens(t);return {tuple(w[i:i+5]) for i in range(max(0,len(w)-4))}
        sa=shingles(pa['core']);sb=shingles(pb['core']);union=sa|sb;similarity=len(sa&sb)/len(union) if union else 0
        if pa['core']==pb['core']:errors.append({'check':'duplicate_main_content','pages':[a,b]})
        sims.append({'pages':[a,b],'shared_5word_ratio':round(similarity,3)})
    urls=[n.text for n in ET.parse(dist/'sitemap.xml').getroot().findall('{*}url/{*}loc')]
    expected_urls=[] if preview else ['https://barmilcareservices.com.au'+r['path'] for r in results]
    if sorted(urls)!=sorted(expected_urls):errors.append({'check':'sitemap_indexability','expected':len(expected_urls),'actual':len(urls)})
    robots=(dist/'robots.txt').read_text()
    if ('Disallow: /\n' in robots)!=preview:errors.append({'check':'robots_file'})
    css=(dist/'styles.css').read_text();assets=set(re.findall(r"url\(['\"]?(/assets/[^)'\"]+)",css))
    for a in assets:
        if not (dist/a.lstrip('/')).is_file():errors.append({'check':'css_asset','target':a})
    for filename in ['404/index.html','thank-you/index.html','netlify-forms.html']:
        d=Document((dist/filename).read_text()).root
        if not any(n.attrs.get('name')=='robots' and 'noindex' in n.attrs.get('content','') for n in d.nodes('meta')):errors.append({'check':'utility_noindex','path':filename})
    headers=(dist/'_headers').read_text().split('/assets/*')[0]
    if ('X-Robots-Tag: noindex' in headers)!=preview:errors.append({'check':'global_x_robots_header'})
    if len({tuple(sorted(set(tokens(t['primary_check'])))) for t in targets})!=len(targets):errors.append({'check':'duplicate_primary_assignment'})
    fonts=[p for p in (dist/'assets').iterdir() if p.suffix in ('.ttf','.woff','.woff2')]
    mainhashes=Counter(hashlib.sha256(p['core'].encode()).hexdigest() for p in pages.values())
    return {'mode':'private-preview' if preview else 'production-build-check','page_count':len(results),'service_count':sum(r['path'].startswith('/services/') for r in results),
            'pages':results,'errors':errors,'warnings':warnings,'duplicates':duplicates,'duplicate_main_bodies':sum(v-1 for v in mainhashes.values()),
            'internal_references_checked':links_checked,'sitemap_urls':urls,'robots_txt':robots,
            'most_similar_pairs':sorted(sims,key=lambda x:x['shared_5word_ratio'],reverse=True)[:12],
            'performance':{'css_bytes':len(css.encode()),'js_bytes':(dist/'app.js').stat().st_size,'font_bytes':sum(p.stat().st_size for p in fonts),'font_files':[p.name for p in fonts],
                           'max_html_bytes':max(r['html_bytes'] for r in results),'max_html_gzip_bytes':max(r['html_gzip_bytes'] for r in results),'browser_metrics':'Unverified: supported browser QA is unavailable; private preview is not publicly crawlable.'},
            'mobile_source_checks':{'viewport_all_pages':all(any(n.attrs.get('name')=='viewport' and 'width=device-width' in n.attrs.get('content','') for n in p['doc'].nodes('meta')) for p in pages.values()),
                                    'responsive_breakpoints':'max-width:850px' in css and 'max-width:540px' in css,'reduced_motion':'prefers-reduced-motion' in css,'browser_visual_qa':'Unverified'}}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--directory',default=str(ROOT/'dist'));ap.add_argument('--output',default=str(ROOT/'seo-audit.json'));ap.add_argument('--production',action='store_true');ap.add_argument('--baseline',action='store_true');a=ap.parse_args()
    result=audit(Path(a.directory),json.loads((ROOT/'seo-targets.json').read_text()),not a.production)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps({k:result[k] for k in ('mode','page_count','service_count','errors','internal_references_checked','performance')},ensure_ascii=False))
    if result['errors'] and not a.baseline:raise SystemExit(1)
