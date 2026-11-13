# @iconstash/sdk

Free, keyless access to [IconStash](https://iconstash.io)'s 134,701 open-source SVG icons across 28 libraries — plus an MCP server for AI assistants.

**No API key. No signup. No rate limit. No backend.** The API is a handful of static JSON files on the CDN; search runs locally in this SDK.

## Install

```bash
npm install @iconstash/sdk
```

Or use it directly from this repo: `node -e "const {createClient}=require('./packages/iconstash')"` / `node packages/iconstash/mcp.js`.

## JavaScript

```js
const { createClient } = require('@iconstash/sdk');
const icons = createClient();

// Search (runs locally over a ~1 MB gzipped index)
const hits = await icons.search('camera', { library: 'lucide', limit: 5 });
// [{ id: 'lucide-camera', name: 'camera', library: 'lucide', license: ... , url: ... }, ...]

// Full record incl. svgPath, viewBox, tags and licence
const icon = await icons.getIcon('lucide-camera');

// Ready-to-use SVG
const svg = await icons.svg('lucide-camera', { color: '#2563eb', size: 32 });

// JSX / CSS / HTML / data URI
const jsx = await icons.snippet('lucide-camera', 'jsx');

// The differentiator: one concept, all 28 libraries
const variants = await icons.compare('camera');

// Catalogue
const libs = await icons.libraries();
const meta = await icons.manifest();
```

Point at a local or self-hosted copy with `createClient({ base: 'http://localhost:8000/api/v1' })` or the `ICONSTASH_API_BASE` environment variable.

## MCP server

Add to your MCP client config (Claude Desktop, Cursor, VS Code, etc.):

```json
{
  "mcpServers": {
    "iconstash": {
      "command": "npx",
      "args": ["-y", "@iconstash/sdk", "iconstash-mcp"]
    }
  }
}
```

Or run without installing:

```bash
node packages/iconstash/mcp.js
```

Tools exposed:

| Tool | What it does |
| --- | --- |
| `search_icons` | Keyword search with optional library/category/style filters |
| `get_icon` | Full record for one icon id |
| `get_svg` | SVG / JSX / CSS / HTML / data URI for one icon |
| `compare_concept` | Same concept across all 28 libraries, with licences |
| `list_libraries` | All 28 libraries, counts, licences, npm packages |

The MCP server is a **local process on your machine**. IconStash hosts nothing for it.

## Raw HTTP

```bash
curl https://iconstash.io/api/v1/manifest.json
curl https://iconstash.io/api/v1/libraries.json
curl https://iconstash.io/api/v1/index.json
curl https://iconstash.io/api/v1/openapi.json
curl https://iconstash.io/data/lucide.json
```

All responses are UTF-8 JSON with `Access-Control-Allow-Origin: *`. See [the API docs](https://iconstash.io/api/).

## Licences

Icons belong to their upstream authors. Every response carries a `license` and `attributionRequired` flag. Only `CC BY 4.0` sets (Solar Icons) require visible attribution; all others are MIT, Apache 2.0, ISC or CC0.

## Regenerating the API data

From the IconStash repo root:

```bash
node scripts/generate-api.js
```

This rebuilds `api/v1/manifest.json`, `libraries.json`, `index.json` and `openapi.json` from the existing `data/*.json` files. It adds no icon data — library payloads are the existing public `data/<slug>.json` files served directly (no copy, no rewrite).
