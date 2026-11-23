import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';

const ROOT = process.cwd();

describe('Public Static API, SDK & MCP Server Parity', () => {
  it('validates all /api/v1/*.json payloads in dist/api/v1/', () => {
    const apiDir = path.join(ROOT, 'dist/api/v1');
    const manifest = JSON.parse(fs.readFileSync(path.join(apiDir, 'manifest.json'), 'utf8'));
    const libraries = JSON.parse(fs.readFileSync(path.join(apiDir, 'libraries.json'), 'utf8'));
    const openapi = JSON.parse(fs.readFileSync(path.join(apiDir, 'openapi.json'), 'utf8'));
    const indexStat = fs.statSync(path.join(apiDir, 'index.json'));

    assert.equal(manifest.stats?.icons ?? manifest.counts?.icons ?? manifest.totalIcons ?? manifest.icons, 134701);
    assert.equal(manifest.stats?.libraries ?? manifest.counts?.libraries ?? manifest.totalLibraries ?? manifest.libraries, 28);
    assert.equal((Array.isArray(libraries) ? libraries : libraries.libraries).length, 28);
    assert.ok(openapi.openapi || openapi.paths, 'OpenAPI spec must define paths');
    assert.ok(indexStat.size > 1_000_000, 'api/v1/index.json should be present and populated');
    assert.ok(fs.existsSync(path.join(ROOT, 'dist/api/iconstash-sdk.js')));
    assert.ok(fs.existsSync(path.join(ROOT, 'dist/api/iconstash-mcp.js')));
    assert.ok(fs.existsSync(path.join(ROOT, 'dist/api/index.html')));
  });

  it('verifies iconstash-mcp responds to JSON-RPC 2.0 initialize & tools/list over stdio', async () => {
    const mcpPath = path.join(ROOT, 'packages/iconstash/mcp.js');
    const proc = spawn(process.execPath, [mcpPath], { stdio: ['pipe', 'pipe', 'pipe'] });

    const responses = [];
    let buf = '';
    proc.stdout.on('data', (chunk) => {
      buf += chunk.toString('utf8');
      const lines = buf.split('\n');
      buf = lines.pop() ?? '';
      for (const line of lines) {
        if (line.trim()) {
          try {
            responses.push(JSON.parse(line));
          } catch {
            // ignore non-JSON debug lines
          }
        }
      }
    });

    const initReq = JSON.stringify({
      jsonrpc: '2.0',
      id: 1,
      method: 'initialize',
      params: { protocolVersion: '2024-11-05', capabilities: {}, clientInfo: { name: 'test', version: '1.0' } },
    });
    const toolsReq = JSON.stringify({ jsonrpc: '2.0', id: 2, method: 'tools/list', params: {} });

    proc.stdin.write(initReq + '\n');
    proc.stdin.write(toolsReq + '\n');

    await new Promise((resolve) => setTimeout(resolve, 600));
    proc.kill();

    const initResp = responses.find((r) => r.id === 1);
    const toolsResp = responses.find((r) => r.id === 2);
    assert.ok(initResp?.result?.serverInfo, 'MCP initialize must return serverInfo');
    assert.ok(Array.isArray(toolsResp?.result?.tools), 'MCP tools/list must return tools array');
    assert.equal(toolsResp.result.tools.length, 5, 'MCP server must expose all 5 tools');
  });
});
