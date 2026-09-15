/**
 * Grand Cayman Shore Excursion — Workers Assets entry (Phase 32B).
 * Canonical: apex HTTPS, extensionless, no trailing slash.
 * Ship-schedule uses the same no-slash form (CF drop-trailing-slash compatible).
 * www → apex; .html → extensionless; HTTP → HTTPS.
 * Real 404 — never soft-home.
 */
const APEX_HOST = 'grandcaymanshoreexcursion.com';

const LEGACY_REDIRECTS = {
  '/index': '/',
  '/index.html': '/',
};

function toCanonicalPath(pathname) {
  let path = pathname || '/';
  if (path.toLowerCase().endsWith('.html')) {
    path = path.slice(0, -5);
    if (path.toLowerCase().endsWith('/index')) path = path.slice(0, -6);
    if (path === '' || path === '/index') path = '/';
  }
  if (path.length > 1 && path.endsWith('/')) {
    path = path.replace(/\/+$/, '') || '/';
  }
  return path || '/';
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();
    const isWww = host === `www.${APEX_HOST}`;
    const isHttp = url.protocol === 'http:';
    const rawPath = url.pathname || '/';
    const rawLower = rawPath.toLowerCase();
    const hasHtml = rawLower.endsWith('.html');
    const is404Doc = rawLower === '/404.html' || rawLower === '/404';
    const hasTrail =
      rawPath.length > 1 && rawPath.endsWith('/') && !rawPath.includes('.');

    const legacyTarget = LEGACY_REDIRECTS[rawLower] || LEGACY_REDIRECTS[rawPath];
    if (legacyTarget && !is404Doc) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      dest.pathname = legacyTarget;
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    // Block fragment / source exposure explicitly
    if (
      rawLower.startsWith('/content/') ||
      rawLower === '/content' ||
      rawLower.startsWith('/partials/') ||
      rawLower === '/partials' ||
      rawLower.startsWith('/scripts/') ||
      rawLower === '/scripts' ||
      rawLower.includes('destination.config.json') ||
      rawLower.endsWith('.py') ||
      rawLower.endsWith('.mjs') ||
      rawLower === '/package.json' ||
      rawLower === '/wrangler.jsonc' ||
      rawLower === '/.gitignore' ||
      rawLower.startsWith('/data/')
    ) {
      const notFound = await env.ASSETS.fetch(new URL('/404.html', url.origin));
      return new Response(notFound.body, {
        status: 404,
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'no-store',
        },
      });
    }

    if ((isWww || isHttp || hasHtml || hasTrail) && !is404Doc) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      dest.pathname = toCanonicalPath(rawPath);
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    if (isWww || isHttp) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    const assetResponse = await env.ASSETS.fetch(request);

    if (assetResponse.status === 404) {
      const notFound = await env.ASSETS.fetch(new URL('/404.html', url.origin));
      return new Response(notFound.body, {
        status: 404,
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'no-store',
        },
      });
    }

    return assetResponse;
  },
};
