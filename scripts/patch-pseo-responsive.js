#!/usr/bin/env node
/* eslint-disable no-console */
/**
 * One-shot patcher: replaces the embedded <style>...</style> block in every
 * generated PSEO page (icons/<slug>/index.html) with the mobile-responsive CSS.
 *
 * This avoids regenerating 145k+ pages from scratch. It is safe to re-run —
 * it only swaps the style block (matched from "<style>" to the first "</style>").
 */
const fs = require("node:fs");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..");
const ICONS_DIR = path.join(ROOT, "icons");

const NEW_STYLE = `  <style>
    :root{color-scheme:dark;--bg:#07070d;--panel:#0f0f1c;--line:#1e1e32;--text:#f0f0ff;--muted:#8888aa;--blue:#2f80ff;--green:#00cc66}
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
    html,body{max-width:100%;width:100%;overflow-x:hidden}
    body{background:var(--bg);color:var(--text);font:15px/1.7 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
    img,svg,video{max-width:100%;height:auto;display:block}
    a{color:var(--blue);text-decoration:none}a:hover{text-decoration:underline}
    .wrap{max-width:980px;width:100%;margin:0 auto;padding:32px 20px 72px}
    .crumbs{display:flex;gap:6px;flex-wrap:wrap;color:var(--muted);font-size:13px;margin-bottom:28px;align-items:center}
    .crumbs a{color:var(--muted)}.crumbs a:hover{color:var(--text)}
    .hero{display:grid;grid-template-columns:200px 1fr;gap:32px;align-items:center;margin-bottom:40px;min-width:0}
    .preview{height:200px;border:1px solid var(--line);border-radius:18px;background:var(--panel);display:grid;place-items:center;color:var(--blue);min-width:0}
    .preview svg{max-width:64%;max-height:64%}
    h1{font-size:clamp(24px,4vw,44px);line-height:1.15;margin-bottom:14px;letter-spacing:-.02em;font-weight:800;overflow-wrap:break-word}
    .lead{color:var(--muted);font-size:16px;line-height:1.65;margin-bottom:20px}
    .cta{display:flex;gap:10px;flex-wrap:wrap}
    .btn{border:1px solid var(--line);border-radius:9px;padding:12px 18px;color:var(--text);background:var(--panel);font-size:15px;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;min-height:44px;line-height:1.2;text-align:center}
    .btn.primary{background:var(--blue);border-color:var(--blue);color:#fff}
    .btn:hover{opacity:.88;text-decoration:none}
    .section-title{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:40px 0 16px}
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:16px}
    .grid.wide{grid-template-columns:1fr}
    .card{border:1px solid var(--line);background:var(--panel);border-radius:14px;padding:20px;min-width:0;overflow-wrap:break-word}
    .card h2{font-size:16px;font-weight:700;margin-bottom:10px;color:var(--text)}
    .card p{color:var(--muted);font-size:14px;line-height:1.65;margin-bottom:10px}
    .card p:last-child{margin-bottom:0}
    .card p.muted{color:#666688}
    .card strong{color:var(--text)}
    .card ul{padding-left:18px;color:var(--muted);font-size:14px}
    .card li{margin:6px 0}
    .card code{background:#0a0a18;border:1px solid var(--line);border-radius:4px;padding:1px 5px;font-size:12px;font-family:"JetBrains Mono",Consolas,monospace;word-break:break-word}
    .lib-meta{list-style:none;padding:0}
    .lib-meta li{display:flex;gap:8px;align-items:baseline;padding:4px 0;border-bottom:1px solid var(--line);font-size:13px}
    .lib-meta li:last-child{border-bottom:none}
    .lib-meta strong{color:var(--text);flex:0 0 120px}
    pre{background:#060610;border:1px solid var(--line);border-radius:10px;padding:16px;overflow-x:auto;max-width:100%;margin-top:8px;-webkit-overflow-scrolling:touch}
    pre code{font:500 12px/1.6 "JetBrains Mono",Consolas,monospace;color:#a8d8a8;white-space:pre;display:block;min-width:max-content}
    .chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:4px}
    .chips a{border:1px solid var(--line);border-radius:999px;padding:8px 14px;font-size:13px;color:var(--muted);display:inline-block;min-height:36px;line-height:20px}
    .chips a:hover{color:var(--text);border-color:#555;text-decoration:none}
    .faq-item{border-bottom:1px solid var(--line);padding:16px 0}
    .faq-item:last-child{border-bottom:none}
    .faq-item h3{font-size:15px;font-weight:700;color:var(--text);margin-bottom:8px}
    .faq-item p{color:var(--muted);font-size:14px;line-height:1.65}
    footer{margin-top:52px;padding-top:24px;border-top:1px solid var(--line);color:var(--muted);font-size:13px;display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center}
    footer a{color:var(--muted)}footer a:hover{color:var(--text)}
    .footer-links{display:flex;gap:16px;flex-wrap:wrap}
    /* Tablet: 768-1024px */
    @media(max-width:1024px){
      .wrap{max-width:880px;padding:28px 24px 64px}
    }
    /* Mobile: <768px */
    @media(max-width:767px){
      .wrap{padding:20px 16px 56px}
      .crumbs{font-size:12px;margin-bottom:20px}
      .hero{grid-template-columns:1fr;gap:18px;margin-bottom:28px}
      .preview{height:160px;margin:0 auto}
      h1{font-size:clamp(22px,7vw,30px)}
      .lead{font-size:15px}
      .cta{flex-direction:column;align-items:stretch}
      .cta .btn{width:100%}
      .section-title{margin:28px 0 12px}
      .grid{grid-template-columns:1fr;gap:12px}
      .card{padding:16px}
      .card h2{font-size:15px}
      .lib-meta strong{flex:0 0 104px}
      pre{padding:12px}
      .faq-item{padding:14px 0}
      footer{flex-direction:column;align-items:flex-start;gap:12px}
      .footer-links{gap:12px}
    }
  </style>`;

