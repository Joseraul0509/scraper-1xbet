#!/bin/bash

echo "Instalando dependencias del sistema..."
apt-get update
apt-get install -y wget curl unzip fonts-liberation libnss3 libatk-bridge2.0-0 libxss1 libgtk-3-0 libasound2 libgbm-dev

echo "Instalando Playwright Chromium..."
playwright install chromium
