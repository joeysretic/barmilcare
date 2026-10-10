from pathlib import Path
import json,re,shutil
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parent.parent
out=root/'dist'; source=root/'.audit-production'
manifest=json.loads((out/'.vite/manifest.json').read_text())
entry=manifest['index.html']['file']
for file in source.rglob('*'):
 if not file.is_file():continue
 rel=file.relative_to(source)
 if file.suffix=='.html':
  if file.name=='netlify-forms.html':continue
  soup=BeautifulSoup(file.read_text(encoding='utf-8'),'html.parser')
  if not soup.body:continue
  scripts=[str(s) for s in soup.body.find_all('script')]
  for s in soup.body.find_all('script'):s.extract()
  body=''.join(str(c) for c in soup.body.contents)
  soup.body.clear()
  wrapper=soup.new_tag('div',id='root')
  child=soup.new_tag('div',attrs={'class':'site-page'})
  child.append(BeautifulSoup(body,'html.parser'))
  wrapper.append(child)
  soup.body.append(wrapper)
  # Original interactive behaviors (mobile navigation, form submission) remain intact.
  for script in scripts:soup.body.append(BeautifulSoup(script,'html.parser'))
  entry_tag=soup.new_tag('script',type='module',src='/'+entry)
  soup.body.append(entry_tag)
  dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True)
  dest.write_text(str(soup),encoding='utf-8')
 else:
  dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(file,dest)
# Vite's hashed CSS bundle contains the original stylesheet imported in React.
# Also retain original /styles.css, which is referenced by pre-rendered pages.
print('Finished production prerender with',len(list(out.rglob('index.html'))),'index routes; Vite bundle:',entry)
