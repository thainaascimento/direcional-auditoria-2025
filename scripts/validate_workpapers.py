#!/usr/bin/env python3
"""Validar completude dos papéis e sinalizar inconsistências factuais contextuais."""
from pathlib import Path
import csv
import json
import re
from assemble_dossier import PAPERS
from openpyxl import load_workbook

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
        required_artifacts = {
            "PT-505.md": ["Modelo de carta de confirmação", "Controle de circularização", "Quadro de tratamento de diferenças", "Procedimentos alternativos"],
            "PT-265.md": ["Matriz de deficiências", "Condição (", "Critério", "Causa", "Efeito", "Recomendação"],
            "PT-230.md": ["Convenção de códigos", "Controle de versões", "Montagem e guarda", "Índice do arquivo"],
        }
        for needle in required_artifacts.get(path.name, []):
            if needle.lower() not in text.lower():
                issues.append(f"{path.name}: artefato exigido pelo roteiro ausente ({needle})")
        if "242011273" not in text:
            issues.append(f"{path.name}: matrícula 242011273 ausente")
        if "EDU-AUD" in text:
            issues.append(f"{path.name}: identificador provisório EDU-AUD ainda presente")
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
            for required in ("data/estoques_sinteticos.csv.gz", "R$6.951.508.000,00", "500.000 registros distintos", "amostra_aleatoria_10000.csv", "sensibilidade_deteccao.csv", "sensibilidade_monetaria.csv", "9.886", "95,17%"):
                if required not in text:
                    issues.append(f"PT-530: falta evidência textual da revisão da amostragem ({required})")
            if "terrenos_sinteticos.csv.gz" in text:
                issues.append("PT-530: ainda aponta para o arquivo anterior de terrenos")
            if "amostra_aleatoria_1000.csv" in text or "algoritmo de reservatório" in text:
                issues.append("PT-530: contém nome/descrição obsoleta da amostra anterior")

        if name == "PT-320" and re.search(r"R\$\s*28[.,]391[.,]190", text):
            issues.append("PT-320: ainda conserva a materialidade específica antiga de terrenos")

    results_path = ROOT / "analysis" / "PT530_resultados.json"
    if results_path.is_file():
        results = json.loads(results_path.read_text(encoding="utf-8"))
        basis = results.get("sample_size_basis", {})
        if results.get("sample_size") != 10_000:
            issues.append("PT-530: tamanho da SRS nos resultados não é 10.000")
        if basis.get("minimum_n_exact_hypergeometric") != 9_886 or basis.get("selected_n_rounded_up") != 10_000:
            issues.append("PT-530: dimensionamento hipergeométrico não confere com o cenário de 0,03%")
        if basis.get("probability_at_selected_n_pct", 0) < 95 or basis.get("probability_at_original_n_1000_pct", 100) >= 30:
            issues.append("PT-530: sensibilidade de detecção não atende aos resultados documentados")
        sensitivity_path = ROOT / "analysis" / "sensibilidade_deteccao.csv"
        if not sensitivity_path.is_file() or len(list(csv.DictReader(sensitivity_path.open(encoding="utf-8")))) != 7:
            issues.append("PT-530: tabela CSV de sensibilidade de detecção ausente ou incompleta")
        sample_path = ROOT / "analysis" / "amostra_aleatoria_10000.csv"
        if not sample_path.is_file():
            issues.append("PT-530: CSV da SRS de 10.000 ausente")
        else:
            with sample_path.open(newline="", encoding="utf-8") as f:
                sample_rows = list(csv.DictReader(f))
            sample_ids = [row["synthetic_item_id"] for row in sample_rows]
            if len(sample_rows) != 10_000 or len(set(sample_ids)) != 10_000:
                issues.append("PT-530: CSV da SRS não contém exatamente 10.000 IDs únicos")
        workbook_path = ROOT / "analysis" / "papel_amostragem_conciliacao.xlsx"
        if workbook_path.is_file():
            workbook = load_workbook(workbook_path, read_only=True, data_only=True)
            required_sheets = {"Sensibilidade detecção", "Sensibilidade monetária", "Amostra SRS"}
            if not required_sheets.issubset(set(workbook.sheetnames)):
                issues.append("PT-530: planilha sem uma ou mais abas de sensibilidade/amostra")
            workbook.close()
        else:
            issues.append("PT-530: planilha de conciliação/amostragem ausente")

    print(f"Papéis esperados: {len(PAPERS)}; ausentes: {len(missing)}; alertas: {len(issues)}")
    for name in missing:
        print("AUSENTE:", name)
    for issue in issues:
        print("REVISAR:", issue)
    return 1 if missing or issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
