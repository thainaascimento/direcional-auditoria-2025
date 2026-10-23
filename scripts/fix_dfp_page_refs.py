#!/usr/bin/env python3
"""Corrige referências impressas à DFP Direcional 2025 com base no PDF integral.

O BP consolidado está nas páginas impressas 16–17; a Demonstração do Resultado,
na p.21; a Nota 5, p.69; e o relatório do auditor, pp.115–117.
Idempotente; não altera valores nem conclusões.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [*ROOT.glob("workpapers/*.md"), ROOT / "reports/relatorio_integrado.md", ROOT / "Dossie_Auditoria_Direcional_2025.md"]
changed_files = 0
changed_lines = 0
for path in TARGETS:
    if not path.exists():
        continue
    original = path.read_text(encoding="utf-8")
    output_lines = []
    edits = 0
    for line in original.splitlines(keepends=True):
        new = line
        # A faixa 16–19 era uma referência conjunta ao BP e às demonstrações
        # subsequentes; o BP ocupa pp. 16–17 e a DRE, p. 21.
        new = re.sub(r"(?<!\d)16[–-]19(?!\d)", "16–17, 21", new)
        # Quando citada explicitamente, a DRE está na página impressa 21,
        # e não nas pp. 18–19 (que contêm o passivo).
        if re.search(r"\bDRE\b|Demonstração do Resultado", new, flags=re.IGNORECASE):
            new = re.sub(r"\bpp?\.\s*18[–-]19\b", "p.21", new)
        if new != line:
            edits += 1
        output_lines.append(new)
    updated = "".join(output_lines)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        changed_files += 1
        changed_lines += edits
        print(f"Corrigido: {path.relative_to(ROOT)} ({edits} linhas)")
print(f"Total: {changed_files} arquivos, {changed_lines} linhas corrigidas.")
