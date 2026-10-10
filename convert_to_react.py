from pathlib import Path
import json, re, shutil, subprocess
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parent
# Convert production HTML output to editable React page content, retaining metadata and pre-rendered HTML.
source=root/'dist'
pages={}
for file in sorted(source.rglob('*.html')):
    if file.name=='netlify-forms.html': continue
    relative=file.relative_to(source)
    soup=BeautifulSoup(file.read_text(), 'html.parser')
    if not soup.body:continue
    route='/' if str(relative)=='index.html' else '/'+str(relative.parent).replace('\\','/')
    if relative.name=='404.html':route='/404'
    inner=''.join(str(c) for c in soup.body.contents if getattr(c,'name',None)!='script')
    pages[route]={'html':inner,'title':soup.title.get_text() if soup.title else ''}
(root/'src').mkdir(exist_ok=True)
(root/'src/pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
print('Converted',len(pages),'routes into React content data')
