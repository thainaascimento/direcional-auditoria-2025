#!/usr/bin/env python3
"""Validar completude dos papéis e sinalizar inconsistências factuais contextuais."""
from pathlib import Path
import re
from assemble_dossier import PAPERS

ROOT = Path(__file__).resolve().parents[1]
WORKPAPERS = ROOT / "workpapers"
REQUIRED_TERMS = {
    "norma/itens": re.compile(r"NBC\s*TA|Estrutura Conceitual", re.I),
    "objetivo": re.compile(r"objetivo", re.I),
    "riscos/afirmações": re.compile(r"risco|afirmaç", re.I),
    "população": re.compile(r"populaç", re.I),
    "procedimentos": re.compile(r"procedimento", re.I),
    "evidências/referências": re.compile(r"evidênc|referênc", re.I),
    "resultados/exceções": re.compile(r"resultado|exceç", re.I),
    "conclusão/limitações": re.compile(r"conclusão|limitaç", re.I),
    "preparador/data": re.compile(r"preparador|data de preparaç", re.I),
    "revisão": re.compile(r"revisão|revisor", re.I),
}


def paragraph_context(text: str, start: int, end: int, radius: int = 220) -> str:
    """Return local context across wrapped Markdown/table lines."""
    left_break = text.rfind("\n\n", 0, start)
    left = max(left_break, start - radius)
    right_break = text.find("\n\n", end)
    right_candidates = [pos for pos in (right_break, end + radius) if pos >= 0]
    right = min(right_candidates) if right_candidates else len(text)
    return text[left:right]


def main() -> int:
    missing = [name for name in PAPERS if not (WORKPAPERS / f"{name}.md").is_file()]
    issues: list[str] = []
    for name in PAPERS:
        path = WORKPAPERS / f"{name}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in REQUIRED_TERMS.items():
            if not pattern.search(text):
                issues.append(f"{path.name}: sem marcador detectável de {label}")

        for match in re.finditer(r"3\.888\.979", text):
            context = paragraph_context(text, match.start(), match.end())
            if not re.search(r"não\s*circulante|componente\s+não\s*circulante|non.?current", context, re.I):
                line = text.count("\n", 0, match.start()) + 1
                issues.append(f"{path.name}:{line}: R$3.888.979 mil requer identificação como componente não circulante de terrenos em 2024")

        for match in re.finditer(r"4\.864\.673", text):
            context = paragraph_context(text, match.start(), match.end())
            if re.search(r"terrenos?|a\s+incorporar", context, re.I) and not re.search(r"não\s*circulante|componente|derivad", context, re.I):
                line = text.count("\n", 0, match.start()) + 1
                issues.append(f"{path.name}:{line}: confirmar que R$4.864.673 mil é componente não circulante, não total de terrenos")

        for n, line in enumerate(text.splitlines(), 1):
            if re.search(r"\bDRE\b.{0,100}18[–-]19|18[–-]19.{0,100}\bDRE\b", line, re.I):
                issues.append(f"{path.name}:{n}: DRE da DFP está na p.21, não nas pp.18–19")

        # A CVM/RAD interface may lack pagination while the RI PDF remains available.
        # Require an unqualified document-unavailability statement before flagging it.
        negative = re.search(
            r"(?:DFP|demonstrações|notas).{0,100}(?:não\s+(?:foi|foram|se)\s+(?:obtido|obtidos|acessado|acessados|disponibilizado|disponibilizadas)|não\s+disponibilizou)",
            text,
            re.I | re.S,
        )
        positive = re.search(
            r"(?:DFP|PDF).{0,140}(?:integral|obtido|obtida|examinado|examinada|lido|diretamente)",
            text,
            re.I | re.S,
        )
        if negative and not positive:
            issues.append(f"{path.name}: alegação possivelmente desatualizada de DFP/notas integrais indisponíveis")

        stale_public_dfp_claims = (
            r"não revelou integralmente as notas",
            r"dados-base do enunciado atribuídos à DFP",
            r"valores publicados fornecidos",
        )
        for phrase in stale_public_dfp_claims:
            if re.search(phrase, text, re.I):
                issues.append(f"{path.name}: alegação documental preliminar desatualizada ({phrase})")

        if name == "PT-600":
            if "api.mziq.com/mzfilemanager" not in text or not re.search(r"DFP integral pública.{0,80}obtida no RI", text, re.I):
                issues.append("PT-600: falta referência direta ou registro de exame da DFP pública integral do RI")

        if name == "PT-530":
            for required in ("data/estoques_sinteticos.csv.gz", "R$6.951.508.000,00", "500.000 registros distintos"):
                if required not in text:
                    issues.append(f"PT-530: falta evidência textual da população integral de Estoques ({required})")
            if "terrenos_sinteticos.csv.gz" in text:
                issues.append("PT-530: ainda aponta para o arquivo anterior de terrenos")

        if name == "PT-320" and re.search(r"R\$\s*28[.,]391[.,]190", text):
            issues.append("PT-320: ainda conserva a materialidade específica antiga de terrenos")

    print(f"Papéis esperados: {len(PAPERS)}; ausentes: {len(missing)}; alertas: {len(issues)}")
    for name in missing:
        print("AUSENTE:", name)
    for issue in issues:
        print("REVISAR:", issue)
    return 1 if missing or issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
