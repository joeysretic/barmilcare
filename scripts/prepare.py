from pathlib import Path
import json,os,subprocess
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parent.parent
settings=os.environ.copy()
settings.update(SITE_PREVIEW='0',FORM_BACKEND='resend',BUILD_OUTPUT_NAME='.audit-production',SITE_URL='https://barmilcareservices.com.au')
settings.setdefault('TURNSTILE_SITE_KEY','TURNSTILE_PUBLIC_SITE_KEY')
subprocess.run(['python3','build.py'],cwd=root,env=settings,check=True)
pages={}
for file in sorted((root/'.audit-production').rglob('*.html')):
 if file.name=='netlify-forms.html':continue
 relative=file.relative_to(root/'.audit-production')
 soup=BeautifulSoup(file.read_text(encoding='utf-8'),'html.parser')
 if not soup.body:continue
 route='/' if str(relative)=='index.html' else '/'+str(relative.parent).replace('\\','/')
 if relative.name=='404.html':route='/404'
 pages[route]={'html':''.join(str(c) for c in soup.body.contents if getattr(c,'name',None)!='script'),'title':soup.title.get_text() if soup.title else ''}
(root/'src/pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
print('React pages prepared:',len(pages))
