const mobileButton=document.querySelector('.mobile-toggle');
const nav=document.querySelector('.main-nav');
const servicesButton=document.querySelector('.dropdown-toggle');
const servicesMenu=document.querySelector('.dropdown');
function closeServices(){if(servicesMenu){servicesMenu.hidden=true;servicesButton.setAttribute('aria-expanded','false')}}
function closeMobile(){nav?.classList.remove('is-open');mobileButton?.setAttribute('aria-expanded','false')}
mobileButton?.addEventListener('click',()=>{const open=mobileButton.getAttribute('aria-expanded')!=='true';mobileButton.setAttribute('aria-expanded',String(open));nav.classList.toggle('is-open',open);if(!open)closeServices()});
servicesButton?.addEventListener('click',()=>{const open=servicesButton.getAttribute('aria-expanded')!=='true';servicesButton.setAttribute('aria-expanded',String(open));servicesMenu.hidden=!open});
document.addEventListener('click',event=>{if(!event.target.closest('.nav-service'))closeServices();if(!event.target.closest('.site-header'))closeMobile()});
document.addEventListener('keydown',event=>{if(event.key==='Escape'){const wasOpen=servicesButton?.getAttribute('aria-expanded')==='true';closeServices();closeMobile();if(wasOpen)servicesButton.focus()}});
document.querySelectorAll('.filter').forEach(button=>button.addEventListener('click',()=>{const category=button.dataset.category;document.querySelectorAll('.filter').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));let count=0;document.querySelectorAll('.service-grid.filterable .service-card').forEach(card=>{card.hidden=category!=='All services'&&card.dataset.category!==category;if(!card.hidden)count++});const status=document.querySelector('#filter-status');if(status)status.textContent=`${count} services shown`;}));
window.matchMedia('(min-width:851px)').addEventListener('change',()=>{closeMobile();closeServices()});
const enquiryForm=document.querySelector('form[name="contact"]');
window.barmilTurnstileReady=()=>{};
window.barmilTurnstileExpired=()=>{const status=enquiryForm?.querySelector('.form-status');if(status)status.textContent='Please complete the security verification again.'};
enquiryForm?.addEventListener('submit',async event=>{
 event.preventDefault();if(!enquiryForm.reportValidity())return;
 const button=enquiryForm.querySelector('button[type="submit"]');const status=enquiryForm.querySelector('.form-status');
 if(button.disabled)return;
 const data=new FormData(enquiryForm);
 if(enquiryForm.id==='barmil-enquiry'&&!data.get('cf-turnstile-response')){status.textContent='Please complete the security verification before sending.';return;}
 button.disabled=true;status.textContent='Sending your enquiry…';
 try{
  const response=await fetch(enquiryForm.action,{method:'POST',body:data,headers:{'Accept':'application/json'}});
  const result=await response.json().catch(()=>({}));
  if(!response.ok)throw new Error(result.error||'Your enquiry could not be sent.');
  window.location.assign('/thank-you');
 }catch(error){status.textContent=error.message||'Unable to send your enquiry. Please try again or call Barmil.';button.disabled=false;
  if(window.turnstile)window.turnstile.reset();
 }
});
