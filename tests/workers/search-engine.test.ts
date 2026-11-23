import { describe, expect, it } from 'vitest';
import {
  BinarySearchEngine,
  CATEGORY_COUNT,
  LIBRARY_COUNT,
  STYLE_COUNT,
  buildBinarySearchIndex,
  packMeta,
  packPosting,
  parseSearchHeader,
  unpackMeta,
  unpackPosting,
  type BinaryIndexIconInput,
} from '../../src/workers/search-core.js';
import {
  createSearchWorkerHandler,
  type SearchWorkerResponse,
} from '../../src/workers/search.worker.js';

const CATALOG_SIZE = 134_701;

const BASE_WORDS = [
  'arrow',
  'home',
  'user',
  'search',
  'check',
  'chevron',
  'bell',
  'calendar',
  'camera',
  'chart',
  'clock',
  'cloud',
  'code',
  'credit',
  'database',
  'download',
  'edit',
  'eye',
  'file',
  'filter',
  'folder',
  'globe',
  'heart',
  'image',
  'inbox',
  'key',
  'layers',
  'link',
  'lock',
  'mail',
  'map',
  'menu',
  'message',
  'mic',
  'moon',
  'music',
  'package',
  'paperclip',
  'phone',
  'play',
  'plus',
  'printer',
  'refresh',
  'rocket',
  'save',
  'scissors',
  'send',
  'server',
  'settings',
  'share',
  'shield',
  'shopping',
  'sliders',
  'sparkles',
  'star',
  'sun',
  'tag',
  'terminal',
  'thumbs',
  'trash',
  'trending',
  'truck',
  'upload',
  'video',
  'volume',
  'wallet',
  'wifi',
  'zap',
];

const MODIFIERS = [
  'left',
  'right',
  'up',
  'down',
  'circle',
  'square',
  'plus',
  'minus',
  'x',
  'check',
  'alert',
  'off',
  'outline',
  'solid',
  'filled',
  'duotone',
  'badge',
  'dot',
  'line',
  'alt',
  '2',
  '3',
  'box',
  'card',
  'list',
  'grid',
  'bar',
  'stack',
  'sync',
  'lock',
];

const EXTRA_TAGS = [
  'ui',
  'interface',
  'navigation',
  'action',
  'direction',
  'pointer',
  'commerce',
  'finance',
  'social',
  'media',
  'audio',
  'developer',
  'security',
  'privacy',
  'weather',
  'analytics',
  'notification',
  'communication',
  'document',
  'hardware',
];

/** Build a realistic 134,701-icon synthetic binary index matching docs/architecture.md §5.1. */
function buildSyntheticCatalogIndex(count: number): ArrayBuffer {
  const icons: BinaryIndexIconInput[] = new Array(count);
  for (let i = 0; i < count; i++) {
    const libId = i % LIBRARY_COUNT;
    const catId = (i >>> 2) % CATEGORY_COUNT;
    const styleId = (i >>> 5) % STYLE_COUNT;
    const w1 = BASE_WORDS[i % BASE_WORDS.length]!;
    const w2 = MODIFIERS[(i >>> 6) % MODIFIERS.length]!;
    // Introduce ~10k unique suffix tokens across the catalog to mirror the real 10,849 vocab
    const bucket = i % 10_000;
    const name = i < 200 ? `${w1}-${w2}` : `${w1}-${w2}-v${bucket}`;
    const t1 = EXTRA_TAGS[catId % EXTRA_TAGS.length]!;
    const t2 = EXTRA_TAGS[(i + 5) % EXTRA_TAGS.length]!;
    icons[i] = {
      name,
      tags: [t1, t2],
      libId,
      catId,
      styleId,
      strokeIdx: styleId % 4,
      isFilled: styleId === 2 || styleId === 5,
      hasVariants: (i & 3) === 0,
      rankScore: (count - i) & 0xffff,
    };
  }
  return buildBinarySearchIndex(icons);
}

