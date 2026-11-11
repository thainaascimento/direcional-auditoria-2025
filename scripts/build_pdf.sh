#!/bin/sh
# Gera o PDF do dossiê a partir do Markdown consolidado (pandoc + wkhtmltopdf).
set -e
cd "$(dirname "$0")/.."
pandoc Dossie_Auditoria_Direcional_2025.md -f gfm -t html5 -s \
  --metadata pagetitle="Dossiê didático de auditoria — Direcional 2025" \
  -c reports/pdf_style.css --embed-resources -o /tmp/dossie.html
wkhtmltopdf --quiet -O Landscape -s A4 -T 12mm -B 14mm -L 12mm -R 12mm \
  --enable-local-file-access /tmp/dossie.html Dossie_Auditoria_Direcional_2025.pdf