const STYLE_RE = /  <style>[\s\S]*?<\/style>/;
const MARKER = ":root{color-scheme:dark";

function patchFile(file) {
  let src = fs.readFileSync(file, "utf8");
  const match = src.match(STYLE_RE);
  if (!match) return "no-style";
  // Avoid rewriting if it already has the new responsive rules.
  if (src.includes("text-size-adjust:100%") && src.includes("max-width:767px")) return "already-patched";
  const replaced = src.replace(STYLE_RE, NEW_STYLE);
  if (replaced === src) return "unchanged";
  fs.writeFileSync(file, replaced);
  return "patched";
}

function main() {
  if (!fs.existsSync(ICONS_DIR)) {
    console.error(`icons directory not found: ${ICONS_DIR}`);
    process.exit(1);
  }
  const dirs = fs.readdirSync(ICONS_DIR);
  const total = dirs.length;
  console.log(`Patching ${total.toLocaleString("en-US")} PSEO pages in ${path.relative(ROOT, ICONS_DIR)}...`);

  let patched = 0;
  let skipped = 0;
  let already = 0;
  let errors = 0;
  let count = 0;
  const reportEvery = Math.max(1, Math.round(total / 10));

  for (const dir of dirs) {
    const file = path.join(ICONS_DIR, dir, "index.html");
    try {
      if (!fs.existsSync(file)) { skipped++; continue; }
      const res = patchFile(file);
      if (res === "patched") patched++;
      else if (res === "already-patched") already++;
      else skipped++;
    } catch (err) {
      errors++;
      if (errors <= 5) console.error(`  ERROR: ${dir}: ${err.message}`);
    }
    count++;
    if (count % reportEvery === 0) {
      console.log(`- Progress: ${Math.round((count / total) * 100)}% (${count.toLocaleString("en-US")} / ${total.toLocaleString("en-US")})`);
    }
  }

  console.log(`\nDone. patched=${patched.toLocaleString("en-US")}, already-patched=${already.toLocaleString("en-US")}, skipped=${skipped.toLocaleString("en-US")}, errors=${errors.toLocaleString("en-US")}`);
}

main();
