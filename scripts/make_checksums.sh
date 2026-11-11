#!/bin/sh
# Gera CHECKSUMS.sha256 com o SHA-256 dos arquivos da versão fechada.
# Verificação: sha256sum -c CHECKSUMS.sha256
set -e
cd "$(dirname "$0")/.."
find workpapers analysis data scripts reports -type f \( -name '*.md' -o -name '*.csv' -o -name '*.json' -o -name '*.xlsx' -o -name '*.py' -o -name '*.sh' -o -name '*.gz' -o -name '*.css' \) | sort > /tmp/files.txt
printf '%s\n' README.md FONTES.md MATRIZ_NORMAS.md Dossie_Auditoria_Direcional_2025.md Dossie_Auditoria_Direcional_2025.pdf >> /tmp/files.txt
xargs sha256sum < /tmp/files.txt > CHECKSUMS.sha256
echo "CHECKSUMS.sha256: $(wc -l < CHECKSUMS.sha256) arquivos"
