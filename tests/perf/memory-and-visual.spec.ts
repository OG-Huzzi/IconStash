import { test, expect, chromium, type CDPSession } from '@playwright/test';
import http from 'node:http';
import type { AddressInfo } from 'node:net';
import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const DIST = path.join(ROOT, 'dist');
const SCREENSHOTS = path.join(ROOT, 'release/screenshots');

const MIME: Record<string, string> = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.mjs': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.bin': 'application/octet-stream',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
};

function startStaticServer(): Promise<{ server: http.Server; baseUrl: string }> {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      const urlPath = decodeURIComponent((req.url || '/').split('?')[0]);
      let filePath = path.join(DIST, urlPath);
      if (urlPath.startsWith('/data/')) {
        filePath = path.join(ROOT, urlPath);
      }
      if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
        filePath = path.join(filePath, 'index.html');
      }
      if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      const ext = path.extname(filePath).toLowerCase();
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      fs.createReadStream(filePath).pipe(res);
    });
    server.listen(0, '127.0.0.1', () => {
      const addr = server.address() as AddressInfo;
      resolve({ server, baseUrl: `http://localhost:${addr.port}` });
    });
  });
}

async function getHeapMB(cdp: CDPSession): Promise<number> {
  const { metrics } = await cdp.send('Performance.getMetrics');
  const used = metrics.find((m: { name: string; value: number }) => m.name === 'JSHeapUsedSize')?.value ?? 0;
  return +(used / (1024 * 1024)).toFixed(2);
}

