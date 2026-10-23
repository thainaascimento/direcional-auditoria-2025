# Dossiê didático de auditoria — Direcional Engenharia S.A. — 2025

**Preparador:** EDU-AUD-001 (matrícula didática, sem identificação de pessoa real) · **Data:** 22/10/2026 · **Revisão:** campo em branco; nenhum revisor ou assinatura foi simulado.

## Natureza e limites

Este é um dossiê acadêmico/didático construído com documentos públicos e uma população **inteiramente sintética**. Não é uma auditoria contratada ou executada sobre os livros da Direcional, não inclui acesso a controles internos, contratos, matrículas de imóveis, razões auxiliares, bancos, assessores jurídicos ou sistemas e **não contém opinião profissional independente**. A opinião sem ressalva citada é a do auditor da companhia, PwC, no relatório público de 2025; não é opinião deste trabalho.

Os fatos da companhia foram obtidos somente em documentos públicos da CVM, da B3 e da área de RI da Direcional. O texto das normas foi consultado em fonte oficial do CFC apenas para identificar os critérios normativos e suas versões; não foi usado como evidência societária. A data de corte das pesquisas de eventos subsequentes é 22/10/2026. Nenhum item, contrato, matrícula, unidade, projeto ou valor individual da base sintética é registro real da companhia.

A DFP de 2025 informa Estoques de R$6.951.508 mil, a maior rubrica individual do ativo consolidado. A Nota 5 detalha terrenos a incorporar de R$5.678.238 mil, imóveis em construção de R$1.174.207 mil e imóveis concluídos de R$99.063 mil. A população sintética contém 500.000 itens únicos, abrange as três classes e soma exatamente R$6.951.508.000,00, inclusive R$2.086.835.000,00 circulantes e R$4.864.673.000,00 não circulantes. Essa conciliação é aritmética e deliberada; **não** valida qualquer registro real da companhia.

## Estrutura do pacote

- `Dossie_Auditoria_Direcional_2025.pdf` — dossiê consolidado, incluindo os papéis de trabalho e referências cruzadas.
- `Dossie_Auditoria_Direcional_2025.md` — fonte editável do relatório consolidado.
- `MATRIZ_NORMAS.md` — cobertura da Estrutura Conceitual e das NBC TAs do roteiro.
- `workpapers/INDEX.md` e `workpapers/` — índice e 27 papéis de trabalho individuais, PT EC e PTs 200 a 600 do roteiro.
- `analysis/papel_amostragem_conciliacao.xlsx` — arquivo editável com materialidade, saldos, reconciliação, cálculo da amostra, testes, fontes, dicionário e amostra aleatória.
- `analysis/analises_e_programas.xlsx` — análises, matriz de riscos, programas por ciclo e mapa de distorções simuladas.
- `data/estoques_sinteticos.csv.gz` — população sintética integral da rubrica Estoques (500.000 linhas, CSV comprimido), com itens de terrenos, obras em andamento e imóveis concluídos.
- `analysis/amostra_aleatoria_1000.csv` e `analysis/amostra_direcionada_top200.csv` — seleções reproduzíveis, respectivamente SRS sem reposição e seleção direcionada dos 200 maiores valores.
- `analysis/excecoes_detectadas_sinteticas.csv`, `analysis/PT530_resultados.json` e `data/injection_register.json` — resultados dos testes e registro das exceções intencionalmente implantadas.
- `analysis/dicionario_variaveis.csv` — dicionário da base.
- `scripts/generate_synthetic_inventory.py` e `scripts/analyze_synthetic_inventory.py` — código que gera a população integral de Estoques e reproduz amostra, exceções, conciliações e planilha PT530.
- `scripts/build_audit_support.py` — código da planilha editável de análises e programas.
- `scripts/assemble_dossier.py` — consolida o relatório, a matriz normativa, as fontes e os papéis em Markdown.
- `scripts/validate_workpapers.py` — verifica a completude formal dos 27 papéis e sinaliza dados públicos preliminares a revisar.
- `scripts/fix_dfp_page_refs.py` — normaliza referências à paginação impressa da DFP (BP pp.16–17; DRE p.21; Nota 5 p.69; relatório pp.115–117).
- `FONTES.md` — endereços, documentos, exercícios, datas de acesso e páginas.
- `.typst-content-manifest.json`, `.typst-build-plan.json`, `reports/` — manifest/plano e fontes de compilação/verificação do PDF.

## Reprodução

Requisitos: Python 3.10+ e `openpyxl` para a geração das planilhas. A base e as análises usam sementes fixas e código Python padrão para gerar os dados.

```bash
python3 scripts/generate_synthetic_inventory.py \
  --out data/estoques_sinteticos.csv.gz

python3 scripts/analyze_synthetic_inventory.py \
  --input data/estoques_sinteticos.csv.gz \
  --outdir analysis \
  --sample-size 1000 \
  --seed 20251232

python3 scripts/fix_dfp_page_refs.py
python3 scripts/validate_workpapers.py
python3 scripts/build_audit_support.py
python3 scripts/assemble_dossier.py
typst compile reports/typst/main.typ Dossie_Auditoria_Direcional_2025.pdf
```

Os testes em 100% da população sintética encontraram exatamente as cinco classes implantadas: 200 pendências documentais, 150 áreas inválidas, 500 sinais sintéticos de valor realizável líquido abaixo do valor contábil, 250 divergências de classificação e 300 avaliações antigas. Não houve falso positivo nem falso negativo **na população artificial conhecida**. A amostra SRS de 1.000 itens encontrou cinco exceções (uma de área, uma de VLR, uma de classificação e duas de avaliação antiga), sem pendência documental; isso ilustra risco amostral, não uma constatação sobre a Direcional.

A projeção de VLR de R$454.595, com intervalo ilustrativo de 95% entre R$0 e R$1.344.711, é calculada somente sobre a população sintética. O shortfall implantado conhecido na base é R$1.191.323,15. Nenhum desses números deve ser atribuído à companhia ou projetado para seus saldos reais.

## Integridade e fonte do arquivo

Os PDFs públicos consultados foram arquivados localmente apenas para suporte ao trabalho e estão excluídos do pacote Git por `.gitignore`; o usuário pode obtê-los nos links em `FONTES.md`. A base sintética comprimida tem aproximadamente 21 MB, está incluída no repositório e não excede o limite por arquivo do GitHub. O repositório GitHub [direcional-auditoria-2025](https://github.com/thainaascimento/direcional-auditoria-2025) é privado; o acesso segue as permissões da conta proprietária.
