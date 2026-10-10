import React from 'react';
import { createRoot, hydrateRoot } from 'react-dom/client';
import pages from './pages.json';
import './site.css';

/**
 * Each route has its own pre-rendered, indexable HTML and metadata.
 * The original site's page markup is preserved in pages.json to avoid redesigning
 * the audited 18 pages. You can replace each page with native JSX components
 * incrementally in Bolt while keeping the same URLs and SEO tags.
 */
type PageRecord = { html: string; title: string };
const allPages = pages as Record<string, PageRecord>;
function currentPath() {
  const path = window.location.pathname.replace(/\/+$/, '') || '/';
  return allPages[path] ? path : '/404';
}
function SitePage() {
  const page = allPages[currentPath()] || allPages['/'];
  return <div className="site-page" dangerouslySetInnerHTML={{ __html: page.html }} />;
}
const mount = document.getElementById('root');
if (mount) {
  if (mount.hasChildNodes()) hydrateRoot(mount, <SitePage />);
  else createRoot(mount).render(<SitePage />);
}
