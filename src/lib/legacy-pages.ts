import fs from 'node:fs';
import path from 'node:path';

export interface LegacyHtmlPage {
  htmlAttrs: string;
  bodyAttrs: string;
  headHtml: string;
  bodyHtml: string;
  title: string;
  canonical: string;
}

export interface LegacyRouteEntry {
  slug: string | undefined;
  filePath: string;
}

const ROOT_DIR = process.cwd();

/**
 * Walks a legacy static directory (e.g. "articles", "Glossary", "compare")
 * and returns Astro rest-param `[...slug]` entries matching exact legacy URLs.
 */
export function listLegacyHtmlRoutes(sectionDir: string): LegacyRouteEntry[] {
  const baseDir = path.join(ROOT_DIR, sectionDir);
  if (!fs.existsSync(baseDir)) return [];

  const results: LegacyRouteEntry[] = [];

  function walk(dir: string, relPrefix: string) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.name.startsWith('.')) continue;
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        const nextRel = relPrefix ? `${relPrefix}/${entry.name}` : entry.name;
        walk(fullPath, nextRel);
      } else if (entry.isFile() && entry.name === 'index.html') {
        results.push({
          slug: relPrefix || undefined,
          filePath: fullPath,
        });
      }
    }
  }

  walk(baseDir, '');
  results.sort((a, b) => (a.slug ?? '').localeCompare(b.slug ?? ''));
  return results;
}

/**
 * Extracts exact head & body HTML from a legacy static HTML file so Astro MPA
 * pages preserve 100% of original SEO tags, JSON-LD, inline styles, and markup
 * with zero framework JS overhead.
 */
export function readLegacyHtmlPage(filePath: string): LegacyHtmlPage {
  const absPath = path.isAbsolute(filePath) ? filePath : path.join(ROOT_DIR, filePath);
  const raw = fs.readFileSync(absPath, 'utf8');

  const htmlOpen = raw.match(/<html\b([^>]*)>/i);
  const bodyOpen = raw.match(/<body\b([^>]*)>/i);
  const headMatch = raw.match(/<head\b[^>]*>([\s\S]*?)<\/head>/i);
  const bodyMatch = raw.match(/<body\b[^>]*>([\s\S]*?)<\/body>/i);

  const rawHead = headMatch ? headMatch[1] : '';
  const bodyHtml = bodyMatch ? bodyMatch[1] : raw;

  // Strip legacy /style.css link because EditorialLayout imports bundled app.css
  const headHtml = rawHead.replace(
    /<link\b[^>]*href=["']\/?style\.css(?:\?[^"']*)?["'][^>]*>/gi,
    ''
  );

  const titleMatch = rawHead.match(/<title>([\s\S]*?)<\/title>/i);
  const canonicalMatch = rawHead.match(/<link\b[^>]*rel=["']canonical["'][^>]*href=["']([^"']+)["'][^>]*>/i);

  return {
    htmlAttrs: htmlOpen ? htmlOpen[1].trim() : 'lang="en"',
    bodyAttrs: bodyOpen ? bodyOpen[1].trim() : '',
    headHtml,
    bodyHtml,
    title: titleMatch ? titleMatch[1].trim() : 'IconStash',
    canonical: canonicalMatch ? canonicalMatch[1].trim() : '',
  };
}
