#!/usr/bin/env node
/* eslint-disable no-console */
/**
 * One-shot patcher: makes the Styles section expandable on all 145k+ PSEO detail pages.
 * Swaps the flat Styles filter-section markup and patches the inline JS array.
 */
const fs = require("node:fs");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..");
const ICONS_DIR = path.join(ROOT, "icons");

const STYLES_RE = /<section class="filter-section">\s*<div class="filter-header">\s*<h2>Styles<\/h2>\s*<\/div>\s*<div class="style-pills">([\s\S]*?)<\/div>\s*<\/section>/;

const JS_RE = /\["category",\s*"customize"\]/g;

function patchFile(file) {
  let src = fs.readFileSync(file, "utf8");
  
  if (src.includes('id="style-section"')) {
    return "already-patched";
  }

  const stylesMatch = src.match(STYLES_RE);
  if (!stylesMatch) return "no-styles-match";

  const pillsContent = stylesMatch[1];
  const newStylesMarkup = `<section class="filter-section expandable" id="style-section">
            <button class="filter-header category-toggle" id="style-toggle" aria-expanded="false">
              <h2>Styles</h2>
              <svg class="chevron" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></svg>
            </button>
            <div class="style-pills">
              ${pillsContent}
            </div>
          </section>`;

  let replaced = src.replace(STYLES_RE, newStylesMarkup);
  replaced = replaced.replace(JS_RE, '["category", "customize", "style"]');

  if (replaced === src) return "unchanged";
  fs.writeFileSync(file, replaced, "utf8");
  return "patched";
}

function main() {
  if (!fs.existsSync(ICONS_DIR)) {
    console.error(`icons directory not found: ${ICONS_DIR}`);
    process.exit(1);
  }
  const dirs = fs.readdirSync(ICONS_DIR);
  const total = dirs.length;
  console.log(`Patching Styles section in ${total.toLocaleString("en-US")} PSEO pages...`);

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
