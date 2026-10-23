#!/usr/bin/env python3
"""Generate a wholly synthetic, exact-reconciling 500k inventory population."""
from __future__ import annotations
import argparse
import csv
import gzip
import json
import random
from datetime import date, timedelta
from pathlib import Path

N_DEFAULT = 500_000
SEED_DEFAULT = 20251231
CURRENT_HORIZON = date(2026, 12, 31)
# Public consolidated balances, DFP 2025 Nota 5, in cents.
CLASSES = [
    {"code": "TERRENOS_A_INCORPORAR", "label": "Terrenos a incorporar", "count": 420_000,
     "total": 567_823_800_000, "current": 81_356_500_000, "noncurrent": 486_467_300_000},
    {"code": "IMOVEIS_EM_CONSTRUCAO", "label": "Imóveis em construção", "count": 75_000,
     "total": 117_420_700_000, "current": 117_420_700_000, "noncurrent": 0},
    {"code": "IMOVEIS_CONCLUIDOS", "label": "Imóveis concluídos", "count": 5_000,
     "total": 9_906_300_000, "current": 9_906_300_000, "noncurrent": 0},
]
INVENTORY_TOTAL = sum(x["total"] for x in CLASSES)
CURRENT_TOTAL = sum(x["current"] for x in CLASSES)
NONCURRENT_TOTAL = sum(x["noncurrent"] for x in CLASSES)
FIELDS = [
    "synthetic_item_id", "synthetic_contract_id", "synthetic_project_id",
    "synthetic_registry_reference", "inventory_class", "item_type",
    "uf_code", "municipality_code_synthetic", "area_m2",
    "acquisition_date", "planned_realization_date", "classification_at_2025_12_31",
    "title_status", "title_registration_date", "valuation_date",
    "historical_cost_cents_synthetic", "book_value_cents_synthetic",
    "estimated_nrv_cents_synthetic", "injected_exception_code", "synthetic_record",
]
EXCEPTIONS = {
    "TITLE_DOCUMENT_INCOMPLETE": 200,
    "AREA_INVALID": 150,
    "NRV_BELOW_BOOK": 500,
    "CLASSIFICATION_MISMATCH": 250,
    "VALUATION_STALE": 300,
}


def allocate_exact(total_cents: int, n: int, rng: random.Random) -> list[int]:
    """Allocate positive integer cents with a skewed distribution and exact sum."""
    floor_cents = 100
    if total_cents < floor_cents * n:
        raise ValueError("Class balance is too small to assign positive values to all synthetic items.")
    remaining = total_cents - floor_cents * n
    weights = [0.15 + rng.gammavariate(1.8, 1.0) for _ in range(n)]
    denom = sum(weights)
    raw = [remaining * w / denom for w in weights]
    whole = [int(x) for x in raw]
    left = remaining - sum(whole)
    fractions = [x - int(x) for x in raw]
    for idx in sorted(range(n), key=fractions.__getitem__, reverse=True)[:left]:
        whole[idx] += 1
    values = [floor_cents + v for v in whole]
    assert sum(values) == total_cents and min(values) >= floor_cents
    return values


