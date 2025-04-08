#!/bin/bash

# Crear carpeta de navegadores en /tmp/playwright
mkdir -p /tmp/playwright

# Descargar los navegadores en esa carpeta
PLAYWRIGHT_BROWSERS_PATH=/tmp/playwright npx playwright install chromium