describe('search-core binary codec & accuracy', () => {
  it('packs and unpacks metaPacked and postingsIds bitfields losslessly', () => {
    const packed = packMeta({
      libId: 27,
      catId: 15,
      styleId: 6,
      strokeIdx: 3,
      isFilled: true,
      hasVariants: true,
      rankScore: 54321,
    });
    expect(unpackMeta(packed)).toEqual({
      libId: 27,
      catId: 15,
      styleId: 6,
      strokeIdx: 3,
      strokeWidth: 2,
      isFilled: true,
      hasVariants: true,
      rankScore: 54321,
    });

    const posting = packPosting(134_700, 4);
    expect(unpackPosting(posting)).toEqual({ iconIndex: 134_700, matchWeight: 4 });
  });

  it('rejects malformed binary buffers', () => {
    expect(() => parseSearchHeader(new ArrayBuffer(16))).toThrow(/too small/i);
    const bad = new ArrayBuffer(64);
    new DataView(bad).setUint32(0, 0xdeadbeef, true);
    expect(() => parseSearchHeader(bad)).toThrow(/magic/i);
  });

  it('supports prefix, substring, multi-token, tag matching, bitmask facets, and all sorts', () => {
    const buffer = buildBinarySearchIndex([
      {
        name: 'arrow-right',
        tags: ['navigation', 'direction'],
        libId: 0,
        catId: 10,
        styleId: 4,
        rankScore: 900,
      },
      {
        name: 'arrow-left',
        tags: ['navigation', 'back'],
        libId: 0,
        catId: 10,
        styleId: 4,
        rankScore: 800,
      },
      {
        name: 'arrow-right-circle',
        tags: ['direction'],
        libId: 1,
        catId: 10,
        styleId: 2,
        rankScore: 1000,
      },
      {
        name: 'chevron-right',
        tags: ['arrow', 'caret'],
        libId: 2,
        catId: 10,
        styleId: 4,
        rankScore: 950,
      },
      {
        name: 'shopping-cart',
        tags: ['commerce', 'checkout'],
        libId: 1,
        catId: 0,
        styleId: 5,
        rankScore: 1200,
      },
      {
        name: 'zebra-badge',
        tags: ['animal'],
        libId: 3,
        catId: 8,
        styleId: 0,
        rankScore: 500,
      },
    ]);

    const engine = new BinarySearchEngine(buffer);

    // Exact + prefix + tag match for "arrow"
    const arrowRes = engine.query({ query: 'arrow', sort: 'relevance' });
    expect(arrowRes.totalMatches).toBe(4);
    // Exact name token matches should rank above tag-only match (chevron-right idx=3)
    expect(arrowRes.indices[arrowRes.indices.length - 1]).toBe(3);

    // Multi-token AND query: "arrow right" -> matches arrow-right (0), arrow-right-circle (2), chevron-right (3 via tag 'arrow' + name 'right')
    const multiRes = engine.query({ query: 'arrow right', sort: 'relevance' });
    expect(Array.from(multiRes.indices)).toContain(0);
    expect(Array.from(multiRes.indices)).toContain(2);
    expect(Array.from(multiRes.indices)).not.toContain(1);
    expect(Array.from(multiRes.indices)).not.toContain(4);

    // Substring match: "ping" -> matches "shopping-cart" (4)
    const subRes = engine.query({ query: 'ping' });
    expect(Array.from(subRes.indices)).toEqual([4]);

    // Multi-facet bitmask: libId=0 OR libId=1, catId=10, styleId=2 (fill) -> only idx=2
    const facetRes = engine.query({
      query: '',
      libMask: (1 << 0) | (1 << 1),
      catMask: 1 << 10,
      styleMask: 1 << 2,
    });
    expect(Array.from(facetRes.indices)).toEqual([2]);
    expect(facetRes.libraryCounts[1]).toBe(1);
    expect(facetRes.categoryCounts[10]).toBe(1);
    expect(facetRes.styleCounts[2]).toBe(1);

    // Alphabetical (az & za)
    const azRes = engine.query({ query: '', sort: 'alphabetical' });
    expect(engine.getIconName(azRes.indices[0]!)).toBe('arrow-left');
    expect(engine.getIconName(azRes.indices[azRes.indices.length - 1]!)).toBe('zebra-badge');

    const zaRes = engine.query({ query: '', sort: 'za' });
    expect(engine.getIconName(zaRes.indices[0]!)).toBe('zebra-badge');

    // Popularity sort
    const popRes = engine.query({ query: '', sort: 'popularity' });
    expect(popRes.indices[0]).toBe(4); // rankScore 1200

    // Library sort
    const libRes = engine.query({ query: '', sort: 'library' });
    expect(engine.getIconMeta(libRes.indices[0]!).libId).toBe(0);
    expect(engine.getIconMeta(libRes.indices[libRes.indices.length - 1]!).libId).toBe(3);
  });
});

