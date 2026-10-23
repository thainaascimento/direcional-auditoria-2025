# Índice dos papéis de trabalho

## Escopo e uso

Este índice organiza os 27 papéis do dossiê didático de auditoria da DIRECIONAL ENGENHARIA S.A., demonstrações consolidadas de 2025. A cobertura norma → PT está na [matriz de normas](../MATRIZ_NORMAS.md); as fontes societárias, URLs, datas de acesso e páginas impressas estão em [`../FONTES.md`](../FONTES.md). Os papéis preservam em cada procedimento a classificação obrigatória: **realizado com evidência pública**, **planejado por falta de acesso** ou **simulado para fins didáticos**.

A DFP integral pública foi obtida diretamente no RI e examinada nas páginas impressas citadas. Não foram obtidos registros internos, razão, contratos, confirmações, entrevistas, inspeção física nem documentação privada da PwC. A base de 500.000 itens da rubrica Estoques é inteiramente sintética; nenhum terreno, unidade, contrato ou transação corresponde a registro real. Nenhum documento do conjunto expressa opinião independente ou asseguração.

## Roteiro dos papéis

| # | Papel | Tema | Arquivo |
|---:|---|---|---|
| 1 | PT-EC | Estrutura Conceitual para Trabalhos de Asseguração | [`PT-EC.md`](PT-EC.md) |
| 2 | PT-200 | Objetivos gerais do auditor independente | [`PT-200.md`](PT-200.md) |
| 3 | PT-210 | Concordância com os termos do trabalho | [`PT-210.md`](PT-210.md) |
| 4 | PT-220 | Gestão da qualidade da auditoria | [`PT-220.md`](PT-220.md) |
| 5 | PT-230 | Documentação de auditoria | [`PT-230.md`](PT-230.md) |
| 6 | PT-240 | Responsabilidade em relação à fraude | [`PT-240.md`](PT-240.md) |
| 7 | PT-250 | Leis e regulamentos | [`PT-250.md`](PT-250.md) |
| 8 | PT-260 | Comunicação com a governança | [`PT-260.md`](PT-260.md) |
| 9 | PT-265 | Deficiências de controle interno | [`PT-265.md`](PT-265.md) |
| 10 | PT-300 | Planejamento da auditoria | [`PT-300.md`](PT-300.md) |
| 11 | PT-315 | Identificação e avaliação de riscos | [`PT-315.md`](PT-315.md) |
| 12 | PT-320 | Materialidade | [`PT-320.md`](PT-320.md) |
| 13 | PT-330 | Respostas aos riscos avaliados | [`PT-330.md`](PT-330.md) |
| 14 | PT-402 | Entidade que utiliza prestador de serviços | [`PT-402.md`](PT-402.md) |
| 15 | PT-450 | Avaliação das distorções identificadas | [`PT-450.md`](PT-450.md) |
| 16 | PT-500 | Evidência de auditoria | [`PT-500.md`](PT-500.md) |
| 17 | PT-501 | Estoques, litígios e informações por segmento | [`PT-501.md`](PT-501.md) |
| 18 | PT-505 | Confirmações externas (modelos; sem envio real) | [`PT-505.md`](PT-505.md) |
| 19 | PT-510 | Saldos iniciais e auditoria inicial didática | [`PT-510.md`](PT-510.md) |
| 20 | PT-520 | Procedimentos analíticos | [`PT-520.md`](PT-520.md) |
| 21 | PT-530 | Amostragem aplicada à base sintética | [`PT-530.md`](PT-530.md) |
| 22 | PT-540 | Estimativas contábeis e divulgações | [`PT-540.md`](PT-540.md) |
| 23 | PT-550 | Partes relacionadas | [`PT-550.md`](PT-550.md) |
| 24 | PT-560 | Eventos subsequentes | [`PT-560.md`](PT-560.md) |
| 25 | PT-570 | Continuidade operacional | [`PT-570.md`](PT-570.md) |
| 26 | PT-580 | Representações formais | [`PT-580.md`](PT-580.md) |
| 27 | PT-600 | Auditoria de demonstrações de grupos | [`PT-600.md`](PT-600.md) |

## Artefatos reproduzíveis relacionados

- População integral de Estoques: `../data/estoques_sinteticos.csv.gz`; esquema: `../analysis/dicionario_variaveis.csv`; registro das injeções: `../data/injection_register.json`.
- Resultados, amostras e conciliação: `../analysis/PT530_resultados.json`, `../analysis/amostra_aleatoria_1000.csv`, `../analysis/amostra_direcionada_top200.csv`, `../analysis/excecoes_detectadas_sinteticas.csv` e `../analysis/papel_amostragem_conciliacao.xlsx`.
- Planilha complementar de riscos/programas: `../analysis/analises_e_programas.xlsx`.
- Código reprodutível: `../scripts/generate_synthetic_inventory.py`, `../scripts/analyze_synthetic_inventory.py`, `../scripts/build_audit_support.py`, `../scripts/fix_dfp_page_refs.py`, `../scripts/validate_workpapers.py` e `../scripts/assemble_dossier.py`.

A presença de um PT indica cobertura documental didática do roteiro, não a execução de auditoria real nem a validação completa dos registros da companhia.
