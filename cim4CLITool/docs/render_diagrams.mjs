import { readFileSync, writeFileSync, readdirSync } from "fs";
import { join } from "path";
import puppeteer from "puppeteer";

const diagramsDir = process.argv[2];
if (!diagramsDir) {
  console.error("Usage: node render_diagrams.mjs <diagrams_dir>");
  process.exit(1);
}

const mmdFiles = readdirSync(diagramsDir).filter((f) => f.endsWith(".mmd"));
if (mmdFiles.length === 0) {
  console.log("No .mmd files to render");
  process.exit(0);
}

console.log(`Rendering ${mmdFiles.length} diagrams...`);

const browser = await puppeteer.launch({ headless: true, args: ["--no-sandbox"] });
const page = await browser.newPage();

// Load mermaid from CDN once
await page.setContent(`<!DOCTYPE html><html><body>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <script>mermaid.initialize({ startOnLoad: false, theme: 'base', themeVariables: { lineColor: '#FF0000' } });</script>
</body></html>`);
await page.waitForFunction(() => typeof mermaid !== "undefined");

let success = 0;
for (const mmdFile of mmdFiles) {
  const inputPath = join(diagramsDir, mmdFile);
  const outputPath = join(diagramsDir, mmdFile.replace(".mmd", ".svg"));
  const code = readFileSync(inputPath, "utf-8");

  try {
    const svg = await page.evaluate(async (code) => {
      const { svg } = await mermaid.render("diagram", code);
      return svg;
    }, code);
    writeFileSync(outputPath, svg);
    success++;
  } catch (err) {
    console.error(`Failed: ${mmdFile}: ${err.message}`);
  }
}

await browser.close();
console.log(`Rendered ${success}/${mmdFiles.length} diagrams`);