describe('search.worker message protocol & Transferables', () => {
  it('handles INIT_BUFFER, QUERY (with Transferable buffers), CONCEPT_MATCHES, CANCEL, and errors', async () => {
    const messages: { msg: SearchWorkerResponse; transfer?: Transferable[] }[] = [];
    const handler = createSearchWorkerHandler((msg, transfer) => {
      messages.push({ msg, transfer });
    });

    // Query before INIT returns ERROR
    await handler.handleMessage({
      type: 'QUERY',
      queryId: 1,
      query: 'home',
      libMask: 0,
      catMask: 0,
      styleMask: 0,
      sort: 'relevance',
    });
    expect(messages[0]?.msg.type).toBe('ERROR');

    // Initialize with binary buffer
    const buf = buildBinarySearchIndex([
      { name: 'home', tags: ['house'], libId: 0, catId: 8, styleId: 4, rankScore: 500 },
      { name: 'home-filled', tags: ['house'], libId: 1, catId: 8, styleId: 2, rankScore: 600 },
      { name: 'user', tags: ['account'], libId: 0, catId: 12, styleId: 4, rankScore: 400 },
    ]);
    await handler.handleMessage({ type: 'INIT_BUFFER', buffer: buf });
    expect(messages[1]?.msg).toMatchObject({ type: 'READY', iconCount: 3 });

    // Query returns RESULTS with 4 Transferable ArrayBuffers
    await handler.handleMessage({
      type: 'QUERY',
      queryId: 2,
      query: 'home',
      libMask: 0,
      catMask: 0,
      styleMask: 0,
      sort: 'relevance',
    });
    const resEntry = messages[2]!;
    expect(resEntry.msg.type).toBe('RESULTS');
    if (resEntry.msg.type === 'RESULTS') {
      expect(resEntry.msg.queryId).toBe(2);
      expect(resEntry.msg.totalMatches).toBe(2);
      expect(resEntry.transfer).toContain(resEntry.msg.indices.buffer);
      expect(resEntry.transfer).toContain(resEntry.msg.libraryCounts.buffer);
    }

    // Concept matches finds cross-library match for index 0 ('home' in lib 0 -> 'home-filled' in lib 1)
    await handler.handleMessage({
      type: 'CONCEPT_MATCHES',
      queryId: 3,
      iconIndex: 0,
      maxPerLibrary: 2,
    });
    const conceptEntry = messages[3]!;
    expect(conceptEntry.msg.type).toBe('CONCEPT_MATCHES');
    if (conceptEntry.msg.type === 'CONCEPT_MATCHES') {
      expect(Array.from(conceptEntry.msg.indices)).toEqual([1]);
      expect(conceptEntry.transfer).toContain(conceptEntry.msg.indices.buffer);
    }

    // Cancelled query produces no response
    const countBefore = messages.length;
    await handler.handleMessage({ type: 'CANCEL', queryId: 99 });
    await handler.handleMessage({
      type: 'QUERY',
      queryId: 99,
      query: 'home',
      libMask: 0,
      catMask: 0,
      styleMask: 0,
      sort: 'relevance',
    });
    expect(messages.length).toBe(countBefore);
  });
});

describe('134,701-icon scale performance benchmark (< 15ms budget)', () => {
  const catalogBuffer = buildSyntheticCatalogIndex(CATALOG_SIZE);
  const engine = new BinarySearchEngine(catalogBuffer);

  it('executes facet, prefix, multi-token, substring, and sorted queries under 15ms across 134,701 icons', () => {
    expect(engine.iconCount).toBe(CATALOG_SIZE);

    // Warm up JIT and lazy sort tables
    engine.query({ query: '', sort: 'relevance' });
    engine.query({ query: 'arrow', sort: 'relevance' });
    engine.query({ query: 'arrow right', sort: 'relevance' });
    engine.query({ query: '', sort: 'az' });

    const benchmarks: { name: string; run: () => ReturnType<BinarySearchEngine['query']> }[] = [
      {
        name: 'empty query (all 134,701 icons, popularity/relevance)',
        run: () => engine.query({ query: '', sort: 'relevance' }),
      },
      {
        name: 'facet-only filter (3 libs + 2 cats + 2 styles)',
        run: () =>
          engine.query({
            query: '',
            libMask: (1 << 0) | (1 << 5) | (1 << 12),
            catMask: (1 << 2) | (1 << 10),
            styleMask: (1 << 1) | (1 << 4),
            sort: 'popularity',
          }),
      },
      {
        name: 'single-token prefix ("arrow")',
        run: () => engine.query({ query: 'arrow', sort: 'relevance' }),
      },
      {
        name: 'multi-token AND ("arrow right")',
        run: () => engine.query({ query: 'arrow right', sort: 'relevance' }),
      },
      {
        name: 'multi-token + facet bitmask ("chevron circle" + libMask)',
        run: () =>
          engine.query({
            query: 'chevron circle',
            libMask: (1 << 0) | (1 << 1) | (1 << 2) | (1 << 3),
            sort: 'relevance',
          }),
      },
      {
        name: 'substring match ("v999")',
        run: () => engine.query({ query: 'v999', sort: 'relevance' }),
      },
      {
        name: 'alphabetical sort ("home", az)',
        run: () => engine.query({ query: 'home', sort: 'az' }),
      },
    ];

    const summary: string[] = [];
    for (const bench of benchmarks) {
      const runs: number[] = [];
      let totalMatches = 0;
      for (let r = 0; r < 10; r++) {
        const res = bench.run();
        runs.push(res.elapsedMs);
        totalMatches = res.totalMatches;
      }
      runs.sort((a, b) => a - b);
      const p50 = runs[Math.floor(runs.length * 0.5)]!;
      const p95 = runs[Math.floor(runs.length * 0.95)]!;
      summary.push(
        `  - ${bench.name}: matches=${totalMatches}, p50=${p50.toFixed(2)}ms, p95=${p95.toFixed(2)}ms`,
      );
      expect(totalMatches).toBeGreaterThan(0);
      expect(p95).toBeLessThan(15);
    }

    console.log(
      `\n[Search Benchmark — ${CATALOG_SIZE.toLocaleString()} icons, ${(catalogBuffer.byteLength / (1024 * 1024)).toFixed(2)} MB index]\n${summary.join('\n')}\n`,
    );
  });
});
