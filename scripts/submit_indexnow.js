const https = require('https');

const payload = JSON.stringify({
  host: 'iconstash.io',
  key: 'e11c5bc79c6d4824bb883b2723c0fa6a',
  keyLocation: 'https://iconstash.io/e11c5bc79c6d4824bb883b2723c0fa6a.txt',
  urlList: [
    'https://iconstash.io/articles/svg-gooey-effects-and-liquid-metaballs-guide/',
    'https://iconstash.io/articles/svg-glassmorphism-and-frosted-glass-guide/',
    'https://iconstash.io/articles/svg-isometric-projection-and-2-5d-graphics-guide/'
  ]
});

const endpoints = [
  'https://api.indexnow.org/indexnow',
  'https://www.bing.com/indexnow',
  'https://yandex.com/indexnow'
];

console.log('Submitting URLs to IndexNow endpoints (Bing, Yandex, IndexNow)...\n');

endpoints.forEach(endpoint => {
  const url = new URL(endpoint);
  const req = https.request({
    hostname: url.hostname,
    path: url.pathname,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Content-Length': Buffer.byteLength(payload)
    }
  }, res => {
    let body = '';
    res.on('data', chunk => body += chunk);
    res.on('end', () => {
      console.log(`[${res.statusCode} ${res.statusMessage}] ${endpoint}`);
      if (body) console.log(`  Response: ${body}`);
    });
  });

  req.on('error', err => {
    console.error(`[ERROR] ${endpoint}: ${err.message}`);
  });

  req.write(payload);
  req.end();
});
