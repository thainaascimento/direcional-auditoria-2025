#!/usr/bin/env python3
"""Assemble the executive report, norm coverage, source list, and 27 workpapers."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAPERS = [
    "PT-EC", "PT-200", "PT-210", "PT-220", "PT-230", "PT-240", "PT-250",
    "PT-260", "PT-265", "PT-300", "PT-315", "PT-320", "PT-330", "PT-402",
    "PT-450", "PT-500", "PT-501", "PT-505", "PT-510", "PT-520", "PT-530",
    "PT-540", "PT-550", "PT-560", "PT-570", "PT-580", "PT-600",
]

def find_matrix() -> Path:
    for path in (ROOT / "MATRIZ_NORMAS.md", ROOT / "workpapers" / "MATRIZ_NORMAS.md"):
        if path.exists():
            return path
    candidates = [
        path for folder in (ROOT, ROOT / "workpapers")
        for path in folder.glob("*.md")
        if "matriz" in path.name.casefold() and "norma" in path.name.casefold()
    ]
    if candidates:
        return sorted(candidates, key=lambda p: (len(p.name), p.name.casefold()))[0]
    raise FileNotFoundError("MATRIZ_NORMAS.md não foi entregue pelo fluxo normativo")

def expose_reference_definitions(text: str) -> str:
    """Render Markdown link definitions as a visible, source-labeled reference list."""
    definition_pattern = re.compile(r'^\[([^\]]+)\]:\s*(\S+)(?:\s+"([^"]*)")?\s*$', re.M)
    definitions = list(definition_pattern.finditer(text))
    if not definitions:
        return text
    items = []
    for match in definitions:
        label, url, title = match.groups()
        items.append(f"- **Ref. {label}** — {title or 'Fonte'}; [abrir fonte](<{url}>).")
    block = "**Fontes citadas neste papel:**\n\n" + "\n".join(items)
    visible_text = definition_pattern.sub("", text)
    visible_text = re.sub(r"\n{3,}", "\n\n", visible_text)
    headings = list(re.finditer(r'^#{1,6}\s+(?:(?:\d+(?:\.\d+)*\.?\s+)?)Refer[eê]ncias\s*$', visible_text, re.M | re.I))
    if not headings:
        return text
    heading = headings[-1]
    return visible_text[:heading.end()] + "\n\n" + block + visible_text[heading.end():]

def main():
    executive = ROOT / "reports" / "relatorio_integrado.md"
    sources = ROOT / "FONTES.md"
    matrix = find_matrix()
    if not executive.exists() or not sources.exists():
        raise FileNotFoundError("Relatório executivo ou FONTES.md ausente")
    canonical_matrix = ROOT / "MATRIZ_NORMAS.md"
    if matrix.resolve() != canonical_matrix.resolve():
        canonical_matrix.write_text(matrix.read_text(encoding="utf-8"), encoding="utf-8")
        matrix = canonical_matrix
    paper_paths = [ROOT / "workpapers" / f"{name}.md" for name in PAPERS]
    missing = [p.name for p in paper_paths if not p.exists()]
    if missing:
        raise FileNotFoundError("Papéis pendentes: " + ", ".join(missing))

    intro = executive.read_text(encoding="utf-8")
    intro = intro.replace("[FONTES.md](FONTES.md)", "Apêndice B — Fontes públicas")
    intro = intro.replace("[MATRIZ_NORMAS.md](MATRIZ_NORMAS.md)", "Apêndice A — Matriz de cobertura das normas")
    pieces = [intro.rstrip(), "\n\n---\n\n**Apêndice A — Matriz de cobertura das normas**\n\n", matrix.read_text(encoding="utf-8").strip()]
    pieces.extend(["\n\n---\n\n**Apêndice B — Fontes públicas**\n\n", sources.read_text(encoding="utf-8").strip()])
    pieces.append("\n\n---\n\n**Apêndice C — Papéis de trabalho**\n")
    for name, path in zip(PAPERS, paper_paths):
        text = expose_reference_definitions(path.read_text(encoding="utf-8").strip())
        pieces.append(f"\n\n---\n\n{text}\n")
    full = "\n".join(pieces).replace("\n\n\n", "\n\n") + "\n"
    # The Typst Markdown route treats unescaped $...$ as inline math; currency
    # markers are literal text and must remain visible in the exported PDF.
    full = re.sub(r"(?<!\\)R\$", r"R\\$", full)
    output = ROOT / "Dossie_Auditoria_Direcional_2025.md"
    output.write_text(full, encoding="utf-8")
    typst_source = ROOT / "reports" / "typst" / "source.md"
    typst_source.write_text(full, encoding="utf-8")
    print(f"Dossiê consolidado: {output} ({len(full):,} caracteres; {len(PAPERS)} papéis)")
    print(f"Fonte Typst atualizada: {typst_source}")

if __name__ == "__main__":
    main()
