"""Validate deployable pages, sitemap and local references without a browser."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,xml.etree.ElementTree as ET,re
ROOT=Path(__file__).resolve().parent; DIST=ROOT/'dist'
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.h1=0;self.links=[];self.ids=set();self.meta={};self.canonical=[];self.scripts=[];self.inschema=False;self.schema='';self.intitle=False;self.title=''
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if 'id' in a:self.ids.add(a['id'])
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag in ('img','script') and a.get('src'):self.links.append(a['src'])
  if tag=='img':assert 'alt' in a,'Missing image alt'
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='link' and a.get('rel') in ('stylesheet','preload','icon','apple-touch-icon'):self.links.append(a['href'])
  if tag=='meta':self.meta[a.get('name',a.get('property'))]=a.get('content')
  if tag=='script' and a.get('type')=='application/ld+json':self.inschema=True;self.schema=''
  if tag=='title':self.intitle=True
 def handle_endtag(self,tag):
  if tag=='script' and self.inschema:self.scripts.append(json.loads(self.schema));self.inschema=False
  if tag=='title':self.intitle=False
 def handle_data(self,data):
  if self.inschema:self.schema+=data
  if self.intitle:self.title+=data
pages={};titles=[];descs=[]
for path in DIST.rglob('index.html'):
 route='/'+str(path.parent.relative_to(DIST)).replace('\\','/');route='/' if route=='/.' else route
 p=Page();p.feed(path.read_text());pages[route]=p
 assert p.h1==1,(route,'H1 count',p.h1)
 assert p.meta.get('description'),(route,'description')
 assert len(p.canonical)==1 and p.canonical[0]=='https://barmilcareservices.com.au'+route,(route,'canonical')
 assert p.scripts,(route,'structured data')
 assert 'Australia-wide' not in path.read_text() and 'registered-style' not in path.read_text(),(route,'old copy')
 titles.append(p.title);descs.append(p.meta['description'])
assert len(titles)==len(set(titles)),'Duplicate titles'
assert len(descs)==len(set(descs)),'Duplicate descriptions'
refs=0
for route,p in pages.items():
 for url in p.links:
  u=urlparse(url)
  if u.scheme or u.netloc:continue
  target=unquote(u.path) or route
  if target in pages:
   if u.fragment:assert u.fragment in pages[target].ids,(route,'broken anchor',url)
  else:assert (DIST/target.lstrip('/')).is_file(),(route,'missing asset or route',url)
  refs+=1
urls=[n.text for n in ET.parse(DIST/'sitemap.xml').getroot().findall('{*}url/{*}loc')]
preview='Disallow: /' in (DIST/'robots.txt').read_text()
expected_urls=0 if preview else 18
assert len(urls)==expected_urls and len(set(urls))==expected_urls,'Sitemap page count'
assert all(u.startswith('https://barmilcareservices.com.au/') for u in urls),'Non-absolute sitemap'
assert all(urlparse(u).path in pages for u in urls),'Sitemap route missing'
assert len([r for r in pages if r.startswith('/services/')])==10
for r,p in pages.items():
 if r.startswith('/services/'):
  assert any(x.get('@type')=='Service' for x in p.scripts[0]['@graph']),(r,'Service schema')
css=(DIST/'styles.css').read_text()
for asset in re.findall(r"url\(['\"]?(/assets/[^)'\"]+)",css):assert (DIST/asset.lstrip('/')).exists(),('CSS asset',asset)
result={'marketing_pages':18,'service_pages':10,'internal_links_and_asset_references_checked':refs,'unique_titles':len(titles),'unique_descriptions':len(descs),'absolute_sitemap_urls':len(urls),'structured_data_json':'valid','browser_qa':'not available','contact_delivery':'not tested','mode':'preview' if 'Disallow: /' in (DIST/'robots.txt').read_text() else 'production'}
(ROOT/'validation.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