def build(out_path: Path, n: int = N_DEFAULT, seed: int = SEED_DEFAULT) -> dict:
    if n != N_DEFAULT:
        raise ValueError("A geração reproduzível foi parametrizada para exatamente 500.000 registros.")
    if sum(x["count"] for x in CLASSES) != n:
        raise AssertionError("Class counts do not sum to population size.")
    rng = random.Random(seed)
    records: list[dict] = []
    current_set_by_class: dict[str, set[int]] = {}
    for cls in CLASSES:
        indices = list(range(cls["count"]))
        current_n = round(cls["count"] * cls["current"] / cls["total"]) if cls["noncurrent"] else cls["count"]
        current_set_by_class[cls["code"]] = set(rng.sample(indices, current_n))
        current_indices = sorted(current_set_by_class[cls["code"]])
        noncurrent_indices = [i for i in indices if i not in current_set_by_class[cls["code"]]]
        values = [0] * cls["count"]
        if cls["current"]:
            allocated = allocate_exact(cls["current"], len(current_indices), rng)
            for i, amount in zip(current_indices, allocated): values[i] = amount
        if cls["noncurrent"]:
            allocated = allocate_exact(cls["noncurrent"], len(noncurrent_indices), rng)
            for i, amount in zip(noncurrent_indices, allocated): values[i] = amount
        assert sum(values) == cls["total"]
        records.extend({"class": cls, "class_index": i, "value": values[i],
                        "current": i in current_set_by_class[cls["code"]]}
                       for i in range(cls["count"]))

    if sum(x["value"] for x in records) != INVENTORY_TOTAL:
        raise AssertionError("Inventory allocation failed to reconcile.")
    shuffled = list(range(n))
    rng.shuffle(shuffled)
    injected: dict[int, str] = {}
    cursor = 0
    for code, size in EXCEPTIONS.items():
        for idx in shuffled[cursor:cursor + size]: injected[idx] = code
        cursor += size

    uf_codes = ["MG", "SP", "RJ", "GO", "DF", "BA", "CE", "PE", "SC", "ES"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    opener = gzip.open if out_path.suffix == ".gz" else open
    mode = "wt" if out_path.suffix == ".gz" else "w"
    class_sums = {x["code"]: 0 for x in CLASSES}
    current_sum = noncurrent_sum = 0
    exception_ids = {code: [] for code in EXCEPTIONS}
    with opener(out_path, mode, newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for i, rec in enumerate(records):
            cls, amount, is_current = rec["class"], rec["value"], rec["current"]
            code = cls["code"]
            class_sums[code] += amount
            current_sum += amount if is_current else 0
            noncurrent_sum += 0 if is_current else amount
            item_type = {
                "TERRENOS_A_INCORPORAR": "PARCELA_DE_TERRENO",
                "IMOVEIS_EM_CONSTRUCAO": "UNIDADE_EM_CONSTRUCAO",
                "IMOVEIS_CONCLUIDOS": "UNIDADE_CONCLUIDA",
            }[code]
            acq = date(2018, 1, 1) + timedelta(days=rng.randint(0, 7 * 365))
            planned = (date(2026, 1, 1) + timedelta(days=rng.randint(0, 364))) if is_current else (date(2027, 1, 1) + timedelta(days=rng.randint(0, 6 * 365)))
            classification = "CIRCULANTE" if is_current else "NAO_CIRCULANTE"
            valuation = date(2025, 1, 1) + timedelta(days=rng.randint(0, 364))
            area = rng.randint(500, 400_000) if code == "TERRENOS_A_INCORPORAR" else rng.randint(25, 300)
            title_status = "DOCUMENTADO"
            title_date = acq + timedelta(days=rng.randint(1, 180))
            exception = injected.get(i, "")
            if exception == "TITLE_DOCUMENT_INCOMPLETE": title_status, title_date = "PENDENTE", None
            elif exception == "AREA_INVALID": area = 0
            elif exception == "CLASSIFICATION_MISMATCH":
                if is_current: planned = date(2027, 1, 1) + timedelta(days=rng.randint(0, 365))
                else: planned = date(2026, 1, 1) + timedelta(days=rng.randint(0, 364))
            elif exception == "VALUATION_STALE": valuation = date(2021, 1, 1) + timedelta(days=rng.randint(0, 364))
            if exception == "NRV_BELOW_BOOK": nrv = max(100, int(amount * rng.uniform(0.70, 0.95)))
            else: nrv = int(amount * rng.uniform(1.01, 1.20))
            item_id = f"SYN-INV-{i + 1:07d}"
            if exception: exception_ids[exception].append(item_id)
            writer.writerow({
                "synthetic_item_id": item_id,
                "synthetic_contract_id": f"SYN-CON-{i + 1:07d}",
                "synthetic_project_id": f"SYN-PRJ-{(i % 350) + 1:04d}",
                "synthetic_registry_reference": f"SYN-REG-{i + 1:07d}",
                "inventory_class": code,
                "item_type": item_type,
                "uf_code": rng.choice(uf_codes),
                "municipality_code_synthetic": f"SYN-MUN-{(i % 1400) + 1:04d}",
                "area_m2": area,
                "acquisition_date": acq.isoformat(),
                "planned_realization_date": planned.isoformat(),
                "classification_at_2025_12_31": classification,
                "title_status": title_status,
                "title_registration_date": title_date.isoformat() if title_date else "",
                "valuation_date": valuation.isoformat(),
                "historical_cost_cents_synthetic": amount,
                "book_value_cents_synthetic": amount,
                "estimated_nrv_cents_synthetic": nrv,
                "injected_exception_code": exception,
                "synthetic_record": "YES — DADOS SINTÉTICOS",
            })

    assert class_sums == {x["code"]: x["total"] for x in CLASSES}
    assert current_sum == CURRENT_TOTAL and noncurrent_sum == NONCURRENT_TOTAL
    result = {
        "dataset": str(out_path), "record_count": n, "unique_synthetic_item_ids": n,
        "seed": seed, "total_book_value_cents": INVENTORY_TOTAL,
        "total_book_value_brl": INVENTORY_TOTAL / 100,
        "current_book_value_cents": current_sum, "noncurrent_book_value_cents": noncurrent_sum,
        "class_totals_brl": {k: v / 100 for k, v in class_sums.items()},
        "injected_exceptions": EXCEPTIONS,
        "exception_ids": exception_ids,
        "nature": "Todos os identificadores, itens, contratos, projetos, datas, valores, localidades e exceções são sintéticos. A alocação concilia somente como exercício aritmético aos saldos públicos da rubrica Estoques; não representa registros, unidades ou operações reais da companhia.",
    }
    (out_path.parent / "injection_register.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="/home/ubuntu/direcional_audit/data/estoques_sinteticos.csv.gz")
    parser.add_argument("--rows", type=int, default=N_DEFAULT)
    parser.add_argument("--seed", type=int, default=SEED_DEFAULT)
    args = parser.parse_args()
    result = build(Path(args.out), args.rows, args.seed)
    print(json.dumps({k: v for k, v in result.items() if k != "exception_ids"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
