// Cloudflare Pages Function. Deploy this source-level /functions directory alongside /dist.
const ALLOWED_SERVICES = new Set([
  "Daily Tasks & Shared Living",
  "Accommodation & Tenancy",
  "Household Tasks",
  "Life Stage & Transition Support",
  "Travel & Transport Assistance",
  "Group & Centre Activities",
  "Personal Activities & Care",
  "Development of Life Skills",
  "Innovative Community Participation",
  "Social & Community Participation"
]);
const reply = (status, error) => Response.json({ok: false, error}, {status, headers: {'Cache-Control':'no-store'}});
const clean = (value, max) => typeof value === 'string' ? value.trim().slice(0, max + 1) : '';
const emailOk = value => /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(value) && value.length <= 254;
const escapeHtml = value => value.replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
async function rateLimit(env, ip) {
  // A Cloudflare rate limiting binding offers an atomic, per-key gate.
  // Configure ENQUIRY_RATE_LIMIT in Cloudflare dashboard / wrangler configuration.
  if (!env.ENQUIRY_RATE_LIMIT || typeof env.ENQUIRY_RATE_LIMIT.limit !== 'function') return null;
  const {success} = await env.ENQUIRY_RATE_LIMIT.limit({key: ip});
  return success;
}
export async function onRequestPost({request, env}) {
  if (!env.RESEND_API_KEY || !env.TURNSTILE_SECRET_KEY || !env.RESEND_FROM || !env.ENQUIRY_TO)
    return reply(503, 'Enquiries are temporarily unavailable. Please contact Barmil by phone or email.');
  if (Number(request.headers.get('content-length') || 0) > 20000) return reply(413, 'The enquiry is too large.');
  const origin = request.headers.get('Origin');
  if (origin && origin !== new URL(request.url).origin) return reply(403, 'Request origin is not allowed.');
  const type = request.headers.get('content-type') || '';
  if (!type.includes('multipart/form-data') && !type.includes('application/x-www-form-urlencoded')) return reply(415, 'Unsupported form format.');
  let form;
  try { form = await request.formData(); } catch { return reply(400, 'Invalid form data.'); }
  if (clean(form.get('company_website'), 200)) return Response.json({ok:true}); // Honeypot: accept silently, never send.
  const name=clean(form.get('name'),120), email=clean(form.get('email'),254), phone=clean(form.get('phone'),40),
        suburb=clean(form.get('suburb'),100), service=clean(form.get('service'),150), message=clean(form.get('message'),5000);
  if (!name || name.length > 120 || !emailOk(email) || !message || message.length > 5000 || phone.length > 40 || suburb.length > 100 ||
      service.length > 150 || (service && !ALLOWED_SERVICES.has(service)) || form.get('consent') !== 'yes')
    return reply(400, 'Please check the required fields and try again.');
  const token=clean(form.get('cf-turnstile-response'),2048);
  if (!token || token.length > 2048) return reply(400, 'Security verification is required.');
  const ip=request.headers.get('CF-Connecting-IP') || 'unknown';
  const verification=new FormData();verification.set('secret',env.TURNSTILE_SECRET_KEY);verification.set('response',token);
  if(ip!=='unknown')verification.set('remoteip',ip);
  let valid=false;
  try {
    const response=await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify',{method:'POST',body:verification});
    const result=await response.json();
    const allowedHosts=(env.TURNSTILE_ALLOWED_HOSTNAMES||'').split(',').map(x=>x.trim()).filter(Boolean);
    valid=response.ok && result.success === true && (allowedHosts.length===0 || allowedHosts.includes(result.hostname));
  } catch { return reply(503,'Security verification is temporarily unavailable. Please try again later.'); }
  if(!valid) return reply(403,'Security verification failed. Please refresh and try again.');
  let allowed;
  try { allowed=await rateLimit(env,ip); } catch { return reply(503,'Please try again shortly.'); }
  if(allowed===false) return reply(429,'Too many enquiries. Please wait before trying again.');
  const fields=[['Name',name],['Email',email],['Phone',phone],['Service',service],['Canberra suburb',suburb],['Message',message]];
  const html='<h2>New Barmil Care Services enquiry</h2>'+fields.map(([label,value])=>`<p><strong>${escapeHtml(label)}:</strong><br>${escapeHtml(value||'Not provided').replace(/\n/g,'<br>')}</p>`).join('');
  let response;
  try {
    response=await fetch('https://api.resend.com/emails',{
      method:'POST',headers:{Authorization:`Bearer ${env.RESEND_API_KEY}`,'Content-Type':'application/json'},
      body:JSON.stringify({from:env.RESEND_FROM,to:[env.ENQUIRY_TO],reply_to:email,subject:'New Barmil website enquiry',html,
        text:fields.map(([label,value])=>`${label}: ${value||'Not provided'}`).join('\n\n')})
    });
  } catch { return reply(502,'Email service is unavailable. Please call or email Barmil.'); }
  if(!response.ok){ console.error('Resend returned status',response.status); return reply(502,'Unable to send your enquiry. Please call or email Barmil.'); }
  return Response.json({ok:true},{headers:{'Cache-Control':'no-store'}});
}
export async function onRequestGet() { return reply(405,'Method not allowed.'); }