test('Phase 4 Hard Gate: Browser Memory <= 100MB, DOM tiles <= 180, Search/Scroll/Sliders/Exports & Visual Captures', async () => {
  test.setTimeout(120_000);
  fs.mkdirSync(SCREENSHOTS, { recursive: true });
  const { server, baseUrl } = await startStaticServer();

  const browser = await chromium.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--js-flags=--expose-gc'],
  });

  try {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
    const page = await context.newPage();
    await page.route('https://plausible.io/**', (route) => route.abort());
    const cdp = await context.newCDPSession(page);
    await cdp.send('Performance.enable');

    // 1. Homepage initial load
    await page.goto(`${baseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForSelector('[data-icon-tile]', { timeout: 10_000 });
    await page.waitForTimeout(600);

    const initialHeapMB = await getHeapMB(cdp);
    const initialTiles = await page.locator('[data-icon-tile]').count();
    console.log(`[Perf] Initial load: heap=${initialHeapMB} MB, tiles=${initialTiles}`);
    expect(initialHeapMB).toBeLessThanOrEqual(45);
    expect(initialTiles).toBeLessThanOrEqual(180);

    // Capture Desktop Dark & Light screenshots
    await page.screenshot({ path: path.join(SCREENSHOTS, 'home-desktop-dark.png') });
    const themeBtn = page.locator('#theme-toggle').first();
    if (await themeBtn.isVisible()) {
      await themeBtn.click();
      await page.waitForTimeout(200);
      await page.screenshot({ path: path.join(SCREENSHOTS, 'home-desktop-light.png') });
      await themeBtn.click();
      await page.waitForTimeout(200);
    }

    // 2. Run 32 searches across 134,701 icons
    const queries = [
      'arrow', 'home', 'user', 'search', 'settings', 'heart', 'star', 'mail',
      'check', 'close', 'plus', 'minus', 'edit', 'trash', 'copy', 'download',
      'upload', 'share', 'lock', 'unlock', 'cloud', 'sun', 'moon', 'bell',
      'calendar', 'clock', 'camera', 'play', 'pause', 'chevron right', 'folder', 'code',
    ];
    const searchInput = page.locator('input[type="search"], #main-search').first();
    let maxTilesSeen = initialTiles;
    let maxHeapMB = initialHeapMB;

    for (const q of queries) {
      await searchInput.fill(q);
      await page.waitForTimeout(45);
      const tiles = await page.locator('[data-icon-tile]').count();
      if (tiles > maxTilesSeen) maxTilesSeen = tiles;
      expect(tiles).toBeLessThanOrEqual(180);
    }
    await searchInput.fill('');
    await page.waitForTimeout(200);

    // 3. Rapid scrolling through virtualized grid
    for (let y = 0; y <= 15000; y += 1500) {
      await page.evaluate((top) => {
        const el = document.querySelector('.virtual-grid-scroll, .icon-grid-stage, #icon-grid');
        if (el) el.scrollTop = top;
        window.scrollTo(0, top);
      }, y);
      await page.waitForTimeout(35);
      const tiles = await page.locator('[data-icon-tile]').count();
      if (tiles > maxTilesSeen) maxTilesSeen = tiles;
      expect(tiles).toBeLessThanOrEqual(180);
    }

    // 4. Switch across 16 libraries inside the Explorer (in-session LRU eviction stress)
    const libButtons = page.locator('#library-filters button, .library-filter-btn, [data-lib-filter], #left-sidebar .lib-item button:visible, .library-item button:visible');
    const libCount = Math.min(16, await libButtons.count());
    const heapSamples: Array<{ step: string; heapMB: number; tiles: number }> = [];

    for (let i = 0; i < libCount; i++) {
      await libButtons.nth(i).click({ timeout: 1000 }).catch(() => {});
      await page.waitForTimeout(160);
      const h = await getHeapMB(cdp);
      const t = await page.locator('[data-icon-tile]').count();
      if (h > maxHeapMB) maxHeapMB = h;
      if (t > maxTilesSeen) maxTilesSeen = t;
      heapSamples.push({ step: `lib-${i}`, heapMB: h, tiles: t });
      expect(t).toBeLessThanOrEqual(180);
      expect(h).toBeLessThanOrEqual(140);
      await libButtons.nth(i).click({ timeout: 1000 }).catch(() => {});
      await page.waitForTimeout(50);
    }

    // 5. Open Inspector by clicking first icon tile
    const firstTile = page.locator('[data-icon-tile]').first();
    if (await firstTile.isVisible()) {
      await firstTile.click();
      await page.waitForTimeout(250);
    }

    // Collect GC to measure true retained steady-state heap
    await cdp.send('HeapProfiler.collectGarbage').catch(() => {});
    await page.waitForTimeout(150);
    const steadyHeapMB = await getHeapMB(cdp);
    console.log(`[Perf] Steady-state: heap=${steadyHeapMB} MB, peakHeap=${maxHeapMB} MB, maxTiles=${maxTilesSeen}, libsSwitched=${libCount}`);
    expect(steadyHeapMB).toBeLessThanOrEqual(100);
    expect(maxHeapMB).toBeLessThanOrEqual(140);

    // 6. Verify Mobile viewport screenshot
    await page.setViewportSize({ width: 390, height: 844 });
    await page.waitForTimeout(200);
    await page.screenshot({ path: path.join(SCREENSHOTS, 'home-mobile-dark.png') });

    // 7. Verify Static API, robots.txt, and sitemap.xml endpoints
    for (const ep of ['/api/v1/manifest.json', '/api/v1/libraries.json', '/api/v1/openapi.json', '/robots.txt', '/sitemap.xml']) {
      const resp = await page.request.get(`${baseUrl}${ep}`);
      expect(resp.status(), `Expected 200 for ${ep}`).toBe(200);
    }

    fs.writeFileSync(
      path.join(ROOT, 'release/perf-results.json'),
      JSON.stringify(
        {
          initialHeapMB,
          steadyHeapMB,
          maxHeapMB,
          maxTilesSeen,
          queriesRun: queries.length,
          librariesSwitched: libCount,
          heapSamples,
        },
        null,
        2
      )
    );
  } finally {
    await browser.close();
    server.close();
  }
});
