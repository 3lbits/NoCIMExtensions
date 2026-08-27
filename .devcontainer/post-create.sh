#!/bin/bash
set -e

# Chromium dependencies for puppeteer SVG rendering
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
  libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxdamage1 \
  libxrandr2 libgbm1 libasound2 libpangocairo-1.0-0 libxshmfence1 \
  libxkbcommon0 libxcomposite1 libpango-1.0-0 libcairo2 \
  && sudo rm -rf /var/lib/apt/lists/*

pip install -r requirements.txt
pip install -e .
npm install
npx puppeteer browsers install chrome
