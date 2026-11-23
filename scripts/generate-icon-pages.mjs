#!/usr/bin/env node
/**
 * Streaming 134,701+ Icon HTML Page Generator (Phase 3)
 *
 * Reads Astro's compiled CSS hash from `dist/_astro/` and streams through
 * `public/chunks/v1/*.json` one shard at a time so peak RAM stays minimal.
 *
 * Usage:
 *   node scripts/generate-icon-pages.mjs --limit 500 --out dist/icons
 *   node scripts/generate-icon-pages.mjs --tarball release/iconstash-icons.tar.gz
 *   node scripts/generate-icon-pages.mjs --limit 1000 --tarball release/smoke.tar.gz
 */

import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

const ROOT = process.cwd();
const TITLE_MAX = 60;
const DESC_MAX = 158;

function escapeHtml(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function titleCase(str) {
  return String(str ?? '')
    .replace(/[-_]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

function clampDesc(str) {
  const clean = String(str).replace(/\s+/g, ' ').trim();
  if (clean.length <= DESC_MAX) return clean;
  const sliced = clean.slice(0, DESC_MAX - 1);
  const lastSpace = sliced.lastIndexOf(' ');
  return (lastSpace > 100 ? sliced.slice(0, lastSpace) : sliced) + '…';
}

export function buildIconTitle(libName, displayName) {
  const candidates = [
    `${libName} ${displayName} Icon — Free SVG & PNG Download`,
    `${libName} ${displayName} Icon — Free SVG`,
    `${displayName} Icon — ${libName} SVG`,
    `${displayName} SVG Icon`,
  ];
  for (const c of candidates) {
    if (c.length <= TITLE_MAX) return c;
  }
  return candidates[candidates.length - 1].slice(0, TITLE_MAX - 1) + '…';
}

export function buildIconDescription(libName, displayName) {
  return clampDesc(
    `Download the free ${displayName} icon from ${libName} in SVG and PNG. Set any size from 16 to 512px, pick a color, copy the code in one click. No login required.`
  );
}

export function findAstroCssHref(distDir = path.join(ROOT, 'dist')) {
  const astroDir = path.join(distDir, '_astro');
  if (fs.existsSync(astroDir)) {
    const cssFiles = fs.readdirSync(astroDir).filter((f) => f.endsWith('.css')).sort();
    const appCss = cssFiles.find((f) => f.startsWith('app.')) || cssFiles[0];
    if (appCss) return `/_astro/${appCss}`;
  }
  return '/style.css';
}

export function renderIconPageHtml(icon, ctx) {
  const {
    id,
    name,
    svgPath,
    viewBox,
    strokeWidth,
    isFill,
    libSlug,
    libName,
    license,
    npmPackage,
    category,
    style,
    related,
  } = icon;

  const displayName = titleCase(name);
  const title = buildIconTitle(libName, displayName);
  const desc = buildIconDescription(libName, displayName);
  const canonical = `https://iconstash.io/icons/${id}/`;
  const catSlug = category.toLowerCase();
  const styleSlug = style.toLowerCase();
  const conceptSlug = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const npmCmd = npmPackage ? `npm install ${npmPackage}` : `npm install @iconstash/sdk`;

  const svgAttrs = isFill
    ? `xmlns="http://www.w3.org/2000/svg" viewBox="${escapeHtml(viewBox)}" fill="currentColor" stroke="none"`
    : `xmlns="http://www.w3.org/2000/svg" viewBox="${escapeHtml(viewBox)}" fill="none" stroke="currentColor" stroke-width="${strokeWidth || 2}" stroke-linecap="round" stroke-linejoin="round"`;

  const jsonLd = JSON.stringify([
    {
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'IconStash', item: 'https://iconstash.io/' },
        { '@type': 'ListItem', position: 2, name: 'Icon libraries', item: 'https://iconstash.io/library/' },
        { '@type': 'ListItem', position: 3, name: libName, item: `https://iconstash.io/library/${libSlug}/` },
        { '@type': 'ListItem', position: 4, name: `${name} icons`, item: `https://iconstash.io/icons/${conceptSlug}-icon/` },
        { '@type': 'ListItem', position: 5, name: displayName, item: canonical },
      ],
    },
    {
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: [
        {
          '@type': 'Question',
          name: `What is the ${displayName} icon?`,
          acceptedAnswer: {
            '@type': 'Answer',
            text: `The ${displayName} icon is a ${styleSlug}-style SVG icon from the ${libName} library, categorized under ${category}.`,
          },
        },
        {
          '@type': 'Question',
          name: `Is the ${displayName} icon free to use?`,
          acceptedAnswer: {
            '@type': 'Answer',
            text: `Yes. ${libName} is licensed under ${license || 'MIT'}, making it free for personal and commercial use with no login required.`,
          },
        },
        {
          '@type': 'Question',
          name: `Can I download the ${displayName} icon as a PNG?`,
          acceptedAnswer: {
            '@type': 'Answer',
            text: `Yes. Choose any size from 16px to 512px and export the ${displayName} icon as SVG or PNG directly in your browser.`,
          },
        },
      ],
    },
    {
      '@context': 'https://schema.org',
      '@type': 'HowTo',
      name: `How to download and use the ${displayName} icon`,
      description: `Step-by-step guide to customizing and exporting the ${displayName} icon from ${libName} on IconStash.`,
      totalTime: 'PT1M',
      step: [
        { '@type': 'HowToStep', position: 1, name: 'Open the icon in IconStash', text: `Open ${displayName} from ${libName}.`, url: canonical },
        { '@type': 'HowToStep', position: 2, name: 'Customize color and size', text: 'Pick a color and pixel size from 16px to 512px.', url: canonical },
        { '@type': 'HowToStep', position: 3, name: 'Copy SVG or download PNG', text: 'Copy SVG code in one click or download a crisp PNG.', url: canonical },
      ],
    },
    {
      '@context': 'https://schema.org',
      '@type': 'SoftwareApplication',
      name: 'IconStash',
      applicationCategory: 'DesignApplication',
      operatingSystem: 'Web',
      url: 'https://iconstash.io',
      offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
    },
    {
      '@context': 'https://schema.org',
      '@type': 'ImageObject',
      name: `${displayName} icon`,
      description: `${styleSlug} style SVG icon from ${libName}`,
      creator: { '@type': 'Organization', name: libName },
      encodingFormat: 'image/svg+xml',
      contentUrl: canonical,
      license: 'https://opensource.org/licenses/MIT',
    },
  ]);

  const relatedHtml = related
    .map(
      (r) =>
        `<a class="pseo-related-card" href="/icons/${escapeHtml(r.id)}/"><span>${escapeHtml(titleCase(r.name))}</span></a>`
    )
    .join('');

  return `<!doctype html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(title)}</title>
  <meta name="description" content="${escapeHtml(desc)}">
  <link rel="canonical" href="${canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="${escapeHtml(title)}">
  <meta property="og:description" content="${escapeHtml(desc)}">
  <meta property="og:url" content="${canonical}">
  <meta property="og:image" content="https://iconstash.io/og-default.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="${escapeHtml(title)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${escapeHtml(title)}">
  <meta name="twitter:image" content="https://iconstash.io/og-default.png">
  <meta name="twitter:description" content="${escapeHtml(desc)}">
  <meta name="theme-color" content="#0A0A0A">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="${escapeHtml(ctx.cssHref)}">
  <script type="application/ld+json">${jsonLd}</script>
  <script>(function(){try{var t=localStorage.getItem('iconvault-theme')||localStorage.getItem('theme');if(t==='light'||t==='dark'){document.documentElement.setAttribute('data-theme',t);}}catch(e){}})();</script>
</head>
<body class="pseo-page">
  <div class="app-shell">
    <header id="main-header">
      <div class="header-left">
        <a class="logo" href="/" aria-label="IconStash.io home">
          <svg class="logo-icon" viewBox="0 0 24 24"><path d="M12 2 21 7v10l-9 5-9-5V7l9-5Z"/><path d="m8 9 4-2 4 2v6l-4 2-4-2V9Z"/></svg>
          <span class="logo-text">IconStash<span class="logo-io">.io</span></span>
        </a>
      </div>
      <div class="header-right">
        <a href="/" class="nav-link">Explore</a>
        <a href="/library/${escapeHtml(libSlug)}/" class="nav-link">${escapeHtml(libName)}</a>
        <a href="/category/${escapeHtml(catSlug)}/" class="nav-link">${escapeHtml(category)}</a>
        <button type="button" class="nav-link" id="ic-theme-btn">Theme</button>
      </div>
    </header>
    <main class="pseo-main" style="max-width:960px;margin:2rem auto;padding:0 1.25rem;">
      <nav aria-label="Breadcrumb" style="font-size:0.85rem;margin-bottom:1rem;opacity:0.8;">
        <a href="/">IconStash</a> / <a href="/library/${escapeHtml(libSlug)}/">${escapeHtml(libName)}</a> / <a href="/category/${escapeHtml(catSlug)}/">${escapeHtml(category)}</a> / <span>${escapeHtml(displayName)}</span>
      </nav>
      <h1>${escapeHtml(displayName)} Icon — ${escapeHtml(libName)}</h1>
      <p>${escapeHtml(desc)}</p>
      <section style="display:flex;flex-wrap:wrap;gap:1.5rem;align-items:center;margin:1.5rem 0;padding:1.5rem;border:1px solid var(--border-subtle,rgba(255,255,255,0.12));border-radius:12px;">
        <div id="ic-preview" style="width:128px;height:128px;display:flex;align-items:center;justify-content:center;color:#ffffff;">
          <svg id="ic-svg" width="96" height="96" ${svgAttrs}>${svgPath}</svg>
        </div>
        <div style="flex:1;min-width:240px;display:flex;flex-direction:column;gap:0.75rem;">
          <div style="display:flex;gap:0.75rem;align-items:center;flex-wrap:wrap;">
            <label>Color <input id="ic-color" type="color" value="#ffffff"></label>
            <label>Size <input id="ic-size" type="range" min="16" max="512" value="96"> <span id="ic-size-val">96px</span></label>
          </div>
          <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
            <button type="button" class="btn-primary" id="ic-copy">Copy SVG</button>
            <button type="button" class="btn-secondary" id="ic-dl-svg">Download SVG</button>
            <button type="button" class="btn-secondary" id="ic-dl-png">Download PNG</button>
            <a class="btn-secondary" href="/?q=${encodeURIComponent(name)}">Open in Studio</a>
          </div>
          <code style="font-size:0.8rem;opacity:0.85;">${escapeHtml(npmCmd)}</code>
        </div>
      </section>
      <section style="margin:2rem 0;">
        <h2>Icon Details</h2>
        <ul>
          <li><strong>Library:</strong> <a href="/library/${escapeHtml(libSlug)}/">${escapeHtml(libName)}</a></li>
          <li><strong>Category:</strong> <a href="/category/${escapeHtml(catSlug)}/">${escapeHtml(category)}</a></li>
          <li><strong>Style:</strong> <a href="/style/${escapeHtml(styleSlug)}/">${escapeHtml(titleCase(styleSlug))}</a></li>
          <li><strong>License:</strong> ${escapeHtml(license || 'MIT')}</li>
        </ul>
      </section>
      <section style="margin:2rem 0;">
        <h3>Related ${escapeHtml(libName)} Icons</h3>
        <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">${relatedHtml}</div>
      </section>
    </main>
  </div>
  <script>(function(){var s=document.getElementById('ic-svg'),c=document.getElementById('ic-color'),z=document.getElementById('ic-size'),zv=document.getElementById('ic-size-val'),p=document.getElementById('ic-preview');if(!s)return;c.oninput=function(){p.style.color=c.value;};z.oninput=function(){zv.textContent=z.value+'px';s.setAttribute('width',z.value);s.setAttribute('height',z.value);};document.getElementById('ic-copy').onclick=function(){var out=s.outerHTML.replace(/currentColor/g,c.value);navigator.clipboard&&navigator.clipboard.writeText(out);};document.getElementById('ic-dl-svg').onclick=function(){var b=new Blob([s.outerHTML.replace(/currentColor/g,c.value)],{type:'image/svg+xml'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download='${escapeHtml(id)}.svg';a.click();setTimeout(function(){URL.revokeObjectURL(u);},1000);};document.getElementById('ic-dl-png').onclick=function(){var sz=parseInt(z.value,10)||96,cv=document.createElement('canvas');cv.width=sz;cv.height=sz;var img=new Image(),b=new Blob([s.outerHTML.replace(/currentColor/g,c.value)],{type:'image/svg+xml'}),u=URL.createObjectURL(b);img.onload=function(){cv.getContext('2d').drawImage(img,0,0,sz,sz);URL.revokeObjectURL(u);cv.toBlob(function(pb){if(!pb)return;var pu=URL.createObjectURL(pb),a=document.createElement('a');a.href=pu;a.download='${escapeHtml(id)}-'+sz+'px.png';a.click();setTimeout(function(){URL.revokeObjectURL(pu);},1000);},'image/png');};img.src=u;};document.getElementById('ic-theme-btn').onclick=function(){var cur=document.documentElement.getAttribute('data-theme')==='light'?'dark':'light';document.documentElement.setAttribute('data-theme',cur);try{localStorage.setItem('iconvault-theme',cur);localStorage.setItem('theme',cur);}catch(e){}};})();</script>
</body>
</html>`;
}

/**
 * Minimal zero-dependency POSIX ustar tar entry encoder.
 */
function createTarHeader(fileName, byteLength) {
  const header = Buffer.alloc(512, 0);
  const nameBuf = Buffer.from(fileName, 'utf8');
  if (nameBuf.length <= 100) {
    nameBuf.copy(header, 0);
  } else {
    const slash = fileName.lastIndexOf('/', 155);
    const prefix = slash > 0 ? fileName.slice(0, slash) : '';
    const base = slash > 0 ? fileName.slice(slash + 1) : fileName.slice(-100);
    Buffer.from(base.slice(0, 100), 'utf8').copy(header, 0);
    Buffer.from(prefix.slice(0, 155), 'utf8').copy(header, 345);
  }
  header.write('0000644\0', 100, 8, 'ascii');
  header.write('0000000\0', 108, 8, 'ascii');
  header.write('0000000\0', 116, 8, 'ascii');
  header.write(byteLength.toString(8).padStart(11, '0') + '\0', 124, 12, 'ascii');
  const mtime = Math.floor(Date.now() / 1000);
  header.write(mtime.toString(8).padStart(11, '0') + '\0', 136, 12, 'ascii');
  header.fill(0x20, 148, 156);
  header.write('0', 156, 1, 'ascii');
  header.write('ustar\0', 257, 6, 'ascii');
  header.write('00', 263, 2, 'ascii');

  let checksum = 0;
  for (let i = 0; i < 512; i++) checksum += header[i];
  header.write(checksum.toString(8).padStart(6, '0') + '\0 ', 148, 8, 'ascii');
  return header;
}

async function writeChunkWithBackpressure(stream, buf) {
  if (!stream.write(buf)) {
    await new Promise((resolve) => stream.once('drain', resolve));
  }
}

export async function generateIconPages(options = {}) {
  const {
    limit = Infinity,
    outDir = null,
    tarballPath = null,
    chunksDir = path.join(ROOT, 'public/chunks/v1'),
    metaPath = path.join(ROOT, 'public/index/v1/search-meta.json'),
    distDir = path.join(ROOT, 'dist'),
  } = options;

  const manifest = JSON.parse(fs.readFileSync(path.join(chunksDir, 'manifest.json'), 'utf8'));
  const searchMeta = JSON.parse(fs.readFileSync(metaPath, 'utf8'));
  const cssHref = findAstroCssHref(distDir);

  let gzipStream = null;
  let fileOutStream = null;
  if (tarballPath) {
    fs.mkdirSync(path.dirname(tarballPath), { recursive: true });
    fileOutStream = fs.createWriteStream(tarballPath);
    gzipStream = zlib.createGzip({ level: 6 });
    gzipStream.pipe(fileOutStream);
  }
  if (outDir) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  const startMs = Date.now();
  let generated = 0;
  let totalHtmlBytes = 0;
  let peakRssBytes = process.memoryUsage().rss;

  for (let libIdx = 0; libIdx < manifest.libraries.length; libIdx++) {
    if (generated >= limit) break;
    const lib = manifest.libraries[libIdx];
    const libMeta = searchMeta.libraries[libIdx] || {};
    const libName = libMeta.name || titleCase(lib.slug);

    for (const shardFile of lib.shards) {
      if (generated >= limit) break;
      const shardRef = typeof shardFile === "string" ? shardFile : (shardFile.url || shardFile.file || "");
      const shardPath = path.join(chunksDir, path.basename(shardRef));
      const shard = JSON.parse(fs.readFileSync(shardPath, 'utf8'));
      const icons = shard.icons || [];
      const idOverrides = shard.idOverrides || {};
      const viewBoxes = shard.viewBoxes || searchMeta.viewBoxes || ['0 0 24 24'];

      for (let i = 0; i < icons.length; i++) {
        if (generated >= limit) break;
        const tuple = icons[i];
        // Tuple: [name, svgPath, viewBoxIdx, strokeIdx, flags, catIdx, styleIdx]
        const name = tuple[0];
        const svgPath = tuple[1];
        const viewBox = viewBoxes[tuple[2]] || '0 0 24 24';
        const strokeWidths = [0, 1, 1.5, 2];
        const strokeWidth = strokeWidths[tuple[3]] ?? 2;
        const flags = tuple[4] ?? 0;
        const isFill = (flags & 1) !== 0;
        const category = searchMeta.categories[tuple[5]] || 'Interface';
        const style = searchMeta.styles[tuple[6]] || 'outline';
        const id = idOverrides[String(i)] || `${lib.slug}-${name}`;

        const related = [];
        for (let r = 1; r <= 6; r++) {
          const idx = (i + r) % icons.length;
          if (idx === i) continue;
          const rName = icons[idx][0];
          related.push({ id: idOverrides[String(idx)] || `${lib.slug}-${rName}`, name: rName });
        }

        const html = renderIconPageHtml(
          {
            id,
            name,
            svgPath,
            viewBox,
            strokeWidth,
            isFill,
            libSlug: lib.slug,
            libName,
            license: libMeta.license || 'MIT',
            npmPackage: libMeta.npmPackage || '',
            category,
            style,
            related,
          },
          { cssHref }
        );

        const htmlBuf = Buffer.from(html, 'utf8');
        totalHtmlBytes += htmlBuf.length;

        if (outDir) {
          const dir = path.join(outDir, id);
          fs.mkdirSync(dir, { recursive: true });
          fs.writeFileSync(path.join(dir, 'index.html'), htmlBuf);
        }

        if (gzipStream) {
          const entryName = `icons/${id}/index.html`;
          const header = createTarHeader(entryName, htmlBuf.length);
          await writeChunkWithBackpressure(gzipStream, header);
          await writeChunkWithBackpressure(gzipStream, htmlBuf);
          const pad = (512 - (htmlBuf.length % 512)) % 512;
          if (pad > 0) {
            await writeChunkWithBackpressure(gzipStream, Buffer.alloc(pad, 0));
          }
        }

        generated++;
        if (generated % 5000 === 0) {
          const rss = process.memoryUsage().rss;
          if (rss > peakRssBytes) peakRssBytes = rss;
        }
      }
    }
  }

  if (gzipStream && fileOutStream) {
    // Two 512-byte zero blocks terminate a POSIX tar archive
    await writeChunkWithBackpressure(gzipStream, Buffer.alloc(1024, 0));
    await new Promise((resolve, reject) => {
      fileOutStream.on('finish', resolve);
      fileOutStream.on('error', reject);
      gzipStream.end();
    });
  }

  const elapsedMs = Date.now() - startMs;
  const finalRss = process.memoryUsage().rss;
  if (finalRss > peakRssBytes) peakRssBytes = finalRss;

  return {
    generated,
    totalHtmlBytes,
    elapsedMs,
    peakRssMB: +(peakRssBytes / (1024 * 1024)).toFixed(1),
    tarballBytes: tarballPath && fs.existsSync(tarballPath) ? fs.statSync(tarballPath).size : 0,
    cssHref,
  };
}

// CLI entrypoint
if (import.meta.url === `file://${process.argv[1]}`) {
  const args = process.argv.slice(2);
  let limit = Infinity;
  let outDir = null;
  let tarballPath = null;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--limit' && args[i + 1]) limit = parseInt(args[++i], 10);
    else if (args[i] === '--out' && args[i + 1]) outDir = path.resolve(args[++i]);
    else if (args[i] === '--tarball' && args[i + 1]) tarballPath = path.resolve(args[++i]);
  }

  if (!outDir && !tarballPath) {
    outDir = path.join(ROOT, 'dist/icons');
  }

  const stats = await generateIconPages({ limit, outDir, tarballPath });
  console.log(JSON.stringify(stats, null, 2));
}
