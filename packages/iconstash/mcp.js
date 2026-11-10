#!/usr/bin/env node
'use strict';

/**
 * IconStash MCP server — zero dependencies, stdio JSON-RPC 2.0.
 *
 * Run directly:  node packages/iconstash/mcp.js
 * Or in an MCP client config:
 *   { "mcpServers": { "iconstash": { "command": "npx", "args": ["-y", "@iconstash/sdk", "iconstash-mcp"] } } }
 *
 * It is a client-side process on the user's machine: nothing is hosted, no
 * API key is needed, and it reads the same static API as the website.
 */

const { createClient } = require('./index.js');

const SERVER_INFO = { name: 'iconstash', version: '1.0.0' };
const PROTOCOL_VERSION = '2024-11-05';

const TOOLS = [
  {
    name: 'search_icons',
    description: 'Search 134,701 free open-source SVG icons across 28 libraries by keyword. Returns ids, names, libraries, licences and canonical URLs.',
    inputSchema: {
      type: 'object',
      properties: {
        query: { type: 'string', description: 'Search term, e.g. "camera", "arrow down", "shopping cart"' },
        library: { type: 'string', description: 'Optional library slug filter, e.g. lucide, tabler, phosphor' },
        category: { type: 'string', description: 'Optional category filter, e.g. media, navigation' },
        style: { type: 'string', description: 'Optional style filter, e.g. outline, fill, bold' },
        limit: { type: 'number', description: 'Max results (1-500, default 20)' }
      },
      required: ['query']
    }
  },
  {
    name: 'get_icon',
    description: 'Get the full record for one icon by id, including svgPath, viewBox, tags and licence.',
    inputSchema: {
      type: 'object',
      properties: { id: { type: 'string', description: 'Icon id, e.g. lucide-camera' } },
      required: ['id']
    }
  },
  {
    name: 'get_svg',
    description: 'Render one icon as ready-to-use SVG markup (or JSX / CSS / HTML / data URI).',
    inputSchema: {
      type: 'object',
      properties: {
        id: { type: 'string', description: 'Icon id, e.g. lucide-camera' },
        color: { type: 'string', description: 'Stroke/fill colour, e.g. #2563eb' },
        size: { type: 'number', description: 'Width/height in px (default 24)' },
        strokeWidth: { type: 'number', description: 'Stroke width for outline icons' },
        format: { type: 'string', description: 'svg (default), jsx, css, html or datauri' }
      },
      required: ['id']
    }
  },
  {
    name: 'compare_concept',
    description: 'Unique to IconStash: show how all 28 libraries draw the same concept (e.g. "camera", "trash", "home"), with each library\'s licence.',
    inputSchema: {
      type: 'object',
      properties: {
        concept: { type: 'string', description: 'Concept name, e.g. camera, trash, home' },
        limit: { type: 'number', description: 'Max libraries (default 28)' }
      },
      required: ['concept']
    }
  },
  {
    name: 'list_libraries',
    description: 'List all 28 icon libraries with icon counts, licences, npm packages and attribution requirements.',
    inputSchema: { type: 'object', properties: {} }
  }
];

function textResult(value) {
  return { content: [{ type: 'text', text: typeof value === 'string' ? value : JSON.stringify(value, null, 2) }] };
}

function errorResult(message) {
  return { content: [{ type: 'text', text: `IconStash error: ${message}` }], isError: true };
}

async function callTool(client, name, args) {
  switch (name) {
    case 'search_icons': {
      if (!args || !String(args.query || '').trim()) throw new Error('query is required');
      const results = await client.search(args.query, args);
      return textResult({ query: args.query, count: results.length, results });
    }
    case 'get_icon': {
      if (!args || !args.id) throw new Error('id is required');
      return textResult(await client.getIcon(args.id));
    }
    case 'get_svg': {
      if (!args || !args.id) throw new Error('id is required');
      const format = String(args.format || 'svg').toLowerCase();
      const opts = {};
      if (args.color) opts.color = args.color;
      if (args.size) opts.size = Number(args.size);
      if (args.strokeWidth != null) opts.strokeWidth = Number(args.strokeWidth);
      const markup = await client.svg(args.id, opts);
      return textResult(format === 'svg' ? markup : await client.snippet(args.id, format));
    }
    case 'compare_concept': {
      if (!args || !String(args.concept || '').trim()) throw new Error('concept is required');
      const variants = await client.compare(args.concept, args);
      return textResult({ concept: args.concept, libraries: variants.length, variants });
    }
    case 'list_libraries': {
      const libs = await client.libraries();
      return textResult({ count: libs.length, libraries: libs });
    }
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
}

function reply(id, result) {
  process.stdout.write(`${JSON.stringify({ jsonrpc: '2.0', id, result })}\n`);
}

function replyError(id, code, message) {
  process.stdout.write(`${JSON.stringify({ jsonrpc: '2.0', id, error: { code, message } })}\n`);
}

async function handle(message, client) {
  const { id, method, params } = message || {};
  const isNotification = id === undefined || id === null;

  if (method === 'initialize') {
    return reply(id, {
      protocolVersion: PROTOCOL_VERSION,
      capabilities: { tools: { listChanged: false } },
      serverInfo: SERVER_INFO
    });
  }
  if (method === 'notifications/initialized' || method === 'notifications/cancelled') return;
  if (method === 'ping') return reply(id, {});
  if (method === 'tools/list') return reply(id, { tools: TOOLS });
  if (method === 'resources/list') return reply(id, { resources: [] });
  if (method === 'resources/templates/list') return reply(id, { resourceTemplates: [] });
  if (method === 'tools/call') {
    try {
      const result = await callTool(client, params && params.name, (params && params.arguments) || {});
      return reply(id, result);
    } catch (error) {
      return reply(id, errorResult(error.message));
    }
  }
  if (isNotification) return;
  return replyError(id, -32601, `Method not found: ${method}`);
}

function main() {
  const client = createClient({ base: process.env.ICONSTASH_API_BASE || undefined });
  let buffer = '';
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', (chunk) => {
    buffer += chunk;
    let newline;
    while ((newline = buffer.indexOf('\n')) !== -1) {
      const line = buffer.slice(0, newline).trim();
      buffer = buffer.slice(newline + 1);
      if (!line) continue;
      let message;
      try { message = JSON.parse(line); } catch (_) { continue; }
      Promise.resolve(handle(message, client)).catch((error) => {
        if (message && message.id !== undefined && message.id !== null) {
          replyError(message.id, -32603, String(error && error.message ? error.message : error));
        }
      });
    }
  });
  process.stdin.on('end', () => process.exit(0));
}

main();
