const fs = require('fs');
const path = require('path');

const outDir = path.join('articles', 'svg-mesh-gradients-and-generative-shading-guide');
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

const htmlPath = path.join(outDir, 'index.html');
if (fs.existsSync(htmlPath)) {
  console.log(`Article 2 already exists at: ${htmlPath}`);
  console.log(`File size: ${Math.round(fs.statSync(htmlPath).size / 1024)} KB`);
} else {
  console.error(`Article 2 file missing at: ${htmlPath}`);
  process.exit(1);
}
