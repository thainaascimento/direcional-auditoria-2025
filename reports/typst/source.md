# Dossiê didático de auditoria independente

## Direcional Engenharia S.A. — exercício encerrado em 31 de dezembro de 2025

**Preparador:** EDU-AUD-001 (matrícula didática, não atribuída a pessoa real)  
**Data:** 22 de outubro de 2026  
**Revisor:** campo não preenchido — nenhuma revisão de terceiro foi simulada.  
**Moeda:** reais; nas demonstrações, em geral R\$ mil.  
**Classificação:** material didático baseado em informação pública e dados sintéticos.

> **Aviso:** Este trabalho não é auditoria contratada nem opinião independente sobre as demonstrações da Direcional. Não houve acesso a livros auxiliares, contratos, títulos, controles, sistemas, extratos, atas, confirmações externas ou instalações. As informações do emissor e o relatório PwC são apresentados como fatos/documentos públicos, sem apropriar os procedimentos do auditor da companhia. Procedimentos que exigiriam evidência interna estão marcados como planejados por falta de acesso; o único teste em população de grande porte foi feito sobre dados sintéticos expressamente identificados.

## 1. Objetivo, escopo e premissas

O dossiê organiza o planejamento didático para a NBC TA Estrutura Conceitual e as NBC TAs 200 a 600 aplicáveis ao roteiro. A população financeira analisada é o exercício de 2025, com comparativos de 2024 e, quando divulgado na DFP, 2023. A pesquisa de eventos subsequentes foi estendida até 22/10/2026. Foram utilizados documentos públicos da CVM, B3 e da área de RI da companhia para fatos corporativos. Endereços, exercícios, datas de acesso, páginas e limites estão no **Apêndice B — Fontes públicas**; versões e cobertura das normas estão no **Apêndice A — Matriz de cobertura das normas**.

O trabalho contém três classes de procedimento, sem confundi-las: **realizado com evidência pública**, quando o procedimento foi executado sobre a DFP/ITR/comunicados; **planejado por falta de acesso**, quando depende de evidência interna ou confirmação e não foi executado; e **simulado para fins didáticos**, para os testes sobre a base artificial. A documentação de cada papel especifica código, objetivo, afirmações, riscos, população, método, referência, conclusão, limitações, preparador/data e campo de revisão.

## 2. Conclusão executiva

A conta selecionada para a base de dados é **Estoques**, a maior rubrica individual do ativo consolidado: R\$6.951.508 mil na Nota 5 de 2025. A conta compreende terrenos a incorporar (R\$5.678.238 mil, 81,7% dos estoques e 43,0% do ativo), imóveis em construção (R\$1.174.207 mil) e imóveis concluídos (R\$99.063 mil). A predominância de terrenos orienta os riscos específicos de direitos/títulos, contratos de permuta, existência, ônus, classificação e mensuração pelo custo e valor realizável líquido; obras em andamento também envolvem capitalização de custos e estimativas para completar.

A DRE consolidada mostra receita de R\$4.343.008 mil, crescimento de 29,7% sobre 2024, e resultado antes de tributos de R\$1.078.495 mil, crescimento de 36,1%. O relatório PwC emitido sobre 2025 apresenta opinião sem modificação e parágrafo de ênfase sobre a política de reconhecimento da receita de unidades imobiliárias em construção; os principais assuntos de auditoria descritos são o reconhecimento de receita e provisões para contingências. Essa opinião pertence à PwC; este dossiê não reexecutou os testes nem emite opinião.

A triagem prioriza: (i) estoques de terrenos e custo/valor realizável; (ii) reconhecimento de receita de construção pelo progresso físico/financeiro e estimativas de custo para completar; (iii) recebíveis/distratos e perdas esperadas; (iv) dívida, liquidez, swaps, covenants e fluxos de caixa; (v) provisões e partes relacionadas; e (vi) perímetro e consolidação de SPEs/SCPs/empreendimentos. A administração declara não conhecer incerteza significativa de continuidade; a declaração e as métricas públicas não substituem a obtenção e teste independente de projeções, vencimentos, covenants, restrições de caixa e cenários.

Há ainda uma **inconsistência cronológica aparente**: a Nota 1 informa aprovação das demonstrações pelo Conselho em 10/03/2026, enquanto o relatório PwC está datado de 09/03/2026. Sem ata, assinaturas eletrônicas e versão final, o efeito é indeterminado; o procedimento apropriado é esclarecer a sequência com evidência formal. Não se conclui irregularidade nem se altera a opinião pública.

## 3. Procedimentos e evidência obtida

### Realizado com evidência pública

Foram identificados e conciliados, no limite dos demonstrativos publicados: a identidade da companhia (Direcional Engenharia S.A., DIRR3), totais consolidados e comparativos, nota de estoques, receita e resultado, saldos de partes relacionadas, política de continuidade, principais assuntos de auditoria, opinião PwC, dívida e posição líquida divulgadas pela administração, eventos subsequentes e documentos pós-período. A comparação da DFP com a ficha da B3 não indicou alteração de denominação empresarial ou ticker no exercício de 2025; essa conclusão limita-se às fontes públicas examinadas. A Nota 5 foi reconciliada aritmeticamente; o balanço publicado foi comparado aos quadros de resultados do RI e à ficha da B3. As tabelas editáveis preservam valores-base, fórmulas, limites de investigação e fonte.

### Planejado por falta de acesso

Não foram realizados circularização de bancos, clientes, advogados ou fornecedores; inspeção física de terrenos/obras; exame de matrícula, escritura, contrato ou laudo interno; entrevista da administração; walkthrough; observação de controles; teste de lançamentos contábeis no razão; recálculo de POC usando orçamento/medições; verificação de pagamentos posteriores ou acesso à TI. Esses procedimentos foram desenhados por ciclo, riscos e afirmações, mas dependem de autorização e fornecimento de evidência interna. Nenhuma solicitação foi enviada em nome da companhia ou de uma firma.

### Simulado para fins didáticos

A população `data/estoques_sinteticos.csv.gz` tem 500.000 itens sintéticos distintos: 420.000 terrenos, 75.000 unidades em construção e 5.000 unidades concluídas. O valor contábil soma exatamente R\$6.951.508.000,00, conciliando por classe com a Nota 5 e entre circulante (R\$2.086.835.000,00) e não circulante (R\$4.864.673.000,00). A amostra aleatória simples sem reposição contém 1.000 itens, semente 20251232; uma seleção dirigida independente contém os 200 maiores saldos e tem uma unidade em comum com a SRS. O desenho estatístico é apenas ilustrativo e não valida saldo real nem substitui desenho amostral profissional.

Cinco grupos de exceções foram implantados para testar a detecção: documentação incompleta (200), áreas inválidas (150), sinais de valor realizável líquido inferior ao saldo (500), classificações divergentes (250) e avaliações antigas (300). O programa identificou exatamente todas as exceções artificiais conhecidas. A amostra de 1.000 detectou cinco ocorrências (0, 1, 1, 1 e 2, respectivamente). O shortfall implantado de VLR na base foi R\$1.191.323,15; a projeção amostral sintética é R\$454.595,00, com intervalo ilustrativo de 95% de R\$0,00 a R\$1.344.710,64. Nenhum desses valores representa a Direcional.

## 4. Materialidade e análise financeira

Como julgamento didático, foi adotado benchmark de 0,75% do ativo consolidado (R\$13.219.635 mil): materialidade global de R\$99.147.262; materialidade para execução de 70% (R\$69.403.084); materialidade específica para Estoques de 0,50% do saldo (R\$34.757.540); e limiar claramente trivial de 5% da global (R\$4.957.363). Esses percentuais não são prescritos como regra pela NBC TA 320 e não correspondem à materialidade fixada pela PwC; devem ser revistos após a análise de erros, volatilidade, usuários e resultados finais.

A comparação anual indica variação de ativos de 31,3%, estoques de 25,7%, terrenos a incorporar de 23,8%, receita de 29,7%, resultado antes de tributos de 36,1% e empréstimos e financiamentos de 78,0% (2024 para 2025). São sinais para explicação e testes, não distorções por si só. A dívida líquida divulgada passou de posição de caixa líquido de R\$68,2 milhões em 2024 a dívida líquida de R\$532,6 milhões em 2025. A administração vincula o movimento ao pagamento de R\$804 milhões em dividendos extraordinários no encerramento. Cerca de 90% do endividamento divulgado é de longo prazo, com prazo médio de 64 meses; a geração de caixa operacional informada para 2025 foi de R\$104 milhões, após efeitos não operacionais líquidos positivos de R\$779 milhões. As métricas reforçam foco em previsões, fluxo de caixa, covenants, restrições, vencimentos e decisões de distribuição, sem provar insuficiência de caixa ou incerteza material.

## 5. Eventos subsequentes e atualização de riscos

O ITR de 30/06/2026 reporta ativo consolidado de R\$14.628.318 mil, terrenos a incorporar de R\$6.345.109 mil e ajuste a NRV em estoques de R\$4.310 mil (2025: R\$4.165 mil). A nota informa capitalização líquida de juros de R\$65.902 mil no semestre, R\$48.217 mil ainda nos estoques de unidades não vendidas. A prévia operacional de 3T26 (não auditada) informa queda de vendas contratadas, lançamentos inferiores ao trimestre anterior, distratos acima do normal, geração operacional de caixa de R\$228 milhões e geração contábil de R\$10 milhões. A companhia também emitiu R\$150 milhões de debêntures em 25/09/2026, encerrando a oferta em 05/10, e divulgou participação acionária de 4,7805% da Driehaus em 16/10, sem intenção declarada de alterar controle/administração.

Esses eventos são considerados para atualizar a avaliação de continuidade, liquidez, estoque e eventos subsequentes. Em regra, eventos que surgiram após a data-base não ajustam 2025; deve-se verificar se fornecem evidência sobre condições já existentes em 31/12/2025 e se há divulgação necessária. Os dados do 3T26 são preliminares e explicitamente não auditados. A emissão de CRI de R\$437,5 milhões em 04/03/2026 é divulgada na Nota 26 como evento subsequente e deve ser tratada conforme a natureza do evento e as condições da data-base.

## 6. Conclusão integrada e limitações

A documentação pública permite identificar uma companhia de incorporação com crescimento substancial e concentração do ativo na rubrica Estoques, predominantemente terrenos, além de reconhecimento de receita e provisões tratados como principais assuntos de auditoria pelo auditor da companhia e evolução material da dívida líquida. Isso sustenta resposta planejada de risco elevado para mensuração de estoque/VLR, direitos sobre terrenos, POC/custo para completar, distratos, dívida/covenants, provisões, partes relacionadas e consolidação de empreendimentos. A declaração da administração sobre continuidade, o perfil de dívida majoritariamente de longo prazo e o alongamento posterior via CRI são fatores mitigantes reportados, mas não substituem a avaliação independente de projeções, maturidades e sensibilidade.

O principal procedimento executado com quantificação completa é o exercício sintético PT530; sua reconciliação exata prova somente a integridade matemática da população artificial. Os demonstrativos públicos possibilitam leitura e tie-out documental, não validação dos registros contábeis subjacentes. Por falta de acesso, não se conclui sobre controles, existência de terrenos, direitos, adequação das estimativas, integridade de passivos, confirmação de saldos, suficiência de caixa ou conformidade efetiva de processos. O dossiê organiza procedimentos e evidência disponível, identifica limitações e apresenta conclusões de planejamento; **não expressa asseguração nem opinião profissional independente sobre a DFP 2025**.

## 7. Índice dos papéis de trabalho

Os papéis estão reunidos após este relatório no PDF consolidado e individualmente em `workpapers/`. A matriz de cobertura liga cada NBC TA ao papel correspondente.

| Papel | Tema |
|---|---|
| PT EC | Estrutura Conceitual para Trabalhos de Asseguração |
| PT 200, 210, 220, 230 | Objetivos gerais; termos; gestão da qualidade; documentação |
| PT 240, 250, 260, 265 | Fraude; leis e regulamentos; comunicação à governança; deficiências de controle |
| PT 300, 315, 320, 330 | Planejamento; riscos; materialidade; respostas |
| PT 402, 450, 500, 501, 505, 510 | Serviços; distorções; evidência; itens específicos; confirmações; saldos iniciais |
| PT 520, 530, 540, 550, 560, 570, 580, 600 | Analíticos; amostragem; estimativas; partes relacionadas; eventos subsequentes; continuidade; representações; grupos |

## Referências cruzadas principais

- `PT315` → `PT320`, `PT330`, `PT520`, `PT530`, `PT540`, `PT550`, `PT560`, `PT570`, `PT600`.
- `PT530` → base, dicionário, registro de injeções, amostras aleatória e direcionada, resultados JSON e planilha de reconciliação.
- `PT450` → registro de exceções sintéticas e tratamento de distorções públicas/documentais.
- `PT560`/`PT570` → ITR 2T26, prévia 3T26, CRI e 16ª emissão de debêntures.
- `PT500`/`PT501` → DFP 2025, Nota 5 e saldos de estoques; procedimento interno permanece planejado.
- `PT600` → notas sobre controladas, SCP/SPE e método de equivalência patrimonial; não se afirma que a informação pública constitua evidência suficiente por componente.

---

**Apêndice A — Matriz de cobertura das normas**

# Matriz de cobertura das normas e papéis de trabalho

## Escopo e leitura

Esta matriz liga os temas expressamente incluídos no roteiro do dossiê a seus papéis de trabalho individuais. As versões normativas consultadas, itens específicos, fontes oficiais e datas de acesso estão registradas em cada PT e em suas referências; a relação abaixo sintetiza a cobertura, sem substituir esses registros.

Os três status obrigatórios são usados nos papéis: **realizado com evidência pública**, **planejado por falta de acesso** e **simulado para fins didáticos**. “Cobertura documental” significa que o tema foi analisado no dossiê; não significa que a auditoria real da Direcional tenha sido reexecutada, que procedimentos internos tenham sido realizados ou que haja asseguração/opinião deste preparador.

## Matriz

1. **NBC TA Estrutura Conceitual para Trabalhos de Asseguração — [PT-EC](workpapers/PT-EC.md).** Versão: texto CFC de 20/11/2015, com Revisão NBC 15 publicada em 2022. Cobertura: natureza do trabalho, partes, objeto, critérios, evidência e diferença entre auditoria e outros trabalhos de asseguração.
2. **NBC TA 200 — Objetivos gerais do auditor independente — [PT-200](workpapers/PT-200.md).** Versão: R1, conforme catálogo/texto oficial CFC consultados em 22/10/2026. Cobertura: ética, independência, ceticismo, julgamento profissional, risco de auditoria e segurança razoável.
3. **NBC TA 210 — Concordância com os termos do trabalho — [PT-210](workpapers/PT-210.md).** Versão: R1, com Revisão NBC 11. Cobertura: precondições da auditoria e minuta didática dos termos, responsabilidades, alcance e relatório.
4. **NBC TA 220 — Gestão da qualidade da auditoria — [PT-220](workpapers/PT-220.md).** Versão: R3, aplicável a períodos iniciados desde 01/01/2023. Cobertura: direção, supervisão, revisão, consultas, recursos e riscos à qualidade, sem atribuir atuação da PwC ao dossiê.
5. **NBC TA 230 — Documentação de auditoria — [PT-230](workpapers/PT-230.md).** Versão: R1, vigente para o exercício de 2025. Cobertura: índice, codificação, referências cruzadas, versões e montagem didática do arquivo.
6. **NBC TA 240 — Responsabilidade do auditor em relação à fraude — [PT-240](workpapers/PT-240.md).** Versão: R1 aplicável ao exercício encerrado em 31/12/2025; R2 indicada para períodos iniciados em 2027. Cobertura: riscos de fraude, reconhecimento de receita, burla de controles e resposta planejada.
7. **NBC TA 250 — Consideração de leis e regulamentos — [PT-250](workpapers/PT-250.md).** Versão: redação aplicável a 2025, com Revisão NBC 15. Cobertura: mapeamento de obrigações, risco de descumprimento e resposta/comunicações diante de indícios.
8. **NBC TA 260 — Comunicação com os responsáveis pela governança — [PT-260](workpapers/PT-260.md).** Versão: R2, texto oficial CFC consultado em 22/10/2026. Cobertura: alcance, época, riscos significativos, independência, dificuldades e comunicação simulada/planejada.
9. **NBC TA 265 — Comunicação de deficiências de controle interno — [PT-265](workpapers/PT-265.md).** Versão: Resolução CFC nº 1.210/09, conforme cadastro oficial consultado. Cobertura: matriz de condição, critério, causa, efeito e recomendação, separando hipóteses de constatações.
10. **NBC TA 300 — Planejamento da auditoria — [PT-300](workpapers/PT-300.md).** Versão: R1, considerada a Revisão NBC 11. Cobertura: estratégia global, plano, cronograma e programas por ciclo.
11. **NBC TA 315 — Identificação e avaliação dos riscos de distorção relevante — [PT-315](workpapers/PT-315.md).** Versão: R2, publicada em 2021 e aplicável ao período. Cobertura: entidade, ambiente, estrutura contábil, TI/controles, riscos por conta/afirmação e riscos significativos.
12. **NBC TA 320 — Materialidade no planejamento e na execução — [PT-320](workpapers/PT-320.md).** Versão: R1, texto oficial CFC publicado em 2016. Cobertura: cenários didáticos — global 0,75% do ativo; execução 70%; nível específico 0,50% para terrenos; limite trivial 5% da global. Não são percentuais normativos nem materialidade da PwC.
13. **NBC TA 330 — Respostas do auditor aos riscos avaliados — [PT-330](workpapers/PT-330.md).** Versão: R1, com Revisão NBC 11. Cobertura: relação entre riscos e respostas, controles/substantivos, natureza, época e extensão, com status por procedimento.
14. **NBC TA 402 — Entidade que utiliza organização prestadora de serviços — [PT-402](workpapers/PT-402.md).** Versão: Resolução CFC nº 1.215/09, com alterações NBC 11/NBC 20. Cobertura: identificação de serviços relevantes, controles complementares, relatórios Tipo 1/2 e procedimentos alternativos.
15. **NBC TA 450 — Avaliação das distorções identificadas — [PT-450](workpapers/PT-450.md).** Versão: R1, itens 1–15 e aplicação A1–A30. Cobertura: registro de distorções observadas/documentais e simuladas, avaliação quantitativa/qualitativa e limites de conclusão.
16. **NBC TA 500 — Evidência de auditoria — [PT-500](workpapers/PT-500.md).** Versão: R1 aplicável ao exercício de 2025. Cobertura: relevância, confiabilidade, suficiência, cotejo com demonstrações e limites da evidência pública/sintética.
17. **NBC TA 501 — Evidência para itens selecionados — [PT-501](workpapers/PT-501.md).** Versão: Resolução CFC nº 1.218/09, alterada pela Revisão NBC 20. Cobertura: estoques (Nota 5 p.69), litígios (Nota 16.2 pp.93–94 e PAA p.116) e segmentos (Nota 2.1.3 p.44); observação física, jurídicos e dados internos permanecem planejados.
18. **NBC TA 505 — Confirmações externas — [PT-505](workpapers/PT-505.md).** Versão: Resolução CFC nº 1.219/09, conforme cadastro oficial consultado. Cobertura: minutas didáticas, controle de circularização, tratamento de diferenças e alternativas; nenhuma solicitação real foi enviada.
19. **NBC TA 510 — Trabalhos iniciais: saldos iniciais — [PT-510](workpapers/PT-510.md).** Versão: R1, texto CFC publicado em 2016. Cobertura: comparativos de 2024, políticas contábeis e implicações do relatório do auditor anterior, sem acesso a papéis privados.
20. **NBC TA 520 — Procedimentos analíticos — [PT-520](workpapers/PT-520.md).** Versão: Resolução CFC nº 1.221/09, conforme cadastro oficial consultado. Cobertura: análises reproduzíveis — ativo +31,3%; estoques/ativo 52,6%; terrenos totais +23,8%, 43,0% do ativo e 81,7% dos estoques.
21. **NBC TA 530 — Amostragem em auditoria — [PT-530](workpapers/PT-530.md).** Versão: Resolução CFC nº 1.222/09, conforme cadastro oficial consultado. Cobertura: população sintética de 500.000 registros, SRS de 1.000 itens, seleção dirigida de 200, cinco classes de exceções implantadas e projeção exclusivamente didática; nenhuma amostra real da companhia.
22. **NBC TA 540 — Auditoria de estimativas contábeis — [PT-540](workpapers/PT-540.md).** Versão: R2, resolução CFC de 2019, aplicável a 2025. Cobertura: estimativa/NRV, método, dados, premissas, incerteza, possível viés e análise de sensibilidade com limitações explícitas.
23. **NBC TA 550 — Partes relacionadas — [PT-550](workpapers/PT-550.md).** Versão: Resolução CFC nº 1.224/09, alterada pela Revisão NBC 20. Cobertura: Nota 6 pp.70–71, saldos/transações divulgados e limites da avaliação de completude sem razão, cadastros, contratos e confirmações.
24. **NBC TA 560 — Eventos subsequentes — [PT-560](workpapers/PT-560.md).** Versão: R1, texto CFC publicado em 2016. Cobertura: data de corte 22/10/2026 e exame de ITR, prévia operacional, debêntures e comunicado acionário posteriores a 2025.
25. **NBC TA 570 — Continuidade operacional — [PT-570](workpapers/PT-570.md).** Versão: redação aplicável a 2025; R1 indicada para períodos iniciados em 2027. Cobertura: liquidez, endividamento, fluxos, divulgações e eventos adversos, distinguindo fatores mitigantes e limitações.
26. **NBC TA 580 — Representações formais — [PT-580](workpapers/PT-580.md).** Versão: R1, texto oficial aplicável a 2025. Cobertura: minuta didática, responsabilidade da administração e explicação de por que representação não substitui outra evidência.
27. **NBC TA 600 — Auditoria de demonstrações contábeis de grupos — [PT-600](workpapers/PT-600.md).** Versão: R2, aplicável a períodos iniciados desde 01/01/2024. Cobertura: grupo/componentes, processo de consolidação, riscos, materialidade, auditores de componentes e suficiência da evidência.

## Limites transversais

A DFP integral pública de 2025 foi obtida no RI e as páginas relevantes citadas nos PTs foram examinadas; o registro CVM fornece metadados, sem paginação impressa estável. Essa leitura documental não equivale a tie-out com razão, confirmação externa, inspeção física ou acesso ao arquivo privado da auditoria. A base de 500.000 itens, suas exceções e seus resultados são inteiramente sintéticos. Os PTs não reproduzem o trabalho da PwC, não concluem sobre a suficiência de seus procedimentos e não emitem opinião ou asseguração independente.

---

**Apêndice B — Fontes públicas**

# Fontes públicas e convenções de citação

**Data de acesso das fontes desta relação:** 22/10/2026. **Corte de pesquisa de eventos subsequentes:** 22/10/2026. Os fatos societários foram obtidos somente em documentos públicos da CVM, B3 e RI da Direcional. As normas e critérios profissionais são citados nas referências normativas dos papéis e da matriz.

## Companhia e demonstrações de 2025

- **S1 — CVM/RAD-ENET, DFP Direcional Engenharia S.A. V1, NSD 155189, protocolo 021350DFP311220250100155189-71.** Exercício 31/12/2025; envio 09/03/2026. URL: [registro oficial CVM](https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1). Uso: metadados da companhia, exercício, versão, protocolo e auditor indicado. A interface dinâmica não tem paginação impressa estável; os valores e notas foram examinados no PDF direto do RI (S2).
- **S2 — RI Direcional, DFP 4T25 V1.** Exercício encerrado em 31/12/2025; acesso 22/10/2026. URLs: [PDF direto](https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2) e [Central de resultados](https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/). PDF com 125 páginas físicas e paginação impressa até 123. Páginas/usos: BP consolidado pp.16–17; DRE p.21; Notas 1/1.1 pp.41–42; política de segmentos p.44; Nota 5 — estoques p.69; Nota 6 — partes relacionadas pp.70–71; Nota 16.2 — contingências pp.93–94; endividamento/administração pp.32 e 38; Nota 26 — evento subsequente p.114; relatório PwC pp.115–117 (PAA de contingências p.116).
- **S3 — B3, ficha listada Direcional Engenharia S.A.** Consulta em 22/10/2026. URL: [ficha da companhia](https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br). Sem paginação. Nome empresarial Direcional Engenharia S.A.; nome de pregão Direcional; ticker DIRR3; código CVM 21350; CNPJ 16.614.075/0001-00; início da negociação 19/11/2009. Não se identificou mudança de nome/ticker que altere a atribuição da companhia.
- **S4 — RI Direcional, DFP 4T24 V1 e relatório anterior PwC.** Exercício 31/12/2024; acesso 22/10/2026. URLs: [PDF direto](https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/71cc6d14-36b4-e7cc-a1e3-7f7974c42ed7?origin=2) e [Central de resultados](https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/). Relatório impresso pp.111–113; opinião sem modificação e ênfase sobre reconhecimento de receita. Usado no planejamento de saldos iniciais; não substitui confirmação com auditor antecessor nem acesso a papéis internos.

### Saldos e fatos-chave do exercício

Na DFP 2025 (S2), o ativo consolidado foi R\$13.219.635 mil (2024: R\$10.067.406 mil; 2023: R\$7.571.598 mil). Estoques totalizaram R\$6.951.508 mil em 2025 e R\$5.532.090 mil em 2024. Nota 5: terrenos a incorporar R\$5.678.238 mil, imóveis em construção R\$1.174.207 mil e imóveis concluídos R\$99.063 mil; o componente corrente de terrenos (R\$813.565 mil) é diferença aritmética entre o total da nota e o componente não circulante de R\$4.864.673 mil. Assim, terrenos a incorporar é a maior classe individual de ativo detalhada na Nota 5, equivalente a 81,7% dos estoques e 43,0% do ativo consolidado.

O ajuste total a valor realizável líquido dos estoques foi R\$4.165 mil em 2025 (2024: R\$4.255 mil), após adições de R\$179 mil e reversões de R\$269 mil. A companhia divulgou R\$594.401 mil de estoque/terrenos/unidades em garantia em 2025 (2024: R\$551.619 mil). Receita consolidada de vendas e serviços foi R\$4.343.008 mil em 2025 (2024: R\$3.348.470 mil); resultado bruto R\$1.722.417 mil; resultado antes de tributos R\$1.078.495 mil.

No comparativo de 2024, o total de terrenos a incorporar foi R\$4.587.823 mil, dos quais R\$3.888.979 mil não circulantes. O total da classe não deve ser confundido com seu componente não circulante.

A administração informou dívida financeira de R\$2.758,3 milhões, 90% classificada no longo prazo, prazo médio ponderado de 64 meses, caixa/equivalentes/aplicações de R\$2.182,8 milhões, swaps líquidos positivos de R\$43,0 milhões, dívida líquida de R\$532,6 milhões e dívida líquida/patrimônio líquido de 23,0% (Relatório da Administração p.38). Em 2024, dívida financeira de R\$1.549,7 milhões e posição de caixa líquido de R\$68,2 milhões. A companhia associa o aumento da dívida líquida a dividendos extraordinários de aproximadamente R\$1,5 bilhão no exercício, incluindo R\$804 milhões nos últimos dias úteis de 2025. Geração de caixa operacional informada de R\$104 milhões e efeitos não operacionais líquidos positivos de R\$779 milhões (p.32). São explicações da administração, não testes independentes.

A Nota 1.1 declara que a administração não conhece incerteza significativa que possa pôr em risco a continuidade. PwC emitiu opinião sem modificação, com ênfase sobre a política de reconhecimento de receita imobiliária conforme Ofício Circular CVM/SNC/SEP 02/2018 e NBC TG 47; os PAA são reconhecimento de receita de unidades em construção e provisões para contingências (pp.115–117). A descrição dos procedimentos PwC é informação pública sobre o auditor da companhia, não procedimento executado neste dossiê.

## Documentos posteriores à DFP 2025

- **S5 — RI Direcional, ITR 2T26 V1.** Data-base 30/06/2026; acesso 22/10/2026. URLs: [PDF direto](https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/e7250290-a0ce-9144-cc4e-169db46844eb?origin=2) e [Central de resultados](https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/). Páginas/usos: quadro consolidado e BP p.22; DRE p.23; DFC p.24; Nota 5 de estoques pp.57–58; continuidade p.49.
- **S6 — RI Direcional, prévia operacional 3T26.** Comunicado 14/10/2026; dados preliminares não auditados. URL: [PDF oficial](https://filemanager-cdn.mziq.com/published/ada9bc2c-f7d0-4359-9eaf-851b679ab788/ec557d57-e4bc-4648-bb3f-e272f7f0ba0a). Páginas/usos: pp.1–4, vendas, lançamentos, distratos, geração de caixa e banco de terrenos; atualização de riscos subsequentes, sem extrapolação para 31/12/2025.
- **S7 — RI Direcional, anúncio de início da 16ª emissão de debêntures.** Data 01/10/2026. URL: [documento oficial](https://filemanager-cdn.mziq.com/published/ada9bc2c-f7d0-4359-9eaf-851b679ab788/2d709687-6743-41d0-a74a-cc287ddf5167). Emissão quirografária, não conversível, 150.000 unidades de R\$1.000, total de R\$150 milhões; emissão em 25/09/2026.
- **S8 — RI Direcional, anúncio de encerramento da 16ª emissão.** Data 05/10/2026. URL: [documento oficial](https://filemanager-cdn.mziq.com/published/ada9bc2c-f7d0-4359-9eaf-851b679ab788/c36f23cd-1a25-423a-806b-31f67912116f). Páginas/usos: pp.1–5, encerramento e montante distribuído de R\$150 milhões. Financiamento posterior, não ajustável por si só às demonstrações de 2025.
- **S9 — RI Direcional, comunicado de participação acionária relevante.** Carta de posição de 15/10 e comunicado de 16/10/2026. URL: [documento oficial](https://filemanager-cdn.mziq.com/published/ada9bc2c-f7d0-4359-9eaf-851b679ab788/15fa5da0-e732-4b16-b364-0f264c093d07). Participação Driehaus de 24.882.388 ações ordinárias, cerca de 4,7805%; sem intenção declarada de mudar controle/administração ou acordo de voto. Não se identificou ajuste a 2025.

No ITR 2T26 (S5), ativo consolidado foi R\$14.628.318 mil; terrenos a incorporar R\$6.345.109 mil (31/12/2025: R\$5.678.238 mil); ajuste a valor realizável de R\$4.310 mil (2025: R\$4.165 mil); aplicações financeiras correntes e não correntes somavam R\$2.750.097 mil; estoques totalizavam R\$7.623.261 mil. A companhia reporta capitalização de juros em estoque de R\$65.902 mil no semestre, R\$48.217 mil remanescentes em unidades não vendidas. São dados subsequentes para atualização de riscos, não ajuste a 2025 sem evidência de condição existente na data-base.

A prévia 3T26 (S6) informa vendas líquidas de R\$1,302 bilhão no trimestre, queda aproximada de 21% versus 2T26 e 20,7% versus 3T25; lançamentos de R\$1,3525 bilhão, queda de 34,5% versus 2T26; geração operacional de caixa de R\$228 milhões e geração contábil de R\$10 milhões, não auditadas. A empresa relaciona menor conversão à concentração de lançamentos no fim do trimestre e distratos acima do normal. Informa VGV potencial de terrenos de R\$61,636 bilhões e custo médio de aquisição equivalente a 11% do VGV. São indícios para atualização de continuidade e mensuração, não prova de distorção em 2025.

## Questão documental a esclarecer

A Nota 1 (S2, p.41) informa aprovação das demonstrações pelo Conselho de Administração em 10/03/2026; o relatório PwC (S2, p.117) traz Belo Horizonte, 09/03/2026. Trata-se de inconsistência cronológica aparente de um dia. Sem ata, versão assinada e sequência documental, não se conclui irregularidade ou efeito sobre a opinião; recomenda-se esclarecer e verificar a documentação formal.

## Limites e dados sintéticos

Os documentos públicos não fornecem razão auxiliar, cadastro de terrenos, matrículas, contratos, orçamentos por empreendimento, avaliações internas, controles, logs, extratos ou confirmações. Nenhuma confirmação, entrevista, inspeção física, consulta a sistemas ou contato com a companhia, auditor ou terceiros foi realizado. A população de 500.000 itens em `data/estoques_sinteticos.csv.gz` foi gerada do zero, com identificadores únicos, abrange as três classes da Nota 5 e concilia aritmeticamente ao total público; não contém registros reais. As normas e versões consultadas estão identificadas em `MATRIZ_NORMAS.md` e nos respectivos PTs.

---

**Apêndice C — Papéis de trabalho**


---

# PT-EC — Estrutura Conceitual para Trabalhos de Asseguração

**Norma e itens:** NBC TA Estrutura Conceitual, itens 1–4, 10–16, 22–26, 27–49, 50–82 e 83–92; texto oficial do CFC e Revisão NBC 15. **Exercício:** demonstrações consolidadas de 31/12/2025. **Preparador:** EDU-AUD-001, matrícula didática. **Data:** 22/10/2026. **Revisão:** campo reservado; não preenchido.

## 1. Objetivo, objeto e partes

Este papel caracteriza, para fins acadêmicos, o trabalho de asseguração relacionado às demonstrações contábeis históricas consolidadas da DIRECIONAL ENGENHARIA S.A. O objeto de avaliação é o conjunto completo das demonstrações de 2025, seus comparativos e divulgações anexas, preparado pela administração da Companhia. A informação sobre o objeto é o conjunto divulgado na DFP V1 de 31/12/2025, protocolada na CVM sob o documento 021350DFP311220250100155189-71; a cópia integral em PDF foi obtida na Central de Resultados do RI e as seções relevantes indicadas neste papel foram lidas. [3] [4]

| Elemento conceitual | Aplicação neste caso didático | Limite |
|---|---|---|
| Partes do trabalho | Administração da Direcional: responsável pela preparação das demonstrações e pelos controles necessários; auditor independente: responsável pela obtenção de segurança e emissão de relatório; usuários previstos: investidores atuais e potenciais, credores e demais usuários das demonstrações públicas. | As pessoas, contratos e usuários específicos de um trabalho real da PwC não foram entrevistados ou confirmados. |
| Objeto | Desempenho, posição patrimonial e fluxos de caixa históricos consolidados do exercício encerrado em 31/12/2025, incluindo notas explicativas. | A leitura pública não equivale a teste sobre os livros, subledger, componentes ou controles subjacentes. |
| Critérios | Estrutura de relatório financeiro declarada pela Companhia na DFP, incluindo práticas contábeis brasileiras e IFRS conforme divulgadas; critérios específicos de reconhecimento, mensuração, apresentação e divulgação nas políticas e notas. | Este papel não representa opinião de conformidade integral às normas contábeis nem reavaliação dos julgamentos da administração. |
| Evidência | DFP e relatório do auditor disponíveis publicamente, ficha societária B3 e normas oficiais CFC. | Não foram obtidas evidências internas nem confirmadas populações completas de transações. |
| Nível de asseguração | Uma auditoria independente de demonstrações históricas é um trabalho de asseguração razoável: redução do risco do trabalho a nível aceitavelmente baixo, mediante evidência apropriada e suficiente, e conclusão expressa em relatório. | Este dossiê didático não é auditoria nem oferece asseguração sobre as demonstrações. |

## 2. Natureza da auditoria e distinção de outros trabalhos

A auditoria de demonstrações históricas procura elevar a confiança dos usuários mediante conclusão do auditor sobre se as demonstrações foram preparadas, em todos os aspectos relevantes, segundo a estrutura aplicável. Segurança razoável é alta, mas não absoluta: limitações inerentes a estimativas, julgamento, fraude encoberta, amostragem e evidência disponível impedem garantir que toda distorção relevante será detectada. A conclusão depende de ceticismo profissional, julgamento, identificação e avaliação de riscos, procedimentos responsivos e evidência apropriada e suficiente. (NBC TA Estrutura Conceitual, itens 10–16, 50–82 e 83–92.) [1]

Uma revisão de informação contábil histórica fornece segurança limitada e envolve procedimentos menos extensos; sua conclusão é normalmente formulada em termos de conhecimento de fatos que levem a crer que a informação não está apresentada adequadamente. Procedimentos previamente acordados reportam achados factuais sem conclusão de asseguração. Serviços de compilação, consultoria ou preparação também não substituem uma auditoria. A classificação decorre da natureza e do nível de asseguração definidos no contrato e no relatório, não apenas do nome do serviço. (Itens 22–26 e 83–92.) [1]

## 3. Fatos públicos revisados e riscos relevantes

A DFP V1 e as notas foram examinadas nas páginas impressas abaixo. Valores estão expressos em R\$ mil, salvo indicação diversa.

| Informação publicada | 2025 | 2024 comparativo | Evidência |
|---|---:|---:|---|
| Ativo consolidado | 13.219.635 | 10.067.406 | Balanço consolidado, pp.16–17; confirmação cruzada da ficha B3 para 2025. |
| Estoques totais | 6.951.508 | 5.532.090 | Balanço e Nota 5 — Estoques, p.69. |
| Terrenos a incorporar — total da Nota 5 | 5.678.238 | 4.587.823 | Nota 5, p.69. É a maior classe individual de ativo detalhada na nota. |
| Estoques circulantes totais | 2.086.835 | — | Balanço consolidado, p.16. |
| Estoques não circulantes totais | 4.864.673 | — | Balanço consolidado, p.17. A nota identifica o saldo não circulante relevante como terrenos a incorporar. |
| Terrenos a incorporar — componente circulante derivado | 813.565 | — | Cálculo didático: total da Nota 5 5.678.238 menos componente não circulante 4.864.673; a demonstração não segrega a classificação corrente por natureza do estoque. |
| Receita líquida | 4.343.008 | 3.348.470 | DRE consolidada, DFP 2025, p.21. |
| Resultado antes dos tributos | 1.078.495 | 792.298 | DRE consolidada, DFP 2025, p.21. |

Terrenos a incorporar correspondem a aproximadamente 81,7% dos estoques e 43,0% do ativo consolidado de 2025. A natureza da conta torna pertinentes as afirmações de existência, direitos e obrigações, avaliação/alocação, classificação e apresentação. Títulos, permutas, ônus, custos capitalizados, cronograma de lançamento, valor realizável líquido e estrutura de SPEs são riscos a investigar, não achados. O relatório público da PwC contém opinião sem modificação, parágrafo de ênfase sobre reconhecimento de receita de unidades imobiliárias em construção e principais assuntos de auditoria sobre reconhecimento de receita e provisões para contingências (pp.115–117). Esses assuntos não constituem, isoladamente, distorção ou deficiência identificada por este papel. [4]

## 4. Procedimentos, população e classificação

| ID | Classe obrigatória | Procedimento e resultado/limite |
|---|---|---|
| EC-01 | Realizado com evidência pública | Consulta ao texto oficial CFC da NBC TA Estrutura Conceitual e à ficha da Revisão NBC 15; itens normativos citados neste papel foram usados como critérios. [1] [2] |
| EC-02 | Realizado com evidência pública | Consulta à DFP 4T25 V1 obtida no RI e leitura das demonstrações consolidadas, Nota 5 e relatório do auditor nas páginas citadas. Rastrearam-se os fatos públicos desta seção ao documento; não houve conciliação a razão ou teste de auditoria. [4] |
| EC-03 | Realizado com evidência pública | Consulta ao registro da DFP no RAD/CVM para identificar emissor, data-base, versão, protocolo, envio e auditor cadastrado; à B3 para nome, código CVM e ticker. Metadados não substituem a leitura do PDF nem comprovam saldos. [3] [5] |
| EC-04 | Planejado por falta de acesso | Identificar e confirmar, em trabalho real, as partes contratantes, usuários previstos, termos de contratação, independência, aceitação/continuidade e controles de qualidade. Nenhum contrato, cadastro de cliente ou registro interno foi obtido. |
| EC-05 | Planejado por falta de acesso | Obter e testar populações internas de terrenos, contratos e transações de receita e contingências; inspecionar títulos, registros, memórias de cálculo, documentos jurídicos e evidência de execução; confirmar direitos, obrigações e premissas. Nada disso foi executado. |
| EC-06 | Simulado para fins didáticos | Riscos e respostas foram associados a estoques/terrenos, receita imobiliária e contingências para demonstrar a aplicação da Estrutura Conceitual. Hipóteses não são constatações; não há amostra real nem conclusão sobre controles. |

A população de registros subjacentes (unidades de terrenos, contratos, custos, receita e processos jurídicos) não foi disponibilizada em fonte pública e não foi obtida; por isso, este papel não estima cobertura nem extrapola resultados para a Companhia. A população artificial de PT530 está em arquivos separados, marcada como sintética e não representa unidades ou lançamentos reais.

## 5. Resultados e conclusão

O enquadramento conceitual é compatível com uma auditoria de demonstrações históricas destinada a proporcionar segurança razoável, se realizada sob os termos, critérios e precondições apropriados. A DFP pública relevante foi obtida e lida; os saldos, a opinião e os PAA acima são referenciados às páginas impressas da fonte oficial de RI. Não se afirma que os procedimentos da PwC foram reexecutados ou que os saldos foram validados por evidência interna.

**Conclusão do PT:** a auditoria difere de revisão, procedimentos acordados e outros serviços de não asseguração pelo objetivo, extensão de evidência, nível de asseguração e forma da conclusão. Este papel demonstra a aplicação dos elementos conceituais e identifica riscos de planejamento, mas não emite opinião independente, não determina se as demonstrações estão livres de distorção relevante e não altera o relatório público da PwC. A limitação relevante é a ausência de acesso a registros e evidência interna; não a indisponibilidade da DFP pública.

**Referências cruzadas:** PT-200 (objetivos gerais), PT-210 (precondições/termos), PT-300/315 (planejamento e riscos), PT-320 (materialidade), PT-500/530 (evidência e dados sintéticos), PT-560/570 (eventos e continuidade).

## Referências

[1] CFC, *NBC TA Estrutura Conceitual para Trabalhos de Asseguração*, texto oficial: https://www1.cfc.org.br/sisweb/SRE/docs/NBCTAESTRUTURACONCEITUAL.pdf. Itens 1–97; acesso em 22/10/2026.

[2] CFC, ficha da NBC TA Estrutura Conceitual e Revisão NBC 15: https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2015/NBCTAESTRUTURACONCEITUAL e https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?codigo=2022/%20REVIS%C3%83O%20NBC15. Acesso em 22/10/2026.

[3] CVM/RAD, DFP Direcional Engenharia S.A., 31/12/2025, V1, documento 155189: https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1. Registro de envio e identificação; acesso em 22/10/2026.

[4] RI Direcional, DFP 4T25 V1, PDF integral, Central de Resultados: https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2. Páginas impressas 16–17, 21, 69 e 115–117; acesso em 22/10/2026.

[5] B3, ficha DIRECIONAL ENGENHARIA S.A., código CVM 21350/ticker DIRR3: https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br. Acesso em 22/10/2026.


---

# PT-200 — Objetivos Gerais do Auditor Independente

**Norma:** NBC TA 200 (R1), em especial itens 3–8, 11–17, 18–24, 26–30, 35–41 e A1–A76, conforme aplicável; texto oficial CFC. **Objeto de planejamento:** demonstrações consolidadas da Direcional Engenharia S.A. em 31/12/2025. **Preparador:** EDU-AUD-001, matrícula didática. **Data:** 22/10/2026. **Revisão:** campo reservado, sem assinatura ou revisor simulado.

## 1. Objetivo e área de foco

Documentar como os objetivos gerais do auditor orientariam uma auditoria de demonstrações históricas da Direcional, sem afirmar que houve contratação ou auditoria por este preparador. A prioridade analítica é **terrenos a incorporar**, maior classe individual de ativo detalhada na Nota 5, sem excluir demais saldos e divulgações.

A DFP 4T25 V1 obtida integralmente no RI informa (R\$ mil): ativo consolidado de 13.219.635; estoques de 6.951.508; terrenos a incorporar de 5.678.238 na Nota 5 p.69; estoques circulantes de 2.086.835 e não circulantes de 4.864.673 no balanço pp.16–17. A parcela corrente de terrenos, 813.565, é derivada aritmeticamente do total da Nota 5 menos o saldo não circulante; o BP não segrega o componente corrente por natureza. Para 2024, ativo consolidado de 10.067.406, estoques de 5.532.090 e terrenos a incorporar de 4.587.823. [3]

Terrenos representam 81,7% dos estoques e 43,0% do ativo consolidado em 2025. Receita líquida foi 4.343.008 e resultado antes dos tributos, 1.078.495; em 2024, 3.348.470 e 792.298, respectivamente (DRE p.21). A DFP também contém PAA sobre reconhecimento de receita imobiliária e provisões para contingências e opinião sem modificação da PwC (relatório pp.115–117). Os números e divulgações foram localizados na DFP pública; não foram conciliados a razão, contratos ou registros internos. [3]

## 2. Objetivos gerais, ética e julgamento

| Requisito da NBC TA 200 | Aplicação e resposta prevista | Status/limitação |
|---|---|---|
| Segurança razoável e conclusão | Obter segurança razoável de que as demonstrações, como um todo, estão livres de distorção relevante por fraude ou erro; emitir relatório em conformidade com a estrutura aplicável com base na evidência obtida. Segurança razoável é alta, não absoluta. | Objetivo de auditoria; não atingido por este trabalho didático. |
| Risco de distorção relevante | Identificar e avaliar riscos nos níveis das demonstrações e das afirmações, desenhar respostas coerentes e avaliar a evidência ao final. | A leitura pública identifica fatores de risco, mas não substitui o entendimento de entidade, controles, populações e dados internos. |
| Evidência apropriada e suficiente | Planejar natureza, época e extensão dos procedimentos; obter evidência confiável e relevante; tratar inconsistências ou dúvidas sobre sua confiabilidade. | Documentos públicos foram inspecionados nas páginas referidas; nenhuma confirmação, inspeção física, teste de controle ou acesso a sistemas foi realizado. |
| Ceticismo profissional | Manter postura questionadora e avaliar criticamente evidências e explicações, reconhecendo que documentação pública e estimativas podem ser incompletas ou enviesadas. | Hipóteses abaixo não são achados; qualquer explicação da administração exigiria corroboração. |
| Julgamento profissional | Aplicar conhecimento, treinamento e experiência para decisões sobre riscos, materialidade, procedimentos, suficiência da evidência e conclusão. | Limiares e procedimentos do dossiê são didáticos, não decisões da PwC. |
| Requisitos éticos e independência | Cumprir requisitos éticos profissionais aplicáveis, inclusive independência quando exigida, antes e durante eventual trabalho; identificar, avaliar e responder a ameaças. | Não houve contratação ou atuação como auditor. A matrícula EDU-AUD-001 é fictícia e não representa declaração de independência de pessoa ou firma real. |

A possibilidade de fraude é considerada em todo o trabalho. O risco de não detectar fraude é maior do que o de não detectar erro, especialmente quando há conluio, falsificação, omissão intencional, representações falsas ou burla de controles pela administração. Presunções de risco e exemplos normativos direcionam procedimentos; não provam fraude. O auditor não promete detectar todo ato ilegal, fraude ou falha de controle. (NBC TA 200, itens 5–7, 15–17 e A1–A76.) [1] [2]

## 3. Riscos e afirmações prioritários

| Área | Afirmações relevantes | Risco hipotético a investigar | Resposta possível em auditoria real |
|---|---|---|---|
| Terrenos e estoques (5.678.238) | Existência; direitos e obrigações; integridade; exatidão, avaliação e alocação; corte; classificação e divulgação. | Título/ônus, permutas, custos capitalizados, custos compartilhados, data de lançamento, cronograma de realização, valor realizável líquido, classificação corrente e completude de SPEs. | Reconciliar cadastro a razão e DFP; inspecionar matrícula/contrato/permuta e pagamentos; confirmar ônus; testar custo e alocação; avaliar NRV/projetos e corte; conferir nota. |
| Receita imobiliária (4.343.008) | Ocorrência, integridade, exatidão, corte, classificação e apresentação. | Julgamentos de desempenho ao longo do tempo, estágio de obra, custos incorridos e a incorrer, distratos, lançamentos manuais e corte. Receita foi PAA e tem presunção normativa de risco de fraude. | Testar contratos e aditivos; recalcular receitas e custos por empreendimento; confrontar orçamento, execução, medição, contas a receber e recebimentos; testar lançamentos e corte. |
| Provisões e contingências | Integridade, existência/obrigação, avaliação, classificação e divulgação. | Omissão de processos, prognóstico jurídico inadequado, incerteza de mensuração e assimetria de estimativas. Também são PAA. | Reconciliar cadastro/razão/nota; obter cartas jurídicas em trabalho real; testar premissas e eventos subsequentes; avaliar probabilidade, valor e divulgações. |
| Consolidação | Completude, direitos, exatidão, apresentação e divulgação. | Perímetro de controladas/SPE/SCP, controle conjunto, consolidação e eliminações. | Obter organograma e pacotes; testar perímetro, ajustes/eliminações, políticas e evidência de componentes. |

A comparação de ativos subiu 31,3% e terrenos, 23,8% entre 2024 e 2025; essas variações são sinais de planejamento, não por si sós anomalias. Estoques e terrenos podem ser materialmente relevantes em montante e qualitativamente. A NBC TA 200 não fixa percentual de materialidade; a análise quantitativa e qualitativa é desenvolvida no PT-320.

## 4. População, fonte, critérios e procedimentos

**Populações necessárias em auditoria efetiva:** cadastro completo de terrenos e estoques; movimentos, contratos e lançamentos; projetos e memórias de custo/receita; processos jurídicos e estimativas; razão, balancete, consolidação, controles e demonstrações. As populações internas não foram disponibilizadas, portanto não há amostragem ou cobertura real neste PT. A base de 500.000 itens de PT530 é inteiramente sintética e segregada.

**Evidência pública efetivamente obtida:** DFP 4T25 V1 da Central de Resultados do RI Direcional (balanço pp.16–17, DRE p.21, Nota 5 p.69 e relatório PwC pp.115–117); registro de protocolo CVM; ficha B3; texto oficial CFC. A interface textual do índice do RI não exibia a DFP no próprio texto, mas o PDF direto foi localizado e baixado; não se confunde essa limitação do extrator do índice com indisponibilidade do documento. [1]–[4]

| ID | Classe | Procedimento e resultado |
|---|---|---|
| E-01 | Realizado com evidência pública | Consultados catálogo/ficha do CFC e texto oficial da NBC TA 200 (R1); itens normativos referenciados neste PT foram identificados. [1] [2] |
| E-02 | Realizado com evidência pública | Inspecionados metadados CVM e B3 para companhia, data-base, protocolo, auditor cadastrado, nome e ticker. A ficha B3 foi usada para identificação e cotejo, não como substituta da DFP. [3] [4] |
| E-03 | Realizado com evidência pública | Lidos balanço, DRE, Nota 5 e relatório PwC da DFP 4T25 V1; saldos e divulgações descritos nas seções 1 e 3 foram referenciados às páginas impressas. Sem teste de registros internos ou opinião deste preparador. [3] |
| RP-01 | Realizado com evidência pública | Recalculadas as relações 5.678.238/6.951.508 = 81,7%; 5.678.238/13.219.635 = 43,0%; e as variações anuais indicadas. Os cálculos são triagem, não procedimento substantivo. |
| P-01 | Planejado por falta de acesso | Em auditoria real, obter/reconciliar razão e balancete aos relatórios, testar populações e fechamento, avaliar controles, risco de fraude e materialidade. A DFP pública já foi obtida; o que falta é evidência interna e execução independente. |
| P-02 | Planejado por falta de acesso | Executar respostas sobre títulos/custos/NRV de estoques, reconhecimento e corte de receita, processos/provisões e consolidação, com seleção baseada em risco. Não foram feitos testes de contratos, amostras reais ou confirmações. |
| P-03 | Planejado por falta de acesso | Acumular distorções identificadas, corrigidas e não corrigidas; avaliar materialidade individual/agregada, evidência contraditória, declarações, comunicações e relatório somente depois de trabalho suficiente. Nenhuma opinião será emitida neste dossiê. |

## 5. Resultados, conclusão e limitações

**Resultado público:** a DFP informa saldo total de terrenos a incorporar de R\$5.678.238 mil em 2025, e não o saldo isolado não circulante de R\$4.864.673 mil; no comparativo, R\$4.587.823 mil. O documento também sustenta a informação de opinião sem modificação e os PAA de receita e contingências. A identificação externa B3 é DIRECIONAL ENGENHARIA S.A., código CVM 21350 e ticker DIRR3; não foi encontrada nas fontes consultadas alteração que afaste essa atribuição para o período analisado. A busca é delimitada às fontes registradas e não constitui histórico societário exaustivo.

**Exceções:** não foram executados testes substantivos ou de controles sobre a Companhia; logo, este papel não registra distorções reais, falhas de controle, exceções de auditoria ou cobertura de população. Os cenários de risco não são constatações.

**Conclusão:** a NBC TA 200 exige condução ética, ceticismo e julgamento profissional, avaliação de riscos e obtenção de evidência apropriada e suficiente para alcançar segurança razoável antes de concluir. Os dados públicos revisados justificam foco nos terrenos/estoques, receita imobiliária, contingências e consolidação. Sem acesso interno e sem execução dos procedimentos planejados, não se conclui se as demonstrações estão livres de distorção relevante nem se emite opinião independente. A opinião pública citada pertence à PwC.

**Limitações:** sem acesso a administração, razão, contratos, títulos, controles, sistemas, advogados, bancos ou instalações; sem entrevista, circularização, inspeção física, observação, teste de controle ou reperformance de registros da Companhia. O PDF completo público da DFP foi obtido e as seções relevantes foram lidas; a limitação é a falta de evidência subjacente e de trabalho de auditoria, não a indisponibilidade da fonte pública.

**Referências cruzadas:** PT-EC; PT-210/220; PT-300/315/320/330; PT-450/500/501/520/530/540/550/560/570/600.

## Referências

[1] CFC, página de NBC TAs: https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/. Acesso em 22/10/2026.

[2] CFC, NBC TA 200 (R1), texto oficial: https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA200%28R1%29.pdf; ficha: https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2016/NBCTA200%28R1%29. Acesso em 22/10/2026.

[3] RI Direcional, DFP 4T25 V1, PDF integral: https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2. Páginas 16–17, 21, 69 e 115–117; acesso em 22/10/2026.

[4] CVM/RAD, DFP 31/12/2025, V1, NSD 155189: https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1; B3, perfil DIRR: https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br. Acesso em 22/10/2026.


---

# PT-210 — Concordância com os termos do trabalho de auditoria

| Identificação | Informação |
|---|---|
| Código / título | **PT-210 — Concordância com os termos do trabalho de auditoria** |
| Entidade / demonstrações | DIRECIONAL ENGENHARIA S.A. — demonstrações contábeis consolidadas |
| Período | Exercício encerrado em 31/12/2025 |
| Natureza | Papel de trabalho **didático**; não integra nem substitui os papéis do auditor independente da Companhia |
| Norma e itens | NBC TA 210 (R1), “Concordância com os Termos do Trabalho de Auditoria”, na redação publicada pelo CFC e alterada pela Revisão NBC 11: itens 1–8, 9–13, 14–21; orientações A1–A35 conforme aplicáveis; Apêndice 1 como exemplo não obrigatório de carta. Referências centrais: itens 3, 4, 6–13 e A11–A28. |
| Preparador | EDU-AUD-001 (matrícula didática) |
| Data | 22/10/2026 |
| Revisor |  |

## Objetivo, conta e processo

Documentar, para fins exclusivamente didáticos, a avaliação de aceitação/continuidade e a formalização dos termos do trabalho de auditoria das demonstrações consolidadas da Companhia. O PT-210 trata das **condições prévias à auditoria**, do entendimento comum entre administração e auditor, do acordo escrito sobre os termos e das mudanças posteriores no trabalho. Não é teste substantivo de estoques, receita ou provisões, nem reconstitui a aceitação efetivamente realizada pela PwC. A NBC TA 210 distingue estas condições dos aspectos de aceitação do trabalho tratados pela norma de gestão da qualidade; ver item 1 e referência à NBC TA 220.

Não há uma conta contábil objeto de teste neste papel. Para contextualizar a aceitação e o escopo do trabalho consolidado, considera-se o processo de fechamento/consolidação e as divulgações publicadas sobre estoques, receita imobiliária e contingências. A aplicação da estrutura contábil, os deveres da administração e o acesso a informações e pessoas são condições a documentar nos termos do item 6 da NBC TA 210.

## Afirmações e riscos relevantes para este PT

A NBC TA 210 exige determinar se a estrutura de relatório financeiro aplicável é aceitável e obter da administração o reconhecimento de suas responsabilidades pela elaboração das demonstrações, pelo controle interno que considere necessário e por prover acesso a informações, informações adicionais solicitadas e pessoas (item 6(a) e (b)). A formalização escrita deve cobrir objetivo e alcance, responsabilidades do auditor e da administração, estrutura contábil aplicável e forma/conteúdo esperados dos relatórios, inclusive a possibilidade de relatório diferente em certas circunstâncias (item 10).

Os dados abaixo caracterizam **riscos e fatores de escopo**, não achados de distorção:

- A DFP 4T25 V1 obtida no RI informa ativo consolidado de R\$13.219.635 mil e estoques de R\$6.951.508 mil. A Nota 5 p.69 detalha terrenos a incorporar de R\$5.678.238 mil; R\$4.864.673 mil é o componente não circulante, não o total. O BP apresenta estoques circulantes de R\$2.086.835 mil; o componente corrente de terrenos, R\$813.565 mil, é derivado. Para 2024, ativo consolidado de R\$10.067.406 mil e terrenos de R\$4.587.823 mil. Esses montantes justificam descrever claramente demonstrações, período, estrutura contábil e acesso a registros em uma carta hipotética, sem concluir titularidade, valorização, classificação ou completude. [9]
- O relatório público da PwC (pp.115–117) contém opinião sem modificação, ênfase sobre reconhecimento da receita de unidades imobiliárias em construção e PAA de reconhecimento de receita imobiliária e provisões para contingências. Esses assuntos justificam prever no escopo e cronograma a obtenção de informações pertinentes à receita e às estimativas de contingências. Um PAA não é, por si só, distorção, deficiência ou ressalva. [9]
- Como hipóteses a avaliar mediante evidência interna, e não como constatações, podem existir riscos de limitação de escopo, divergência sobre a estrutura de relatório financeiro, mudanças em administração/controle/porte, ou incompreensão do alcance da auditoria. A NBC TA 210 requer discutir ausência de condições prévias (item 8), recusar trabalho sujeito a limitação que provavelmente leve à abstenção, salvo obrigação legal (item 7), e reavaliar termos em auditorias recorrentes conforme as circunstâncias (item 13 e A28).

## População, fontes e critérios

**População / unidade de análise:** o trabalho proposto ou recorrente de auditoria independente das demonstrações consolidadas da Companhia para o exercício encerrado em 31/12/2025; eventual carta/contrato, aditivos, aprovações e comunicações de termos que deveriam compor o dossiê de aceitação. Esses documentos internos não foram disponibilizados. Não se selecionou amostra de saldos, pois o objeto é a documentação do trabalho e suas condições de aceitação.

**Fontes públicas consultadas:**

1. CFC, página “NBC TA – de Auditoria Independente de Informação Contábil Histórica”, que lista NBC TA 210 (R1), DOU de 05/09/2016, e link para a resolução/documento oficial [1].
2. CFC, registro oficial da NBC TA 210 (R1): Resolução 2016/NBCTA210(R1), publicada em 05/09/2016, marcada como vigente e não revogada; o cadastro também registra alterações posteriores, inclusive Revisão NBC 11 [2]. O arquivo oficial da resolução é referenciado em [3].
3. CFC, registro oficial da Revisão NBC 11, publicada em 02/09/2021 e marcada como vigente [4]. Para fins deste papel, a versão é designada **NBC TA 210 (R1), com alterações da Revisão NBC 11**; o cadastro público consultado confirma a alteração da NBC TA 210 (R1). A redação aplicável deve ser lida no texto oficial consolidado disponibilizado pelo CFC, e não apenas no livro histórico de 2012.
4. CVM/RAD, DFP da DIRECIONAL ENGENHARIA S.A., protocolo sequencial 155189, formulário de 31/12/2025, versão 1; endereço eletrônico de entrada no documento [5]. A página identifica PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA como auditor cadastrado e oferece seções consolidadas e pareceres. O PDF integral foi obtido no RI e as páginas impressas pertinentes foram lidas; a tela RAD dinâmica não substitui o documento nem a evidência privada de contratação. [9]
5. B3, página de dados da companhia DIRECIONAL ENGENHARIA S.A., código CVM 21350. A consulta apresenta, em dados econômico-financeiros consolidados, o ativo total de 31/12/2025 de R\$ 13.219.635 mil [6].
6. RI Direcional, páginas Central de Resultados e Documentos Entregues à CVM [7] [8]. A extração textual do índice é dinâmica e não exibe o PDF no próprio corpo; o link direto oficial foi localizado e usado para baixar a DFP anual [9].

**Critérios:** NBC TA 210 (R1) e alterações vigentes para o período, especialmente itens 3–8 e 9–13; exigências sobre mudanças de termos nos itens 14–17; considerações adicionais de aceitação nos itens 18–21. O item 10 exige os elementos mínimos da carta/acordo escrito. O Apêndice 1 oferece exemplo adaptável e não obrigatório. Como critério didático para a estrutura contábil, a equipe deve identificar e avaliar a estrutura declarada pela administração à luz das demonstrações e notas aplicáveis; não se presume neste PT que essa verificação interna tenha ocorrido.

## Procedimentos e classificação

| Nº | Procedimento | Classificação | Evidência / situação |
|---|---|---|---|
| 1 | Consultar a página oficial do CFC para identificar norma, revisão, título e status normativo aplicáveis ao período. | **Realizado com evidência pública** | CFC lista NBC TA 210 (R1), DOU 05/09/2016; cadastro da resolução indica vigente e não revogada. Revisão NBC 11, publicada em 02/09/2021, consta como ato vigente que alterou normas, incluindo NBC TA 210 (R1). [1] [2] [4] |
| 2 | Consultar o RAD/CVM para confirmar a identificação do emissor, período/documento e auditor independente vinculado à DFP. | **Realizado com evidência pública** | Página do DFP sequencial 155189, data-base 31/12/2025, V1; na interface consultada consta PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. Trata-se de evidência do registro público, não de carta de contratação nem dos procedimentos de aceitação da firma. [5] |
| 3 | Corroborar a identificação do emissor e o saldo de ativo total consolidado no perfil B3. | **Realizado com evidência pública** | Página B3 identifica DIRECIONAL ENGENHARIA S.A. e código CVM 21350; tabela consolidada inclui ativo total de 31/12/2025 de R\$ 13.219.635 mil. [6] |
| 4 | Obter a DFP 4T25 V1 integral do RI e ler as seções pertinentes; referenciar por página impressa saldos, comparativos, principais assuntos e opinião. | **Realizado com evidência pública** | PDF obtido; balanço pp.16–17, DRE p.21, Nota 5 p.69 e relatório PwC pp.115–117 lidos. Valores, PAA e opinião foram localizados. Não houve tie-out a razão, teste de auditoria, nem acesso a carta/arquivo privado. [9] |
| 5 | Inspecionar carta de contratação/acordo escrito, aprovação pelos responsáveis apropriados e confirmação do entendimento da administração sobre suas responsabilidades do item 6(b). | **Planejado por falta de acesso** | Carta, ata, aceite e evidência de concordância são documentação privada da Companhia/auditor e não constam das fontes públicas examinadas. Não afirmar que existiram, foram assinados ou continham os requisitos do item 10. |
| 6 | Avaliar a aceitabilidade da estrutura de relatório financeiro efetivamente escolhida, responsabilidades da administração, suficiência de controles e disponibilidade de acesso irrestrito a informações e pessoas. | **Planejado por falta de acesso** | Requer discussão com administração, exame das demonstrações completas, estrutura adotada, controles relevantes e condições efetivas de acesso; nada disso foi acessado neste trabalho didático. Aplicável item 6(a)–(b). |
| 7 | Verificar se houve limitação imposta antes da aceitação, impedimento de acesso ou condição que levasse a relatório com abstenção, e avaliar consequência para aceitar/recusar o trabalho. | **Planejado por falta de acesso** | Não houve contato com administração, auditor ou governança nem acesso aos termos propostos. Aplicável itens 7–8. Não se presume ausência de restrição pelo fato de existir relatório público posterior. |
| 8 | Inspecionar termos de trabalho recorrente, reavaliar necessidade de revisão/lembrete, verificar aditivos ou mudança de escopo e validar justificativa e acordo escrito se alterados. | **Planejado por falta de acesso** | Histórico de contratos e aditivos não é público na evidência obtida. Aplicável itens 13–17 e A28–A33. |
| 9 | Preparar, para fins de treinamento, lista de verificação / minuta hipotética de carta com objetivo, alcance, responsabilidades, estrutura contábil e relatórios previstos, incluindo circunstâncias de forma/conteúdo diferentes. | **Simulado para fins didáticos** | A minuta hipotética não é carta da Companhia, não deve ser assinada nem apresentada como acordo real. Deve seguir item 10 e adaptar o exemplo não obrigatório do Apêndice 1 às circunstâncias. |
| 10 | Considerar se existem exigências legais ou regulatórias suplementares ou estrutura legalmente prescrita que modifiquem os termos ou o relatório previsto. | **Planejado por falta de acesso** | A análise exigiria leitura da base legal e demonstrações completas e, se aplicável, avaliação dos itens 18–21. Não foi realizada conclusão jurídica/regulatória específica neste PT. |

## Evidências e referências cruzadas

- **E-210-01:** página de normas de auditoria CFC e índice de NBC TA [1]. Referência cruzada: norma/itens aplicáveis acima.
- **E-210-02:** cadastro CFC de NBC TA 210 (R1) e resolução oficial [2] [3]. O registro informa publicação em 05/09/2016, vigor e ausência de revogação.
- **E-210-03:** cadastro CFC da Revisão NBC 11 [4], publicada em 02/09/2021; a alteração pertinente integra a identificação da versão aqui usada.
- **E-210-04:** RAD/CVM, DFP 2025 V1, sequencial 155189, data-base 31/12/2025 [5]. A interface CVM confirma metadados e auditor indicado. O PDF integral da mesma DFP foi obtido na Central de Resultados do RI [9]; foram lidas as páginas impressas 16–17, 21, 69 e 115–117 para documentar saldos, PAA e opinião. Isso não fornece acesso ao arquivo de auditoria privado da PwC.
- **E-210-05:** B3, cadastro e dados consolidados do emissor [6]. Confirma nome, código CVM e ativo total em 31/12/2025, mas não constitui evidência das condições prévias ou do acordo escrito.
- **E-210-06:** páginas RI Direcional de navegação de resultados/documentos entregues [7] [8]. A extração textual do índice é dinâmica e não mostra o PDF no próprio texto; o arquivo anual foi obtido diretamente pelo link oficial [9].
- **X-210-1 (proposto, não obtido):** carta de contratação aprovada/assinada e eventuais aditivos.
- **X-210-2 (proposto, não obtido):** memorando de aceitação/continuidade, checklist da estrutura de relatório financeiro, conflitos/independência e recursos.
- **X-210-3 (proposto, não obtido):** evidência da administração sobre controles e acesso a registros, documentação, informações adicionais e pessoas.

## Resultados, exceções e conclusão

**Resultados de inspeção pública:** a DFP 4T25 V1, obtida no RI e lida nas páginas impressas 16–17, 21, 69 e 115–117, informa ativo consolidado de R\$13.219.635 mil, estoques de R\$6.951.508 mil e terrenos a incorporar de R\$5.678.238 mil em 2025. O saldo de R\$4.864.673 mil é o componente não circulante, não o total da classe; o saldo comparativo de terrenos em 2024 é R\$4.587.823 mil. A DFP contém PAA sobre reconhecimento de receita imobiliária e provisões para contingências e opinião PwC sem modificação. O registro CVM identifica auditor e protocolo; a B3 confirma nome, código CVM e ticker. A leitura pública não comprova precondições, aceitação ou termos privados do trabalho da PwC. [5] [6] [9]

**Exceção documental principal:** não foi obtida evidência pública da carta/contrato de auditoria nem de reconhecimento, pela administração, das responsabilidades do item 6(b). Não é possível determinar com esta evidência se a estrutura financeira foi avaliada como aceitável, se houve acesso irrestrito acordado, se termos foram aprovados ou se ocorreu revisão da contratação. A presença de DFP publicada e opinião do auditor não substitui tais evidências e não prova, isoladamente, como as condições foram avaliadas antes da aceitação.

**Conclusão didática:** a DFP pública foi obtida e lida nas páginas identificadas, o que permite localizar o período, a entidade, os saldos, PAA e opinião divulgados. **Isso não é suficiente para concluir que os requisitos da NBC TA 210 foram cumpridos na aceitação/continuidade ou na formalização dos termos do trabalho real da Direcional/PwC.** Em um dossiê real, a conclusão ficaria pendente até obter carta/acordo escrito, confirmar as condições do item 6, avaliar a estrutura de relatório financeiro, acesso acordado e eventuais limitações/aditivos. Não se identificou, nem se afirma, não conformidade ou distorção contábil da Companhia.

## Limitações e uso

Este é um produto pedagógico baseado em fontes abertas. O PDF integral da DFP foi obtido; foram examinadas as páginas relevantes indicadas em E-210-04, sem auditoria item a item da totalidade das divulgações. Não houve entrevista, confirmação externa, consulta à administração ou ao auditor, inspeção física, acesso a controles/razões/documentos internos ou obtenção da carta/contrato da PwC. Nenhum procedimento do auditor independente foi reproduzido ou atribuído ao preparador. Procedimentos internos faltantes são planos; a minuta de carta é apenas simulação.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA de Auditoria Independente de Informação Contábil Histórica, índice normativo consultado em 22/10/2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, Resolução 2016/NBCTA210(R1), registro oficial, publicada no DOU de 05/09/2016; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2016/NBCTA210%28R1%29>).
- **Ref. 3** — CFC, NBC TA 210 (R1), arquivo oficial da resolução; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA210%28R1%29.pdf>).
- **Ref. 4** — CFC, Revisão NBC 11, registro oficial, publicada no DOU de 02/09/2021; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?codigo=2021/REVIS%C3%83ONBC11>).
- **Ref. 5** — CVM/RAD, DIRECIONAL ENGENHARIA S.A., DFP 31/12/2025, V1, protocolo sequencial 155189; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 6** — B3, DIRECIONAL ENGENHARIA S.A., perfil e dados econômico-financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 7** — RI Direcional, Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 8** — RI Direcional, Documentos Entregues à CVM; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/documentos-entregues-a-cvm/>).
- **Ref. 9** — RI Direcional, DFP 4T25 V1, páginas impressas 16–17, 21, 69 e 115–117; acesso em 22/10/2026; [abrir fonte](<https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2>).


---

# PT-220 — Gestão da qualidade da auditoria de demonstrações contábeis

**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações contábeis consolidadas  
**Exercício:** encerrado em 31/12/2025  
**Tipo de documento:** papel de trabalho didático; não é relatório de auditoria nem documentação do auditor independente  
**Data de acesso às fontes:** 22/10/2026  
**Preparador:** matrícula didática **EDU-AUD-001** — 22/10/2026  
**Revisor:** ____________________________________  **Data:** __________________

## Código, título, norma e itens

**Código 220.** Gestão da qualidade no nível do trabalho de auditoria de demonstrações contábeis, incluindo auditoria de grupo.

Norma aplicável ao período: **NBC TA 220 (R3) — Gestão de Qualidade da Auditoria de Demonstrações Contábeis**, texto oficial do Conselho Federal de Contabilidade (CFC), aprovada em 18/11/2021 e publicada no DOU em 09/12/2021. O item 10 estabelece aplicação às auditorias de períodos iniciados em ou após 01/01/2023; portanto, é a versão pertinente ao exercício de 2025. O índice oficial do CFC identifica a revisão como R3. O texto substituiu a NBC TA 220 (R2). [1] [2]

Itens centrais para este papel: alcance e aplicação a demonstrações de grupos (itens 1 e A1); objetivo (11); liderança e responsabilidade geral (13–15, 40); ética e independência (16–21); aceitação e continuidade (22–24); recursos (25–28); direção, supervisão, revisão e evidência (29–34); consultas (35); revisão de qualidade do trabalho (36); diferenças de opinião (37–38); monitoramento e remediação (39); documentação (41). A seleção orienta a avaliação didática do processo de qualidade e não substitui a aplicação integral da norma.

## Objetivo, conta e processo

**Objetivo do PT:** estruturar a avaliação da gestão de qualidade que deveria sustentar uma auditoria independente das demonstrações consolidadas de 2025, identificando quais aspectos podem ser reconhecidos somente em documentos públicos e quais exigiriam inspeção da documentação de auditoria e dos controles da firma. O objetivo final previsto na NBC TA 220, item 11, é obter segurança razoável de que as responsabilidades do auditor foram cumpridas conforme as normas e requisitos aplicáveis e que o relatório é apropriado nas circunstâncias. Este PT didático **não** conclui que a equipe real cumpriu esses requisitos.

**Processo abrangido:** governança da qualidade do trabalho de auditoria consolidada da companhia, com ênfase no envolvimento do sócio, competência e suficiência de recursos, revisão de julgamentos significativos, consultas, eventual revisão de qualidade do trabalho, conclusão de evidência suficiente e documentação.

**Contas/processos que motivam o foco de qualidade (não são objeto de teste substantivo neste PT):** estoques imobiliários, especialmente terrenos a incorporar, reconhecimento de receita imobiliária e provisões para contingências. O documento público da DFP identifica reconhecimento de receita imobiliária e provisões para contingências como principais assuntos de auditoria (PAA). Isso é relevante para definir onde se esperaria evidência de supervisão, julgamento e revisão, mas **não** demonstra por si só a adequação ou inadequação do trabalho realizado.

## Afirmações e riscos relevantes

Este é um papel de qualidade, e não um programa de auditoria de saldos. As afirmações abaixo são dimensões de risco a considerar na gestão do trabalho, não exceções encontradas.

- **Existência e direitos sobre terrenos/estoques:** hipótese de risco de distorção caso registros, títulos, contratos, estágio dos empreendimentos ou controle sobre terrenos não estejam suficientemente suportados. Procedimentos de confirmação, inspeção física, exame de títulos e confronto com razão contábil não foram executados neste trabalho didático.
- **Avaliação e alocação dos estoques:** hipótese de risco relacionada a custo incorporado, capitalização, alocação de custos, recuperabilidade e estimativas. Nenhuma avaliação independente de custo ou valor realizável líquido foi realizada.
- **Reconhecimento e corte de receita imobiliária:** tema indicado publicamente como PAA. A complexidade do reconhecimento ao longo do tempo, mensuração de progresso, contratos e corte constitui hipótese de risco para fins de planejamento, não constatação de falha.
- **Completude e mensuração de provisões para contingências:** tema indicado publicamente como PAA. Incerteza de desfecho, probabilidade, mensuração e divulgação podem exigir julgamentos e consulta; não houve acesso a processos judiciais, cartas de advogados nem cálculos internos.
- **Qualidade no nível do trabalho:** risco de que recursos, competências, tempo, supervisão, revisão de julgamentos significativos, consultas ou documentação não fossem suficientes. Sem o arquivo de auditoria da PwC, esses fatores não podem ser verificados; são procedimentos planejados, não achados.
- **Independência, aceitação e continuidade:** requisitos previstos nos itens 16–24, cuja evidência é predominantemente interna à firma. Nenhuma declaração de independência ou registro de aceitação/continuidade foi inspecionado.
- **Grupo/consolidação:** como a DFP é consolidada, considerar coordenação e evidência em componentes como risco de planejamento, se houver componentes relevantes. A composição do grupo, uso de auditores de componentes, materialidade e extensão do trabalho por componente não foram inferidos nem confirmados neste PT.

## População, fontes e critérios

**População conceitual:** documentação do trabalho de auditoria independente da DFP consolidada de 2025, inclusive arquivo do sócio e da equipe, papéis relativos a estoques, receitas e contingências, consultas, revisões, comunicações, aprovação do relatório e evidências de qualidade da firma. Essa população não foi disponibilizada ao preparador didático. Não foi definida amostra de documentos internos.

**População pública consultada:** (i) DFP de 31/12/2025 informada na CVM, versão 1, protocolo de 09/03/2026, número sequencial 155189; (ii) página oficial da Central de Resultados da companhia; e (iii) perfil da companhia na B3. A tela CVM consultada identifica PricewaterhouseCoopers Auditores Independentes Ltda. como auditor e permite selecionar demonstrativos individuais/consolidados, notas, pareceres e declarações. A página B3 identifica DIRECIONAL ENGENHARIA S.A., código CVM 21350 e negociação DIRR3; exibe o ativo total consolidado de 31/12/2025 de R\$ 13.219.635 mil, corroborando esse dado público. [3] [4] [5]

**Dados públicos revisados (valores em R\$ mil):** ativo consolidado de 13.219.635 em 31/12/2025 e 10.067.406 em 31/12/2024; estoques de 6.951.508 e 5.532.090; terrenos a incorporar de 5.678.238 em 2025 e 4.587.823 em 2024; estoques circulantes de 2.086.835 e não circulantes de 4.864.673 em 2025. O componente circulante de terrenos, 813.565, é diferença aritmética, pois o BP não o segrega por natureza. As páginas impressas 16–17, 21, 69 e 115–117 da DFP 4T25 V1 foram lidas. A PwC emitiu opinião sem modificação; o relatório descreve reconhecimento de receita imobiliária e provisões para contingências como PAA. Revisão documental pública não valida a qualidade do trabalho da PwC nem os registros internos. [6]

**Critérios:** NBC TA 220 (R3), itens citados acima; documentação pública restrita aos emissores oficiais indicados; suficiência, competência e confiabilidade da evidência a serem avaliadas pela equipe com base nas normas de auditoria. B3 e RI servem para identificação e navegação pública, não substituem os demonstrativos oficiais arquivados na CVM. Data de corte das consultas: 22/10/2026.

## Procedimentos realizados e planejados

Legenda: **PÚBLICO — realizado com evidência pública** significa somente leitura/consulta de material público. **PLANEJADO — falta de acesso** significa que o procedimento requer arquivo de auditoria, acesso à firma/companhia ou evidência independente não disponível. **SIMULADO — didático** significa exercício hipotético de desenho ou aplicação em material fornecido para fins didáticos, sem execução sobre o arquivo real.

| ID | Classificação | Procedimento e vínculo normativo | Evidência/resultado |
|---|---|---|---|
| 220-01 | PÚBLICO — realizado | Consultar o índice oficial CFC e identificar a edição aplicável ao exercício; verificar título, versão, data e vigência (itens 1, 10–11). | CFC identifica NBC TA 220 (R3), DOU 09/12/2021; vigência para períodos iniciados a partir de 01/01/2023. Realizado por consulta documental, não é avaliação de cumprimento pela firma. [1] [2] |
| 220-02 | PÚBLICO — realizado | Consultar o registro CVM indicado, identificar o documento DFP, seu número sequencial, demonstrativos disponíveis e auditor cadastrado (contexto para itens 1–4 e 22–24). | Página da CVM, documento seq. 155189, campos de DFP e auditor; auditor exibido como PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. Não houve confirmação externa do vínculo nem contato com a firma. [3] |
| 220-03 | PÚBLICO — realizado | Consultar o perfil oficial B3 para confirmar a identificação do emissor e cotejar o ativo consolidado de 31/12/2025 com o dado-base (população e escopo). | Perfil B3 identifica DIRECIONAL ENGENHARIA S.A., DIRR3, CVM 21350 e mostra ativo consolidado de 13.219.635 (R\$ mil) em 31/12/2025. É cotejo de dado publicado, não teste de detalhe nem confirmação de saldo. [5] |
| 220-04 | PÚBLICO — realizado | Consultar a Central de Resultados oficial da companhia e ler o PDF anual da DFP 4T25 V1 obtido pelo link oficial (escopo de fonte e população). | O extrator textual do índice dinâmico não exibia o arquivo no corpo da página; o PDF integral foi baixado diretamente do RI. Foram lidos BP pp.16–17, DRE p.21, Nota 5 p.69 e relatório do auditor pp.115–117. Sem acesso a papéis privados da firma. [6] |
| 220-05 | PLANEJADO — falta de acesso | Obter carta/termo de contratação, avaliação de aceitação e continuidade, conflitos, independência da firma/rede e documentação de ética; verificar aprovações, consultas e solução de ameaças (itens 16–24 e 41(a)). | Requer evidência interna da firma. Não executado. Solicitar evidência datada e específica ao trabalho e avaliar violações/medidas, sem pressupor sua inexistência. |
| 220-06 | PLANEJADO — falta de acesso | Inspecionar plano de auditoria, organograma da equipe, matriz de competências, disponibilidade de tempo, especialistas e auditores de componentes, quando aplicável; examinar alterações de recursos (itens 25–28). | Requer arquivo de planejamento e registros de pessoal/tempo. Não executado; nenhuma conclusão sobre suficiência ou competência da equipe real. |
| 220-07 | PLANEJADO — falta de acesso | Inspecionar evidência de direção, supervisão e revisão, especialmente papéis relacionados a julgamentos significativos sobre receita, provisões e estoques, e a revisão oportuna pelo sócio (itens 29–34 e 40). | Requer papéis de auditoria e trilha de revisão; não foi inspecionado arquivo interno. PAA públicos apenas ajudam a delimitar áreas de foco. |
| 220-08 | PLANEJADO — falta de acesso | Obter consultas técnicas, divergências, conclusões, implementação, comunicações formais e eventual documentação de revisão de qualidade do trabalho; conferir conclusão antes da data do relatório (itens 35–38 e 41(b)–(c)). | Nenhum registro interno disponível. Não se conclui se consulta ou revisão independente foi exigida, nomeada ou concluída. |
| 220-09 | PLANEJADO — falta de acesso | Examinar avaliação final do sócio de que evidência apropriada e suficiente foi obtida, revisão das demonstrações/relatório, comunicações à governança e registros de monitoramento/remediação relevantes (itens 31–34, 39–41). | Requer arquivo de encerramento e informações internas de monitoramento. Não executado. A opinião sem ressalva divulgada não constitui, isoladamente, prova de atendimento aos requisitos de qualidade. |
| 220-10 | SIMULADO — didático | Aplicar, somente como desenho de programa, uma matriz de julgamento crítico para receita, contingências e terrenos, relacionando risco, procedimento, revisor e evidência esperada (itens 13–15 e 29–35). | Exercício de planejamento hipotético. Nenhum procedimento da matriz foi executado no trabalho real da PwC, e nenhum resultado ou exceção é atribuído ao auditor. |
| 220-11 | SIMULADO — didático | Preencher uma lista de verificação fictícia de conclusão do sócio com campos para ética, recursos, consultas, revisão e documentação (itens 21, 25–41). | Modelo didático sem conteúdo de arquivo real. Não representa declaração, aprovação ou confirmação do sócio do trabalho. |

## Evidências e referências cruzadas

- **E-01 / REF 1–2:** texto e índice oficiais do CFC para versão, título, itens e vigência da NBC TA 220 (R3). Referência cruzada aos procedimentos 220-01 e à seleção normativa deste PT.
- **E-02 / REF 3:** página CVM do documento de número sequencial 155189, DFP 2025, identificador de auditor e seções disponíveis para demonstrações e notas. Referência a 220-02 e à população pública. A tela dinâmica não preserva uma paginação de relatório verificável neste acesso; não foi criada numeração de página.
- **E-03 / REF 4:** índice da Central de Resultados da Direcional; extração textual dinâmica não exibia o PDF no próprio texto. A cópia integral da DFP foi obtida diretamente pelo endereço oficial e as páginas impressas citadas foram lidas. Referência a 220-04. [6]
- **E-04 / REF 5:** página B3 do emissor, identificação da companhia e resumo de balanço consolidado. Referência a 220-03. O resumo exibe o ativo consolidado comparativo, não detalha todas as rubricas de estoque.
- **E-05 / DFP pública:** Nota 5 p.69, balanço pp.16–17, DRE p.21 e relatório PwC pp.115–117 da DFP 4T25 V1 obtida do RI; saldos, PAA e opinião foram localizados no documento. Não houve tie-out a razão ou exame de evidência interna. [6]
- **PL-01:** itens 220-05 a 220-09 formam a lista de evidências internas a solicitar. Não são evidência obtida.
- **SIM-01:** itens 220-10 e 220-11 são somente modelos demonstrativos, sem relação de execução com o trabalho independente real.

## Resultados, exceções, conclusão e limitações

**Resultados públicos observados:** a versão oficial pertinente é NBC TA 220 (R3), vigente para períodos iniciados a partir de 01/01/2023. A DFP 4T25 V1 foi obtida e lida nas páginas registradas; estoques e terrenos são 6.951.508 e 5.678.238 em 2025, com comparativos de 5.532.090 e 4.587.823. O relatório público identifica PwC, opinião sem modificação e PAA de receita e contingências. A leitura não permite inferir se a equipe real cumpriu os requisitos de qualidade nem substitui acesso ao arquivo da firma.

**Exceções:** não foram executados testes de qualidade, independência ou supervisão sobre o arquivo da firma; portanto, não há achado sobre esses temas. A leitura das páginas da DFP sustenta os fatos societários citados, mas não comprova como a PwC planejou ou executou o trabalho. Não se atribuem falhas ou conformidade à firma sem evidência apropriada.

**Conclusão didática:** com base exclusivamente na leitura de fontes públicas especificadas, foi possível identificar o referencial normativo e o contexto do trabalho e estabelecer áreas de qualidade a investigar. **Não há base de evidência para concluir se a PwC ou o sócio do trabalho cumpriram, ou deixaram de cumprir, a NBC TA 220 (R3).** A conclusão de qualidade permanece em aberto até que sejam executados os procedimentos planejados e examinada documentação apropriada. A opinião pública sem ressalva não substitui essa evidência.

**Limitações e salvaguardas:** este PT é didático, preparado sem acesso ao arquivo de auditoria, à administração, à governança, aos sistemas contábeis ou aos auditores. Não houve entrevista, confirmação externa, inspeção física, observação, recálculo, reperformance, inspeção de contratos, títulos de terrenos, processos judiciais, papéis de trabalho, cartas de independência ou comunicações internas. Nenhuma constatação sobre fatos sem suporte foi formulada. Hipóteses de risco são identificadas como tais. As informações públicas sobre procedimentos do auditor limitam-se ao que a companhia/CVM divulgou.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA de Auditoria Independente, índice oficial, NBC TA 220 (R3), acesso em 22/10/2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, Norma Brasileira de Contabilidade NBC TA 220 (R3), Gestão de Qualidade da Auditoria de Demonstrações Contábeis, 18/11/2021, DOU 09/12/2021, texto oficial, itens 1, 10–41 e A1; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA220%20%28R3%29.pdf>).
- **Ref. 3** — CVM, DIRECIONAL ENGENHARIA S.A., DFP de 31/12/2025, V1, protocolo de 09/03/2026, documento seq. 155189, seções DFs Consolidadas, Notas Explicativas e Pareceres e Declarações, ano-base 2025; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — DIRECIONAL ENGENHARIA S.A., RI, Central de Resultados, página de navegação de documentos financeiros, acesso em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 5** — B3, DIRECIONAL ENGENHARIA S.A., perfil do emissor, código CVM 21350, DIRR3, resumo de balanço consolidado, 31/12/2025, acesso em 22/10/2026; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 6** — RI Direcional, DFP 4T25 V1, páginas impressas 16–17, 21, 69 e 115–117; acesso em 22/10/2026; [abrir fonte](<https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2>).


---

# PT-230 — Documentação de auditoria

**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações contábeis consolidadas  
**Exercício:** encerrado em 31/12/2025  
**Norma:** NBC TA 230 (R1) — Documentação de Auditoria; texto oficial CFC aplicável a períodos encerrados em ou após 31/12/2016. Itens 1–16 e A1–A24.  
**Tipo de trabalho:** papel de trabalho didático; não é papel integrante do arquivo da auditoria da PwC nem asseguração independente.  
**Data de acesso às fontes:** 22/10/2026  
**Preparador:** EDU-AUD-001 — matrícula didática; 22/10/2026  
**Revisor:** ____________________________________ **Data:** __________________

## Objetivo, conta e processo

Documentar, para fins didáticos, como registrar o planejamento, os procedimentos e as limitações relativos à conta consolidada de estoques, com foco em terrenos a incorporar, e os vínculos com os assuntos-chave de auditoria (PAA) de reconhecimento de receita imobiliária e provisões para contingências divulgados no relatório do auditor independente. O objetivo específico deste PT, em linha com NBC TA 230, item 5, é exemplificar documentação que permita entender o trabalho que foi de fato executado e diferenciar claramente esse trabalho de procedimentos ainda planejados ou simulados.

**Conta/processo central:** estoques consolidados em 31/12/2025, incluindo terrenos a incorporar; reconhecimento, mensuração, classificação e divulgação dos estoques no processo de incorporação/construção imobiliária. **Interfaces consideradas:** reconhecimento de receita imobiliária (PAA) e provisões/contingências (PAA). Este PT não conclui sobre a adequação contábil dos saldos nem sobre a suficiência da auditoria da companhia.

## Norma e requisitos de documentação considerados

O texto oficial do CFC identifica a norma como **NBC TA 230 (R1) — Documentação de Auditoria**. A ficha oficial informa Resolução CFC **2016/NBCTA230(R1)**, publicação no DOU em 05/09/2016, vigente e não revogada; a alteração posterior ali relacionada é a Revisão NBC 03, que não altera a sigla de consolidação indicada para a norma. A NBC TA 230 (R1) estabelece aplicação para auditorias de períodos findos em ou após 31/12/2016, portanto a versão aplicável ao exercício findo em 31/12/2025 é R1, conforme conferência da listagem oficial do CFC em 22/10/2026. [1] [2]

Os requisitos usados neste PT são: **itens 1–6**, alcance, finalidade, objetivo e definições; **item 7**, documentação tempestiva; **item 8**, documentação suficiente para que auditor experiente entenda natureza, época e extensão dos procedimentos, resultados/evidências e assuntos/julgamentos significativos; **item 9**, identificação dos itens testados, executor/data e revisor/data/extensão; **itens 10–11**, discussões significativas e tratamento de informações inconsistentes; **itens 12–13**, eventual não atendimento de requisito e fatos/procedimentos/conclusões posteriores à data do relatório; **itens 14–16**, montagem tempestiva, retenção e alterações posteriores do arquivo final. A1–A24 são considerados como material explicativo, especialmente tempestividade, forma/conteúdo/extensão, documentação de assuntos significativos e montagem do arquivo. [1]

## Afirmações e riscos considerados

As afirmações relevantes para estoques são **existência**, **direitos e obrigações**, **integralidade**, **avaliação e alocação**, **classificação** e **apresentação/divulgação**. Para receita imobiliária, as afirmações relacionadas incluem **ocorrência**, **exatidão**, **corte**, **integralidade** e **apresentação**. Para contingências/provisões, incluem **integralidade**, **avaliação**, **classificação** e **divulgação**.

A DFP pública e os fatos-base disponibilizados para este exercício identificam estoques como parcela expressiva do ativo consolidado e terrenos a incorporar como maior rubrica individual. Isso sustenta uma **área de atenção/risco de auditoria didático**, não uma constatação de distorção: saldos relevantes de terrenos podem estar expostos, em tese, a risco de existência, titularidade, custo apropriado, alocação por empreendimento, recuperabilidade e classificação. O elevado volume de julgamentos em incorporação e construção também pode, em tese, afetar a mensuração de estoque e o corte/valor da receita. Essas possibilidades não foram testadas nem confirmadas neste PT.

A existência de PAA de reconhecimento de receita imobiliária e provisões para contingências no relatório público da PwC orienta a seleção de áreas para documentação didática. Um PAA descreve assunto que exigiu atenção significativa do auditor, mas não constitui por si só evidência pública dos testes subjacentes, de achado de distorção ou de falha de controle. Não se infere risco ocorrido além do que o relatório expressamente divulga. A opinião sem ressalva reportada publicamente não substitui exame independente nem permite inferir procedimentos específicos realizados pela PwC.

## População, fontes e critérios

**População conceitual para uma auditoria completa:** composição integral do saldo consolidado de estoques por entidade, empreendimento, natureza (inclusive terrenos), localização e estágio; razão auxiliar e conciliações com razão geral e demonstrações; documentação de titularidade/aquisição; contratos, orçamento/custo incorrido e estimativas; movimentações e baixas do exercício; inventário físico quando pertinente; e divulgações relacionadas. Para receita e contingências, populações seriam os contratos/vendas e processos/assuntos jurídicos pertinentes ao período e data-base. **Essas populações internas não foram obtidas**; não foi definida amostra real.

**Fontes públicas efetivamente consultadas:** (i) CVM, consulta da DFP 31/12/2025 V1, documento identificado pelo endereço fornecido e protocolo informado como enviado em 09/03/2026; (ii) perfil da companhia na B3; (iii) RI Direcional, central de resultados; e (iv) texto e ficha oficiais CFC da NBC TA 230. A consulta da DFP identifica PwC como auditor independente; a fonte B3 apresenta informações consolidadas, inclusive ativo total em 31/12/2025. Para os valores detalhados de estoque e terreno e para PAA/opinião, este PT registra os fatos-base indicados para a tarefa como dados a confrontar na DFP/relatório público, sem afirmar reexecução de teste contábil. [1] [2] [3] [4] [5]

**Critérios de execução e documentação:** (a) rastreabilidade da afirmação para sua fonte identificável; (b) separação entre dado publicado e hipótese; (c) identificação do status do procedimento; (d) registro de população, seleção e característica do item quando houver teste; e (e) resultados, exceções, julgamento e limitação explicitados. Nenhum limiar de materialidade foi determinado, pois não se obteve plano de auditoria, materialidade definida pela equipe ou dados necessários para estabelecer uma base apropriada.

## Procedimentos e evidências

Legenda obrigatória: **[REALIZADO — evidência pública]** significa apenas inspeção documental de publicação pública, sem validação de registros subjacentes; **[PLANEJADO — falta de acesso]** indica procedimento futuro, não executado; **[SIMULADO — didático]** é exemplo de desenho/registro de teste, sem seleção ou execução real. Nenhum procedimento abaixo representa confirmação externa, entrevista, inspeção física, acesso a sistemas/registros internos ou reexecução dos testes da PwC.

| ID / status | Procedimento e alcance | Evidência e referência cruzada | Resultado/limitação |
|---|---|---|---|
| P01 **[REALIZADO — evidência pública]** | Inspecionar a ficha oficial CFC e a relação vigente de NBC TA para identificar nome, revisão e vigência da NBC TA 230 para o exercício. | E-01; refs. [1] e [2]. | A fonte oficial identifica NBC TA 230 (R1), Resolução 2016/NBCTA230(R1), vigente; período encerrado em 31/12/2025 está dentro da vigência indicada. Não é teste dos procedimentos da companhia. |
| P02 **[REALIZADO — evidência pública]** | Consultar a tela pública CVM indicada para identificar o emissor/DFP e auditor nela apresentado. | E-02; ref. [3], DFP 31/12/2025 V1, consulta de dados da empresa/identificação do auditor, sem página estável na tela HTML. | A tela identifica PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. como auditor. Isso comprova apenas o que a divulgação informa; não autentica o arquivo de auditoria da PwC. |
| P03 **[REALIZADO — evidência pública]** | Confrontar a informação de ativo total consolidado da DFP fornecida como fato-base com o campo consolidado de 31/12/2025 no perfil B3. | E-03; ref. [4], B3, “Dados Econômico-Financeiros — R\$ mil / Balanço Patrimonial — Consolidado”, linha “Ativo Total”, coluna 31/12/2025, s.p. (página web). | B3 apresenta R\$13.219.635 mil. Confronto de publicação apenas; sem conciliação a razão geral nem atestação de saldo. |
| P04 **[REALIZADO — evidência pública]** | Ler o PDF integral da DFP 4T25 V1 obtido diretamente na Central de Resultados do RI; rastrear saldos, notas, PAA e opinião às páginas impressas. | E-04; refs. [3] e [6]. Balanço pp.16–17; DRE p.21; Nota 5 p.69; relatório PwC pp.115–117. | Estoques: R\$6.951.508 mil em 2025; terrenos a incorporar total R\$5.678.238 mil, dos quais R\$4.864.673 mil não circulantes e R\$813.565 mil de componente corrente derivado. Em 2024, terrenos R\$4.587.823 mil. A DFP informa PAA de receita e contingências e opinião sem modificação. Leitura pública não é teste de registros nem reexecução de trabalho da PwC. |
| P05 **[PLANEJADO — falta de acesso]** | Obter razão geral e composição analítica de estoques em 31/12/2025; reconciliar total por conta/empreendimento e grupo consolidado com demonstrações e notas; investigar diferenças. | Evidência futura a obter: razão geral, subledger, consolidação e conciliação assinada; vinculação futura E-05. | Não executado. Sem os relatórios internos não há população, reconciliação ou conclusão sobre integridade/exatidão do saldo. |
| P06 **[PLANEJADO — falta de acesso]** | Selecionar itens da população com método documentado; inspecionar documentos de aquisição/registro, contratos, pagamentos e evidência legal adequada para titularidade e existência dos terrenos selecionados; examinar custos capitalizados e alocação por empreendimento. | Evidência futura: documentação de compra/titularidade, pagamentos, cadastro do terreno, composição de custos e critério de seleção; vinculação futura E-06. | Não executado. Não se selecionou amostra, não se fez confirmação externa nem inspeção física/legal. |
| P07 **[PLANEJADO — falta de acesso]** | Avaliar mensuração e recuperabilidade de estoque, incluindo custo, orçamento atualizado, evidências de venda/realização quando aplicável e alocação entre terreno, obra e unidades; testar corte e movimentações próximas a 31/12/2025. | Evidência futura: memória de custos, orçamento por projeto, relatórios de vendas e movimentações, documentos suporte e critérios contábeis; vinculação futura E-07. | Não executado. Riscos de custo indevido, alocação inadequada, corte ou recuperabilidade são hipóteses de risco, não exceções constatadas. |
| P08 **[PLANEJADO — falta de acesso]** | Para o PAA de receita imobiliária, obter a descrição detalhada do assunto e executar testes selecionados de contratos, obrigações de desempenho/medição, cálculo e corte contra documentação pertinente, além de avaliar estimativas e divulgações. | Evidência futura: programa de auditoria, contratos e documentos de medição/recebimento, lançamentos e notas; vinculação futura E-08. | Não executado. O PAA público não revela a amostra, os resultados ou o detalhe integral dos procedimentos da PwC. |
| P09 **[PLANEJADO — falta de acesso]** | Para provisões/contingências, obter composição da administração, cartas/retornos jurídicos, andamento e avaliação dos casos; confrontar classificação, estimativas, eventos subsequentes pertinentes e divulgação. | Evidência futura: listagem completa, respostas jurídicas, análises e atas pertinentes, cálculos e divulgações; vinculação futura E-09. | Não executado. Não houve circularização, contato com advogados, consulta a processos internos nem confirmação. Não se conclui sobre completude ou adequação de provisões. |
| P10 **[SIMULADO — didático]** | Exemplo de registro que seria exigido por TA 230, itens 8–9: “seleção de 1 terreno da população reconciliada; identificar por código interno, município e projeto; documentar origem do item, período, execução, resultado, evidência e conclusão; registrar nome/matrícula do executor e data; revisor, data e extensão”. | Modelo demonstrativo sem código real de terreno ou evidência; não se cria número E de evidência real. | Nenhum item foi selecionado ou testado. A frase não registra trabalho feito e não deve ser copiada ao arquivo real como evidência de execução. |
| P11 **[SIMULADO — didático]** | Exemplo de memorial para assunto significativo: documentar por que a concentração de terrenos e o PAA de receita/contingências mereceriam avaliação de risco; premissas, fontes, respostas planejadas, fatos contraditórios, conclusões e revisão. | Referências públicas E-03/E-04 apenas para planejar; ver refs. [3] e [4]. | Simulação de formato. Nenhuma discussão com administração/governança ou consulta à equipe de auditoria foi realizada; não foi avaliada a conclusão da PwC. |
| P12 **[PLANEJADO — falta de acesso]** | Completar documentação de executor/revisor, revisão de diferenças, discussões de assuntos significativos, aprovação e montagem tempestiva do arquivo final, nos termos dos itens 9–16 da NBC TA 230. | Evidência futura: assinaturas/identificações e datas, revisão, comunicações, índice e registro de montagem/retenção; vinculação futura E-10. | Não executado. Revisão deste PT permanece em branco; não há arquivo final de auditoria real sob controle do preparador. |

### Mapa de evidências e referências cruzadas

- **E-01 — Norma:** ficha oficial CFC NBC TA 230 (R1) e texto integral oficial; base normativa deste PT. Referências [1] e [2].
- **E-02 — Identificação do auditor/DFP:** consulta CVM indicada, DFP 31/12/2025 V1; a tela HTML identifica a PwC. Ref. [3].
- **E-03 — Ativo total consolidado:** perfil B3, balanço consolidado, linha “Ativo Total”, data 31/12/2025; valor apresentado em R\$ mil. Ref. [4].
- **E-04 — Saldos, PAA e opinião:** DFP 4T25 V1 obtida no RI; balanço pp.16–17, DRE p.21, Nota 5 p.69 e relatório PwC pp.115–117. Valores e divulgações citados no P04 foram localizados no documento. Sem conciliação a razão, confirmação, amostra real ou reexecução de procedimentos da PwC. Refs. [3] e [6].
- **E-05 a E-10:** **não existem evidências obtidas** para os procedimentos internos planejados; IDs são apenas remissões de controle futuro e não documentos existentes.

Os identificadores E-01 a E-04 apontam para fontes públicas, não para evidência de auditoria independente suficiente sobre a conta. Os itens planejados e simulados ficam explicitamente fora de qualquer conclusão factual.

## Resultados, exceções e conclusão

**Resultado do exame documental público:** CFC identifica a NBC TA 230 (R1) como vigente para o período. A DFP 4T25 V1 foi obtida e as páginas impressas 16–17, 21, 69 e 115–117 foram lidas. Elas sustentam os saldos, comparativos, PAA e opinião citados, inclusive o total de terrenos a incorporar de R\$5.678.238 mil; o saldo de R\$4.864.673 mil é o componente não circulante, e o comparativo correto de terrenos em 2024 é R\$4.587.823 mil. B3 confirma o ativo total e a identificação; CVM confirma protocolo e auditor cadastrado. Nenhum dado foi conciliado a registros internos. [3] [4] [6]

**Exceções:** não foram identificadas exceções de auditoria sobre saldos, direitos, custos, receitas ou provisões, porque nenhum teste substantivo ou de controles foi realizado e nenhuma população interna foi recebida. Ausência de exceção neste PT significa ausência de teste, não ausência de distorção. Também não foi possível reconstituir dados, amostras, julgamentos, revisões ou documentação pertencentes à PwC.

**Conclusão didática:** este PT documenta adequadamente o escopo limitado de revisão pública efetuado e separa tal revisão de procedimentos planejados e simulações, em coerência com os princípios da NBC TA 230 (R1). Com a evidência disponível, **não há base para concluir sobre existência, titularidade, avaliação, alocação, corte ou apresentação dos estoques, nem sobre reconhecimento de receita ou provisões/contingências**. Não se emite opinião de auditoria, asseguração ou conclusão sobre conformidade do arquivo da PwC. Para uma auditoria real, os procedimentos P05–P09 e P12 dependeriam de acesso autorizado, execução documentada, evidência suficiente e apropriada, supervisão/revisão e resolução de eventuais diferenças.

**Limitações e salvaguardas:** consulta a fontes públicas registradas; sem acesso a registros, controles, contratos ou pessoal da Companhia/auditor; sem entrevista, confirmação, inspeção física, teste de sistema, reexecução ou trabalho em nome da PwC. O PDF público da DFP foi obtido e as páginas citadas foram verificadas; isso não substitui evidência interna nem uma auditoria independente. A revisão formal deste PT permanece em branco. Qualquer uso profissional exige trabalho de auditoria próprio e evidência apropriada e suficiente.

## Preparação e revisão

**Preparador (matrícula didática):** EDU-AUD-001  
**Data:** 22/10/2026  
**Assinatura/identificação:** EDU-AUD-001  
**Revisor:** ____________________________________  
**Data da revisão:** __________________  
**Extensão/resultado da revisão:** __________________________________________________

## Referências

[1] Conselho Federal de Contabilidade, **NBC TA 230 (R1) — Documentação de Auditoria**, Resolução 2016/NBCTA230(R1), publicação DOU 05/09/2016, texto oficial PDF, pp. impressas 1–4 (itens 1–16) e páginas subsequentes A1–A24; norma aplicável a períodos findos em ou após 31/12/2016. https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA230%28R1%29.pdf

[2] Conselho Federal de Contabilidade, **Resoluções e Ementas — NBC TA 230 (R1)**, ficha normativa oficial, registro 2016/NBCTA230(R1), status vigente/não revogada e data de publicação 05/09/2016; consultada em 22/10/2026. https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2016/NBCTA230%28R1%29 ; ver também listagem oficial de normas NBC TA: https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/

[3] Comissão de Valores Mobiliários, **DIRECIONAL ENGENHARIA S.A. — Demonstrações Financeiras Padronizadas, 31/12/2025, V1**, documento/consulta CVM com número sequencial 155189, protocolo informado em 09/03/2026; seções de identificação do auditor, demonstrações consolidadas, balanço patrimonial ativo, notas explicativas e relatório do auditor independente. A tela pública consultada não fornece paginação fixa estável; referências neste PT são por seção, não por folha. https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1

[4] B3, **DIRECIONAL ENGENHARIA S.A. — Perfil da companhia / Dados Econômico-Financeiros**, balanço patrimonial consolidado, linha “Ativo Total”, coluna 31/12/2025, R\$ mil; página web sem paginação impressa, informação recebida conforme indicação do perfil consultado em 22/10/2026. https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br

[5] Direcional Engenharia S.A., Relações com Investidores, **Central de Resultados**, página de acesso aos resultados/DFP da companhia, consultada em 22/10/2026; página web sem paginação impressa. https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/

[6] Direcional Engenharia S.A., Relações com Investidores, **DFP 4T25 V1**, PDF integral; páginas impressas 16–17, 21, 69 e 115–117. Acesso em 22/10/2026. https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2


---

# PT-240 — Responsabilidade do auditor em relação à fraude

## Identificação do papel de trabalho

- **Código / título:** PT-240 — Responsabilidade do auditor em relação à fraude.
- **Entidade / demonstrações:** DIRECIONAL ENGENHARIA S.A. — demonstrações contábeis consolidadas.
- **Data-base / exercício:** 31/12/2025.
- **Norma e versão aplicável:** NBC TA 240 (R1), “Responsabilidade do Auditor em Relação a Fraude, no Contexto da Auditoria de Demonstrações Contábeis”, texto oficial CFC com alterações aplicáveis ao exercício de 2025; itens 10–48 e orientações A1–A69, conforme referências abaixo. A NBC TA 240 (R2), publicada em 25/09/2026, é aplicável a períodos iniciados a partir de 01/01/2027; portanto, não rege o período de 2025 tratado neste PT. [1] [2]
- **Natureza:** auditoria didática baseada somente em evidências públicas. Não é papel de auditoria real da companhia nem substitui o arquivo de auditoria do auditor independente.
- **Preparador:** matrícula didática **EDU-AUD-001**.
- **Data:** **22/10/2026**.
- **Revisão / revisor:**
- **Unidade monetária:** R\$ mil, salvo indicação em contrário.

## Objetivo, conta e processo

Documentar, para fins didáticos, a identificação e avaliação de riscos de distorção relevante decorrente de fraude nas demonstrações consolidadas de 2025, e delinear respostas de auditoria compatíveis com a NBC TA 240 (R1). O objetivo profissional subjacente é identificar e avaliar esses riscos, obter evidência suficiente e apropriada para respondê-los e tratar adequadamente fraude ou suspeita de fraude identificada (item 10).

O foco de contas e processos deste PT é: **(a)** reconhecimento de receita imobiliária, incluindo unidades em construção; **(b)** estoques imobiliários, com ênfase analítica em terrenos a incorporar; **(c)** provisões e divulgações de contingências; e **(d)** risco de burla de controles pela administração, inclusive lançamentos contábeis e estimativas. A seleção focaliza áreas sensíveis a julgamento, significativas por valor ou destacadas no relatório público do auditor; não constitui afirmação de fraude ou de deficiência de controle.

## Contexto público utilizado

A DFP da companhia para 31/12/2025 é a versão 1, protocolada na CVM em 09/03/2026. A ficha da B3 identifica a entidade como DIRECIONAL ENGENHARIA S.A., código CVM 21350 e ticker DIRR3. [3] [4]

Na DFP consolidada, o ativo total foi **R\$13.219.635 mil** em 2025 e R\$10.067.406 mil em 2024. Estoques totalizaram **R\$6.951.508 mil** e R\$5.532.090 mil, respectivamente. A Nota 5 detalha, em 2025, terrenos a incorporar de **R\$5.678.238 mil**, imóveis em construção de R\$1.174.207 mil e imóveis concluídos de R\$99.063 mil; em 2024, terrenos de R\$4.587.823 mil, em construção de R\$852.800 mil e concluídos de R\$91.467 mil. O estoque circulante foi R\$2.086.835 mil e o não circulante, R\$4.864.673 mil. Este último corresponde à parcela não circulante de terrenos; a parcela circulante de terrenos, R\$813.565 mil, é uma diferença aritmética entre o total da classe e o valor não circulante, e não uma linha individual apresentada como tal na nota. [3] [5]

Recalculos simples sobre esses valores: estoques representam 52,6% do ativo; terrenos a incorporar equivalem a 81,7% dos estoques e 43,0% do ativo consolidado. O total dos estoques aumentou 25,7% e terrenos a incorporar 23,8% sobre 2024. A receita consolidada de vendas e serviços foi R\$4.343.008 mil em 2025, ante R\$3.348.470 mil em 2024, aumento aritmético de 29,7%; o resultado antes dos tributos foi R\$1.078.495 mil e R\$792.298 mil, respectivamente. Esses indicadores descrevem escala e variação, não constituem, isoladamente, indícios de fraude ou prova de distorção. [5] [6]

O relatório de auditoria PwC apresenta opinião sem modificação, parágrafo de ênfase sobre a política de reconhecimento de receita imobiliária e principais assuntos de auditoria relacionados ao reconhecimento de receita de unidades em construção e às provisões para contingências (DFP, pp. 115–117). Isso é informação pública sobre o relatório emitido por PwC; **não** é evidência de que este preparador executou os procedimentos descritos naquele relatório nem prova de ausência de fraude. [7]

## Afirmações e riscos de fraude considerados

Os riscos abaixo são **avaliações/hipóteses de planejamento**, formuladas a partir de demonstrações publicadas. Não são constatações de fraude, erro ou falha de controle.

- **Receita imobiliária e unidades em construção.** Afirmações: ocorrência, exatidão, corte, classificação, apresentação e divulgação; mensuração do progresso/obrigações de desempenho. **Hipótese de risco:** possível reconhecimento prematuro, receita não suportada por progresso/entrega contratual, aplicação enviesada de estimativas ou reconhecimento em período incorreto. A receita cresceu 29,7% e PwC destacou esse tema como PAA e incluiu ênfase sobre a política de reconhecimento. São fatores para direcionar testes, não evidência de manipulação. A presunção de risco de fraude no reconhecimento de receita deve ser tratada segundo o item 26; eventual conclusão para afastá-la exige justificativa documentada (item 48). **Avaliação didática:** risco presumido a avaliar; possibilidade de risco significativo, pendente de avaliação com dados e entendimento interno. [1] [5] [6] [7]
- **Estoques imobiliários — terrenos a incorporar e empreendimentos.** Afirmações: existência, direitos e obrigações, integridade, classificação, mensuração/avaliação e divulgação. **Hipótese de risco:** possível superavaliação por existência/direitos não comprovados, custos capitalizados indevidamente, premissas de valor realizável líquido enviesadas ou classificação/transferência entre circulante e não circulante para influenciar indicadores. Terrenos somam 81,7% do estoque e 43,0% do ativo. A concentração de valor e os julgamentos de desenvolvimento justificam prioridade de auditoria, mas não demonstram irregularidade. **Avaliação didática:** área focal de risco; avaliar significância e desenho dos testes após obter registros, contratos e critérios internos. [5]
- **Provisões e contingências.** Afirmações: integridade, mensuração, classificação, apresentação e divulgação. **Hipótese de risco:** possível omissão de casos, classificação ou mensuração enviesada da probabilidade/valor, ou divulgação incompleta. O tema foi PAA no relatório PwC; isso denota julgamento relevante para a auditoria pública, não ocorrência de fraude. **Avaliação didática:** risco de estimativa e completude a avaliar; nenhuma exceção conhecida neste PT. [7]
- **Lançamentos, estimativas e controles da administração.** Afirmações: ocorrência, exatidão, corte, classificação e apresentação em múltiplas contas. **Hipótese de risco:** a administração pode, em tese, sobrepor controles por lançamentos manuais, ajustes de fechamento, alteração de premissas, omissão/antecipação de eventos ou operações não usuais. Trata-se de risco inerente a auditorias nos termos dos itens 31–33 e A4–A6; não há dados públicos examinados neste PT sobre lançamentos específicos, incentivos ou controles que permitam afirmar que isso ocorreu. **Avaliação didática:** resposta obrigatória de auditoria a planejar; existência de lançamentos suspeitos não constatada. [1]

**Risco de nível das demonstrações contábeis:** ceticismo profissional e imprevisibilidade dos procedimentos devem ser mantidos durante o trabalho (itens 12–15 e 29). Os dados públicos disponíveis não permitem concluir sobre ambiente de controle, pressões da administração, canais de denúncia, acesso privilegiado, integridade dos sistemas, incentivos ou qualidade dos controles. Qualquer fator desse tipo permanece hipótese até ser corroborado.

## População, fontes e critérios

**População examinada com evidência pública:** documentos publicados da DFP 2025 V1 e informações de identificação da companhia. Para os procedimentos públicos abaixo, a população limita-se às demonstrações, notas e relatório do auditor constantes da DFP; não equivale à população de lançamentos, contratos, terrenos, processos judiciais ou unidades imobiliárias contabilizados.

**Fontes efetivamente consultadas:**

- DFP 4T25 V1 da Direcional no RI, PDF integral com 125 páginas físicas e paginação impressa até 123. As páginas usadas são identificadas por assunto abaixo. O registro da mesma DFP consta da CVM (NSD 155189). [3] [5]
- Ficha da companhia listada na B3 para identificação societária e ticker, sem paginação. [4]
- Texto normativo oficial NBC TA 240 (R1) disponibilizado pelo CFC; lista oficial de normas CFC e publicação da NBC TA 240 (R2) no DOU apenas para verificar a versão e a vigência. [1] [2]

**Critérios profissionais:** NBC TA 240 (R1), especialmente itens 10–15 (objetivo, ceticismo e discussão); 16–24 (avaliação de riscos e indagações); 25–28 (identificação, reconhecimento de receita e riscos avaliados); 29–33 (respostas e burla de controles); 34–39 (avaliação da evidência, continuidade e representações); 40–44 (comunicações); e 45–48 (documentação). Referências adicionais de aplicação: A1–A69 e apêndices 1–3. A NBC TA 315 e a NBC TA 330 são relacionadas pela própria NBC TA 240; não se pretende aqui substituí-las nem documentar seu cumprimento integral. [1]

**Critério para classificar o trabalho didático:**

- **Realizado com evidência pública:** leitura/inspeção documental de publicação pública acessível e recálculos aritméticos reproduzíveis com dados publicados. Não significa que procedimentos de auditoria completos foram realizados ou que os saldos foram confirmados.
- **Planejado por falta de acesso:** resposta de auditoria que exige documentos, registros, sistemas, interlocutores, especialistas ou terceiros não disponíveis neste dossiê.
- **Simulado para fins didáticos:** exemplo de desenho de procedimento ou seleção fictícia sem execução em registro ou item real da companhia. Não há dados sintéticos apresentados como população real neste PT.

## Procedimentos, evidências e referências cruzadas

- **P1 — Inspeção de DFP e identificação de entidade/auditor. Classificação: realizado com evidência pública.** Inspecionar a DFP pública para identificar período, versão, envio/protocolo, entidade, auditor independente e conteúdo consolidado. Evidência: DFP 2025 V1; registro CVM NSD 155189; BP consolidado e identificação no relatório; B3 ficha DIRR3. Identificados exercício encerrado em 31/12/2025, versão 1, envio em 09/03/2026 e auditor PwC. Não se validou a autenticidade de registros subjacentes nem se examinou arquivo de auditoria. [3] [4] [5]
- **P2 — Analíticos de estoques e terrenos. Classificação: realizado com evidência pública.** Inspecionar BP consolidado e Nota 5; recalcular percentuais de estoque/terrenos sobre ativos e estoque, e variações anuais para localizar classes de maior exposição. Evidência: BP, DFP pp. 16–17; Nota 5, p. 69; cálculos reproduzíveis em “Contexto público”. Terrenos representam 81,7% dos estoques e 43,0% do ativo. O analítico não inclui teste de suporte, existência, propriedade, custo ou valor realizável. [5]
- **P3 — Analítico de receita. Classificação: realizado com evidência pública.** Inspecionar a DRE consolidada e comparar receita de 2025 com 2024, relacionando a variação ao risco presumido de reconhecimento de receita e ao PAA divulgado. Evidência: DRE consolidada, p. 21; relatório PwC, pp. 115–117; política contábil, p. 44. Crescimento aritmético de receita de 29,7%; tema consta como PAA e há ênfase em política de reconhecimento. A comparação não prova reconhecimento impróprio nem confirma premissas de progresso ou cut-off. [6] [7]
- **P4 — Leitura do relatório independente. Classificação: realizado com evidência pública.** Ler o relatório para identificar opinião, ênfase e PAA relevantes ao foco deste PT. Evidência: relatório do Auditor Independente, DFP pp. 115–117. Resultado: opinião sem modificação, ênfase em política de reconhecimento imobiliário e PAA de receita e contingências. Isso descreve o relatório de PwC, não procedimentos executados neste PT. [7]
- **P5 — Indagações sobre fraude e discussão da equipe. Classificação: planejado por falta de acesso.** Indagar administração e responsáveis pela governança sobre avaliação de risco de fraude, processo de identificação/resposta, suspeitas ou denúncias; discutir suscetibilidade com equipe. Referência: itens 15 e 17–21. Nenhuma entrevista ou reunião foi realizada. Não há resposta da administração ou governança disponível; portanto, não se avaliou consistência de respostas ou existência de suspeitas internas. [1]
- **P6 — Testes de lançamentos e ajustes manuais. Classificação: planejado por falta de acesso.** Obter razão geral/auxiliares e testar lançamentos de fim de período e ajustes manuais, inclusive filtros por usuários, contas incomuns, horários, descrições e lançamentos sem suporte. Referência: resposta à burla de controles, itens 31–33 e orientações A41–A48. Razão, trilhas de aprovação, logs e documentos não foram acessados; nenhum lançamento foi selecionado ou testado. [1]
- **P7 — Testes de receita e cut-off. Classificação: planejado por falta de acesso.** Testar amostra de contratos e vendas contra obrigações de desempenho, medições de progresso, documentação de obra, aditivos, distratos, recebimentos e registros contábeis, incluindo corte antes/depois de 31/12/2025. Sem contratos, base de unidades, medições ou documentos de suporte, nenhuma confirmação de receita, ocorrência, mensuração ou corte foi executada. Referência: NBC TA 240 itens 26–28 e DFP pp. 21, 44 e 115–117. [1] [6] [7]
- **P8 — Testes de existência, direitos e mensuração de terrenos. Classificação: planejado por falta de acesso.** Inspecionar/confirmar por amostra terrenos e direitos: matrículas, escrituras, contratos/opções, aprovações, pagamentos, empreendimento associado, orçamento/custos e classificação circulante/não circulante; recalcular valor realizável líquido com premissas suportadas. Não houve inspeção física, consulta a cartório, confirmação com vendedor, análise de contrato ou validação de título. Existência, direitos, mensuração e classificação permanecem não testadas. Referência: Nota 5, p. 69; BP pp. 16–17. [1] [5]
- **P9 — Completude e mensuração de contingências. Classificação: planejado por falta de acesso.** Obter listagem completa de processos e cartas de advogados; comparar com atas, notificações, pagamentos e contabilização/divulgação de contingências; testar premissas das provisões. Não foram obtidas cartas de advogados, listagens internas ou confirmações externas. Não se confirmou completude ou suficiência de provisões. Referência: PAA sobre contingências, DFP pp. 115–117; NBC TA 240 itens 16–24 e 34–37. [1] [7]
- **P10 — Imprevisibilidade na seleção. Classificação: simulado para fins didáticos; não executado.** Como exemplo, selecionar empreendimento ou lançamento contábil fora da amostra dirigida mediante critério aleatório documentado e rastreável. Trata-se apenas de desenho pedagógico: não foi gerada amostra de dados reais e nenhum item da Direcional foi selecionado ou examinado. Referência: item 29(c) e orientação A37; inexiste população interna disponível. [1]
- **P11 — Avaliação de distorções, representações e comunicações. Classificação: planejado por falta de acesso.** Avaliar distorções identificadas, obter representações formais sobre fraude e avaliar comunicações necessárias à administração, governança ou autoridades, se aplicável. Não houve achados de auditoria interna, solicitação de carta de representação ou comunicação à administração, governança ou autoridade. Não se conclui que comunicação seria dispensável em auditoria real. Referência: NBC TA 240 itens 34–44. [1]

## Resultados, exceções e conclusão

**Resultados dos procedimentos públicos:** foram lidos os documentos públicos especificados e recalculadas as métricas analíticas descritas. A concentração de terrenos a incorporar, o aumento dos saldos de estoques e receita, e a inclusão de receita e contingências entre os temas destacados pelo auditor independente justificam atenção prioritária no planejamento didático. Os dados não demonstram fraude, intencionalidade, viés de estimativa ou inadequação contábil.

**Exceções:** nenhum desvio de auditoria foi identificado porque não houve teste substantivo ou de controle sobre documentos contábeis subjacentes. A opinião sem modificação de PwC não pode ser reapresentada como conclusão própria deste PT. Tampouco se conclui sobre ausência de fraude: os procedimentos públicos têm alcance insuficiente para essa conclusão.

**Conclusão didática:** com base exclusivamente na DFP e em fontes públicas descritas, os riscos de fraude relacionados a reconhecimento de receita imobiliária e burla de controles requerem respostas específicas; estoques, especialmente terrenos, e estimativas de contingências merecem procedimentos substantivos dirigidos por risco. O trabalho aqui documentado limita-se à inspeção de informação pública e recálculos; riscos residuais não foram reduzidos por testes de auditoria. **Não é possível emitir conclusão de asseguração sobre as demonstrações de 2025 nem concluir que estejam livres de distorção relevante decorrente de fraude.**

## Limitações

Este PT não teve acesso a balancetes, razão geral, auxiliares, população de operações, contratos, matrículas, medições de obra, orçamentos por projeto, premissas internas, correspondência jurídica, atas, canal de denúncias, controles, sistemas, trilhas de auditoria, confirmações externas ou papéis de trabalho de PwC. Não foram realizados contatos ou entrevistas, confirmações, inspeções físicas, observação de controles, consultas a registros externos, testes de amostragem, procedimento analítico sobre dados internos ou revisão dos papéis de trabalho do auditor. As classificações “planejado” e “simulado” acima não podem ser interpretadas como execução.

## Referências

[1] Conselho Federal de Contabilidade (CFC), **NBC TA 240 (R1) — Responsabilidade do Auditor em Relação a Fraude, no Contexto da Auditoria de Demonstrações Contábeis**, texto oficial consolidado disponibilizado pelo CFC; R1 publicada no DOU em 05/09/2016, com revisões posteriores incorporadas ao texto vigente em 2025. Localizadores no PDF oficial (41 páginas físicas): requisitos itens 10–48, pp. 4–11; itens 26 e 29–33, pp. 6–7; itens 45–48, pp. 10–11; orientação A4, p. 13; A37, p. 21; A41, p. 22; demais orientações A1–A69 e apêndices 1–3. URL: https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA240%28R1%29.pdf

[2] CFC, **NBC TA – de Auditoria Independente de Informação Contábil Histórica**, página oficial de normas, consulta em 22/10/2026, registro da NBC TA 240 (R2), DOU 25/09/2026; Imprensa Nacional, **Norma Brasileira de Contabilidade TA nº 240 (R2), de 17 de setembro de 2026**, DOU 25/09/2026, edição 182, seção 1, p. 153, vigência para períodos iniciados em ou após 01/01/2027. URLs: https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/ ; https://www.in.gov.br/web/dou/-/norma-brasileira-de-contabilidade-ta-n-240-r2-de-17-de-setembro-de-2026-734493789

[3] Comissão de Valores Mobiliários (CVM), **DFP — DIRECIONAL ENGENHARIA S.A., exercício 31/12/2025, Versão 1**, protocolo de 09/03/2026, NSD 155189, consulta em 22/10/2026; formulário oficial de demonstrações financeiras. URL: https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1

[4] B3, **DIRECIONAL ENGENHARIA S.A. — ficha da companhia listada**, ticker DIRR3, código CVM 21350, consulta em 22/10/2026, sem paginação. URL: https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br

[5] RI Direcional, **DFP 4T25 V1 — Demonstrações Financeiras Padronizadas de 31/12/2025**, PDF integral, 125 páginas físicas; páginas impressas 16–17 (BP consolidado) e 69 (Nota 5 — estoques), consulta em 22/10/2026. URL: https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2 ; página de acesso: https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/

[6] RI Direcional, **DFP 4T25 V1 — Demonstrações Financeiras Padronizadas de 31/12/2025**, DRE consolidada, p. 21, políticas contábeis, p. 44, consulta em 22/10/2026. URLs: https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2 ; https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/

[7] RI Direcional, **DFP 4T25 V1 — Relatório do Auditor Independente (PwC)**, relatório impresso pp. 115–117, incluindo opinião, ênfase e principais assuntos de auditoria, consulta em 22/10/2026. URL: https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2


---

# PT-250 — Consideração de leis e regulamentos

**Entidade:** DIRECIONAL ENGENHARIA S.A. e entidades consolidadas  
**Exercício:** encerrado em 31/12/2025  
**Natureza:** papel de trabalho didático, baseado em evidência pública  
**Data de acesso e preparação:** 22/10/2026  
**Preparador:** matrícula didática EDU-AUD-001  
**Revisão:** ____________________________________

## Identificação, norma e itens

**Código/título:** PT-250 — Consideração de leis e regulamentos.  
**Norma:** NBC TA 250, *Consideração de Leis e Regulamentos na Auditoria de Demonstrações Contábeis*. Para o exercício de 2025, a base normativa é a redação aprovada em 7/2/2019, aplicável a períodos iniciados em ou após 31/12/2018, considerada com a alteração indicada pelo CFC como Revisão NBC 15, publicada em 2/12/2022. O cadastro oficial do CFC identifica a norma de 2019 como vigente, alterada e não revogada. A referência usada é o texto oficial CFC, PDF da NBC TA 250, especialmente itens 1–12 e 13–30, pp. 2–6 do arquivo; requisitos relevantes neste PT: itens 3–9, 10–11, 13–18, 19–22, 23–29 e 30. [1] [2] [3]

**Referência de paginação normativa:** páginas referem-se ao PDF oficial da NBC TA 250 disponibilizado pelo CFC, não à paginação de outra compilação. A Revisão NBC 15 é identificada pelo registro oficial do CFC como alteração da NBC TA 250; este PT não atribui à revisão alteração específica de requisito sem conferir um texto consolidado comparativo. [2] [3]

## Objetivo, conta e processo

**Objetivo.** Documentar, para fins didáticos, como uma auditoria das demonstrações consolidadas de 2025 poderia considerar a possibilidade de distorções relevantes decorrentes de não conformidade com leis e regulamentos, conforme a NBC TA 250. A norma distingue regras com efeito direto sobre valores ou divulgações contábeis e outras cuja conformidade pode ser essencial à operação, à continuidade ou à prevenção de penalidades relevantes. O papel de trabalho não é uma certificação autônoma de conformidade legal. [1, itens 2–8 e 11]

**Contas e processos focalizados.** O recorte considera: (a) estoques imobiliários, com foco de planejamento em terrenos a incorporar; (b) reconhecimento de receita imobiliária; e (c) provisões e divulgações relacionadas a contingências. A DFP indicada para este trabalho contém esses dois últimos temas entre os Principais Assuntos de Auditoria (PAA), conforme os fatos-base fornecidos para o exercício. Estoques e terrenos são selecionados por materialidade relativa observável nos valores-base, não porque haja indício de irregularidade. A atividade principal informada pela B3 abrange incorporação, construção e comercialização de imóveis próprios ou de terceiros e serviços de engenharia. [4] [5]

**Responsabilidade e limite do auditor.** A administração, sob supervisão da governança, responde pela conformidade. A auditoria busca segurança razoável sobre demonstrações sem distorção relevante e não prevenção ou detecção de toda infração. A NBC TA 250 não transforma a auditoria de demonstrações em investigação geral de todos os atos da entidade. [1, itens 3–9]

## Afirmações e riscos considerados

| Área | Afirmações contábeis relacionadas | Risco para planejamento — hipótese, não constatação |
|---|---|---|
| Terrenos a incorporar e demais estoques imobiliários | Existência, direitos e obrigações, integridade, avaliação/alocação e apresentação | Se existissem falhas em direitos sobre terrenos, aprovações ou obrigações legais vinculadas a empreendimentos, seus efeitos poderiam afetar reconhecimento, custo, recuperabilidade, provisões ou divulgação. A existência de tais falhas não foi estabelecida. |
| Receita imobiliária | Ocorrência, competência/corte, exatidão, classificação e divulgação | O PAA informado sobre reconhecimento de receita sinaliza julgamento e complexidade de auditoria, não descumprimento legal. Como hipótese, requisitos legais ou regulatórios que afetassem contratos, tributos ou divulgação poderiam refletir-se em valores ou notas. Não foi identificada violação. |
| Provisões para contingências | Integridade, avaliação, classificação, apresentação e divulgação | O PAA informado sobre contingências justifica atenção a completude e mensuração. Como hipótese, processos, sanções ou obrigações regulatórias não capturados poderiam gerar passivos ou divulgações incompletos. Não há evidência pública revisada neste PT que demonstre omissão. |
| Conformidade transversal do grupo | Apresentação e divulgação; efeitos sobre ativos, passivos, resultado e continuidade | A estrutura societária consolidada e a atuação imobiliária/construtiva podem envolver obrigações fiscais, societárias, ambientais, urbanísticas, trabalhistas, consumeristas e de mercado de capitais, conforme aplicável a cada componente. Sem cadastro legal, mapa de entidades, comunicações ou assessoria interna, essa lista é hipótese de escopo e não afirma que cada regra se aplique nem que tenha ocorrido descumprimento. |

A DFP-base informa ativo consolidado de R\$ 13.219.635 mil; estoques de R\$ 6.951.508 mil, incluindo terrenos a incorporar total de R\$ 5.678.238 mil, dos quais R\$ 4.864.673 mil são não circulantes, e estoques circulantes de R\$ 2.086.835 mil; os comparativos são ativo de R\$ 10.067.406 mil e terrenos a incorporar total de R\$ 4.587.823 mil em 2024, dos quais R\$ 3.888.979 mil são não circulantes. Considerados apenas como valores-base públicos indicados para o exercício, os estoques equivalem a cerca de 52,6% do ativo; terrenos a incorporar totais, a 81,7% dos estoques e 43,0% do ativo; o saldo total de terrenos é aproximadamente 23,8% maior que o comparativo. São relações aritméticas para direcionar atenção; não constituem limiar de materialidade, evidência de distorção nem teste de conformidade. A B3 também exibe ativo consolidado de R\$ 13.219.635 mil em 31/12/2025. [4] [5]

## População, fontes e critérios

**População pretendida para uma auditoria completa.** A população relevante seria o universo de entidades e empreendimentos incluídos na consolidação, as regras aplicáveis a cada um, as transações e saldos afetados, e os registros de ocorrências, processos, autos, licenças, notificações e correspondência com autoridades. O dossiê público consultado não contém um inventário completo de leis aplicáveis, a relação de componentes/empreendimentos, o cadastro de processos ou o universo de correspondências regulatórias. Portanto, esses dados não foram presumidos nem tratados como população efetivamente obtida. A amostra para testes substantivos e de conformidade permanece a definir após obtenção de tais bases.

**Fontes efetivamente consultadas.** Texto e cadastro normativo oficiais CFC; registro público CVM da DFP identificada pelo número sequencial 155189; página de dados da companhia na B3; e Central de Resultados do RI da companhia. A DFP pública de 31/12/2025, versão 1, indicada como protocolada/enviada em 09/03/2026, com PwC como auditor, foi obtida integralmente por canal oficial e teve as páginas relevantes examinadas; são também fatos do trabalho os PAA de reconhecimento da receita imobiliária e provisões para contingências e a opinião sem ressalva. A interface CVM e o extrator textual do RI são dinâmicos e não oferecem paginação estável no corpo, mas isso não impede o acesso ao PDF público. Permanecem sem acesso a evidência subjacente, registros internos e arquivo privado de auditoria. [4] [5] [6]

**Critérios de auditoria.** Aplicam-se as responsabilidades e procedimentos da NBC TA 250: entendimento da estrutura legal/regulatória pertinente; evidência apropriada e suficiente sobre regras com efeito direto; procedimentos para ajudar a identificar não conformidades que possam ter efeito relevante quanto às demais regras; ceticismo e atenção durante o trabalho; indagações e inspeção de correspondência quando exigidas; representações formais; resposta a não conformidade identificada ou suspeita; comunicação; consideração de assessoria jurídica, relatório e documentação conforme as circunstâncias. [1, itens 13–30]

Não foram fornecidos materialidade global/de execução, materialidade específica, tolerância para diferenças, matriz de risco aprovada, estratégia de amostragem ou avaliação dos controles do grupo. Nenhum limiar foi inventado. A lei/regulamento específico e o critério de conformidade a testar precisam ser definidos para cada componente e processo, com suporte da administração e, conforme adequado, assessoria jurídica.

## Procedimentos realizados com evidência pública

| Ref. | Procedimento e classificação | Evidência pública/resultado |
|---|---|---|
| P250-01 | **Realizado com evidência pública:** leitura do texto oficial CFC da NBC TA 250 e verificação do cadastro oficial quanto à data, vigência, alteração e revogação. | Texto datado de 7/2/2019, vigência para períodos iniciados em/ após 31/12/2018; registro CFC: vigente, alterada e não revogada; alteração indicada pela Revisão NBC 15. Não é teste de conformidade da companhia. [1] [2] [3] |
| P250-02 | **Realizado com evidência pública:** consulta ao registro CVM indicado para identificar o documento anual e o auditor. | O registro CVM refere-se à DFP da Direcional e informa PricewaterhouseCoopers Auditores Independentes Ltda. A DFP pública integral foi obtida separadamente e as páginas relevantes examinadas; não houve acesso a papéis de auditoria, arquivos internos ou conciliação de saldos. A tela CVM não possui paginação impressa estável. [4] |
| P250-03 | **Realizado com evidência pública:** consulta ao perfil oficial B3 para identificar emissor, atividade e dado consolidado comparável. | A B3 identifica DIRECIONAL ENGENHARIA S.A., código CVM 21350 e atividade principal imobiliária/construtiva; exibe ativo consolidado de R\$ 13.219.635 mil em 31/12/2025. A B3 não comprova conformidade legal nem substitui a DFP. [5] |
| P250-04 | **Realizado com evidência pública indicada e recálculo aritmético:** comparação simples dos saldos-base de estoques/terrenos e ativo. | Os percentuais e variação descritos na seção de riscos foram recalculados usando os valores publicados na DFP pública integral, cujas páginas relevantes foram examinadas. Não houve conciliação independente ao razão ou às demonstrações internas. A informação é suficiente apenas para orientar risco didático, não para formar conclusão sobre saldo. [4] |
| P250-05 | **Realizado com evidência pública:** consulta à Central de Resultados do RI como fonte de divulgação da companhia. | A página lista anos e categorias de relatórios, mas o extrator textual não expõe o arquivo no corpo; o PDF anual da DFP 2025 foi obtido diretamente pelo link oficial e as páginas relevantes foram examinadas. Não se infere indisponibilidade do documento nem se usa a tela dinâmica como evidência de valor. [6] |

Nenhum dos procedimentos acima correspondeu a confirmação externa de conformidade, entrevista, inspeção física, leitura de correspondência privada, inspeção de documentos internos, consulta a advogado da companhia ou reexecução de testes do auditor independente.

## Procedimentos planejados por falta de acesso

Os procedimentos seguintes são **planejados**, não executados. Devem ser adaptados à avaliação de riscos, materialidade, estrutura do grupo e aos requisitos aplicáveis antes de se tirar conclusão de auditoria. “Inspeção de correspondência” abaixo significa procedimento de auditoria futuro sobre evidência a ser disponibilizada, não inspeção já realizada neste PT.

| Ref. | Status | Procedimento proposto / objetivo |
|---|---|---|
| P250-P01 | **Planejado — falta de acesso** | Obter organograma do grupo e lista de entidades, SPEs e empreendimentos consolidados; mapear, com responsáveis competentes, leis e regulamentos relevantes por natureza de operação e jurisdição; documentar por que cada regra pode afetar valores/divulgações ou a operação. |
| P250-P02 | **Planejado — falta de acesso** | Indagar administração e, quando apropriado, governança sobre políticas e processos de conformidade, mudanças em leis, notificações, autos, sanções, investigações, litígios e suspeitas de não conformidade no exercício; avaliar consistência das respostas com outras evidências. A indagação ainda não ocorreu. |
| P250-P03 | **Planejado — falta de acesso** | Para regras com efeito direto nos números e divulgações, definir requisitos concretos e obter evidência apropriada e suficiente sobre sua aplicação aos saldos e transações (por exemplo, recálculos, inspeção documental, rastreamento a registros e teste de corte), com foco nos efeitos em tributos, contratos, custos e provisões conforme o mapa legal suportado. Não há teste ou amostra selecionada neste PT. |
| P250-P04 | **Planejado — falta de acesso** | Para regras sem efeito contábil direto, executar indagações sobre conformidade e inspecionar correspondência disponível com autoridades de licenciamento/regulação, conforme item 15 da NBC TA 250; avaliar se qualquer ocorrência pode causar distorção relevante. A correspondência não foi solicitada nem vista neste trabalho. |
| P250-P05 | **Planejado — falta de acesso** | Estoques/terrenos: obter listagem por empreendimento, conciliar ao razão e às notas, e, conforme riscos identificados, examinar documentação de direitos, aquisição, licenças/aprovações pertinentes, custos capitalizados e indicadores de recuperabilidade; cruzar questões legais com os processos e provisões correspondentes. Não houve inspeção física ou documental neste PT. |
| P250-P06 | **Planejado — falta de acesso** | Receita imobiliária: obter processo contábil e amostra determinada pela equipe; examinar documentos e marcos contratuais relevantes para reconhecimento/corte e requisitos legais/regulatórios que tenham efeito contábil; avaliar se o tratamento e as divulgações são consistentes. O PAA divulgado não substitui esse procedimento. |
| P250-P07 | **Planejado — falta de acesso** | Contingências: obter relação completa de casos e reconciliação com registros contábeis; comparar com respostas de assessores jurídicos externos e documentos disponíveis, examinar eventos subsequentes e avaliar estimativas, classificação e divulgação segundo os critérios contábeis aplicáveis. Nenhuma confirmação jurídica foi solicitada ou recebida neste PT. |
| P250-P08 | **Planejado — falta de acesso** | Solicitar representação formal da administração e, quando apropriado, governança de que todos os casos conhecidos ou suspeitos cujos efeitos devam ser considerados foram divulgados ao auditor; confrontar a representação com demais evidências. Nenhuma representação foi solicitada ou recebida. |
| P250-P09 | **Planejado — falta de acesso** | Para qualquer ocorrência identificada ou suspeita, obter entendimento de natureza e circunstâncias, coletar informação adicional, discutir com nível apropriado da administração/governança (salvo proibição), avaliar materialidade e outras implicações da auditoria, considerar assessoria jurídica e cumprir comunicações legais e normativas. Nenhum caso foi identificado neste papel como ocorrência real. |

## Procedimento simulado para fins didáticos

| Ref. | Status | Exercício e limite |
|---|---|---|
| P250-S01 | **Simulado para fins didáticos — não executado** | Supor, exclusivamente como cenário de treinamento, que uma futura inspeção de documentos disponibilizados revelasse dúvida sobre a validade de autorização de determinado empreendimento. A equipe deveria obter a norma e o documento pertinente, apurar natureza e circunstâncias, identificar possíveis efeitos sobre direito ao terreno, custo, provisão, divulgação ou continuidade, escalar a discussão ao nível apropriado, consultar assessoria jurídica quando necessário e documentar conclusões. Este cenário é hipotético; não se refere a empreendimento, documento, infração ou exceção identificados na Direcional. Não há montante estimado nem saldo atribuído ao cenário. |

## Evidências e referências cruzadas

| Referência | Fonte / documento | Uso e localização |
|---|---|---|
| E-01 | CFC, *Norma Brasileira de Contabilidade NBC TA 250*, de 7/2/2019, PDF oficial. | Itens 1–30 e A1–A36; requisitos nos itens 13–30, especialmente pp. 4–6 do PDF. Base normativa deste PT. [1] |
| E-02 | CFC, cadastro da resolução 2019/NBCTA250 e registro da Revisão NBC 15. | Data de publicação, situação vigente/alterada/não revogada e vínculo da Revisão NBC 15 publicada em 2/12/2022. [2] [3] |
| E-03 | CVM, DFP de DIRECIONAL ENGENHARIA S.A., exercício 2025, documento sequencial 155189, indicada como versão 1, enviada em 09/03/2026; DFs consolidadas, relatório do auditor e notas explicativas. | A DFP pública integral foi obtida por canal oficial e as páginas relevantes foram examinadas. A interface CVM não expõe numeração impressa estável; por isso, páginas do PDF são usadas apenas quando verificadas e não se atribui paginação à tela. Referência cruzada: P250-02 e P250-04. [4] |
| E-04 | B3, página de DIRECIONAL ENGENHARIA S.A., código CVM 21350. | Dados da companhia, atividade principal e balanço consolidado, coluna de 31/12/2025. Apoia a identificação do emissor e a conferência pública do ativo total, não os detalhes de estoques/terrenos. Referência cruzada: P250-03. [5] |
| E-05 | RI Direcional, Central de Resultados. | Página oficial consultada para localizar DFP e documentos financeiros anuais; o extrator textual não expôs o arquivo no corpo, mas o PDF anual de 2025 foi obtido pelo link direto oficial e examinado nas páginas relevantes. Referência cruzada: P250-05. [6] |

**Nota de paginação das demonstrações:** a DFP pública integral foi obtida e as páginas relevantes foram lidas. A interface CVM e o acesso estático do RI são eletrônicos/dinâmicos e não fornecem paginação impressa estável no corpo; por isso, referências CVM identificam documento e seção, enquanto as páginas do PDF são indicadas somente quando confirmadas. A ausência de paginação na tela não significa indisponibilidade do PDF.

## Resultados, exceções, conclusão e limitações

**Resultado dos procedimentos realizados.** Os procedimentos de gabinete confirmaram a versão normativa vigente identificada no cadastro CFC, localizaram o registro CVM e o auditor PwC, e corroboraram na B3 a identidade/atividade da companhia e o ativo consolidado de 31/12/2025. A DFP pública integral foi obtida diretamente por canal oficial e as páginas relevantes foram examinadas; o extrator textual do RI não expõe o link no corpo, sem que isso indique indisponibilidade do arquivo. A comparação aritmética dos valores públicos posiciona estoques e terrenos entre as exposições de planejamento relevantes. O fato de a DFP indicar PAA de receita imobiliária e contingências e opinião sem ressalva é informação sobre o relatório publicado, não evidência de que este papel realizou os testes que sustentaram a opinião. [1]–[6]

**Exceções.** Não foram identificadas exceções de conformidade nos procedimentos executados, pois estes se limitaram à consulta de fontes públicas e recálculos. Isso **não** significa que se tenha testado ou confirmado conformidade, nem que não existam não conformidades. Não foi constatada irregularidade, notificação omitida, falha de licença, deficiência de controle ou erro contábil. Riscos descritos são hipóteses para planejamento, não fatos atribuídos à companhia.

**Conclusão didática.** Com evidência pública limitada, este PT permite apenas registrar fontes disponíveis e direcionar procedimentos adicionais, com atenção a estoques/terrenos e aos PAA de receita e contingências. Não há base para uma conclusão de auditoria sobre conformidade legal/regulatória, suficiência de provisões, reconhecimento de receita, existência/direitos/avaliação de estoques, nem sobre as demonstrações consolidadas como um todo. Uma conclusão exigiria executar os procedimentos planejados e avaliar evidência apropriada e suficiente conforme a NBC TA 250 e demais NBC TAs pertinentes.

**Limitações expressas.** Não houve acesso a razão contábil, contratos, licenças, processos, cadastro legal, controles, correspondências, assessores jurídicos, entidades componentes, administração ou governança. Não foram realizadas confirmação, entrevista/indagação, inspeção física, inspeção de documentos internos, circularização jurídica, teste de amostra, observação, reexecução do trabalho da PwC ou procedimentos de auditoria no local. A interface CVM não oferece paginação impressa estável; as páginas relevantes do PDF público foram examinadas. Os valores detalhados da DFP e os PAA foram conferidos na cópia pública, mas não conciliados independentemente à documentação interna. O trabalho é didático e não é um relatório de asseguração.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC. NBC TA 250, Consideração de Leis e Regulamentos na Auditoria de Demonstrações Contábeis, 7 de fevereiro de 2019, PDF oficial; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA250.pdf>).
- **Ref. 2** — CFC. Resolução 2019/NBCTA250, cadastro oficial e situação da norma; [abrir fonte](<https://www1.cfc.org.br/sisweb/sre/detalhes_sre.aspx?codigo=2019/NBCTA250>).
- **Ref. 3** — CFC. Revisão NBC 15, publicada em 2 de dezembro de 2022, cadastro oficial; [abrir fonte](<https://www1.cfc.org.br/sisweb/sre/detalhes_sre.aspx?codigo=2022/%20REVIS%C3%83O%20NBC15>).
- **Ref. 4** — CVM. DIRECIONAL ENGENHARIA S.A., DFP do exercício encerrado em 31 de dezembro de 2025, documento sequencial 155189; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 5** — B3. DIRECIONAL ENGENHARIA S.A., dados da companhia e financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 6** — RI Direcional. Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-260 — Comunicação com os responsáveis pela governança

## Identificação do papel de trabalho

| Campo | Informação |
|---|---|
| Código / título | **PT-260 — Comunicação com os responsáveis pela governança** |
| Entidade / demonstrações | DIRECIONAL ENGENHARIA S.A. — demonstrações contábeis consolidadas |
| Exercício | Encerrado em 31/12/2025 |
| Norma / versão | **NBC TA 260 (R2)** — texto oficial do CFC, originado em 17/06/2016 e aplicável a auditorias de demonstrações contábeis para períodos encerrados em ou após 31/12/2016. No texto oficial consolidado consultado, a Revisão NBC 27 está identificada, inclusive a inclusão do item 16A. Referências principais: itens 1–3, 8–10, 11–23; aplicação A1–A8, A11–A16, A17–A32, A37–A54; Apêndice 2. PDF oficial do CFC, pp. 1–25; requisitos de comunicação, pp. 5–6. [1] [2] |
| Preparador | Matrícula didática **EDU-AUD-001** |
| Data de preparação / acesso | **22/10/2026** |
| Revisor | ______________________________ (em branco) |
| Natureza | Papel de trabalho **didático**, limitado a fontes públicas; não representa auditoria executada nem arquivo de auditoria da PwC ou da companhia. |

## Objetivo, conta e processo

**Objetivo.** Estruturar, para fins didáticos, as comunicações que um auditor independente teria de estabelecer, realizar tempestivamente e documentar com os responsáveis pela governança, observadas as responsabilidades do auditor, o alcance e a época planejados, constatações significativas e demais comunicações previstas na NBC TA 260 (R2), itens 9 e 14–23. Este PT avalia apenas o que é observável em documentos públicos e propõe assuntos para comunicação futura; não atesta que tenham ocorrido comunicações entre PwC, administração e governança.

**Conta/processo em foco.** Processo de elaboração e supervisão das demonstrações financeiras consolidadas de 31/12/2025. Para contextualizar riscos potencialmente relevantes à governança, o papel considera estoques — especialmente terrenos a incorporar —, reconhecimento de receita imobiliária e provisões para contingências. O PT-260 trata da comunicação com governança, não constitui teste substantivo dessas contas.

## Afirmações e riscos para discussão

Os tópicos abaixo são **riscos/hipóteses para planejamento e comunicação**, não constatações de distorção, deficiência ou falha de controle. A indicação pública de um principal assunto de auditoria (PAA) no relatório da PwC informa que o assunto recebeu atenção de auditoria, mas, por si só, não comprova distorção nem deficiência.

| Área | Afirmações e risco hipotético a considerar | Base pública / qualificação |
|---|---|---|
| Estoques, em especial terrenos a incorporar | **Existência, direitos e obrigações, avaliação/alocação, classificação e divulgação.** Hipótese de risco: por representar saldo expressivo, eventual erro de existência/titularidade, custo atribuível, classificação ou recuperabilidade poderia afetar materialmente os ativos e divulgações consolidados. A existência de riscos de documentação, regularização, licenças, custos ou impairment **não foi constatada**; deve ser avaliada com documentação apropriada. | DFP consolidada: estoques de R\$ 6.951.508 mil; terrenos a incorporar totalizam R\$ 5.678.238 mil, dos quais R\$ 4.864.673 mil são não circulantes; estoques circulantes totalizam R\$ 2.086.835 mil. A variação de saldo também é somente indicador analítico, não explicação causal. [3] |
| Receita imobiliária | **Ocorrência, exatidão, corte, classificação e apresentação/divulgação**, conforme aplicável à política de reconhecimento adotada. Hipótese de risco: estimativas, mensuração do avanço/obrigações de desempenho, alocação de preço e corte entre períodos podem exigir julgamento. Não foram testados contratos, medições, vendas ou lançamentos. | A PwC identificou reconhecimento de receita imobiliária como PAA no relatório independente divulgado com a DFP. O PAA é evidência pública sobre a atenção do auditor externo, não conclusão autônoma deste papel. [3] |
| Provisões para contingências | **Completude, avaliação e divulgação.** Hipótese de risco: identificação incompleta de processos ou incerteza na estimativa de saída/provisão e divulgações relacionadas. Não foram consultados advogados, autos, cartas de circularização nem controles internos. | A PwC identificou provisões para contingências como PAA no relatório independente divulgado com a DFP. Isso não permite concluir que haja contingência não registrada ou provisão inadequada. [3] |
| Comunicação e governança | Hipótese de que a supervisão geral do processo de relatórios financeiros necessite de comunicação tempestiva sobre estratégia/época, riscos significativos, estimativas, PAA, dificuldades, distorções não corrigidas, independência e outras matérias pertinentes. | A existência, composição e recebimento efetivo de comunicação por conselho, comitê de auditoria ou outro órgão não foram comprovados pelas fontes acessadas. A identidade dos responsáveis pela governança deve ser confirmada no trabalho real (NBC TA 260, itens 10–13). |

**Contexto quantitativo (R\$ mil).** Os montantes divulgados indicam ativo consolidado de R\$ 13.219.635 em 31/12/2025, ante R\$ 10.067.406 em 31/12/2024; estoques totais de R\$ 6.951.508, terrenos a incorporar totais de R\$ 5.678.238 (dos quais R\$ 4.864.673 não circulantes), e estoques circulantes de R\$ 2.086.835. A partir desses valores públicos, os estoques equivalem a cerca de **52,6%** do ativo; terrenos a incorporar totais equivalem a cerca de **43,0%** do ativo e **81,7%** dos estoques. Ativo consolidado cresceu aproximadamente **31,3%** e terrenos a incorporar totais aproximadamente **23,8%** em relação aos respectivos saldos comparativos. São cálculos aritméticos feitos neste PT a partir dos valores informados na DFP; não são benchmark de materialidade, teste de auditoria nem explicação da variação. Os saldos não são aqui arredondados além dos percentuais indicativos.

## População, fontes e critérios

**População conceitual.** As comunicações requeridas pela NBC TA 260 (R2) para a auditoria das demonstrações consolidadas do exercício: comunicação de responsabilidades e alcance/época (itens 14–15); constatações significativas e independência (itens 16–17 e 16A, conforme texto oficial consultado); processo, forma, época e adequação da comunicação recíproca (itens 18–22); e documentação (item 23). Não foi disponibilizada lista de reuniões, interlocutores, e-mails ou cartas para constituir/testar população de comunicações realmente realizadas.

**Fontes públicas examinadas.**

- **CFC — NBC TA 260 (R2), texto oficial e índice oficial de normas**, consultados em 22/10/2026. O índice identifica a norma como NBC TA 260(R2), DOU 04/07/2016; o PDF oficial intitula-se “Norma Brasileira de Contabilidade – NBC TA 260 (R2), de 17 de junho de 2016”. [1] [2]
- **CVM — DFP de DIRECIONAL ENGENHARIA S.A., data-base 31/12/2025, V1**, protocolo/enviado em 09/03/2026; seção de demonstrações consolidadas, balanço patrimonial ativo, notas explicativas e pareceres/declarações. A tela estruturada da CVM identifica auditor PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. Os quadros consultáveis são estruturados em HTML e não oferecem numeração de página estável na visualização; por isso, este PT referencia a seção/quadro, sem atribuir número de página não verificado. [3]
- **B3 — perfil de DIRECIONAL ENGENHARIA S.A. (DIRR3), código CVM 21350**, consultado em 22/10/2026; perfil lista atividade e dados econômico-financeiros consolidados, incluindo ativo total em 31/12/2025 de R\$ 13.219.635 mil. A página não é usada para inferir composição dos estoques. [4]
- **RI da companhia — Central de Resultados**, fonte institucional consultada em 22/10/2026. A interface pública lista anos de resultado e documentos; a versão acessada não expôs link estável da DFP 2025, por isso não foi usada como fonte primária de saldos específicos neste PT. [5]

**Critérios.** NBC TA 260 (R2), em especial itens 9, 14–23; informações efetivamente acessíveis nas fontes primárias permitidas (CFC para norma e CVM, B3 e RI da companhia para fatos societários); nenhuma inferência sobre evidência interna. Valores monetários em milhares de reais conforme reportados pela DFP. Não foi definida nem presumida materialidade de auditoria.

## Procedimentos realizados e planejados

| Ref. | Procedimento | Classificação | Evidência/resultado |
|---|---|---|---|
| P01 | Consultar o índice de normas e o texto oficial do CFC; identificar norma, título, vigência e parágrafos pertinentes às comunicações. | **Realizado com evidência pública** | NBC TA 260 (R2), título/datas e itens 1–23; no PDF oficial, itens 14–16A iniciam na p. 5, itens 17–23 nas pp. 5–6. Revisão NBC 27 identificada junto ao item 16A. [1] [2] |
| P02 | Consultar a página de protocolo CVM da DFP para identificar emissor, período, versão/data de envio e auditor nomeado. | **Realizado com evidência pública** | DFP 31/12/2025, V1, enviada em 09/03/2026; PwC indicada como auditor. Registro público CVM, tela sem paginação estável. [3] |
| P03 | Ler os elementos públicos identificados para a DFP: demonstrações consolidadas, relatório de auditor independente/PAA e opinião; registrar somente o que está divulgado. | **Realizado com evidência pública** | Registro da DFP e categorias de informação na CVM; a leitura do relatório na DFP 4T25 V1 (PDF público do RI, pp. 115–117) identificou opinião sem modificação e PAA de reconhecimento de receita imobiliária e provisões para contingências. A leitura não equivale a validar os procedimentos da PwC nem a reexecutar sua auditoria. Referência: seção “Pareceres e Declarações”/relatório do auditor da DFP; sem número de página estável na tela estruturada consultada. [3] |
| P04 | Comparar, em nível geral, o ativo consolidado e saldos informados de estoques/terrenos entre 2025 e 2024 e calcular proporções aritméticas para priorizar temas de discussão. | **Realizado com evidência pública** | Cálculos apresentados no contexto quantitativo; dependem exclusivamente dos valores públicos da DFP e não constituem teste, validação de saldos ou conclusão de razoabilidade. [3] |
| P05 | Cruzar a identidade, código CVM, atividade e ativo total divulgado com o perfil de companhia listada da B3. | **Realizado com evidência pública** | Perfil B3: DIRECIONAL ENGENHARIA S.A., DIRR3, código CVM 21350; ativo consolidado de 31/12/2025. Cruzamento limitado a identidade e ativo total. [4] |
| P06 | Obter carta/ata/e-mail de abertura de auditoria, plano aprovado, calendário de reuniões, comunicações periódicas, respostas da governança e evidência de que os interlocutores são os responsáveis apropriados. | **Planejado por falta de acesso** | Não há acesso a arquivos, atas, correspondência nem pessoas da companhia ou do auditor. No trabalho real, identificar governança e avaliar a oportunidade/conteúdo da comunicação, conforme itens 11–13, 18 e 21–22. Nenhuma solicitação ou confirmação foi feita neste trabalho. |
| P07 | Comunicar, no início do trabalho real, responsabilidades do auditor e da administração/governança; visão geral do alcance, época, riscos significativos e forma/época/conteúdo previstos da comunicação. | **Planejado por falta de acesso** | Requer contato e estratégia de auditoria não disponíveis. Itens 14–15 e 18; incluir riscos identificados pela equipe após avaliação, sem tratá-los como fatos antes dos procedimentos. |
| P08 | Discutir com governança conclusões e assuntos significativos efetivamente decorrentes da auditoria real: julgamentos contábeis, receita imobiliária, estoques/terrenos, contingências, dificuldades, assuntos tratados com administração, representações formais, distorções corrigidas/não corrigidas e efeitos no relatório. | **Planejado por falta de acesso** | Nenhuma constatação, diferença, dificuldade, carta de representação, minuta ou comunicação da equipe de auditoria foi disponibilizada. Itens 16 e 19–21; comunicar somente fatos suportados pelo arquivo real. |
| P09 | Realizar a comunicação de independência exigida, incluindo requisitos éticos relevantes, relações/honorários e salvaguardas quando aplicáveis; reter comunicação escrita. | **Planejado por falta de acesso** | A indicação pública de PwC como auditora não prova declaração de independência ou comunicação a governança. Necessários dados de honorários/serviços, relações e documentação do auditor; itens 16A–17 e 20. Nada disso foi solicitado, confirmado ou testado aqui. |
| P10 | Aplicar uma agenda didática simulada de reunião final para organizar temas que poderiam ser propostos, sem atribuir falas, decisões ou anuência a qualquer pessoa. | **Simulado para fins didáticos** | Agenda-modelo: (1) responsabilidades; (2) alcance e época; (3) riscos/estimativas e assuntos públicos de PAA; (4) dificuldades e diferenças somente se apuradas no trabalho real; (5) independência e honorários conforme dados verificados; (6) conclusões e relatório; (7) avaliação da comunicação recíproca. **Não houve reunião, entrevista nem comunicação real.** |
| P11 | Inspecionar terrenos, obter confirmações de terceiros, examinar contratos/processos, testar controles, recalcular receita/provisões ou acessar papéis de auditoria. | **Planejado por falta de acesso; não executado** | Fora do escopo público deste PT e sem acesso. Não se declara confirmação externa, inspeção física, entrevista, revisão de papéis da PwC ou evidência interna executada. |

## Evidências e referências cruzadas

- **E1 / N1 — Norma:** CFC, NBC TA 260 (R2), “Comunicação com os Responsáveis pela Governança”, texto oficial consolidado; vigência informada no próprio texto para períodos findos a partir de 31/12/2016. Itens 9–10 (objetivo/definições, p. 4); 14–16A (p. 5); 17–23 (pp. 5–6); aplicação correspondente A1–A54 e Apêndice 2. Índice oficial CFC identifica a publicação DOU 04/07/2016. [1] [2]
- **E2 / F1 — DFP CVM:** DIRECIONAL ENGENHARIA S.A., Demonstrações Financeiras Padronizadas (DFP), 31/12/2025, V1, envio de 09/03/2026. Referência de visualização: demonstrações consolidadas → Balanço Patrimonial Ativo e Notas Explicativas; Pareceres e Declarações → relatório do auditor independente. Valores em R\$ mil. A interface HTML da CVM não tem paginação estável; o relatório foi lido no PDF direto do RI, pp. 115–117 (fonte S2 em FONTES.md). Usado em P02–P04 e nas informações PAA/opinião. [3]
- **E3 / F2 — Perfil B3:** B3, “DIRECIONAL ENGENHARIA S.A. — overview”, quadro “Dados da Companhia” e quadro “Balanço Patrimonial — Consolidado”, coluna 31/12/2025. Informação recebida no perfil em 01/10/2026, conforme própria página; consulta deste PT em 22/10/2026. Página web sem numeração. Usado em P05. [4]
- **E4 — RI:** Direcional, “Central de Resultados”. Consulta de 22/10/2026; a interface lista exercícios/relatórios, mas a resposta acessada não exibia o documento anual 2025. Referência de contexto/disponibilidade, não suporte independente de saldo. [5]

**Conciliação numérica de contexto:** o componente não circulante de terrenos a incorporar (R\$ 4.864.673 mil) + estoques circulantes totais (R\$ 2.086.835 mil) = estoques totais (R\$ 6.951.508 mil). Essa igualdade aritmética reconcilia os valores fornecidos para contextualização, mas não demonstra que as classificações ou mensurações sejam corretas.

## Resultados, exceções, conclusão e limitações

**Resultados.** As fontes públicas examinadas suportam a identificação da entidade e do exercício, da DFP V1 protocolada/enviada à CVM em 09/03/2026, da PwC como auditora indicada e dos montantes públicos usados para a contextualização. A informação pública do relatório da PwC registra opinião sem ressalva e PAA sobre reconhecimento de receita imobiliária e provisões para contingências. O ativo consolidado de R\$ 13.219.635 mil também consta do perfil B3. A dimensão dos estoques e dos terrenos justifica que sejam propostos para discussão como áreas de atenção, sem afirmar que tenham sido classificados formalmente como risco significativo pela equipe didática.

**Exceções.** Não foi encontrada evidência pública acessível neste procedimento que demonstre (i) quais pessoas/órgãos foram destinatários das comunicações; (ii) quando, em que forma ou conteúdo houve comunicação; (iii) discussão de riscos, estimativas, diferenças, dificuldades ou assuntos com administração; (iv) comunicação de independência e honorários; ou (v) avaliação da comunicação recíproca. Isso é **limitação de evidência deste PT**, não exceção de auditoria atribuível à companhia ou à PwC, e não permite concluir que as comunicações requeridas tenham faltado.

**Conclusão didática.** Com base exclusivamente em evidência pública, foram documentados a norma aplicável, os fatos públicos selecionados e uma análise preliminar de riscos/temas a submeter à governança. Não há evidência suficiente para concluir se o auditor real cumpriu os requisitos de comunicação da NBC TA 260 (R2), se as comunicações foram tempestivas/adequadas, ou se o relatório sem ressalva e os PAA são sustentados pelos papéis de trabalho. Para encerrar este PT numa auditoria real, seria necessário obter e avaliar documentação contemporânea das comunicações, identificar os responsáveis pela governança e correlacionar comunicações com o arquivo completo da auditoria.

**Limitações expressas.** Nenhuma entrevista, confirmação externa, inspeção física, observação de reunião, acesso a registros internos, teste de controles, leitura de contratos/processos ou exame dos papéis internos da PwC foi executado. Nenhuma comunicação foi enviada ou recebida por este preparador. Fatores não documentados foram mantidos como hipóteses de risco, não como constatações. Este PT não constitui opinião independente sobre as demonstrações financeiras.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA de Auditoria Independente, índice oficial de normas; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, Norma Brasileira de Contabilidade NBC TA 260 R2, texto oficial; [abrir fonte](<https://cfc.org.br/wp-content/uploads/2026/06/NBCTA260-R2-2.pdf>).
- **Ref. 3** — CVM, DIRECIONAL ENGENHARIA S.A., DFP 31/12/2025 V1, documento 155189; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3, DIRECIONAL ENGENHARIA S.A., perfil de companhia listada; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — Direcional Engenharia, Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-265 — Comunicação de deficiências de controle interno

| Identificação | Informação |
|---|---|
| **Código / título** | PT-265 — Comunicação de deficiências de controle interno |
| **Entidade / trabalho** | DIRECIONAL ENGENHARIA S.A. — auditoria didática das demonstrações contábeis consolidadas |
| **Exercício** | Encerrado em 31/12/2025 |
| **Norma / itens** | NBC TA 265 — Resolução CFC nº 1.210/09, texto aprovado sem revisão indicada no cadastro oficial do CFC; itens 1–11 e materiais de aplicação A1–A30, em especial A5–A11 e A27–A30. Aplicável a períodos iniciados em ou após 01/01/2010. Versão normativa aplicável ao exercício, verificada em 22/10/2026: NBC TA 265 (sem sufixo R), Resolução CFC nº 1.210/09, vigente e sem alteração/revogação no cadastro oficial. [1] [2] |
| **Data de acesso / elaboração** | 22/10/2026 |
| **Preparador** | EDU-AUD-001 (matrícula didática) |
| **Revisão** | ____________________ (em branco) |

> **Natureza do documento:** papel de trabalho exclusivamente didático, baseado em informações públicas indicadas neste documento. Não é parte dos papéis de trabalho da PwC nem representa auditoria executada pela pessoa preparadora. Não houve acesso a registros, controles, pessoas ou instalações internas da Companhia. A classificação de qualquer hipótese abaixo não constitui achado nem constatação de deficiência.

## Objetivo, contas e processos

Aplicar o enquadramento da NBC TA 265 para estruturar a avaliação e eventual comunicação de deficiências de controle interno no contexto da auditoria das demonstrações consolidadas do exercício findo em 31/12/2025. A Norma exige que o auditor determine, com base no trabalho executado, se identificou deficiências e, se identificadas, se são significativas individualmente ou em conjunto (itens 7–8). A comunicação escrita tempestiva à governança é requerida para deficiências significativas identificadas; a comunicação à administração é tratada no item 10. O item 11 especifica o conteúdo da comunicação. A mera existência de um PAA no relatório do auditor não demonstra, por si só, deficiência de controle interno. [2, p. 5–7 do PDF da Resolução, itens 7–11; páginas impressas da norma, itens 7–11]

**Contas/processos selecionados para planejamento didático:** estoques imobiliários, com foco em terrenos a incorporar; processo de reconhecimento de receita imobiliária; provisões para contingências e processo de estimativas/avaliação jurídica. A seleção decorre da dimensão das rubricas e dos assuntos tratados como principais assuntos de auditoria (PAA) nas informações públicas de base, não de risco de controle confirmado. A DFP indicada identifica reconhecimento de receita imobiliária e provisões para contingências como PAAs e informa opinião sem ressalva, conforme os fatos públicos-base fornecidos para este PT. [3]

## Afirmações e riscos considerados

Os saldos informados para 31/12/2025 estão expressos em **R\$ mil**. Ativo consolidado: R\$ 13.219.635; estoques: R\$ 6.951.508, dos quais terrenos a incorporar totalizam R\$ 5.678.238, incluindo R\$ 4.864.673 não circulantes, e estoques circulantes: R\$ 2.086.835. O total de terrenos a incorporar é a maior classe individual entre os estoques detalhados na Nota 5. Para 31/12/2024, ativo consolidado: R\$ 10.067.406 e terrenos a incorporar totais: R\$ 4.587.823, incluindo R\$ 3.888.979 não circulantes. Como conferência aritmética sobre esses dados públicos-base, estoques correspondem a aproximadamente 52,6% do ativo de 2025; terrenos a incorporar totais, 43,0% do ativo e 81,7% dos estoques. O saldo total de terrenos informado aumentou R\$ 1.090.415 mil (aproximadamente 23,8%) entre os exercícios; o ativo total aumentou R\$ 3.152.229 mil (aproximadamente 31,3%). Os percentuais e variações são cálculos derivados dos valores acima, não saldos adicionais extraídos da DFP. [3] [4]

| Processo / afirmação relevante | Risco hipotético para orientar procedimentos — não constatado |
|---|---|
| Estoques e terrenos a incorporar — existência, direitos e obrigações, integralidade, classificação e avaliação | **Hipótese de risco:** se controles de cadastro de terrenos, documentação de titularidade, movimentações entre projetos, custo atribuível e revisão de recuperabilidade forem inadequados, poderia haver saldo incorreto, classificação inadequada ou perda não reconhecida. O valor expressivo aumenta a exposição potencial, mas não comprova falha de controle. |
| Reconhecimento de receita imobiliária — ocorrência, exatidão, corte, classificação e apresentação | **Hipótese de risco:** se controles de aprovação de contratos, dados de evolução das obras, apuração do percentual de conclusão, cálculo da receita e lançamentos contábeis não forem desenhados ou operados adequadamente, poderia haver reconhecimento em período ou montante incorreto. A existência de PAA sobre receita é fator de atenção de auditoria, não evidência de deficiência. |
| Provisões para contingências — integralidade, avaliação, corte, classificação e divulgação | **Hipótese de risco:** se controles de captura de processos, atualização de prognósticos e valores, conciliação com assessores jurídicos e aprovação de premissas forem insuficientes, poderia haver omissão, mensuração ou divulgação inadequada de contingência. O PAA público não permite inferir erro ou deficiência. |
| Consolidação e fechamento — integralidade, exatidão, classificação e apresentação | **Hipótese de risco:** em estruturas com múltiplas entidades/projetos, falhas potenciais em reconciliações, lançamentos de consolidação ou revisão de estimativas poderiam afetar saldos consolidados. A estrutura concreta e a operação desses controles não foram acessadas neste trabalho. |

A NBC TA 265 define deficiência de controle interno em termos de desenho, implementação ou operação incapaz de prevenir, ou detectar e corrigir tempestivamente, distorções; ou ausência de controle necessário (item 6). A significância depende de julgamento profissional e considera probabilidade e magnitude potencial, não apenas distorção efetivamente identificada; são fatores pertinentes os listados em A5–A7. Assim, magnitude de conta, PAA e variação anual são apenas sinais para planejamento e não bastam para classificar deficiência significativa. [2, p. 4–6 do PDF da Resolução, itens 6–8 e A5–A7]

## População, fontes e critérios

**População pretendida para uma auditoria completa:** controles e transações do período de 01/01 a 31/12/2025 associados a estoques/terrenos, contratos e receita imobiliária, contingências e fechamento/consolidação; e controles sobre saldos comparativos relevantes. Não foi disponibilizado cadastro de controles, universo de transações, mapa de processos, lista de projetos/entidades ou amostra interna. Portanto, nenhum universo estatístico ou amostra de auditoria foi definido neste PT.

**Fontes públicas consultadas:** (i) cadastro e texto da NBC TA 265 no Conselho Federal de Contabilidade; (ii) protocolo/visualizador CVM informado para DFP de 31/12/2025, versão 1, protocolo indicado como 09/03/2026; (iii) página B3 de DIRECIONAL ENGENHARIA S.A.; e (iv) Central de Resultados do RI da Companhia. O visualizador CVM abriu a moldura do formulário e identificou PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA, mas sua interface não oferece paginação impressa estável. A DFP pública integral foi obtida diretamente no RI e as páginas relevantes foram examinadas. Logo, os dados detalhados, PAAs, data/protocolo e opinião são fatos públicos examinados para este exercício didático, sem conciliação a registros internos ou acesso à evidência privada de auditoria. A B3 exibe o ativo consolidado em 31/12/2025 no quadro de dados econômico-financeiros. [3] [4] [5] [6]

**Critérios:** NBC TA 265, itens 5–11 e A5–A11, quanto a identificar e avaliar deficiências e comunicar; norma não expressa opinião sobre eficácia de controles. Para cada hipótese, critérios de auditoria subsequentes e documentação operacional exigiriam conhecer desenho, implementação, operação, evidência de supervisão e fluxo de correção. Não foi definida materialidade de auditoria neste papel de trabalho, nem se presume qualquer limite material.

## Procedimentos e classificação

| Ref. | Procedimento e classificação | Resultado / documentação |
|---|---|---|
| P01 | **Realizado com evidência pública:** consulta ao cadastro oficial CFC para identificar número, título e status da NBC TA 265; leitura do PDF oficial da Resolução nº 1.210/09 e dos itens 1–11 e A5–A11 pertinentes. | Norma registrada como vigente, sem alteração ou revogação no cadastro consultado. A norma aplicável é NBC TA 265 — Resolução CFC nº 1.210/09, sem sufixo de revisão. Ref. E1. |
| P02 | **Realizado com evidência pública, alcance limitado:** acesso à página CVM fornecida para o documento sequencial 155189 e inspeção da informação exibida sobre auditor independente. | A página exibida identifica PwC como auditor; a interface CVM não oferece paginação estável, mas a DFP pública integral foi obtida separadamente e suas páginas relevantes examinadas. Não foram reexecutados testes de auditoria, nem houve conciliação a registros internos. Ref. E2. |
| P03 | **Realizado com evidência pública:** consulta à página B3 da companhia. | A B3 identifica a entidade e apresenta ativo total consolidado de R\$ 13.219.635 mil em 31/12/2025. Os saldos detalhados de estoques e terrenos foram localizados no PDF integral da DFP, no BP (pp. 16–17) e na Nota 5 (p. 69); não foram conciliados a registros internos. Ref. E3. |
| P04 | **Realizado com evidência pública:** consulta à Central de Resultados do RI indicada. | A página oficial foi consultada; seu extrator dinâmico não expõe o arquivo no corpo da resposta, mas o PDF oficial da DFP foi obtido pelo link direto e lido nas páginas relevantes. O RI não foi usado como evidência de controles internos. Ref. E4. |
| P05 | **Realizado com evidência pública:** cálculo analítico simples das proporções e variações a partir dos valores publicados no BP e na Nota 5 da DFP (pp. 16–17 e 69). | Recomputados os percentuais e variações apresentados acima. Trata-se de recálculo aritmético dos dados-base, sem confronto com razão, balancete ou documento-fonte integral; não é teste substantivo nem teste de controle. Ref. E5. |
| P06 | **Planejado por falta de acesso:** obter narrativa/fluxogramas, matriz de riscos e controles, responsáveis, evidência de desenho e implementação, relatórios de monitoramento e registro de deficiências/correções. | Pendente. Necessário para identificar controles relevantes, verificar desenho e implementação e compreender controles manuais e de TI relacionados aos processos selecionados. Nenhum walkthrough ou entrevista foi realizado. |
| P07 | **Planejado por falta de acesso:** testar operação dos controles selecionados por período/amostra, inspecionando evidência de aprovação, conciliações, revisão independente, cálculos e tratamento de exceções; avaliar controles gerais e de aplicação de TI quando relevantes. | Pendente. Sem arquivos ou acesso aos sistemas, não se pode afirmar que controle operou, que exceção ocorreu ou que controle compensatório exista. |
| P08 | **Planejado por falta de acesso:** para terrenos/estoques, obter composição analítica conciliada, contratos/documentos de titularidade, suporte de custos por empreendimento, política e memória de revisão de recuperabilidade; executar procedimentos apropriados sobre itens selecionados. | Pendente. Nenhuma inspeção física, confirmação de titularidade, inspeção de documentos internos ou teste de custo/valor realizável foi executado. |
| P09 | **Planejado por falta de acesso:** para reconhecimento da receita, selecionar contratos e eventos de 2025 e confrontar termos, documentação de desempenho/obra, bases de cálculo, aprovações e corte com registros e razão. | Pendente. Nenhum contrato, medição, cálculo interno ou lançamento foi inspecionado. O PAA indicado não substitui esses procedimentos. |
| P10 | **Planejado por falta de acesso:** para contingências, obter universo conciliado de ações/obrigações, respostas jurídicas, premissas, avaliação da administração, movimentação e divulgação; testar integralidade e mensuração. | Pendente. Nenhuma consulta, confirmação ou comunicação a assessores jurídicos foi feita. Não se infere omissão, suficiência ou inadequação de provisão. |
| P11 | **Planejado por falta de acesso:** acumular deficiências identificadas, avaliar individual e conjuntamente probabilidade, magnitude potencial, interação, causa e resposta da administração; determinar significância conforme item 8 e A5–A11. | Pendente, pois não há resultados de teste nem evidência suficiente para classificar deficiência. Materialidade e tolerância não foram disponibilizadas. |
| P12 | **Planejado por falta de acesso:** se forem identificadas deficiências significativas, redigir e comunicar tempestivamente por escrito à governança, incluindo descrição e possíveis efeitos; comunicar à administração conforme item 10, e documentar datas, destinatários e respostas. | Pendente e condicional à identificação de deficiência significativa. Nenhuma comunicação foi emitida ou recebida neste trabalho didático. |
| P13 | **Simulado para fins didáticos:** considerar, sem afirmar ocorrência, cenário hipotético em que conciliações/validações essenciais de terrenos, receitas ou contingências não fossem executadas e não houvesse revisão compensatória. | Exercício de aplicação de critério: seria necessário verificar condição, causa, controles compensatórios, exposições e probabilidade/magnitude antes de classificar; se significativo, a comunicação observaria os itens 9–11. Não constitui achado, evidência, teste realizado ou afirmação de que a Companhia opera dessa forma. |

## Evidências e referências cruzadas

| Referência | Evidência / fonte | Localização e alcance |
|---|---|---|
| E1 | CFC, **NBC TA 265 — Resolução nº 1.210/09**, registro oficial e PDF da Resolução. [1] [2] | Registro normativo sem paginação; PDF oficial com 14 páginas. Itens 5–11 e A5–A11, páginas impressas correspondentes no corpo da norma. A publicação compilada NBC TA 200–810 do CFC lista a NBC TA 265 a partir da p. 162, mas este PT usa a Resolução individual oficial como referência primária. |
| E2 | CVM, **DFP DIRECIONAL ENGENHARIA S.A., data-base 31/12/2025, documento sequencial 155189**. [3] | Visualizador eletrônico, seções “DFs Consolidadas”, “Balanço Patrimonial Ativo”, “Notas Explicativas” e “Pareceres e Declarações”. A interface CVM é eletrônica e não oferece paginação impressa estável; a DFP pública integral foi obtida no RI e as páginas relevantes foram examinadas. Não se atribui página CVM inexistente; protocolo 09/03/2026 e versão 1 são dados públicos do documento. |
| E3 | B3, **DIRECIONAL ENGENHARIA S.A. — Overview / Dados Econômico-Financeiros**. [4] | Página eletrônica, quadro “Balanço Patrimonial — Consolidado”, coluna 31/12/2025; confirma o ativo total consolidado. A página não tem paginação impressa. |
| E4 | RI da Direcional, **Central de Resultados**. [5] | Página eletrônica sem paginação impressa; o extrator do índice é dinâmico, mas a cópia integral da DFP foi obtida pelo link oficial e as páginas relevantes foram examinadas. A página é canal de localização; o PDF é a fonte pública do conteúdo. |
| E5 | Recálculos preparados neste papel de trabalho a partir dos valores públicos da DFP examinada. | PT-265, seção “Afirmações e riscos considerados”; cálculos aproximados, não constituem evidência independente dos saldos-fonte. |

## Resultados, exceções, conclusão e limitações

**Resultado dos procedimentos públicos:** foi possível corroborar no cadastro oficial CFC que a NBC TA 265 (Resolução 1.210/09) consta vigente e sem alteração/revogação; verificar a identificação da companhia na B3 e o ativo total consolidado de 31/12/2025 exibido pela B3; e observar na página CVM a identificação de PwC como auditor. A interface CVM não apresenta a DFP paginada como PDF, e o extrator do índice RI é dinâmico; contudo, a DFP pública integral foi obtida diretamente e as páginas relevantes foram examinadas. Os saldos detalhados de estoques e terrenos, comparativo de 2024, protocolo/data da versão e os PAAs/opinião foram localizados na DFP. Permanecem sem teste a conciliação com razão, registros internos e evidência privada de auditoria.

**Exceções:** limitação de acesso a informações internas e à evidência subjacente; a DFP pública integral foi obtida e as páginas relevantes foram examinadas. Nenhuma exceção de controle foi identificada, testada ou confirmada. A ausência de exceção observada em fontes públicas não significa ausência de deficiência.

**Conclusão didática:** com evidência exclusivamente pública e incompleta, não é possível concluir se a Companhia tinha deficiência de controle interno, se alguma deficiência era significativa ou se houve necessidade de comunicação nos termos dos itens 9–11 da NBC TA 265. Os fatores descritos são hipóteses de risco para orientar procedimentos, e não constatações. A opinião sem ressalva e os PAAs atribuídos à DFP-base não fornecem, por si, conclusão sobre eficácia de controles nem alteram essa limitação. Para conclusão de auditoria seria necessário executar os procedimentos planejados, avaliar evidência suficiente e apropriada e documentar julgamento profissional.

**Limitações expressas:** este trabalho não alega confirmação externa, entrevista, inspeção física, observação, walkthrough, inspeção de documentação interna, acesso a sistemas, teste de controle ou teste substantivo executado. Não se atribui achado, deficiência, distorção ou controle compensatório à DIRECIONAL ENGENHARIA S.A. A opinião da PwC e os números da DFP foram localizados na cópia pública examinada; isso não substitui testes de auditoria nem conciliação a registros internos.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA — de Auditoria Independente de Informação Contábil Histórica, cadastro normativo consultado em 22/10/2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, Resolução nº 1.210/09, NBC TA 265 — Comunicação de Deficiências de Controle Interno, texto oficial; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/RES_1210.pdf>).
- **Ref. 3** — CVM, DIRECIONAL ENGENHARIA S.A., DFP 31/12/2025, documento sequencial 155189, visualizador eletrônico; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3, DIRECIONAL ENGENHARIA S.A., Overview e dados econômico-financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — Direcional Engenharia S.A., RI, Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 6** — CVM, registro/visualizador do documento anual indicado para a DFP 2025; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).


---

# PT-300 — Planejamento da auditoria das demonstrações consolidadas

**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas (grupo)  
**Período:** exercício encerrado em 31/12/2025  
**Código/título:** PT-300 — Planejamento da auditoria  
**Norma aplicável:** NBC TA 300 (R1), *Planejamento da Auditoria de Demonstrações Contábeis*, texto oficial do CFC vigente para o exercício de 2025, consideradas as alterações da Revisão NBC 11/2021. A página de normas do CFC identifica a norma como NBC TA 300 (R1), publicada no DOU em 05/09/2016; a ficha oficial registra a Revisão NBC 11, publicada em 02/09/2021, como alteração da NBC TA 300 (R1). O arquivo normativo do CFC apresenta os itens 1–13 e materiais explicativos A1–A22. [1] [2] [3]  
**Itens da NBC TA 300 relacionados:** 2–13, A1–A22 e Apêndice. Em especial: objetivo no item 4; envolvimento da equipe-chave e atividades preliminares nos itens 5–6; estratégia global no item 7–8; plano de auditoria no item 9; atualização no item 10; direção, supervisão e revisão no item 11; documentação no item 12; e considerações de auditoria inicial no item 13.  
**Data de acesso às fontes:** 22/10/2026  
**Preparador:** matrícula didática EDU-AUD-001 — preparação didática, sem vínculo declarado com a companhia ou com o auditor independente.  
**Revisão:** ______________________________  
**Data da revisão:** _______________________

> **Natureza deste papel:** documento didático de planejamento retrospectivo, elaborado com informações públicas consultadas, sem acesso a registros internos. Não é papel de trabalho da PwC nem evidência de que procedimentos foram executados na auditoria independente publicada. Nenhuma entrevista, confirmação externa, inspeção física, acesso a registros internos ou teste de auditoria foi realizado para este papel.

## Objetivo, conta e processo

Documentar uma estratégia e um plano didáticos para auditoria das demonstrações contábeis consolidadas da companhia e controladas, para o exercício findo em 31/12/2025, com foco de planejamento em estoques imobiliários — sobretudo terrenos a incorporar — e na articulação com os principais assuntos de auditoria publicados para reconhecimento de receita imobiliária e provisões para contingências. O objetivo da auditoria, conforme NBC TA 300, item 4, é planejar o trabalho de forma a realizá-lo eficazmente; este papel não formula opinião de auditoria.

**Contas/processos no foco deste planejamento:** (i) estoques consolidados, circulantes e não circulantes, incluindo terrenos a incorporar, custos capitalizados e avaliação; (ii) processo de reconhecimento de receita de incorporação imobiliária e contas/estimativas relacionadas; (iii) provisões, contingências e divulgações; e (iv) consolidação, incluindo completude do perímetro e eliminações intragrupo. O foco é orientado pelos valores e assuntos informados nas demonstrações públicas, não constitui conclusão de que exista distorção.

## Contexto público considerado

A DFP consolidada de 31/12/2025, versão 1, foi protocolada na CVM em 09/03/2026. A companhia indicou como auditor independente a PricewaterhouseCoopers Auditores Independentes Ltda. (PwC). Os dados públicos-base indicam ativo consolidado de R\$ 13.219.635 mil, ante R\$ 10.067.406 mil em 2024; estoques de R\$ 6.951.508 mil, dos quais terrenos a incorporar totalizam R\$ 5.678.238 mil, incluindo R\$ 4.864.673 mil não circulantes, e estoques circulantes de R\$ 2.086.835 mil. Para 2024, terrenos a incorporar totalizavam R\$ 4.587.823 mil, incluindo R\$ 3.888.979 mil não circulantes. A DFP divulgou como principais assuntos de auditoria o reconhecimento de receita imobiliária e as provisões para contingências, e relatório com opinião sem ressalva. A fonte documental é a DFP pública integral examinada; a visualização CVM organiza as demonstrações por quadros, sem paginação impressa estável na tela. [4]

A página pública da B3 identifica DIRECIONAL ENGENHARIA S.A., código CVM 21350, negociação DIRR3 e atividade de incorporação, construção e comercialização de imóveis; nela, o balanço consolidado também apresenta ativo total de R\$ 13.219.635 mil em 31/12/2025. Essa informação é usada como referência pública de identificação e confronto do total, não como evidência sobre as demais rubricas ou sobre lançamentos individuais. [5] A central de resultados da companhia é uma fonte pública para localização de divulgações financeiras; sua consulta não substitui a DFP depositada na CVM. [6]

Como análise aritmética derivada dos saldos-base, os estoques representam aproximadamente 52,6% do ativo consolidado de 2025 e terrenos a incorporar totais aproximadamente 43,0% do ativo e 81,7% dos estoques. O saldo total de terrenos cresceu R\$ 1.090.415 mil, cerca de 23,8%, frente a 2024; o ativo consolidado cresceu R\$ 3.152.229 mil, cerca de 31,3%. Os percentuais e variações são cálculos deste papel sobre os valores acima, não valores adicionais transcritos da companhia. A concentração de ativos em estoque, sua dimensão e o assunto de receita reportado justificam atenção e procedimentos proporcionais, mas não provam risco materializado nem erro.

## Afirmações relevantes e riscos de distorção a considerar

As afirmações a seguir representam riscos/hipóteses de planejamento. Exceto pelos fatos explicitamente identificados como divulgados publicamente, não são constatações sobre controles, transações ou saldos da companhia.

| Área | Afirmações relevantes | Riscos/hipóteses para direcionar o planejamento |
|---|---|---|
| Terrenos a incorporar e demais estoques | Existência; direitos e obrigações; integralidade; mensuração/valorização e alocação; classificação e apresentação. | Dada a dimensão do saldo, planejar testes de titularidade e existência, custo de aquisição e capitalização, alocação entre projetos, corte e recuperabilidade. Como hipóteses, podem existir risco de direitos não comprovados, custos indevidos capitalizados, classificação incorreta ou valor contábil superior ao recuperável; nenhuma dessas situações foi constatada neste trabalho. |
| Receita imobiliária | Ocorrência; integralidade; exatidão; corte; classificação e apresentação; mensuração de estimativas relacionadas. | A receita imobiliária figura entre os PAA divulgados. Planejar entendimento do processo e resposta de auditoria a reconhecimento e mensuração, inclusive premissas, contratos, evolução das obrigações/desempenho e corte, conforme aplicável ao modelo contábil adotado. A inclusão como PAA não é afirmação de distorção. |
| Provisões e contingências | Integralidade; existência/obrigação; avaliação e alocação; classificação, apresentação e divulgação. | As provisões para contingências figuram entre os PAA divulgados. Considerar, como risco, passivos não identificados ou mensurados/divulgados inadequadamente, dependentes de informações jurídicas e estimativas. Não se afirma ausência ou insuficiência de provisões. |
| Consolidação | Integralidade, exatidão, classificação, apresentação e direitos/obrigações nas entidades do grupo; eliminação de saldos e transações intragrupo. | Sem acesso à estrutura societária detalhada, balancetes e papéis de consolidação, manter como hipótese risco de perímetro incompleto, conversão ou eliminação incorreta. Confirmar o perímetro e planejar trabalho sobre componentes somente após obter informações apropriadas. |

## População, fontes e critérios

**População pretendida para testes:** população integral de lançamentos, adições, baixas e transferências de estoques no exercício e saldos por empreendimento/unidade; população de contratos e eventos de receita reconhecidos no exercício; população de processos/consultas jurídicas e contingências; balancetes, demonstrações e ajustes de consolidação de todas as entidades do grupo. As populações detalhadas, listagens, completude e confiabilidade não foram disponibilizadas neste trabalho. Não se definiu ou simulou tamanho de amostra estatístico, pois faltam população testável, materialidade e avaliação de risco documentadas.

**Fontes públicas examinadas:** DFP consolidada CVM de 31/12/2025 V1 e seus quadros/documentos; página de dados da companhia na B3; central de resultados do RI; e texto normativo e cadastro de normas do CFC. Para fatos societários e financeiros da companhia, este papel restringe suas referências à CVM, B3 e RI, conforme escopo solicitado. Fontes públicas não fornecem os documentos contábeis transacionais nem o suporte jurídico e operacional necessários para testes substantivos.

**Critérios de seleção e avaliação para o plano:** materialidade a ser estabelecida para o conjunto das demonstrações e materialidade de execução, considerando referencial apropriado e julgamento profissional (não calculados neste PT); avaliação de risco por conta/afirmação; priorização de rubricas relevantes ou individualmente significativas; e amostragem desenhada somente após obtenção da população e definição dos parâmetros. Os valores agregados citados orientam a priorização, não substituem cálculo formal de materialidade nem critério de amostragem. Confrontar reconhecimento, mensuração, classificação e divulgação com a estrutura contábil efetivamente aplicável e as políticas descritas pela administração, cuja validação ainda é necessária.

## Estratégia global e plano de auditoria didáticos

Em linha com os itens 7–9 da NBC TA 300, a estratégia proposta é auditar as demonstrações consolidadas como um todo, começar pela avaliação dos riscos do grupo, entender o perímetro e os processos relevantes e então desenhar procedimentos de avaliação de risco e respostas no nível das afirmações. Os procedimentos abaixo especificam natureza, época e extensão pretendidas em nível de planejamento; sua aplicação requer acesso autorizado à administração, aos registros e às evidências originais. A equipe, o orçamento, a materialidade, o cronograma de campo e eventual uso de especialistas/component auditors ainda precisariam ser definidos pelo responsável pelo trabalho. A estratégia e o plano devem ser atualizados quando surgirem informações adicionais, conforme item 10.

### Procedimentos e status

| ID | Status | Procedimento e propósito | Evidência/limite |
|---|---|---|---|
| PUB-01 | **Realizado com evidência pública** | Consultada a identificação da DFP na página RAD/CVM e registrados período, versão, protocolo e auditor, com base nos metadados CVM e na DFP 4T25 V1 obtida integralmente no RI. | Referência EV-01. Evidência documental pública de divulgação; não confirma execução ou suficiência do trabalho da PwC. |
| PUB-02 | **Realizado com evidência pública** | Considerados os saldos agregados de ativo, estoques, terrenos a incorporar e comparativos publicados na DFP; recalculadas neste papel as variações percentuais e proporções indicadas no contexto. | Referência EV-01; cálculo aritmético reproduzível sobre os dados-base. Sem conciliação a razão, subledger ou suporte de saldo. |
| PUB-03 | **Realizado com evidência pública** | Confrontado o ativo total consolidado de 31/12/2025 informado na DFP com o valor de 31/12/2025 apresentado na página B3; ambos são R\$ 13.219.635 mil. | Referências EV-01 e EV-02. Concordância entre divulgações públicas não é teste de auditoria do saldo. |
| PUB-04 | **Realizado com evidência pública** | Considerados os PAA e a opinião divulgados no relatório de auditoria que acompanha a DFP: reconhecimento de receita imobiliária, provisões para contingências e opinião sem ressalva. | Referência EV-01. Leitura do relatório publicado apenas; não foram obtidos arquivos de auditoria, evidências subjacentes ou comunicações com o auditor. |
| PUB-05 | **Realizado com evidência pública** | Consultadas a página societária/dados de companhia da B3 e a central de resultados do RI para confirmar o acesso aos canais públicos e a identificação geral da companhia. | Referências EV-02 e EV-03. A página RI, por si só, não comprova saldo; a DFP CVM é a fonte-base dos valores. |
| PLN-01 | **Planejado por falta de acesso** | Obter carta de contratação e entendimento de termos, confirmar independência/ética, aceitação e continuidade, envolver sócio e membros-chave e realizar discussão de equipe sobre riscos de fraude/erro e direção do trabalho. | Evidências internas e confirmações de independência/aceitação não foram disponibilizadas. Requisitos correlatos da NBC TA 300, itens 5–6 e, se auditoria inicial, item 13. |
| PLN-02 | **Planejado por falta de acesso** | Obter estrutura legal do grupo e lista de componentes; entender controles e processos de consolidação; conciliar demonstrações publicadas com balancetes e razão; avaliar componentes e necessidade de instruções/trabalho de outros auditores. | Requer organograma, balancetes, consolidação, políticas e acesso a componentes, indisponíveis. |
| PLN-03 | **Planejado por falta de acesso** | Para estoques, obter listagem por projeto e movimentação; testar amostras de aquisições/custos contra contratos, títulos e comprovantes; verificar corte, apropriação e rateio; observar contagens físicas selecionadas na data ou próxima, com reconciliação; testar premissas de recuperabilidade e divulgação. | População, documentos e locais não acessados. A inspeção física é exclusivamente planejada; nenhuma visita ou contagem foi feita. Seleção e extensão dependem de risco/materialidade e logística. |
| PLN-04 | **Planejado por falta de acesso** | Para receita, entender o modelo/política; selecionar contratos e transações depois de obter população; inspecionar contratos e aditivos, recalcular reconhecimento e estimativas relevantes, testar lançamentos/corte e conciliar divulgações. | Contratos, registros e população não acessados. O PAA público orienta o foco, mas não substitui procedimentos independentes. |
| PLN-05 | **Planejado por falta de acesso** | Para contingências, obter relação completa de processos e consultas, solicitar respostas diretas aos assessores jurídicos, inspecionar documentação pertinente, avaliar probabilidade/mensuração e conferir registro e divulgação. | Não houve solicitação ou confirmação a advogados, nem acesso a cadastro jurídico ou documentos. Nenhuma contingência foi confirmada neste PT. |
| PLN-06 | **Planejado por falta de acesso** | Definir materialidade global e de execução, procedimentos analíticos de avaliação de risco, natureza/época/extensão dos testes por afirmação, amostras, supervisão e revisão; atualizar o plano e documentar mudanças significativas. | Materialidade, populações, equipe e cronograma de auditoria não foram fornecidos. Nenhum parâmetro foi presumido. |
| SIM-01 | **Simulado para fins didáticos** | Exemplo de desenho: após receber listagens completas e testar sua integridade, estratificar estoques por empreendimento e valor/risco, escolher itens individualmente significativos e selecionar amostra dos demais itens para testar documentação, custo, corte e recuperabilidade. | É somente uma ilustração de como o plano poderia ser operacionalizado. Nenhum item foi selecionado, solicitado ou testado; não há amostra, resultado ou exceção simulada. |

## Evidências e referências cruzadas

- **EV-01 — CVM/RAD:** DFP da DIRECIONAL ENGENHARIA S.A., exercício social encerrado em 31/12/2025, versão 1, protocolo informado como 09/03/2026; quadros de DFs consolidadas, balanço patrimonial ativo, notas explicativas e relatório do auditor. Documento identificado pelo CVM 155189. A consulta RAD é organizada por abas/quadros e não oferece paginação estável; a DFP pública integral foi obtida por canal oficial e as páginas relevantes foram examinadas. [4]
- **EV-02 — B3:** página “DIRECIONAL ENGENHARIA S.A.”, dados da companhia e dados econômico-financeiros consolidados, coluna 31/12/2025. Usada para identificação e confronto do ativo total, não para testar estoques por subconta. [5]
- **EV-03 — RI da companhia:** “Central de Resultados”, página de localização das divulgações da companhia. Usada apenas como canal público de referência. [6]
- **EV-04 — CFC:** NBC TA 300 (R1), *Planejamento da Auditoria de Demonstrações Contábeis*, arquivo normativo oficial; itens 2–13 e A1–A22. A fonte identifica o propósito e os requisitos de planejamento, documentação e atualização. [1] [2] [3]

**Rastreabilidade:** PUB-01, PUB-02 e PUB-04 remetem a EV-01; PUB-03 a EV-01/EV-02; PUB-05 a EV-02/EV-03; PLN-01 a PLN-06 e SIM-01 são planos, não evidência de execução. Referências EV-01 a EV-04 documentam fontes consultadas, não constituem arquivos de suporte de testes sobre saldos.

## Resultados, exceções e conclusão

**Resultado dos procedimentos públicos delimitados:** a DFP 4T25 V1 (BP pp. 16–17 e Nota 5 p. 69) e a página B3 apresentam ativo consolidado de R\$ 13.219.635 mil em 31/12/2025. Os valores de estoque e terrenos acima foram tratados como valores divulgados na DFP; os recálculos das variações e percentuais aritméticos deste PT são coerentes com os valores apresentados. A DFP informa os PAA de receita imobiliária e provisões para contingências e opinião sem ressalva. Isso descreve informações publicadas, não comprova os saldos nem permite avaliar independentemente os procedimentos que fundamentaram o relatório da PwC.

**Exceções:** nenhuma exceção de auditoria foi identificada ou avaliada, pois não foram executados testes de detalhes, inspeções, confirmações, entrevistas ou procedimentos sobre registros internos. A concordância entre fontes públicas para o ativo total não é exceção zero nem asseguração.

**Conclusão de planejamento:** os dados públicos justificam planejar atenção significativa para estoques imobiliários, especialmente terrenos a incorporar, e para os processos associados aos PAA de reconhecimento de receita e provisões para contingências, além dos riscos de consolidação. Isso é uma priorização de risco hipotético/de planejamento, não uma constatação de erro, deficiência de controle ou fraude. O plano permanece preliminar até acesso às informações internas, definição documentada de materialidade e riscos, obtenção de populações e recursos adequados. Não se emite opinião sobre as demonstrações.

**Limitações:** papel didático elaborado com fontes públicas examinadas; acesso realizado em 22/10/2026. Não representa documentação da auditoria estatutária nem trabalho da PwC. Não houve consulta a administração, empregados, assessores jurídicos, auditor predecessor ou terceiros; não houve confirmação, inspeção física, acesso a contratos, sistemas, razão, consolidação ou evidência interna; nenhuma amostra foi extraída ou testada. A ausência de exceções reportadas aqui não deve ser interpretada como ausência de distorção.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA 300 R1 Planejamento da Auditoria de Demonstrações Contábeis, texto normativo oficial, 2016, itens 1–13 e A1–A22; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA300%28R1%29.pdf>).
- **Ref. 2** — CFC, NBC TA de Auditoria Independente, listagem de normas e identificação NBC TA 300 R1, acesso em 22/10/2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 3** — CFC, Revisão NBC 11, publicada no DOU em 02/09/2021, ficha normativa; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?codigo=2021/REVIS%C3%83ONBC11>).
- **Ref. 4** — CVM, DIRECIONAL ENGENHARIA S.A., DFP consolidada de 31/12/2025, versão 1, documento/identificador 155189, quadros, notas e relatório do auditor; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 5** — B3, DIRECIONAL ENGENHARIA S.A., página de companhia e dados econômico-financeiros consolidados, coluna 31/12/2025; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 6** — DIRECIONAL ENGENHARIA S.A., Relações com Investidores, Central de Resultados, acesso em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-315 — Identificação e avaliação dos riscos de distorção relevante

| Campo | Informação |
|---|---|
| **Código / título** | PT-315 — Identificação e avaliação dos riscos de distorção relevante |
| **Entidade / demonstrações** | DIRECIONAL ENGENHARIA S.A. — demonstrações financeiras consolidadas |
| **Período** | Exercício encerrado em 31/12/2025 |
| **Norma / itens** | NBC TA 315 (R2), de 19/08/2021, publicada no DOU em 02/09/2021. Aplicação para períodos iniciados a partir de 01/01/2022, item 10. Requisitos considerados: itens 11–13, 16–20, 23–29, 30–38; definições do item 12; material explicativo A11–A47, A48–A183 e A184–A241; Apêndices 1–4, em especial o Apêndice 4 sobre afirmações. O registro oficial CFC consultado informa norma vigente, não alterada e não revogada na data de acesso. [1] [2] |
| **Data de acesso** | 22/10/2026 |
| **Preparador** | Matrícula didática EDU-AUD-001 |
| **Data de preparação** | 22/10/2026 |
| **Revisão** | ____________________________________ |

## Objetivo, conta e processo

Identificar e avaliar, em nível preliminar e didático, riscos potenciais de distorção relevante nas demonstrações consolidadas da Companhia para 2025, com foco na rubrica de estoques, em reconhecimento de receita imobiliária e em provisões para contingências. Considera-se o entendimento limitado à informação pública identificada neste papel. Não é uma auditoria, não é uma conclusão sobre efetividade de controles e não substitui a avaliação feita por equipe com acesso à administração, aos registros contábeis e às investidas.

As contas/processos em foco são: (i) estoques circulantes e não circulantes, especialmente terrenos a incorporar; (ii) reconhecimento de receita imobiliária e respectivos custos/estoques; (iii) identificação, mensuração e divulgação de provisões e contingências; e (iv) consolidação, eliminações e participações de não controladores, dada a apresentação consolidada. A B3 descreve a atividade principal da emissora como incorporação, construção e comercialização de imóveis próprios ou de terceiros e serviços de engenharia. [4]

## Base factual pública e população

A fonte primária do período é a DFP de 31/12/2025, versão 1, enviada à CVM em 09/03/2026 às 18:29:30, protocolo **021350DFP311220250100155189-71**. A tela de consulta identifica PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA como auditor. [3] A população disponível para esta avaliação é a informação publicada nas demonstrações consolidadas e no relatório do auditor, mais os dados padronizados de balanço no conjunto aberto DFP/CVM de 2025. Não se obteve razão contábil, balancete, cadastro analítico de terrenos, carteira de empreendimentos, contratos, memória de cálculo de custos/receitas, composição de contingências ou dados de entidades consolidadas.

Valores abaixo em **R\$ mil**. As rubricas e números foram confrontados com o arquivo CVM de dados abertos “dfp_cia_aberta_BPA_con_2025.csv”, filtro Companhia CVM 21350, DFP de referência 31/12/2025, colunas “DF Consolidado – Balanço Patrimonial Ativo” e exercício “Último”; comparativos são do exercício “Penúltimo”. Os percentuais e a variação foram calculados para este PT a partir desses saldos, sem limiar de materialidade aprovado. [3] [5]

| Rubrica consolidada | 31/12/2025 | 31/12/2024 | Observação analítica |
|---|---:|---:|---|
| Ativo total | 13.219.635 | 10.067.406 | Aumento calculado de 31,3%. |
| Estoques circulantes | 2.086.835 | — | 15,8% do ativo total em 2025. A comparação de 2024 não é reproduzida neste PT. |
| Terrenos a incorporar, não circulante | 4.864.673 | 3.888.979 | Aumento calculado de 25,1%; 36,8% do ativo total; maior rubrica individual do ativo. |
| Estoques totais informados | 6.951.508 | — | 52,6% do ativo total; soma dos estoques circulantes e não circulantes conforme base pública informada. |

O traço na tabela significa que o valor comparativo não foi incluído neste papel, e não saldo zero. A apresentação do ativo separa estoques circulantes e estoques não circulantes, incluindo terrenos a incorporar. A Central de Resultados e a área de documentos entregues à CVM do RI foram consultadas como canais oficiais da companhia; a referência primária usada para versão, envio e demonstrações permanece o protocolo CVM acima. [6] [7]

## Afirmações e avaliação preliminar de riscos

A NBC TA 315 requer identificação de riscos em nível das demonstrações e das afirmações, com avaliação de risco inerente e risco de controle conforme a norma; para classificar risco significativo é necessário aplicar os critérios do item 12 e considerar a posição na faixa de risco inerente (itens 28–32 e explicativos A184–A236). A equipe didática não tem materialidade, informações internas, entendimento de controles ou evidência de projeto suficientes para concluir a posição final na faixa ou afirmar que algum risco atende à definição normativa de “risco significativo”. As classificações abaixo são **hipóteses/preocupações preliminares**, não constatações de erro, fraude, deficiência ou controle ineficaz.

| Área / afirmações potencialmente relevantes | Hipótese de risco de distorção relevante e fundamento público | Avaliação preliminar didática |
|---|---|---|
| **Terrenos a incorporar e demais estoques** — existência; direitos e obrigações; integralidade; exatidão, valorização e alocação; classificação e apresentação | O saldo total de terrenos a incorporar é elevado em relação ao ativo (43,0%), é a maior classe individual detalhada na Nota 5 e aumentou 23,8% em comparação anual. É hipótese que custos capitalizados, classificação, titularidade, custo atribuível ou redução ao valor realizável líquido possam requerer julgamento e produzir distorção. Também é hipótese que haja risco de integridade da população ou de registro em período/classificação inadequados. Nenhuma dessas condições foi verificada em projetos ou documentos-fonte. | Exposição inerente preliminar **elevada a avaliar**, pela magnitude e potencial julgamento; sem avaliação final de risco de controle ou de risco significativo. |
| **Receita imobiliária e custos associados** — ocorrência; integralidade; exatidão; corte; classificação/apresentação; e, quando pertinente, direitos e obrigações | A DFP identifica reconhecimento de receita imobiliária como Principal Assunto de Auditoria (PAA), conforme base pública fornecida para este trabalho. Isso sinaliza área de atenção do auditor independente, não evidência de distorção. É hipótese que critérios de reconhecimento, mensuração de progresso/obrigações de desempenho, estimativas de custos para conclusão, corte e vínculo entre receita, recebíveis e estoques possam gerar distorção relevante. Não se examinou contrato, medição, cálculo ou lançamento. | Área prioritária para entendimento e avaliação; risco e afirmações específicos dependem de modelo contratual e política contábil, ainda não obtidos. Não se declara risco significativo. |
| **Provisões e contingências** — integralidade; exatidão/valorização e alocação; classificação; apresentação e divulgação | A DFP identifica provisões para contingências como PAA conforme a base pública fornecida. É hipótese de risco que processos não identificados ou incompletos, avaliação jurídica/contábil, probabilidade, estimativa de desembolso, atualização ou divulgação possam ser inadequados. Não se acessaram confirmações ou cartas de advogados nem processos. O PAA não é constatação de passivo omitido nem de estimativa incorreta. | Área prioritária de julgamento e completude; magnitude e risco residual não avaliáveis sem inventário de processos e suporte jurídico. Não se declara risco significativo. |
| **Consolidação do grupo** — integralidade; exatidão/valorização; classificação/apresentação; direitos e obrigações | Dadas as demonstrações consolidadas, é hipótese que perímetro de consolidação, datas, saldos e transações intragrupo, eliminações, alocação de resultados e participações não controladoras exijam tratamento complexo. Não se confirmou número ou estrutura de controladas, aquisições, sistemas ou eliminações. | Risco transversal a entender; insuficiência de evidência para classificar probabilidade ou impacto. |
| **Nível das demonstrações / viés ou sobreposição de controles** — várias afirmações | Em razão da magnitude de estimativas e do escopo consolidado, deve-se considerar se fatores de risco de fraude, viés da administração ou sobreposição de controles estão presentes, conforme norma e NBC TA 240. Isso é consideração de risco, não alegação de fraude ou de que a administração tenha sobreposto controles. | Sem evidência para concluir presença; exige discussão de equipe, indagações e evidência corroborativa. |

## Fontes, critérios e evidências / referências cruzadas

**Fontes consultadas:** (a) CFC, “NBC TA – de Auditoria Independente de Informação Contábil Histórica”, registro da NBC TA 315 (R2), e texto oficial em PDF; (b) CVM/RAD, DFP da Direcional, protocolo acima; (c) CVM Dados Abertos, arquivo CSV de balanço patrimonial consolidado de 2025; (d) perfil institucional da Direcional na B3; e (e) páginas de RI da Central de Resultados e Documentos Entregues à CVM. A área dinâmica do RAD mostra as abas/seções “DFs Consolidadas”, “Notas Explicativas”, “Pareceres e Declarações” e “Balanço Patrimonial Ativo”, mas não oferece paginação estável. A DFP pública integral foi obtida diretamente no RI e as páginas relevantes foram examinadas; não se inventa número de página da tela CVM. [1]–[7]

**Critérios de seleção e avaliação:** período encerrado em 31/12/2025; demonstrações consolidadas; saldos em reais mil; relevância qualitativa e magnitude relativa do estoque e dos terrenos; identificação dos PAA comunicados no relatório do auditor; afirmações nos termos do Apêndice 4 da NBC TA 315 (R2); consideração de fatores de risco inerente, complexidade, subjetividade, mudança, incerteza e suscetibilidade a distorção, sem determinar materialidade ou risco significativo na ausência de suporte suficiente. As tendências de saldos são análises de informação pública, não procedimentos substantivos de auditoria nem evidência sobre a população detalhada.

## Procedimentos e status

| Procedimento | Status exigido | Evidência / referência cruzada e resultado |
|---|---|---|
| Consultar a página oficial CFC e o texto da NBC TA 315 para identificar versão, vigência, objetivo, requisitos e afirmações aplicáveis. | **Realizado com evidência pública** | Registro CFC informa NBC TA 315 (R2), DOU de 02/09/2021, vigente, não alterada e não revogada; PDF oficial, especialmente itens 10–13, 19–20, 28–38 e Apêndice 4. [1] [2] |
| Consultar o registro CVM da DFP para identificar emissor, data de referência, versão, protocolo, data de envio e auditor. | **Realizado com evidência pública** | Tela CVM/RAD: Demonstrações Financeiras Padronizadas 31/12/2025 V1; protocolo 021350DFP311220250100155189-71; envio 09/03/2026; auditor PwC. [3] |
| Obter/consultar os saldos publicados de ativo, estoques circulantes e terrenos não circulantes, incluindo comparativo disponível. | **Realizado com evidência pública** | DFP e dados abertos CVM, arquivo de BP consolidado. As cifras deste PT foram conferidas pela companhia CVM 21350 e rubricas correspondentes. Isso não representa confirmação de saldos em razão, titularidade ou existência física. [3] [5] |
| Calcular proporções de estoques/ativo, percentual dos terrenos sobre o ativo e variação anual de terrenos e ativo. | **Realizado com evidência pública** | Aritmética sobre os saldos públicos da tabela: 6.951.508/13.219.635 = 52,6%; 5.678.238/13.219.635 = 43,0%; crescimento do total de terrenos = 23,8%; crescimento do ativo = 31,3%. Sem benchmark de materialidade; análises não comprovam valor realizável ou risco de erro. [3] [5] |
| Consultar o perfil B3 para conhecer atividade principal e identificar, em alto nível, o setor em que a entidade opera. | **Realizado com evidência pública** | Atividade principal declarada no perfil B3: incorporação, construção e comercialização de imóveis próprios ou de terceiros e serviços de engenharia. [4] |
| Considerar para fins didáticos a indicação de reconhecimento de receita imobiliária e provisões para contingências como PAA e a opinião sem ressalva informadas na base pública deste encargo, relacionando-as à avaliação de riscos. | **Realizado com evidência pública** | O relatório da DFP pública foi obtido e lido nas pp. 115–117; a menção a PAA/opinião não é reexecução nem validação do trabalho de PwC. [3] |
| Inferir a existência de fatores específicos a partir de crescimento do saldo, PAA ou perfil setorial. | **Simulado para fins didáticos** | Foram formuladas hipóteses de exposição em estoque, reconhecimento de receita, contingências e consolidação. Não são achados nem condições constatadas. Sem atribuição de fraude, distorção ou deficiência. |
| Obter entendimento de políticas contábeis aplicadas, modelo operacional, contratos, apropriação de custos, condições de terrenos, eventos, sistemas e estrutura do grupo; realizar indagações com administração, contabilidade, jurídico e responsáveis pela governança. | **Planejado por falta de acesso** | Necessário para concluir avaliação de risco por afirmação e identificar a população completa. Não houve entrevista nem confirmação. |
| Inspecionar razão/balancete, cadastro e documentação de terrenos, matrículas/títulos, contratos, orçamentos, mapas de custo, relatórios de valor realizável, medições e reconciliações entre módulos e demonstrações. | **Planejado por falta de acesso** | Procedimentos previstos para validar entendimento, origens dos saldos, classificação, direitos, valorização e trilha de dados. Não houve acesso, inspeção de documentos internos ou teste executado. |
| Obter listagem de ações judiciais e administrativas, carta/relatórios dos advogados, avaliações da administração, conciliações, pagamentos e eventos subsequentes relevantes para contingências. | **Planejado por falta de acesso** | Procedimentos necessários à avaliação da completude, estimativa e divulgação. Não houve consulta a advogados, confirmação externa ou inspeção de processos. |
| Realizar walkthroughs dos fluxos de vendas/receita, custos de construção, estoques, provisões e consolidação; mapear controles e testar desenho/implementação. | **Planejado por falta de acesso** | Não houve walkthrough, observação, teste de controle ou avaliação de implementação. |
| Obter composição do grupo, demonstrações de controladas, reconciliações/eliminações intercompanhias e informações de eventos societários; avaliar perímetro e processo de consolidação. | **Planejado por falta de acesso** | Procedimento essencial a risco de consolidação; estrutura detalhada não foi inferida a partir das demonstrações publicadas. |
| Fazer observação física de inventários ou confirmação direta de titularidade/terceiros. | **Planejado por falta de acesso** | Nenhuma contagem, inspeção física, confirmação ou consulta a registro externo foi realizada. A observação direta pode ser considerada na resposta posterior de auditoria, conforme risco e circunstância. |

## Resultados, exceções e conclusão

A informação pública indica saldos expressivos de estoques e terrenos a incorporar, concentração relevante do ativo nessa rubrica e crescimento anual dos terrenos. O arquivo CVM de demonstrações apresenta R\$ 13.219.635 mil de ativo total, R\$ 2.086.835 mil de estoques circulantes e R\$ 4.864.673 mil em terrenos a incorporar não circulantes; o total de estoques de R\$ 6.951.508 mil informado para este papel equivale a 52,6% do ativo. O relatório de auditoria identificado na base de trabalho reporta opinião sem ressalva e PAA de reconhecimento de receita imobiliária e provisões para contingências. Esses fatos públicos orientam as hipóteses de risco, mas não demonstram que haja erro, fraude, deficiência de controle ou provisão inadequada. [3] [5]

**Exceções de auditoria:** nenhuma exceção de teste foi identificada porque não foram executados testes de auditoria de saldos ou controles. Os pontos abertos são lacunas de evidência e de entendimento, não exceções constatadas. A opinião sem ressalva emitida por PwC é a opinião do auditor independente sobre as demonstrações e não uma conclusão deste preparador didático. A identificação de PAA não implica distorção; indica assunto de maior significância no julgamento do auditor que reportou.

**Conclusão didática:** para planejamento, tratar estoques/terrenos, reconhecimento de receita imobiliária, contingências e consolidação como áreas prioritárias de entendimento e avaliação por afirmação. As avaliações de risco aqui são preliminares e baseadas em evidência pública limitada. A conclusão formal de NBC TA 315 requer completar procedimentos de avaliação de riscos, obter evidência suficiente e apropriada sobre a entidade, seu ambiente, a estrutura de relatório financeiro e os componentes do sistema de controles internos, avaliar risco inerente/risco de controle e revisar os riscos se novas informações surgirem. Não se conclui aqui sobre materialidade, risco significativo, adequação de políticas, efetividade de controles, saldo correto ou suficiência de provisões.

## Limitações

Este papel tem finalidade didática e não foi preparado ou autorizado pela companhia, pelo auditor independente ou pelo CFC. O escopo limita-se a informações públicas de CFC, CVM, B3 e RI e aos fatos-base examinados. Não houve confirmação externa, entrevista, inspeção física, observação, consulta a advogados, acesso a papéis de trabalho de PwC, acesso a registros internos, amostragem, testes substantivos, teste de controles ou reexecução da auditoria. A interface CVM não oferece paginação impressa estável; o PDF público integral foi obtido e as páginas relevantes foram lidas. Todas as afirmações sobre condições não documentadas estão qualificadas como hipótese ou risco potencial.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA – de Auditoria Independente de Informação Contábil Histórica, listagem normativa consultada em 2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, NBC TA 315 (R2), texto oficial, PDF de 93 páginas, aprovada em 19/08/2021 e publicada no DOU de 02/09/2021; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA315%28R2%29.pdf>).
- **Ref. 3** — CVM/RAD, DIRECIONAL ENGENHARIA S.A., Demonstrações Financeiras Padronizadas de 31/12/2025, V1, protocolo 021350DFP311220250100155189-71, enviado em 09/03/2026; seções DFs Consolidadas, Notas Explicativas, Pareceres e Declarações e Balanço Patrimonial Ativo; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3, perfil da companhia DIRECIONAL ENGENHARIA S.A., código CVM 21350, consulta em 22/10/2026; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — CVM Dados Abertos, DFP de companhias abertas 2025, arquivo dfp_cia_aberta_BPA_con_2025.csv, BP consolidado, unidade monetária em milhares de reais; [abrir fonte](<https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip>).
- **Ref. 6** — Direcional RI, Central de Resultados, consulta em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 7** — Direcional RI, Documentos Entregues à CVM, consulta em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/documentos-entregues-a-cvm/>).


---

# PT-320 — Materialidade no planejamento e na execução

## Identificação e escopo

| Campo | Registro |
|---|---|
| Código / título | **PT-320 — Materialidade no planejamento e na execução** |
| Entidade / demonstrações | DIRECIONAL ENGENHARIA S.A. — demonstrações contábeis **consolidadas** |
| Data-base / exercício | 31/12/2025; exercício encerrado nessa data |
| Finalidade | Papel de trabalho **didático**. Não é documentação do trabalho da PwC nem afirma que este preparador participou da auditoria independente. |
| Norma | NBC TA 320 (R1), *Materialidade no Planejamento e na Execução da Auditoria*. Texto oficial do CFC; resolução de 19/08/2016, publicada no DOU em 05/09/2016. O registro oficial consultado em 22/10/2026 identifica-a como vigente, não alterada e não revogada. Aplicação às auditorias de períodos findos em ou após 31/12/2016. [1] [2] |
| Itens normativos considerados | Itens 1–14, com foco nos itens 4–6 e 10–14; material de aplicação A1–A14, especialmente A3–A13. A norma estabelece julgamento profissional, não percentuais obrigatórios de benchmark. [2] |
| Preparador | Matrícula didática **EDU-AUD-001** |
| Data | **22/10/2026** |
| Revisão |  |

## Objetivo, contas e processo

Documentar, para planejamento didático, uma base ilustrativa de materialidade para as demonstrações consolidadas do exercício de 2025, identificar classes de saldos e divulgações que podem exigir atenção e indicar como a materialidade poderia orientar procedimentos posteriores. O objetivo da NBC TA 320 é aplicar o conceito de materialidade no planejamento e na execução da auditoria; o auditor determina materialidade para as demonstrações como um todo e materialidade para execução, avalia se são necessários níveis específicos para determinadas classes e revisa os valores quando informações novas o justificam. [2, itens 1, 4–6 e 10–14]

**Contas e processos no escopo de planejamento:** ativos totais consolidados como benchmark ilustrativo; estoques imobiliários, inclusive terrenos a incorporar; reconhecimento de receita imobiliária; provisões para contingências e respectivas divulgações. Os dois últimos temas aparecem como PAA no relatório público do auditor (DFP direta, pp.115–117); a classificação como PAA indica assunto de maior significância de auditoria, não distorção identificada ou opinião modificada. [6]

## Afirmações e riscos de distorção relevante

- **Estoques e terrenos a incorporar — existência, direitos e obrigações, integridade, avaliação e alocação, classificação e apresentação.** Os terrenos a incorporar são a maior rubrica individual divulgada dentro dos estoques. A dimensão relativa e o aumento em relação ao comparativo justificam priorização didática. Risco de avaliação, titularidade, classificação ou alocação é uma **hipótese de risco**, não uma constatação sobre a companhia. A informação pública por si só não evidencia problema de título, custo, recuperabilidade ou corte.
- **Reconhecimento de receita imobiliária — ocorrência, exatidão, corte, classificação e apresentação.** A receita imobiliária foi assunto de PAA no relatório do auditor. Estimativas e julgamentos relacionados ao reconhecimento são áreas de risco a avaliar no planejamento; não se infere erro, fraude ou inadequação do reconhecimento publicado. [3]
- **Provisões para contingências — integridade, avaliação, classificação e divulgação.** O tema também consta como PAA. Incerteza de estimativa, completude de processos e suficiência de divulgação são riscos potenciais para investigação. Não se afirma que existam contingências omitidas, provisões insuficientes ou litígios específicos. [3]
- **Apresentação e divulgação consolidadas.** Distorções qualitativas em divulgações podem ser relevantes mesmo quando inferiores a um limite quantitativo. A relevância de assuntos de receita e contingências para usuários deve ser considerada ao decidir se cabe materialidade específica ou qualitativamente mais baixa; não há informação interna suficiente para fixar aqui um limite específico. [2, itens 10 e A10–A12]

## População, fontes e critérios

**População de planejamento:** saldos, classes de transações e divulgações das demonstrações consolidadas da DFP de 31/12/2025, versão 1, incluindo comparativos de 2024. Não houve acesso à população contábil detalhada, razão auxiliar, razão geral, base de transações, relatórios de consolidação ou suportes de estimativas. A DFP pública foi obtida no RI e as páginas relevantes foram examinadas; o registro CVM informa protocolo 021350DFP311220250100155189-71, envio em 09/03/2026 e auditor PwC. [3] [6]

**Fontes públicas utilizadas:** registro CVM da DFP [3], PDF DFP 4T25 V1 obtido no RI [6], perfil econômico-financeiro da B3 [4], Central de Resultados do RI [5] e texto/cadastro oficial da NBC TA 320 (R1) no CFC [1] [2]. As páginas impressas verificadas são BP pp.16–17, DRE p.21, Nota 5 p.69 e relatório do auditor pp.115–117. A interface CVM é dinâmica e sem paginação impressa, mas isso não se aplica ao PDF direto do RI.

**Critério didático simulado, não percentual normativo:** usar **0,75% do ativo total consolidado** como materialidade ilustrativa para as demonstrações como um todo, **70% da materialidade geral** como materialidade para execução e, devido à concentração e natureza de Estoques, **0,50% do saldo total da rubrica Estoques** como nível específico ilustrativo. A escolha é pedagógica e conservadora para demonstrar julgamentos; a NBC TA 320 não prescreve esses percentuais. Em trabalho real, benchmark, porcentagens e níveis específicos exigiriam julgamento documentado, entendimento de usuários, desempenho, riscos e aprovação do responsável pelo trabalho. Os valores não são parâmetros da PwC nem da auditoria publicada. [2, itens 2, 5–6, 8–11 e A1–A3, A13]

## Procedimentos, resultados e evidências

### Realizados com evidência pública

1. **Identificação do documento-base e do auditor.** Consulta ao registro de DFP da CVM: demonstrações financeiras padronizadas de 31/12/2025, versão 1, protocolo indicado acima, envio em 09/03/2026; identificação de PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. **Resultado:** dados de identificação documental e auditoria externa observados na página pública. Isso não representa inspeção dos papéis da PwC nem reexecução de seus procedimentos. Referência cruzada: **PT-320.1 / CVM DFP**. [3]
2. **Leitura das divulgações públicas selecionadas.** Examinados o balanço consolidado, Nota 5 e o relatório do auditor na DFP integral pública: BP pp.16–17, Nota 5 p.69 e PAA/opinião pp.115–117. **Resultado:** os dados delimitam assuntos e áreas para planejamento, mas não permitem concluir sobre a suficiência da evidência obtida pela PwC, qualidade de estimativas ou ausência de distorções. Uma opinião sem ressalva não é evidência de que este PT tenha realizado testes. Referência cruzada: **PT-320.2 / DFP RI e registro CVM**. [3] [6]
3. **Corroboração pública do ativo total.** Comparado o ativo total consolidado de 31/12/2025 ao perfil econômico-financeiro da B3, que exibe R\$ 13.219.635 mil para a mesma data. **Resultado:** o total coincide com o fato-base da DFP usado neste PT. A consulta à B3 não foi confirmação externa solicitada pelo auditor; trata-se de leitura de informação divulgada publicamente. Referência cruzada: **PT-320.3 / perfil B3, Balanço Patrimonial — Consolidado**. [4]
4. **Recalculo analítico de indicadores a partir dos valores divulgados.** Em R\$ mil: estoques de R\$ 6.951.508 representam aproximadamente **52,6%** do ativo; terrenos a incorporar totais de R\$ 5.678.238 representam **43,0%** do ativo e **81,7%** dos estoques; estoques circulantes de R\$ 2.086.835 representam **15,8%** do ativo. O total de terrenos a incorporar aumentou R\$ 1.090.415 mil, cerca de **23,8%**, ante R\$ 4.587.823 mil em 2024; o ativo total aumentou cerca de **31,3%** ante R\$ 10.067.406 mil em 2024. O componente não circulante de terrenos era R\$ 4.864.673 mil em 2025 e R\$ 3.888.979 mil em 2024. Percentuais são cálculos deste PT sobre os saldos divulgados, arredondados a uma casa decimal; variação não constitui explicação causal nem evidência de erro. Referência cruzada: **PT-320.4 / DFP CVM, Balanço Patrimonial Ativo e Nota 5, saldos 2025 e 2024**. [3]
5. **Consulta normativa.** Conferida no CFC a identificação NBC TA 320 (R1), a data de publicação e o estado oficial da norma; consultado o texto integral para os requisitos e parágrafos acima. **Resultado:** versão aplicável ao período encerrado em 31/12/2025 é NBC TA 320 (R1), não uma norma posterior. Referência cruzada: **PT-320.5 / CFC**. [1] [2]

### Planejados por falta de acesso a evidência interna

Os procedimentos abaixo **não foram executados**. Exigem acesso à administração, documentos, sistemas ou instalações, indisponíveis para este trabalho didático. A avaliação de materialidade permanece provisória até que os riscos e informações do cliente sejam entendidos e documentados.

- Obter demonstrações e balancetes consolidados finais, reconciliações com os quadros da DFP, razão geral e composição analítica completa de estoques e terrenos; testar conciliações, consolidação e integridade da população.
- Para terrenos e estoque imobiliário, selecionar itens pela materialidade para execução e risco; inspecionar contratos de aquisição e registros de propriedade, documentação do empreendimento, movimentações e custos apropriáveis; avaliar corte e classificação; comparar premissas de recuperabilidade e orçamento com evidência de suporte; planejar inspeção física quando aplicável e pertinente. Nenhum desses documentos foi obtido e nenhuma inspeção física foi feita.
- Para receita imobiliária, obter contratos, cronogramas, bases de cálculo, documentação de progresso/entrega e lançamentos; testar amostras e corte em períodos próximos ao encerramento; testar premissas relevantes e conciliações com saldos e divulgações. Nenhum contrato ou registro interno foi inspecionado e nenhuma entrevista foi realizada.
- Para contingências, obter composição, movimentação, política de provisões e divulgações; planejar inspeção de documentação de suporte e comunicações pertinentes e procedimento de confirmação/consulta a assessores jurídicos conforme aplicável; avaliar premissas, classificação e divulgação. Não houve confirmação, consulta a advogado, inspeção documental interna ou entrevista.
- Obter as métricas financeiras usadas pela administração e a informação sobre usuários e covenants, bem como dados de desempenho, orçamento e previsões, para avaliar se ativo total é benchmark apropriado e se materialidade geral ou específica deve ser revista. Não se presume que exista covenant, restrição ou violação.
- Após execução, acumular distorções, avaliá-las individualmente e em conjunto, considerar aspectos qualitativos, discutir correções com a administração e revisar materialidade quando novas informações o justifiquem. A classificação dos procedimentos pendentes deve ser atualizada somente se evidência apropriada for realmente obtida. [2, itens 6, 10–14]

### Simulados para fins didáticos

1. **Materialidade geral ilustrativa:** R\$ 13.219.635 mil × 0,75% = **R\$ 99.147,26 mil**.
2. **Materialidade para execução ilustrativa:** R\$ 99.147,26 mil × 70% = **R\$ 69.403,08 mil**.
3. **Materialidade específica para Estoques:** R\$ 6.951.508 mil × 0,50% = **R\$ 34.757,54 mil**. O critério procura demonstrar atenção específica à maior rubrica de ativo; terrenos a incorporar, seu componente predominante, representam 81,7% dos estoques. Não foi adotado valor específico para receita ou contingências, embora sua natureza/PAA possa demandar julgamento qualitativo.
4. **Valor claramente trivial ilustrativo:** 5% da materialidade geral = **R\$ 4.957,36 mil**, apenas como premissa didática de acumulação de distorções.
5. **Aplicação ilustrativa:** os limites não são tolerâncias por conta, não substituem avaliação de risco e não demonstram que os saldos estejam incorretos. Os saldos elevados de estoques e terrenos orientariam a alocação de esforço, natureza, época e extensão dos testes, sem autorizar conclusão sobre avaliação ou existência.

Referência cruzada: **PT-320.6 / cálculo didático**, com insumos públicos referidos em PT-320.3 e PT-320.4 e conciliação de materialidade em `analysis/PT530_resultados.json`/`analysis/papel_amostragem_conciliacao.xlsx`. As estimativas dos limites são simuladas e não foram aprovadas por sócio ou pela administração.

## Conclusão, exceções e limitações

Para fins exclusivamente didáticos, os dados públicos apontam estoques — especialmente terrenos a incorporar — como uma concentração relevante do ativo consolidado e a DFP destaca reconhecimento de receita imobiliária e provisões para contingências como PAA. Esses elementos sustentam priorização preliminar e planejamento de procedimentos, não uma conclusão de auditoria sobre saldos ou divulgações.

Os limites de R\$99.147,26 mil, R\$69.403,08 mil, R\$34.757,54 mil e R\$4.957,36 mil são cenários simulados, não materialidade efetivamente estabelecida pela PwC ou por qualquer auditor. Benchmark e percentuais precisam ser reavaliados com informações de desempenho e usuários, perfil de risco, necessidade de níveis específicos e evidência interna. Não foram obtidos razão, papéis de consolidação, documentos de suporte, contratos, registros de propriedade, avaliações, cartas jurídicas ou confirmações. Não foram realizadas entrevista, confirmação, inspeção física, observação de controles ou procedimentos substantivos sobre a Companhia. Os saldos e divulgações selecionados foram lidos no PDF público; nenhum foi conciliado a registros internos. Portanto, este PT não oferece asseguração nem conclui sobre adequação das demonstrações ou suficiência do trabalho do auditor independente. Não foram observadas exceções de auditoria por não terem sido realizados testes substantivos; inexistência de exceção não deve ser inferida.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC. NBC TA de Auditoria Independente de Informação Contábil Histórica. Listagem oficial da NBC TA 320 R1 e data DOU, consulta em 22/10/2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC. NBC TA 320 R1 — Materialidade no Planejamento e na Execução da Auditoria. Texto oficial, 11 páginas, 2016; itens e aplicação citados no texto; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA320%28R1%29.pdf>).
- **Ref. 3** — CVM. DIRECIONAL ENGENHARIA S.A. Demonstrações Financeiras Padronizadas de 31/12/2025, versão 1, protocolo 021350DFP311220250100155189-71. Quadros consolidados, notas explicativas e relatório do auditor. Documento eletrônico sem paginação estável no visualizador consultado; exercício 2025, protocolo em 09/03/2026; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3. DIRECIONAL ENGENHARIA S.A. Perfil da companhia e dados econômico-financeiros; Balanço Patrimonial — Consolidado, 31/12/2025. Consulta em 22/10/2026; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — DIRECIONAL ENGENHARIA S.A. RI. Central de Resultados; repositório institucional de informações financeiras. Consulta em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 6** — RI Direcional, DFP 4T25 V1; BP pp.16–17, DRE p.21, Nota 5 p.69, PAA e relatório PwC pp.115–117; acesso em 22/10/2026; [abrir fonte](<https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2>).


---

# PT-330 — Respostas do auditor aos riscos avaliados

## Identificação e referência normativa

| Campo | Informação |
|---|---|
| Código / título | **PT-330 — Respostas do auditor aos riscos avaliados** |
| Entidade / período | DIRECIONAL ENGENHARIA S.A. — demonstrações contábeis consolidadas do exercício findo em 31/12/2025 |
| Natureza | Papel de trabalho didático, preparado com informações públicas identificadas e documentos da DFP efetivamente examinados. Não é arquivo de auditoria da PwC nem representa trabalho executado pela PwC. |
| Norma | **NBC TA 330 (R1), Resposta do Auditor aos Riscos Avaliados**, texto oficial do CFC vigente consultado em 22/10/2026. A versão R1 foi publicada no DOU em 05/09/2016; a página oficial do CFC registra que a norma permanece em vigor, foi alterada pela Revisão NBC 11 (DOU 02/09/2021) e não foi revogada. A redação aplicável deve ser lida com as alterações da Revisão NBC 11. [1] [2] |
| Itens da norma considerados | Objetivo e requisitos: itens 5–10 (respostas gerais, procedimentos adicionais, natureza/época/extensão), 11–17 (testes de controles, quando aplicáveis), 18–23 (procedimentos substantivos e respostas a riscos significativos), 24–27 (apresentação, suficiência de evidência e providências se insuficiente) e 28–30 (documentação e conciliação com registros). Aplicação pertinente: A1–A3, A4–A6, A7–A10, A11–A20, A21–A25, A26–A30, A35–A36, A59–A65, conforme o tema. [2] |
| Preparador | Matrícula didática **EDU-AUD-001** |
| Data | **22/10/2026** |
| Revisão |  |

## Objetivo, contas e processos

Documentar, para fins didáticos, respostas apropriadas a riscos de distorção relevante hipotéticos relacionados a estoques imobiliários — com ênfase em terrenos a incorporar —, reconhecimento de receita imobiliária e provisões para contingências nas demonstrações consolidadas de 31/12/2025. O escopo é ilustrativo: sem avaliação interna de risco, materialidade, controles, registros contábeis ou evidências de auditoria não públicas, este PT não conclui sobre a correção dos saldos nem substitui os papéis do auditor independente.

A base factual indicada para este exercício é a DFP CVM de 31/12/2025, V1, protocolo nº 021350DFP311220250100155189-71, enviada em 09/03/2026, e os dados societários e contábeis descritos adiante. O portal da CVM identifica o auditor independente como PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. O relatório público lido na DFP 4T25 V1 (pp. 115–117) registra opinião sem modificação e PAA sobre reconhecimento de receita imobiliária e provisões para contingências. Essas informações identificam o contexto do exercício; não são prova suficiente para validar os saldos nem atestam que os procedimentos deste PT foram executados. [3] [4]

## Afirmações e riscos a responder

Os saldos e comparativos abaixo são em **R\$ mil**, conforme os saldos publicados e lidos no PDF integral da DFP 4T25 V1 (BP pp. 16–17; Nota 5 p. 69). A B3 exibe ativo total consolidado de R\$ 13.219.635 mil em 31/12/2025. [4] A DFP apresenta estoques de R\$ 6.951.508 mil, dos quais terrenos a incorporar totalizam R\$ 5.678.238 mil, incluindo R\$ 4.864.673 mil não circulantes, e estoques circulantes de R\$ 2.086.835 mil. Para 31/12/2024, os comparativos são ativo total de R\$ 10.067.406 mil e terrenos a incorporar total de R\$ 4.587.823 mil, incluindo R\$ 3.888.979 mil não circulantes. O recálculo aritmético indica aumento de R\$ 1.090.415 mil (23,8%) no total de terrenos e de R\$ 3.152.229 mil (31,3%) no ativo total entre os períodos; terrenos a incorporar totais equivalem a cerca de 81,7% dos estoques de 2025 e 43,0% do ativo total de 2025. Esses quocientes são análises aritméticas dos valores públicos, não avaliação de materialidade nem conclusão sobre risco ou mensuração. [3] [4]

| Área / afirmação | Risco de distorção relevante considerado para desenho didático |
|---|---|
| Terrenos a incorporar e demais estoques — existência, direitos e obrigações, integridade, avaliação/alocação, corte, classificação e apresentação | **Hipótese/risco, não constatação:** possibilidade de terrenos registrados sem direitos comprovados, incompletude ou erro na base de custo, custo inelegível capitalizado, classificação inadequada entre circulante e não circulante, ou perda por valor realizável líquido não reconhecida. O crescimento comparativo e a concentração em terrenos justificam resposta específica, mas, isoladamente, não comprovam distorção. |
| Reconhecimento de receita imobiliária — ocorrência, integridade, exatidão, corte e apresentação; direitos e obrigações e mensuração de saldos contratuais quando aplicável | **Hipótese/risco, não constatação:** possibilidade de reconhecimento em período inadequado ou em desacordo com os termos dos contratos e com o progresso/critério contábil aplicável. A área consta como PAA no relatório público, o que indica foco de auditoria divulgado, não erro constatado. |
| Provisões para contingências e divulgações — integridade, existência/obrigação, avaliação e apresentação | **Hipótese/risco, não constatação:** possibilidade de processos ou obrigações não identificados, estimativas de perda/desembolso inadequadas ou divulgação incompleta. A área consta como PAA no relatório público, não sendo isso, por si só, evidência de insuficiência ou distorção. |
| Demonstrações consolidadas e divulgações — apresentação, classificação e integridade | **Hipótese/risco, não constatação:** possibilidade de informações do razão, sub-razões e divulgações não estarem conciliadas, ou de classificação/apresentação não refletir a estrutura contábil aplicável. A demonstração pública e a opinião sem ressalva informadas não substituem a avaliação de evidência exigida nos itens 24–27 da NBC TA 330. |

As afirmações e respostas são propostas para fins de planejamento didático. Não representam riscos formalmente avaliados pela equipe da auditoria de 2025. A natureza, época e extensão definitivas dos procedimentos dependeriam da avaliação de risco nos termos da NBC TA 315, da materialidade definida e da evidência obtida no trabalho real.

## População, fontes e critérios

**População pretendida para auditoria real:** razão e balancetes consolidados de estoques e receitas; cadastro integral de terrenos e empreendimentos; movimentações e composições de custo; contratos de aquisição de terrenos e contratos imobiliários; medições e bases de reconhecimento de receitas; relação integral de processos judiciais, fiscais e trabalhistas; cálculos e documentos de suporte das provisões; lançamentos de fechamento e divulgações da DFP. Não recebemos esses dados. Logo, população, integridade, quantidade de itens, unidade amostral e seleção de amostras **não foram verificadas** e nenhuma amostra real foi extraída.

**Fontes efetivamente consultadas:** CFC para o texto e situação da norma; portal RAD/CVM para a página da DFP identificada e o campo do auditor; B3 para dados públicos do emissor e balanço consolidado; RI da companhia como rota oficial da Central de Resultados. A interface CVM e o índice do RI são dinâmicos e não oferecem paginação impressa estável. O PDF integral da DFP 4T25 V1 foi obtido diretamente no RI e lido neste PT: BP pp. 16–17, DRE p. 21, Nota 5 p. 69 e relatório PwC pp. 115–117 (fonte S2 em FONTES.md). Metadados do protocolo são referenciados à tela CVM, sem atribuição de página HTML. [3] [5]

**Critérios e parâmetros:** NBC TA 330 (R1), conforme alterada pela Revisão NBC 11, particularmente itens 5–10, 18–27 e 28–30; condições contratuais e políticas contábeis que seriam obtidas em auditoria real; base contábil e demonstrações divulgadas. Não se atribuem aqui critérios específicos de reconhecimento contábil, taxa, margem, materialidade, tolerância ou premissa de estimativa não disponíveis nas fontes consultadas. Amostragem, materialidade e seleção seriam definidas após obter os registros e avaliar os riscos; este PT não inventa tais parâmetros.

## Procedimentos e classificação de execução

| ID / classificação | Procedimento e objetivo | Resultado/evidência disponível |
|---|---|---|
| P01 — **Realizado com evidência pública** | Consultar a página normativa oficial do CFC e o texto da NBC TA 330 (R1), incluindo situação, histórico de revisão, data de publicação e requisitos para respostas aos riscos e documentação. | O CFC apresenta NBC TA 330 (R1), DOU 05/09/2016, em vigor, alterada pela Revisão NBC 11 e não revogada; a revisão 11 consta publicada em 02/09/2021. Referência normativa confirmada. Não é teste de controle ou de saldo da companhia. [1] [2] |
| P02 — **Realizado com evidência pública, limitado à identificação** | Consultar a página RAD/CVM da DFP informada para identificar documento/período, versão e auditor constante do registro. | A página identifica a DFP como “Demonstrações Financeiras Padronizadas – 31/12/2025 – V1”, o protocolo nº 021350DFP311220250100155189-71 e PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. A tela CVM registra a data de envio de 09/03/2026. Não houve obtenção de confirmação do auditor, contato com a entidade ou inspeção de arquivo-fonte interno. [3] |
| P03 — **Realizado com evidência pública** | Consultar a ficha da B3 para corroborar identidade do emissor, companhia listada e o ativo total consolidado de 31/12/2025 publicado no painel. | A ficha identifica DIRECIONAL ENGENHARIA S.A., código CVM 21350 e negociação DIRR3; seu painel mostra ativo total consolidado de R\$ 13.219.635 mil em 31/12/2025. É corroboração pública do total apresentado no painel, não conciliação com razão ou prova do saldo de estoque. [4] |
| P04 — **Realizado como recálculo aritmético limitado; inputs lidos no PDF direto da DFP** | Recalcular soma do total de estoques informado, variações comparativas e proporções do total de terrenos a incorporar. | R\$ 5.678.238 mil é o total de terrenos a incorporar na Nota 5; seu componente não circulante de R\$ 4.864.673 mil não deve ser somado ao total de estoques circulantes para representar a classe total. Aumento do total de terrenos = R\$ 1.090.415 mil (aprox. 23,8%); alta do ativo total = R\$ 3.152.229 mil (aprox. 31,3%); terrenos/estoques = aprox. 81,7%; terrenos/ativo total = aprox. 43,0%. Cálculo analítico sobre números públicos; não houve reconciliação independente a razão ou documentação de suporte. [3] [4] |
| P05 — **Planejado por falta de acesso** | Obter balancete/razão, conciliar estoque total e suas classes aos demonstrativos consolidados e notas; testar a integridade dos relatórios usados na conciliação e rastrear lançamentos relevantes de fechamento. | Não executado: razão, balancetes, relatórios auxiliares e documentação de consolidação não foram disponibilizados. Resposta proposta aos itens 18, 20 e 30 da NBC TA 330. |
| P06 — **Planejado por falta de acesso** | Para seleção baseada em população validada, inspecionar contratos de aquisição de terrenos, registros de titularidade, pagamentos, aprovações e documentos de custo; verificar existência/direitos, completude, corte e elegibilidade dos custos; considerar confirmação independente de titularidade quando apropriada. | Não executado: nenhum contrato, matrícula, pagamento ou confirmação foi obtido. Nenhuma inspeção física foi realizada. Quantidade e seleção de itens ficam pendentes do cadastro integral e critérios de materialidade/risco. |
| P07 — **Planejado por falta de acesso** | Examinar composição do custo de terrenos e empreendimentos, apropriações e alocações; confrontar premissas e custos incorridos com evidência de suporte; avaliar indícios de perda e comparar custo ao valor realizável líquido com premissas suportadas. | Não executado: sem composição, orçamento, evidência de venda, estimativa ou relatório de avaliação; não se conclui sobre recuperabilidade ou adequação dos valores. Resposta proposta a risco hipotético de avaliação. |
| P08 — **Planejado por falta de acesso** | Selecionar contratos imobiliários e transações de receita; ler termos relevantes e confrontar amostra de vendas, recebimentos, medições/avanço e registros de receita com o critério contábil aplicável; executar testes de corte antes e depois de 31/12/2025 e reconciliar bases de contrato a razão. | Não executado: nenhum contrato, medição, recebimento, lançamento ou teste de corte foi inspecionado. Resposta planejada ao risco hipotético e à área identificada como PAA no relatório público, em coerência com itens 6–7 e 18–21. |
| P09 — **Planejado por falta de acesso** | Obter relação completa de processos e cartas dos assessores jurídicos; reconciliar a população a consultas/controles internos e examinar casos relevantes, avaliação de probabilidade, estimativa, eventos posteriores e adequação de apresentação/divulgação. | Não executado: não houve entrevistas, confirmações de advogados, consulta interna, acesso a processos ou avaliação de provisão. Resposta planejada à área de PAA descrita no relatório público; não se conclui sobre completude, mensuração ou divulgação. |
| P10 — **Planejado por falta de acesso** | Avaliar controles relevantes e, somente se apropriado e planejada confiança, testar desenho/implementação e efetividade operacional durante o período; mapear controles indiretos e desvios. Caso não se planeje confiança ou não haja evidência adequada, responder substantivamente. | Não executado: sem walkthroughs, observação, inspeção de controles ou testes. Não se presume eficácia ou falha de controles e não se transfere evidência de auditoria anterior. Resposta compatível com itens 8–17. |
| P11 — **Planejado por falta de acesso** | Executar revisão de lançamentos relevantes de diário e ajustes de encerramento, conciliar informações divulgadas com razão e sub-razões e verificar apresentação/classificação das demonstrações e divulgações. | Não executado: sem razão, arquivo de lançamentos ou suporte de divulgação. Planejado conforme itens 20, 24 e 30. |
| P12 — **Simulado para fins didáticos — não executado** | Em um caso de treinamento com conjunto de dados disponibilizado, demonstrar como seriam documentados seleção de itens por risco, rastreamento de afirmações, evidência obtida, exceções, avaliação de causa/efeito e eventual ampliação de testes. | Nenhuma população ou resultado simulado foi criado, observado ou tratado como evidência. Este item é apenas orientação de desenho para treinamento; não produz conclusão nem substitui os procedimentos P05–P11. |

Os procedimentos P05–P11 são propostas, não atividades em andamento ou já realizadas. A NBC TA 330 exige que a natureza, época e extensão das respostas sejam adequadas aos riscos efetivamente avaliados. Procedimentos analíticos sobre valores publicados e a existência de opinião sem ressalva não bastam para sustentar uma conclusão sobre existência, direitos, mensuração, corte ou completude. Se evidência apropriada e suficiente não fosse obtida após tentativas adicionais em auditoria real, seria necessário avaliar o efeito na opinião, conforme item 27. [2]

## Evidências e referências cruzadas

| Ref. | Evidência / documento | Uso e limitação |
|---|---|---|
| E1 | CFC, página “NBC TA – de Auditoria Independente de Informação Contábil Histórica”, versão consultada em 22/10/2026. [1] | Índice oficial confirma identificação e situação da NBC TA 330 (R1), publicação no DOU em 05/09/2016, e vínculo com Revisão NBC 11. |
| E2 | CFC, **NBC TA 330 (R1) — Resposta do Auditor aos Riscos Avaliados**, texto oficial PDF, resolução 2016/NBCTA330(R1), incluindo alterações atribuídas à Revisão NBC 11. [2] | Critérios normativos deste PT. A página aplicável do texto oficial deve ser lida no PDF; não são citadas páginas impressas aqui, pois o arquivo eletrônico contém quebras/variações de paginação e a referência por item normativo é inequívoca. |
| E3 | CVM/RAD, **Demonstrações Financeiras Padronizadas (DFP), DIRECIONAL ENGENHARIA S.A., data-base 31/12/2025, versão 1**, protocolo 021350DFP311220250100155189-71, envio informado em 09/03/2026; campos “DFs Consolidadas”, “Notas Explicativas” e “Relatório da Administração/Comentário do Desempenho”; auditor PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. [3] | Identificação da DFP/auditor e referência do caso-base para valores, PAA e opinião. A interface CVM não oferece paginação impressa; os saldos e PAA foram conferidos no PDF direto da DFP 4T25 V1, BP pp. 16–17, Nota 5 p. 69 e relatório pp. 115–117 (S2 em FONTES.md). |
| E4 | B3, página da companhia **DIRECIONAL ENGENHARIA S.A.**, seção “Dados da Companhia” e tabela “Balanço Patrimonial – Consolidado”, coluna 31/12/2025; consulta em 22/10/2026. [4] | Corrobora identidade do emissor e ativo total consolidado de R\$ 13.219.635 mil. A tabela de visão geral não constitui suporte detalhado de estoques ou papéis de titularidade. |
| E5 | RI Direcional, **Central de Resultados**, rota oficial de Informações Financeiras, consultada em 22/10/2026. [5] | Rota oficial de consulta ao arquivo anual. O PDF integral da DFP 4T25 V1 foi obtido diretamente no RI; BP pp. 16–17, Nota 5 p. 69 e relatório pp. 115–117. A Central de Resultados é a rota institucional de localização. |

**Referências cruzadas internas:** E1–E2 → P01 e critério normativo; E3 → P02, P04 e contexto; E4 → P03–P04; E5 → rota de fonte, sem evidência de saldo; P05–P11 → pendentes de evidência interna; P12 → simulação não executada. Nenhuma confirmação externa, entrevista, inspeção física, walkthrough, teste de controle, teste substantivo ou procedimento sobre documentação interna foi executado neste PT.

## Resultados, exceções, conclusão e limitações

**Resultados públicos e recálculos:** a consulta ao painel público da B3 corroborou o ativo total consolidado de 31/12/2025 de R\$ 13.219.635 mil. O recálculo dos valores públicos da DFP é aritmeticamente consistente quanto à soma dos dois componentes de estoques informados e às variações/proporções apresentadas em P04. A página da CVM identificou DFP V1 e auditor PwC. O exercício toma como fatos-base, sem validação independente da página do documento, os saldos detalhados, os PAA e a opinião sem ressalva indicados na seção de identificação. [3] [4]

**Exceções:** não foram identificadas exceções de auditoria, pois não foram executados testes sobre registros e transações. A leitura da DFP pública direta confirmou a apresentação dos estoques, a composição dos terrenos, os PAA e a opinião nas páginas impressas citadas; a falta de acesso a registros internos e papéis de suporte impede atestar saldos ou reexecutar procedimentos. A ausência de evidência neste exercício não é inferência de erro, fraude, deficiência de controle ou omissão da companhia.

**Conclusão do papel:** como exercício didático, as respostas propostas são direcionadas aos riscos hipotéticos de existência/direitos, avaliação e corte de estoques, reconhecimento de receita, provisões e apresentação/divulgação. A evidência pública examinada é limitada a identificação e informação agregada; não é apropriada nem suficiente para concluir sobre as afirmações relevantes. Portanto, este PT **não expressa opinião de auditoria, não afirma que os saldos estão corretos e não replica nem valida a opinião sem ressalva atribuída ao auditor independente**. Em auditoria real, os procedimentos planejados, eventuais procedimentos adicionais e a avaliação do efeito de limitações seriam necessários antes de qualquer conclusão. [2]

**Limitações:** não houve acesso a razão, sub-razões, contratos, registros de terrenos, comprovantes, relatórios de vendas ou progresso de obras, cadastro de processos, assessores jurídicos, controles, correspondência, atas, cálculos, auditoria do grupo ou papéis de trabalho do auditor. Não houve confirmação, entrevista, observação, inspeção física, teste ou contato com a companhia, CVM, B3, PwC, cartórios, clientes, bancos ou advogados. A interface da CVM e o índice do RI não oferecem paginação impressa estável; o PDF direto da DFP foi obtido e as páginas impressas pertinentes são citadas. Não houve acesso a registros internos nem aos papéis privados do auditor. Fatores sem suporte documental são apresentados apenas como hipóteses/risco.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC — NBC TA de Auditoria Independente de Informação Contábil Histórica; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC — NBC TA 330 R1, Resposta do Auditor aos Riscos Avaliados, PDF oficial; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA330%28R1%29.pdf>).
- **Ref. 3** — CVM RAD — DFP Direcional Engenharia 31/12/2025 V1, protocolo 021350DFP311220250100155189-71; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3 — DIRECIONAL ENGENHARIA S.A., perfil e dados consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — RI Direcional — Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-402 — Organização prestadora de serviços

## Identificação do papel de trabalho

| Campo | Informação |
|---|---|
| Código / título | **PT-402 — Considerações de auditoria para entidade que utiliza organização prestadora de serviços** |
| Norma | **NBC TA 402**, Resolução CFC nº 1.215/09; vigente e não revogada, com alterações. O texto oficial da resolução assinala alterações da **Revisão NBC11**; o cadastro CFC identifica também a **Revisão NBC20**, publicada no DOU em 06/12/2023, entre as alterações. Referência para o exercício iniciado em 01/01/2025: NBC TA 402 conforme alterações oficiais identificadas, itens 1–22 e aplicação A1–A44. [1] [2] [3] [7] [8] |
| Entidade / demonstrações | DIRECIONAL ENGENHARIA S.A. — demonstrações contábeis **consolidadas** para o exercício findo em **31/12/2025** |
| Natureza do trabalho | **Didático**. Este documento não é papel de trabalho de auditoria real, não pertence à PwC e não expressa asseguração ou opinião sobre as demonstrações. |
| Data de acesso e preparação | **22/10/2026** |
| Preparador | Matrícula didática **EDU-AUD-001** |
| Revisor |  |

## Objetivo, conta e processo

Avaliar, para fins didáticos, como a auditoria do grupo deveria identificar e responder ao uso de organização(ões) prestadora(s) de serviços quando os serviços e controles associados integram o sistema de informações ou processos de negócio relevantes para preparar as demonstrações consolidadas. O objetivo normativo é entender natureza e importância dos serviços e seus efeitos sobre o controle interno relevante, identificar e avaliar riscos de distorção relevante e planejar procedimentos adicionais que respondam a esses riscos (NBC TA 402, itens 1, 3–4 e 7; publicação oficial do CFC, pp. 254–256). [3]

**Área foco para escopo didático:** estoques imobiliários, com ênfase em terrenos a incorporar, incluindo processos e registros que possam afetar reconhecimento, mensuração, classificação, consolidação e divulgação. A análise também considera, apenas se houver serviço terceirizado relevante confirmado, interfaces com reconhecimento de receita imobiliária e provisões para contingências, temas mencionados como principais assuntos de auditoria (PAA) no caso-base. Não se presume que qualquer desses processos tenha sido terceirizado.

A NBC TA 402 trata dos serviços terceirizados que façam parte do sistema de informações/processos relevantes da entidade usuária; a mera contratação de fornecedor ou uso de serviço externo não demonstra, por si só, incidência da norma. A natureza e extensão do trabalho dependem da importância e relevância do serviço (itens 3–5). [3]

## Dados públicos de contexto e ressalvas de atribuição

A identificação da DFP no sistema CVM é **Demonstrações Financeiras Padronizadas — 31/12/2025 — V1**, documento datado de 31/12/2025, enviado em **09/03/2026 às 18:29:30**, protocolo **021350DFP311220250100155189-71**. O cadastro indica **PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA** como auditor. [4]

A DFP pública integral foi obtida diretamente no RI e as páginas impressas pertinentes foram examinadas. Os saldos abaixo foram localizados no BP (pp. 16–17), na Nota 5 (p. 69) e no relatório do auditor (pp. 115–117), fonte S2 em FONTES.md: ativo consolidado de **R\$ 13.219.635 mil** em 31/12/2025; estoques de **R\$ 6.951.508 mil**, dos quais terrenos a incorporar totalizam **R\$ 5.678.238 mil**, incluindo **R\$ 4.864.673 mil** no não circulante, e estoques circulantes de **R\$ 2.086.835 mil**; comparativos de ativo total de **R\$ 10.067.406 mil** e terrenos a incorporar totais de **R\$ 4.587.823 mil** em 2024, incluindo **R\$ 3.888.979 mil** no não circulante; PAA de reconhecimento de receita imobiliária e provisões para contingências; opinião sem ressalva. Os valores detalhados de estoques, os PAA e a conclusão do relatório são tratados neste PT como dados públicos atribuídos à DFP; a DFP integral pública foi obtida e as páginas relevantes examinadas, embora a interface CVM não forneça paginação estável. [4] [5]

A página da B3 identifica DIRECIONAL ENGENHARIA S.A., código CVM 21350, ticker DIRR3 e atividade principal de incorporação, construção e comercialização de imóveis. Sua tabela de dados econômico-financeiros consolidados exibe ativo total de R\$ 13.219.635 mil em 31/12/2025 e R\$ 10.067.406 mil em 31/12/2024. [5] A descrição de atividade e a dimensão do saldo, isoladamente, não provam utilização de organização prestadora de serviços nem deficiência de controles.

Como cálculos de contexto sobre os saldos publicados na DFP (não materialidade ou teste de auditoria): estoques representam aproximadamente **52,58%** do ativo consolidado; terrenos a incorporar totais, **81,68%** dos estoques e **42,96%** do ativo; estoques circulantes, aproximadamente **15,79%** do ativo. O ativo cresceu aproximadamente **31,31%** entre os comparativos e terrenos a incorporar totais, aproximadamente **23,77%**. O cálculo usa o total da classe da Nota 5, não apenas seu componente não circulante. Os cálculos indicam concentração e magnitude para direcionar o planejamento didático; não são conclusão de risco ou distorção.

## Afirmações e riscos considerados

As afirmações potencialmente relevantes para estoques e terrenos são **existência**, **direitos e obrigações**, **integridade**, **exatidão**, **avaliação e alocação**, **corte**, **classificação** e **apresentação/divulgação**. A relevância concreta deve ser determinada depois de entender o processo, os saldos e os controles — não foi estabelecida por inspeção ou teste neste trabalho didático.

| Processo/afirmações | Hipótese de risco a investigar — não constatada | Relação possível com a NBC TA 402 |
|---|---|---|
| Cadastro, aquisição e manutenção dos registros de terrenos; existência, direitos, integridade, corte, avaliação/classificação | Se um prestador externo processar cadastros, documentos, custos ou dados de terrenos, interface incompleta entre registros do prestador e razão/consolidação poderia, em tese, causar saldo incompleto, duplicado, incorretamente classificado ou mensurado. **Não há constatação de terceirização ou falha.** | Confirmar natureza, materialidade, interação, termos do serviço e controles de interface (itens 9–14). |
| Apuração e alocação de custos de estoque de empreendimentos; avaliação e alocação | Se dados de custos, progresso, orçamento ou relatórios técnicos forem hospedados/processados por organização externa, informação incompleta ou incorreta pode, em tese, afetar custo do estoque e estimativas. **Hipótese apenas.** | Entender transações, registros, controles do prestador e controles complementares da usuária; obter evidência suficiente nas afirmações relevantes (itens 9–17). |
| Sistemas de TI, hospedagem, processamento de dados e contabilidade do grupo; integridade, exatidão, corte e divulgação | Dependência de aplicação/ambiente terceirizado ou serviço de escrituração é uma possibilidade a identificar, não fato conhecido. Falhas potenciais de acesso, interfaces, alterações ou processamento podem afetar dados contábeis se o serviço existir e for relevante. | Identificar serviços relevantes no sistema de informações, controles relevantes e responsabilidades entre grupo e prestador (itens 3, 9–14). |
| Reconhecimento de receita imobiliária; ocorrência, exatidão, corte, classificação e divulgação | Caso exista prestador que processe vendas, medições, recebimentos ou dados contratuais, dados/processamento inadequados poderiam, em tese, afetar reconhecimento e divulgação. O fato de receita ser PAA não demonstra terceirização nem falha. | Mapear interfaces e avaliar controles e evidência do prestador apenas se a relação e relevância forem confirmadas. |
| Provisões para contingências; integridade, avaliação e divulgação | Se houver serviço externo de gestão de casos/documentos ou processamento jurídico-financeiro relevante, omissões ou atraso de dados poderiam, em tese, afetar estimativas/divulgação. O fato de contingências serem PAA não prova uso de prestador. | Determinar se os serviços integram processo de relatórios financeiros e obter evidência apropriada sobre controles/dados relevantes. |
| Consolidação do grupo e transferências de dados entre entidades | Se um prestador processar consolidações, dados e eliminações, erro de interface ou escopo incompleto poderia, em tese, afetar saldos consolidados e divulgação. Nenhum prestador ou erro foi identificado publicamente neste PT. | Avaliar entidade usuária, componente/processo, serviço, controles da usuária e subcontratações relevantes; a NBC TA 402 não substitui outros procedimentos de auditoria de grupo. |

## População, fontes e critérios

**População planejada:** serviços usados por DIRECIONAL ENGENHARIA S.A. e entidades consolidadas, no período de 01/01/2025 a 31/12/2025, que possam integrar o sistema de informações ou afetar transações, saldos, estimativas, divulgações, TI ou consolidação. Exemplos de categorias a pesquisar — **não identificadas como serviços efetivamente contratados** — são processamento/contabilidade, sistemas e hospedagem, folha/pagamentos, gestão de dados de contratos ou custos e processamento de informação para consolidação.

**Completude da população:** não obtida. Não há neste PT relação de entidades consolidadas, cadastro de fornecedores/serviços, contratos, relatório de sistemas, mapas de fluxo, nem lista de prestadores ou subcontratados. Não foram definidos tamanho da população, seleção de amostra ou período de cobertura de relatório de controles; isso requer acesso interno.

**Fontes públicas consultadas:** cadastro e texto oficial do CFC para a NBC TA 402; registro CVM para metadados da DFP; perfil B3; Central de Resultados do RI e PDF integral DFP 4T25 V1 obtido diretamente no RI. Foram examinados o BP (pp.16–17), Nota 5 (p.69) e relatório do auditor (pp.115–117). A interface CVM/RI é dinâmica e não tem paginação estável, mas o PDF direto fornece páginas impressas identificáveis. [1]–[6] [10]

**Critérios normativos e de execução:** NBC TA 402, itens 1–22 e aplicação A1–A44, lida com NBC TA 315 e NBC TA 330 conforme citado pela própria norma; a evidência deve ser apropriada e suficiente para as afirmações relevantes. Requisitos especialmente pertinentes: entendimento de natureza/importância/materialidade/interação/termos (itens 9–11); obtenção de entendimento por Relatório Tipo 1 ou 2, informação da organização, visita ou outro auditor se necessário (item 12); avaliação do desenho, implementação, controles complementares e adequação do relatório (itens 13–14); procedimentos adicionais e evidência de eficácia operacional quando o auditor pretende confiar em controles (itens 15–17); consideração de subcontratados (item 18); indagação sobre fraude, descumprimento legal ou distorções não corrigidas comunicadas (item 19); e consequências de limitação de evidência e referência no relatório (itens 20–22). [3]

## Procedimentos e classificação

**Legenda:** “Realizado com evidência pública” significa apenas que foi feita consulta documental pública indicada na referência, não auditoria dos controles internos ou confirmação externa. “Planejado — falta de acesso” não foi executado. “Simulado para fins didáticos” usa dados-base e análise hipotética para ilustrar o planejamento, sem constituir evidência de auditoria.

| Ref. | Procedimento | Classificação | Evidência/resultado e limite |
|---|---|---|---|
| PT402-01 | Consultar o catálogo e o cadastro oficial CFC para identificar a NBC TA 402, resolução de origem, status vigente/não revogada e alterações registradas; consultar o texto oficial para escopo, objetivos, requisitos e intervalos de itens. | **Realizado com evidência pública** | O CFC identifica NBC TA 402 como Resolução 1.215/09, em vigor, alterada e não revogada; indica a Revisão NBC20 de 2023 entre as alterações. A resolução original estabelece aplicação desde períodos iniciados em/apos 01/01/2010. As referências normativas detalhadas constam abaixo. Isso valida identificação e status público, não substitui leitura/controle de cópia da redação consolidada por equipe de auditoria real. [1] [2] [3] |
| PT402-02 | Consultar o registro CVM da DFP para confirmar entidade, tipo/versão, protocolo, data de envio e auditor listado. | **Realizado com evidência pública** | O registro informa Direcional Engenharia S.A., DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71, envio em 09/03/2026 18:29:30 e PwC. Consulta de cadastro, não confirmação independente com o auditor, não revisão dos papéis de auditoria e não inspeção de controles. [4] |
| PT402-03 | Consultar perfil e demonstração consolidada resumida da companhia na B3; corroborar identidade/listagem e ativo total comparativo. | **Realizado com evidência pública** | A B3 identifica a companhia, ticker/código CVM e atividade principal; exibe ativo consolidado de R\$ 13.219.635 mil em 31/12/2025 e R\$ 10.067.406 mil em 31/12/2024. A página não demonstra uso de prestador, nem corrobora saldos detalhados de estoques ou efetividade de controles. [5] |
| PT402-04 | Ler a DFP integral pública e identificar estoques, terrenos, saldos circulantes, PAA e opinião, registrando as páginas impressas. | **Realizado com evidência pública** | O PDF direto do RI [10] apresenta ativos consolidados pp.16–17; Nota 5 p.69; relatório do auditor/PAA pp.115–117. O exame sustenta somente o que foi publicado; não reconcilia ao razão nem testa contratos, controles ou documentação privada. |
| PT402-05 | Obter mapa completo de serviços/prestadores/subcontratados por entidade consolidada e processo, período, sistema, transação, conta, volume e materialidade; reconciliar com contratos, razão de fornecedores, compras e cadastro de TI. | **Planejado — falta de acesso** | Não acessados cadastro, contratos, razão, políticas ou inventário interno. Necessário para estabelecer se há organização prestadora de serviços relevante e para completar população. Nenhum prestador identificado. |
| PT402-06 | Entender e documentar fluxos entre grupo e cada prestador potencial: sistemas, dados de entrada/saída, lançamentos, reconciliações, tratamento de exceções, responsabilidades e controles complementares da usuária; avaliar desenho e implementação. | **Planejado — falta de acesso** | Não realizados walkthroughs, observação de fluxo, inspeção de sistema ou avaliação de controle. Entrevistas e walkthroughs seriam procedimentos futuros, nunca evidência obtida neste PT. Base normativa: itens 9–14. |
| PT402-07 | Para prestador relevante, solicitar relatório Tipo 1 ou Tipo 2 aplicável; conferir escopo, período, serviços, subcontratados, opinião, qualificação/independência do auditor da prestadora, testes, exceções e controles complementares; avaliar adequação e cobertura. | **Planejado — falta de acesso** | Nenhum relatório Tipo 1/2 foi obtido ou inspecionado. Se não disponível/suficiente, aplicar alternativas previstas no item 12: solicitar informação específica por meio da entidade, planejar visita/procedimentos no prestador ou usar outro auditor. Nenhum contato ou visita foi feito. |
| PT402-08 | Se a estratégia considerar confiar em controles do prestador, testar sua eficácia operacional via Relatório Tipo 2 apropriado, teste próprio ou outro auditor; avaliar período, exceções e controles complementares implementados e testar os controles da usuária relevantes. | **Planejado — falta de acesso** | Não foram executados testes de controles no prestador ou na companhia; não se conclui sobre eficácia. A estratégia e extensão dependem da avaliação de risco e evidência (itens 16–17). |
| PT402-09 | Obter e avaliar evidência substantiva para saldos/afirmações afetados no razão e registros da usuária; por exemplo, reconciliar extratos de prestador à contabilidade, testar dados/lançamentos e documentos de suporte selecionados, custos e corte, títulos/ônus conforme apropriado. | **Planejado — falta de acesso** | Não obtidos razão, suportes de aquisição, relatórios de custos, documentos de propriedade, confirmação, amostras ou evidência externa. São procedimentos propostos sob resposta de auditoria apropriada, não testes executados. Base geral NBC TA 402, itens 15–17; extensão depende da natureza do serviço e risco. |
| PT402-10 | Indagar administração sobre fraude, não conformidade com leis/regulamentos e distorções não corrigidas comunicadas por prestadores, e avaliar implicações para procedimentos/conclusão. | **Planejado — falta de acesso** | Nenhuma indagação ou entrevista realizada; nenhuma conclusão quanto a fraude, descumprimento ou distorções. O requisito consta do item 19. |
| PT402-11 | Recalcular percentuais e variações dos saldos publicados para orientar foco didático. | **Realizado com evidência pública** | Aritmética reproduzível sobre os valores da DFP examinados em “Dados públicos de contexto”; não estabelece materialidade, erro, risco inerente ou risco de controle e não rastreia a registros internos. [10] |
| PT402-12 | Avaliar uso de prestadores em receita imobiliária e contingências por causa da relevância indicada nos PAA do relatório público. | **Simulado para fins didáticos** | Os PAA elevam a prioridade para perguntar se algum serviço externo integra os processos; são exclusivamente gatilho de planejamento hipotético. Não permitem concluir terceirização, falha ou impacto de prestador. |

## Evidências e referências cruzadas

| Ref. | Evidência / referência | Uso neste PT |
|---|---|---|
| E-01 / N-01 | Página CFC “NBC TA – de Auditoria Independente de Informação Contábil Histórica”; lista NBC TA 402, Resolução 1.215/09 e status/alteração. [1] | Identificação da norma e caminho oficial para texto e alterações. |
| E-02 / N-02 | Cadastro oficial CFC da Resolução **2009/001215**, publicada em 03/12/2009: em vigor, alterada, não revogada; indica Revisão NBC20 publicada em 06/12/2023. [2] | Status normativo consultado à data deste papel. |
| E-03 / N-03 | CFC, *Resolução CFC nº 1.215/09 — NBC TA 402*, texto oficial em PDF, para redação e requisitos. A paginação citada corresponde à publicação eletrônica CFC *NBC TA 200 a 810*: índice da norma na p. 252; escopo/itens 1–8 nas pp. 254–256; itens 9–14 nas pp. 257–258; itens 15–19 nas pp. 258–259; itens 20–22 e aplicação A1–A44 a partir da p. 259, com seção até p. 277. [3] [9] | Referência cruzada a parágrafos e páginas normativas; os requisitos aplicados constam do texto do PT. |
| E-04 / C-01 | CVM, DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71, envio 09/03/2026; auditor listado PwC. Página web sem paginação impressa. [4] | Identificação e metadados do documento; conteúdo detalhado é referenciado no PDF direto abaixo. |
| E-05 / C-02 | B3, perfil Direcional Engenharia S.A., DIRR3, código CVM 21350; tabela “Balanço Patrimonial — Consolidado”, colunas 31/12/2025 e 31/12/2024. [5] | Identificação societária pública e ativo consolidado comparativo. |
| E-06 / C-03 | RI Direcional, Central de Resultados, como índice institucional sem paginação. [6] | Localizador da documentação societária pública; não é usado sozinho como prova dos valores. |
| E-07 / C-04 | RI Direcional, DFP 4T25 V1, PDF direto [10]; BP pp.16–17, Nota 5 p.69, relatório PwC pp.115–117. | Evidência pública para os saldos/notas efetivamente lidos; não substitui registros subjacentes ou papéis de auditoria. |

## Resultados, exceções, conclusão e limitações

**Resultado dos procedimentos públicos:** foi confirmada a identificação oficial da NBC TA 402 e o status publicado da Resolução CFC 1.215/09; o texto normativo consultado assinala Revisão NBC11 e o cadastro oficial identifica Revisão NBC20. O registro CVM confirma identificação/envio da DFP V1 e auditor listado; a B3 confirma identidade e ativos consolidados. O PDF direto do RI [10] foi lido nas páginas impressas indicadas e sustenta os saldos/notas públicos selecionados; não houve rastreamento a razão ou contratos.

**Exceções:** nenhuma exceção de auditoria ou deficiência de controle foi identificada, pois não houve acesso aos registros e controles nem teste de auditoria. A falta de identificação pública de um prestador **não** é evidência de que não exista. Também não foram obtidos relatórios Tipo 1/2, contratos, lista de serviços, controles complementares ou informação sobre subcontratação. Portanto, permanece indeterminado se e quais serviços prestados por terceiros são relevantes nos termos da NBC TA 402.

**Conclusão didática:** a concentração informada de estoques e terrenos a incorporar torna esses saldos candidatos a foco de planejamento; os PAA fornecidos justificam incluir receita e contingências na investigação de possíveis interfaces terceirizadas. A evidência pública aqui documentada, por si só, **não permite concluir** se o grupo utilizou organizações prestadoras de serviços relevantes, se os controles dessas organizações foram adequadamente desenhados/implementados/operaram eficazmente, ou se existe evidência suficiente para afirmações afetadas. A conclusão de auditoria sobre essas matérias fica **pendente** da execução dos procedimentos planejados e da obtenção de evidência suficiente e apropriada.

A opinião sem modificação lida no relatório público da DFP, não conclusão deste PT e não prova de que a equipe deste exercício executou testes da NBC TA 402. Este papel não reproduz nem reavalia a opinião do auditor independente. Não foram realizadas **confirmações, entrevistas/indagações, visitas ou inspeções físicas, testes de controles, inspeções de sistemas, acesso interno, contato com prestadores ou consulta a papéis de auditoria**. Nenhuma afirmação de execução desses procedimentos é feita.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA de Auditoria Independente, cadastro de normas, consulta em 22/10/2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, Resolução 2009/001215, status e alterações; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001215>).
- **Ref. 3** — CFC, Resolução CFC nº 1.215/09, NBC TA 402, texto oficial; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/RES_1215.pdf>).
- **Ref. 4** — CVM, Direcional Engenharia S.A., DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71; [abrir fonte](<https://www.rad.cvm.gov.br/ENETWEB/frmNBC.aspx?NSD=155189>).
- **Ref. 5** — B3, Direcional Engenharia S.A., perfil e dados econômico-financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 6** — Direcional RI, Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 7** — CFC, Revisão NBC20, alterações decorrentes da NBC TA 600 R2, publicada em 06/12/2023; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?codigo=2023/NBC20>).
- **Ref. 8** — CFC, Revisão NBC11, alteração normativa indicada no texto oficial da NBC TA 402; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?codigo=2021/NBC11>).
- **Ref. 9** — CFC, publicação eletrônica NBC TA 200 a 810, paginação da NBC TA 402; [abrir fonte](<https://cfc.org.br/wp-content/uploads/2018/04/Publicacao_NBC_TA_AUDITORIA.pdf>).
- **Ref. 10** — RI Direcional, DFP 4T25 V1; BP pp.16–17, Nota 5 p.69 e relatório PwC pp.115–117; acesso em 22/10/2026; [abrir fonte](<https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2>).


---

# PT-450 — Avaliação das distorções identificadas

**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações contábeis consolidadas  
**Exercício:** encerrado em 31/12/2025  
**Data de acesso às fontes públicas:** 22/10/2026  
**Natureza:** papel de trabalho exclusivamente didático, baseado em informação pública. Não integra nem representa os papéis da PwC ou de qualquer auditoria efetivamente conduzida.  
**Norma:** NBC TA 450 (R1), *Avaliação das Distorções Identificadas durante a Auditoria*, texto oficial CFC. Versão R1, publicada no DOU em 05/09/2016, aplicável às auditorias de demonstrações contábeis de períodos findos em ou após 31/12/2016. A página de normas do CFC consultada em 22/10/2026 ainda identifica NBC TA 450 (R1) como norma em vigor; não foi identificada revisão posterior aplicável a este tema no índice consultado. [1] [2]  
**Itens normativos considerados:** NBC TA 450, itens 1–5 (alcance, objetivo, definição e acumulação); 6–7 (reavaliação da estratégia/plano e procedimentos adicionais); 8–9 (comunicação e correção); 10–13 (avaliação de distorções não corrigidas e comunicação à governança); 14 (representação formal); 15 (documentação); e material de aplicação A1–A30, em especial A2–A9, A10–A13, A14–A28 e A29–A30. Referências correlatas: NBC TA 320, NBC TA 230 e NBC TA 260. [1]

## Objetivo, contas e processo

Avaliar, no limite estrito das evidências públicas consultadas, como se acumulariam e avaliariam distorções identificadas ou não corrigidas nas demonstrações consolidadas de 31/12/2025; registrar os fatores de risco relacionados aos estoques imobiliários e aos temas de auditoria divulgados; e distinguir com clareza o que foi observado publicamente do que dependeria de procedimentos de auditoria com acesso à Companhia.

**Contas/processos em foco:** estoques consolidados, com ênfase em terrenos a incorporar; processos de reconhecimento de receita imobiliária e de estimativa/divulgação de provisões para contingências, por serem os principais assuntos de auditoria (PAA) informados como base deste exercício didático. O fato de uma área ser PAA indica foco significativo de auditoria, não uma distorção nem uma conclusão de que há deficiência ou erro.

Este PT não reexecuta nem substitui os trabalhos do auditor independente. Não há acesso a razão contábil, balancetes, documentação de suporte, cadastro de terrenos, contratos, cálculos de estimativas, materialidade definida no trabalho, lista de diferenças, comunicações com a administração/governança ou papéis de auditoria.

## Afirmações e riscos

As afirmações relevantes a testar quanto a estoques incluem existência, direitos e obrigações, integridade, exatidão/valoração e alocação, corte, classificação entre circulante e não circulante e apresentação/divulgação. Para reconhecimento de receita, são pertinentes ocorrência, exatidão, corte, classificação e apresentação/divulgação. Para provisões e contingências, são pertinentes integridade, obrigação, mensuração/valoração e divulgação.

Os fatores a seguir são **hipóteses de risco para planejamento didático**, não constatações de distorção:

- O saldo de estoques informado é expressivo em relação ao ativo consolidado e terrenos a incorporar é a maior rubrica individual de estoque. Isso aumenta a relevância potencial de diferenças de existência, titularidade, custo atribuível, recuperabilidade, capitalização, classificação ou divulgação. A dimensão do saldo, sozinha, não demonstra que qualquer desses problemas ocorreu.
- A variação dos terrenos a incorporar entre 2024 e 2025 pode justificar investigação de aquisições, desenvolvimento, transferências, baixas e reclassificações, mediante razão e suporte. A variação não evidencia, por si, erro ou mudança indevida.
- A existência dos PAA de receita imobiliária e provisões para contingências, conforme premissa pública fornecida para o caso, orienta atenção a julgamentos e estimativas. Não permite inferir que reconhecimento de receita ou provisões estejam incorretos.
- A opinião sem ressalva informada para o relatório público não constitui garantia de ausência de distorções não corrigidas abaixo da materialidade, nem evidência de que os procedimentos previstos neste PT foram executados.

## População, fontes e critérios

**População prevista para auditoria integral:** universo de diferenças de auditoria detectadas no trabalho para as demonstrações consolidadas de 2025, inclusive erros factuais, de julgamento e projetados, conforme a NBC TA 450 e respectiva aplicação; inclui diferenças de períodos anteriores ainda não corrigidas e distorções de apresentação/divulgação. **A população transacional não foi obtida neste exercício didático.** A tabela pública de saldos não substitui a população de lançamentos, itens de estoque, estimativas e divulgações.

**Fontes públicas consultadas:** registro CVM da DFP da companhia, identificado como DFP 31/12/2025, versão 1, protocolo 021350DFP311220250100155189-71, enviado em 09/03/2026 às 18:29:30; página institucional B3 de DIRECIONAL ENGENHARIA S.A.; página Central de Resultados de RI; índice oficial CFC de normas NBC TA e arquivo oficial da NBC TA 450 (R1). No registro CVM foi possível verificar os metadados do formulário, o auditor indicado e a lista de quadros, entre eles “DFs Consolidadas”, “Notas Explicativas” e “Pareceres e Declarações”. A página dinâmica não expôs nesta consulta as páginas numeradas nem o conteúdo dos quadros de 2025. Por isso, os saldos detalhados, PAA e opinião citados abaixo são tratados como **premissas públicas fornecidas para este caso didático**; não se atribui número de página que não foi possível verificar. [2] [3] [4]

**Premissas quantitativas do caso (R\$ mil):** ativo consolidado em 31/12/2025 de 13.219.635 e em 31/12/2024 de 10.067.406; estoques consolidados de 6.951.508, incluindo terrenos a incorporar totais de 5.678.238, dos quais 4.864.673 não circulantes; estoques circulantes de 2.086.835; terrenos a incorporar totais em 2024 de 4.587.823, dos quais 3.888.979 não circulantes. A apresentação pública permite conferir que o estoque circulante total e o componente não circulante de terrenos somam aritmeticamente 6.951.508, mas isso não transforma o componente em total da classe. Os valores foram tratados como informação pública do caso, sem conciliação com razão ou documentos subjacentes.

**Critérios:** identificar/acumular as distorções que não sejam claramente triviais (item 5); avaliar natureza, magnitude e circunstâncias, individual e conjuntamente, e efeito de diferenças de períodos anteriores (itens 10–11); reconsiderar plano se indicado (6); comunicar tempestivamente e requerer correção (8–9); comunicar diferenças não corrigidas e efeitos à governança (12–13); obter representação formal (14); documentar limite de trivialidade, diferenças e conclusão (15). Não foram fornecidos os valores de materialidade, materialidade de execução, limite de claramente trivial nem demonstrativo de diferenças do auditor. Não se presume nem se estima esses parâmetros neste PT.

## Procedimentos realizados e planejados

| Ref. | Procedimento e classificação | Evidência/resultado e limite |
|---|---|---|
| P1 | **Realizado com evidência pública:** consulta ao registro CVM da DFP para verificar identidade do emissor, período, versão, protocolo, data de envio, auditor indicado e quadros disponibilizados. | O registro identifica DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71, envio em 09/03/2026 e PricewaterhouseCoopers Auditores Independentes Ltda.; lista os quadros consolidados, notas e pareceres. Não foi possível extrair os quadros/PDF completos ou suas páginas numeradas pela visualização dinâmica consultada. Ref. E1. [2] |
| P2 | **Realizado com evidência pública:** consulta à página B3 da companhia e comparação do ativo consolidado divulgado para 31/12/2025 com a DFP 4T25 V1 (p. 16). | A página B3 apresenta ativo total consolidado de R\$13.219.635 mil em 31/12/2025; converge com a premissa informada. B3 não fornece, nessa tela, detalhamento para validar os componentes de estoque ou diferenças de auditoria. Ref. E2. [3] |
| P3 | **Realizado com evidência pública: recálculo aritmético de variações e razões com os saldos do caso, sem extrapolar a apresentação consolidada para lançamentos individuais. | Ativo: aumento de R\$3.152.229 mil (31,3%) ante 2024. Terrenos a incorporar totais: aumento de R\$1.090.415 mil (23,8%). Estoques: 52,6% do ativo de 2025; terrenos totais: 43,0% do ativo e 81,7% dos estoques. Cálculos analíticos apenas direcionam riscos; não demonstram distorção e utilizam valores públicos examinados, sem teste de saldos subjacentes. Ref. E3. |
| P4 | **Realizado com evidência pública:** leitura do índice e do texto oficial CFC da NBC TA 450 (R1), com identificação dos requisitos relevantes. | Confirmadas a designação da versão, vigência, requisitos dos itens 5–15 e materiais explicativos A1–A30. Ref. E4. [1] [4] |
| P5 | **Planejado por falta de acesso:** obter do auditor o mapa de diferenças, incluindo diferenças corrigidas e não corrigidas, natureza, causa, conta/afirmação, período, valor bruto/líquido, imposto/efeito em resultado e saldo acumulado; reconciliar com os papéis de auditoria e demonstrações finais. | Não realizado. Sem esses elementos não é possível concluir sobre distorções detectadas pela auditoria, acumulação, valor claramente trivial ou efeito conjunto. |
| P6 | **Planejado por falta de acesso:** reconciliar a população completa de diferenças com o balancete consolidado final e a DFP arquivada, validando cada ajuste e reclassificação nas demonstrações e notas, inclusive diferenças de período anterior e efeitos no exercício corrente. | Não realizado. Requer balancete/razão, planilha de diferenças, versões dos demonstrativos e suporte de consolidação. |
| P7 | **Planejado por falta de acesso:** obter materialidade global e específica, materialidade de execução e limite de claramente trivial; recalcular comparação com o resultado efetivo e avaliar necessidade de revisão, agregação por classe/saldo/divulgação e efeitos qualitativos. | Não realizado. Nenhum limiar de materialidade foi inventado neste documento; saldos públicos não são base suficiente para adotar o parâmetro do auditor. |
| P8 | **Planejado por falta de acesso:** examinar cada diferença não corrigida, de modo individual e agregado, considerando magnitude, natureza, circunstância, intenção/possível viés, efeito de períodos anteriores e efeito sobre divulgação; avaliar distorções qualitativas e eventual padrão sistêmico. | Não realizado. Não há diferenças nem evidência interna disponível para essa avaliação. |
| P9 | **Planejado por falta de acesso:** solicitar evidência da comunicação tempestiva à administração, dos pedidos de correção, das razões para eventual recusa, das comunicações à governança e da representação formal com demonstrativo de ajustes não registrados. | Não realizado. Não houve comunicação, entrevista, confirmação nem solicitação de representação neste exercício didático. |
| P10 | **Planejado por falta de acesso:** para estoques, obter composição e movimentos por empreendimento/terreno, reconciliação com razão, documentos de titularidade e aquisição, custos capitalizados, baixa/venda, corte e avaliação de recuperabilidade; para receita e contingências, inspecionar contratos, memória de cálculos, processos, pareceres jurídicos e divulgações. | Não realizado. Não houve inspeção física, confirmação, exame de documento interno ou teste de transação. Os procedimentos requereriam evidência apropriada obtida no trabalho de auditoria. |
| P11 | **Simulado para fins didáticos:** considerar um lançamento hipotético de diferença de mensuração/classificação e demonstrar seu tratamento no mapa de diferenças. | Nenhuma quantia ou lançamento da Companhia foi criado. O exemplo é somente a regra de registro: identificar fato/evidência, afirmar a correção requerida, quantificar efeito e tributos quando mensuráveis, registrar correção ou saldo não corrigido, agregá-lo e avaliar natureza/magnitude/contexto contra materialidade. Sem valor, evidência e materialidade, não se poderia rotular o item como trivial ou relevante. |
| P12 | **Simulado para fins didáticos:** avaliar a resposta se a soma de diferenças se aproximasse da materialidade ou se o padrão das diferenças sugerisse outras não detectadas. | Não ocorreu na Companhia. Em auditoria real, reavaliar estratégia e plano conforme item 6, ampliar procedimentos e avaliar a população relacionada, inclusive se a administração corrigiu uma classe a pedido do auditor (item 7). |

## Evidências e referências cruzadas

| Referência | Conteúdo/uso no PT |
|---|---|
| E1 | Registro oficial CVM da DFP 31/12/2025 V1: metadados, protocolo, envio, auditor indicado e identificação dos quadros. Suporta P1. A interface dinâmica consultada não exibiu o conteúdo/paginação dos quadros. |
| E2 | B3, página de DIRECIONAL ENGENHARIA S.A., dados econômico-financeiros consolidados: ativo total de 31/12/2025. Suporta P2. |
| E3 | Premissas públicas-base reproduzidas neste PT: saldos, comparação, PAA e opinião. Suporta os recálculos P3, sem comprovação sobre contas subjacentes. |
| E4 | CFC, página oficial de normas NBC TA e texto integral oficial da NBC TA 450 (R1). Suporta P4 e critérios normativos. |
| X1 | Referência cruzada didática a obter, não existente: PT de estoques e seus testes de existência/direitos/valoração; necessário para vincular eventuais diferenças de estoque ao mapa de ajustes. |
| X2 | Referência cruzada didática a obter, não existente: PT de receita imobiliária e PT de contingências/provisões; necessário para examinar eventuais diferenças das áreas indicadas como PAA. |
| X3 | Referência cruzada didática a obter, não existente: mapa consolidado de diferenças, balancete final, materialidade e sumário de distorções não corrigidas. |

**Rastreabilidade de páginas:** o formulário CVM permite selecionar “Balanço Patrimonial Ativo”, “DFs Consolidadas”, “Notas Explicativas” e “Pareceres e Declarações”, mas a consulta pública estática não revelou páginas numeradas ou arquivo legível dos quadros DFP de 2025. Assim, este PT cita o nome do formulário, período, versão e seção disponível; registra a página como **não verificável na interface consultada**, em vez de fabricar numeração. O PDF anual integral da DFP 4T25 V1 foi obtido diretamente pelo RI e lido nas páginas impressas pertinentes (S2 em FONTES.md). [2] [4]

## Resultados, exceções, conclusão e limitações

**Resultado dos procedimentos públicos:** os metadados consultados identificam a DFP da companhia, sua versão e envio à CVM, e indicam a PwC como auditor. A tela B3 confirma o ativo consolidado de 2025 informado no caso. O recálculo dos saldos-base demonstra as variações e proporções descritas em P3. A leitura do relatório PwC no PDF direto da DFP 4T25 V1 (pp. 115–117) confirmou os PAA de reconhecimento de receita imobiliária e provisões para contingências e a opinião sem modificação. Isso descreve somente o relatório publicado, sem reexecução de procedimentos ou acesso a papéis privados. A página da companhia na B3 informa também atividade principal de incorporação, construção e comercialização de imóveis e prestação de serviços de engenharia. [2] [3]

**Exceções/distorções identificadas neste trabalho:** nenhuma diferença contábil foi identificada nos procedimentos limitados às fontes públicas e cálculos aritméticos descritos. Isso significa apenas que **não houve distorção quantificável identificada neste PT didático**. Não significa que não existam diferenças detectadas no trabalho da PwC, diferenças não corrigidas, limitações de auditoria ou distorções nas demonstrações.

**Conclusão normativa condicionada:** não há evidência acessível neste exercício para determinar se as diferenças eventualmente identificadas pela auditoria foram acumuladas conforme item 5, se a materialidade e o limiar de claramente trivial eram apropriados, se diferenças não corrigidas seriam relevantes individualmente/em conjunto conforme itens 10–11, ou se comunicações e representação formal requeridas nos itens 8–9 e 12–14 ocorreram. Consequentemente, **não é possível emitir uma conclusão de conformidade com a NBC TA 450 sobre a auditoria real nem concluir se as demonstrações estão livres de distorção relevante**. A conclusão didática limita-se à ausência de exceção quantificada nos dados públicos efetivamente examinados e à necessidade de executar os procedimentos P5–P10 com acesso autorizado.

**Limitações e ressalvas de uso:** este documento é acadêmico e baseado em fontes públicas. Não foi realizado trabalho de auditoria ou revisão; não houve acesso a registros e suportes internos, entrevistas, confirmações, inspeção física, consulta a processos, comunicação com administração/governança nem contato com PwC. Os saldos e divulgações citados foram localizados na DFP pública integral; não foram conciliados a razão, subrazões ou suportes internos. A opinião sem ressalva e os PAA citados não substituem as conclusões e papéis do auditor responsável. O material não deve ser apresentado como evidência de auditoria ou como papel de trabalho elaborado/revisado pela PwC.

## Preparação e revisão

**Preparador:** matrícula didática EDU-AUD-001  
**Data:** 22/10/2026  
**Revisão (nome, assinatura e data):** ______________________________________________  

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC. NBC TA 450 R1 Avaliação das Distorções Identificadas durante a Auditoria. Texto normativo oficial, versão R1, 2016; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA450%28R1%29.pdf>).
- **Ref. 2** — CVM. Direcional Engenharia S.A. Demonstrações Financeiras Padronizadas 31/12/2025 V1. Protocolo 021350DFP311220250100155189-71. Envio em 09/03/2026; [abrir fonte](<https://www.rad.cvm.gov.br/ENETWEB/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 3** — B3. DIRECIONAL ENGENHARIA S.A. Página da companhia e dados econômico-financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 4** — CFC. Índice oficial das NBC TA de Auditoria Independente. Consulta da NBC TA 450 R1 e status da norma; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 5** — Direcional Engenharia S.A. Relações com Investidores. Central de Resultados, consultada em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-500 — Evidência de auditoria: estoques de terrenos a incorporar e assuntos relacionados

## Identificação, norma e itens aplicáveis

**Código:** PT-500  
**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações consolidadas  
**Data-base:** exercício encerrado em 31/12/2025  
**Norma:** NBC TA 500 (R1), *Evidência de Auditoria*, versão do CFC publicada no DOU em 05/09/2016 e aplicável a períodos encerrados a partir de 31/12/2016. A página oficial do CFC identifica a R1 como vigente e não revogada; a resolução R1 altera a NBC TA 500 original. Aplicada aqui a versão vigente para o exercício de 2025, sem importar revisões normativas publicadas depois desse período. [1] [2]

**Itens normativos usados:** NBC TA 500 (R1), itens 1–2 (escopo), 3–5 (aplicabilidade, objetivo e termos), 6–7 (procedimentos apropriados e relevância/confiabilidade da evidência), 8–9 (informação preparada pela entidade e avaliação de sua precisão, integridade, nível de detalhe e exatidão), 10 (seleção de itens para teste) e 11 (tratamento de evidências inconsistentes ou dúvida de confiabilidade). Referência de paginação do texto oficial: PDF CFC da resolução, pp. 1–4; itens numerados citados acima. [2]

A norma define evidência de auditoria como informação utilizada para fundamentar conclusões e exige evidência apropriada e suficiente. Evidência pública documental pode apoiar procedimentos limitados sobre informações divulgadas, mas não substitui registros contábeis subjacentes ou procedimentos necessários para afirmações não demonstradas por essas fontes. A distinção entre relevância e confiabilidade, e entre suficiência e adequação, orienta as conclusões deste PT. [2]

## Objetivo, conta e processo

**Objetivo didático:** documentar a natureza, a qualidade e os limites das evidências públicas disponíveis sobre estoques consolidados, com ênfase nos terrenos a incorporar, e definir evidência adicional necessária para conclusões de auditoria sobre saldos e divulgações. O PT também registra como contexto os principais assuntos de auditoria (PAA) divulgados para reconhecimento de receita imobiliária e provisões para contingências. Não substitui testes de auditoria nem o arquivo de auditoria do auditor independente.

**Conta/processo principal:** estoques consolidados em 31/12/2025 — estoques circulantes e terrenos a incorporar classificados no ativo não circulante; processo relacionado de aquisição, capitalização, acompanhamento de empreendimentos, classificação e avaliação dos terrenos.

**Processos relacionados considerados somente para direcionar evidência:** reconhecimento de receita imobiliária e provisões para contingências, identificados como PAA no relatório do auditor mencionado na DFP. Este PT não reexecuta nem conclui sobre os procedimentos de PwC nesses assuntos.

## Afirmações e riscos direcionadores

O saldo de estoques divulgado é de **R\$ 6.951.508 mil**, composto pelo total de estoques circulantes de **R\$ 2.086.835 mil** e pelo componente não circulante de terrenos a incorporar de **R\$ 4.864.673 mil**; a Nota 5 informa terrenos a incorporar totais de **R\$ 5.678.238 mil**, dos quais R\$ 813.565 mil são componente circulante derivado. O total de terrenos a incorporar é a maior classe individual de estoque detalhada na Nota 5. O comparativo total de terrenos é **R\$ 4.587.823 mil** em 31/12/2024, dos quais **R\$ 3.888.979 mil** são não circulantes; o ativo consolidado é **R\$ 13.219.635 mil** em 31/12/2025 e **R\$ 10.067.406 mil** em 31/12/2024. Valores em R\$ mil, conforme a DFP pública integral e Nota 5. [3]

A soma aritmética do estoque circulante total e do componente não circulante de terrenos é R\$ 6.951.508 mil. O total de terrenos a incorporar cresceu R\$ 1.090.415 mil, ou aproximadamente 23,8%, entre os períodos comparativos; o ativo total aumentou R\$ 3.152.229 mil, ou aproximadamente 31,3%. São recálculos de dados públicos, não testes sobre lançamentos, avaliações ou transações. [3]

| Afirmação | Risco de distorção relevante a considerar — hipótese, não constatação | Evidência requerida para conclusão |
|---|---|---|
| Existência | Risco de que terrenos ou outros custos registrados não correspondam a ativos existentes ou a direitos da entidade na data-base. A magnitude do saldo e sua variação tornam a afirmação relevante para o plano de evidências. | Inventário analítico por terreno/empreendimento, documentação de aquisição e titularidade, reconciliação ao razão, e inspeção física ou outra evidência corroborativa conforme o caso. |
| Direitos e obrigações | Risco de que direitos de propriedade, opções, compromissos, ônus, condições suspensivas ou obrigações associadas não sejam adequadamente reconhecidos ou divulgados. Não há constatação pública neste PT sobre a existência desses fatores. | Escrituras e matrículas atualizadas, contratos, registros públicos pertinentes, confirmação independente quando apropriada e conciliação de compromissos e gravames. |
| Integralidade | Risco de omissão de terrenos, custos diretamente atribuíveis, obrigações ou divulgações de compromissos relacionados. | Reconciliação da população de terrenos e aquisições a razão e demonstrações, teste de pagamentos e documentos de aquisição, busca de passivos não registrados e exame de divulgação. |
| Avaliação e alocação | Risco de custo indevidamente capitalizado, custo alocado incorretamente a projetos, valor contábil não recuperável ou estimativas não sustentadas. São hipóteses de auditoria, não indícios de erro identificados. | Teste de custos por item, avaliação da política de capitalização, premissas e orçamentos de projeto, evidência de vendas/custos subsequentes, análise de valor realizável líquido e sensibilidade quando pertinente. |
| Classificação, apresentação e divulgação | Risco de classificação circulante/não circulante, agregação, descrição ou divulgação não coerente com a natureza e o horizonte de realização do ativo. | Critérios de classificação documentados, cronogramas de realização aprovados, reconciliação entre suporte e nota explicativa e avaliação das divulgações aplicáveis. |
| Receita imobiliária — processo relacionado | Por ser PAA divulgado, constitui área de julgamento e risco de auditoria a considerar, especialmente quanto a critérios de reconhecimento, progresso, alocação de custos, corte e informações subjacentes. A divulgação como PAA não demonstra erro nem equivale a ressalva. | Contratos e aditivos, evidência de progresso das obras, bases de custos, cálculos de receita, recebimentos, cortes antes/depois da data-base e suporte dos controles e estimativas. |
| Provisões para contingências — processo relacionado | Por ser PAA divulgado, há risco possível associado a integralidade, avaliação, classificação e divulgação de estimativas e incertezas. Não se infere aqui existência, suficiência ou insuficiência de qualquer provisão. | Relação completa de processos, cartas de assessores jurídicos externos, movimentação e metodologia de avaliação, pagamentos/acordos subsequentes e reconciliação da nota ao razão. |

## População, fontes e critérios

**População acessível nesta revisão:** divulgações públicas da DFP de 31/12/2025, versão 1, na CVM, incluindo o quadro estruturado de balanço consolidado, e informações públicas de identificação do emissor na B3. O protocolo CVM é **021350DFP311220250100155189-71**; a tela da DFP indica data do documento 31/12/2025 e envio em 09/03/2026. [3] [4]

**População necessária para uma auditoria de saldos, mas não fornecida neste PT:** listagem completa de terrenos e unidades de estoque por SPE/empreendimento, razão e balancete consolidados, reconciliação de consolidação, documentos de aquisição e pagamentos, custos acumulados, orçamentos e previsões de conclusão/venda, avaliações e testes de recuperabilidade, cronogramas de realização e notas de suporte. Não foi obtida população transacional para amostragem.

**Fontes públicas consideradas:**

- DFP CVM da companhia, 31/12/2025, versão 1; quadro estruturado “DFs Consolidadas / Balanço Patrimonial Ativo”; relatório do auditor e notas integrantes do protocolo, quando referidos na divulgação. A tela estruturada não apresenta paginação PDF; por isso, a referência precisa é ao nome do quadro e à data, e não a um número de página inventado. [3]
- Página de dados da Direcional na B3, que identifica o emissor, o código CVM 21350, a negociação DIRR3 e os dados econômico-financeiros apresentados pela B3. A informação de ativo consolidado em 31/12/2025 exibida na página é usada apenas como checagem pública secundária; não é evidência independente dos registros contábeis da companhia. [4]
- Central de Resultados da Direcional, canal de divulgação da companhia, considerada como referência pública de RI; não se atribuiu a essa página nenhum saldo ou número de página que não estivesse visível no documento efetivamente identificado. [5]
- Texto e catálogo oficiais CFC da NBC TA 500 (R1). [1] [2]

**Critérios de avaliação:** (i) compatibilidade do dado com o objetivo do procedimento; (ii) origem, natureza e confiabilidade da fonte; (iii) possibilidade de rastreio a documento identificável; (iv) consistência interna e entre fontes; (v) suficiência e adequação considerando risco e materialidade. Não foi estabelecida materialidade numérica, pois não foram fornecidos planejamento, materialidade global ou materialidade de execução do auditor. Não foram definidos tamanhos de amostra nem limiares quantitativos.

## Procedimentos realizados e planejados

Cada procedimento abaixo está expressamente classificado. “Realizado com evidência pública” descreve somente a revisão documental desta tarefa, não trabalho executado pela PwC nem auditoria de campo. Os procedimentos planejados são necessários para obter evidência sobre as afirmações que não podem ser cobertas pela informação pública.

| Ref. | Procedimento | Classificação e evidência/limite |
|---|---|---|
| 500-01 | Consultar a tela da DFP CVM, identificar documento, versão, protocolo, data de envio e auditor informado. | **Realizado com evidência pública.** Tela de detalhes da DFP CVM: documento 31/12/2025, V1, enviado em 09/03/2026; a página identifica PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. Isso comprova o que foi divulgado na tela, não a execução ou extensão dos trabalhos da firma. [3] |
| 500-02 | Inspecionar o quadro estruturado “DFs Consolidadas / Balanço Patrimonial Ativo” da DFP e transcrever os saldos pertinentes. | **Realizado com evidência pública.** Quadro CVM em R\$ mil: ativo total de R\$ 13.219.635 mil (2025) e R\$ 10.067.406 mil (2024); estoques circulantes de R\$ 2.086.835 mil; terrenos a incorporar no não circulante de R\$ 4.864.673 mil (2025) e R\$ 3.888.979 mil (2024). A tela estruturada não tem número de página. [3] |
| 500-03 | Recalcular soma entre estoques circulantes e o componente não circulante de terrenos, e comparar saldos anuais publicados. | **Realizado com evidência pública.** A soma resulta em R\$ 6.951.508 mil; variação do total de terrenos = R\$ 1.090.415 mil (aprox. 23,8%); variação de ativo total = R\$ 3.152.229 mil (aprox. 31,3%). Procedimento analítico limitado às cifras divulgadas; não valida a existência, integralidade, avaliação ou classificação subjacentes. [3] |
| 500-04 | Comparar o dado de ativo consolidado em 31/12/2025 da CVM com o dado correspondente que a página B3 apresenta para o mesmo período. | **Realizado com evidência pública.** A página B3 exibe R\$ 13.219.635 mil em 31/12/2025, compatível com a DFP CVM. Como a B3 apresenta informação econômico-financeira do emissor, a comparação é uma checagem de consistência de publicação, não confirmação externa nem evidência independente do saldo. [3] [4] |
| 500-05 | Considerar a informação divulgada sobre PAA (reconhecimento de receita imobiliária e provisões para contingências) e sobre opinião sem ressalva somente como contexto para direcionar o plano deste PT. | **Realizado com evidência pública, limitado à divulgação reportada.** Não é recálculo nem avaliação dos PAA, do julgamento do auditor, da suficiência da evidência obtida pela PwC ou de eventual erro. A opinião sem ressalva não fornece, por si, evidência específica para este saldo. Referência: DFP CVM, relatório do auditor independente integrante do protocolo; identificador de documento e referência pública do relatório em [3]. |
| 500-06 | Obter razão, balancete consolidado e conciliar total e classes de estoque à população analítica de terrenos por SPE/projeto; testar integridade e exatidão dos relatórios gerados pela entidade antes de usá-los como evidência (itens 8–9). | **Planejado por falta de acesso.** Solicitar dados íntegros com parâmetros de extração, conciliar totalizadores ao razão e à DFP, validar campos e alterações de dados e documentar exceções. Não executado. |
| 500-07 | Selecionar itens por valor, risco, localização, status e amostragem apropriada após conhecer a população e a materialidade; rastrear aquisições e pagamentos e inspecionar escrituras, contratos, matrículas e ônus. | **Planejado por falta de acesso.** Sem população nem critério de materialidade, não há seleção nem quantidade defensável de itens. Nenhum terreno, documento de titularidade ou pagamento foi inspecionado nesta tarefa. |
| 500-08 | Inspecionar evidência de existência e condição dos terrenos e confrontar dados-chave do cadastro aos registros pertinentes. | **Planejado por falta de acesso.** Procedimento futuro condicionado à natureza do ativo e à avaliação de risco, com inspeção física ou evidência alternativa apropriada. Nenhuma inspeção física foi realizada. |
| 500-09 | Testar custo capitalizado, alocação e recuperabilidade: confrontar custos elegíveis e alocações a documentos-fonte; examinar orçamentos, aprovações, vendas/custos posteriores e premissas de valor realizável líquido. | **Planejado por falta de acesso.** Depende de razão, bases de custo, orçamentos, premissas e suportes internos. Nenhuma avaliação independente ou reexecução foi realizada. |
| 500-10 | Verificar classificação circulante/não circulante, compromissos e divulgações frente aos planos aprovados e documentos de suporte. | **Planejado por falta de acesso.** A classificação foi observada apenas como divulgada na DFP; não foram obtidos planos de realização, documentos contratuais completos ou suporte de nota. |
| 500-11 | Para receita imobiliária, obter amostra de contratos e aditivos, recalcular reconhecimento e corte a partir de evidência de progresso, custos e recebimentos, confrontando informação produzida pela administração com fontes subjacentes. | **Planejado por falta de acesso.** O fato de ser PAA é público; nenhum contrato, cálculo ou corte foi testado neste PT. |
| 500-12 | Para contingências, reconciliar cadastro completo de processos, obter cartas de assessores jurídicos, avaliar respostas e premissas da administração e verificar pagamentos/acordos subsequentes e divulgação. | **Planejado por falta de acesso.** Nenhuma confirmação, carta jurídica ou consulta a advogado foi realizada. Este PT não apresenta valor de provisão nem conclusão sobre suficiência. |
| 500-13 | Investigar discrepâncias ou dúvida sobre confiabilidade entre relatórios internos, documentação de suporte, DFP e outras fontes, ampliar/modificar procedimentos e avaliar efeitos, conforme item 11. | **Planejado por falta de acesso.** Não foi possível executar procedimentos sobre informações internas, pois não foram disponibilizadas. O dado de CVM/B3 consistente não elimina riscos de fonte comum nem comprova os saldos subjacentes. |

**Procedimentos não executados:** nenhuma confirmação externa; entrevista ou indagação de administradores, pessoal, advogados ou terceiros; inspeção física; acesso a livros, sistemas, documentos internos ou arquivos de auditoria; teste de controles; observação de processo; reexecução de procedimento da entidade; ou auditoria de componentes. Qualquer menção a esses procedimentos neste PT é somente planejamento, nunca evidência de execução.

## Evidências e referências cruzadas

- **E-500-01 — DFP CVM V1, identificação do documento:** tela de detalhes do documento 31/12/2025, protocolo 021350DFP311220250100155189-71, envio em 09/03/2026; auditor informado como PwC. Fonte [3].
- **E-500-02 — DFP CVM V1, quadro de balanço:** “DFs Consolidadas / Balanço Patrimonial Ativo”, colunas 31/12/2025 e 31/12/2024, unidade R\$ mil. A referência é o título do quadro porque a tela estruturada não tem paginação. Fonte [3].
- **E-500-03 — Recálculos analíticos públicos:** soma e variações aritméticas descritas no procedimento 500-03, derivados exclusivamente de E-500-02. Não constituem documentação transacional nem teste de saldo.
- **E-500-04 — B3, perfil DIRECIONAL ENGENHARIA S.A.:** quadro econômico-financeiro “Balanço Patrimonial — Consolidado”, data 31/12/2025. Fonte [4]. Evidência secundária de consistência de publicação, não confirmação externa.
- **E-500-05 — Contexto do relatório de auditor independente e PAA:** DFP CVM, bloco “Pareceres e Declarações”/relatório de auditor independente e notas relacionadas, dentro do protocolo [3]. O arquivo consultado é referido por bloco/título; não se atribui página de PDF que não foi identificada na tela estruturada. Conforme o fato público-base deste PT, a opinião é sem ressalva e os PAA são reconhecimento de receita imobiliária e provisões para contingências. Não se conclui sobre a suficiência da auditoria da PwC.
- **E-500-06 — Norma:** CFC, NBC TA 500 (R1), resolução publicada em 05/09/2016, especialmente itens 6–11 e páginas 1–4 do PDF oficial. Fontes [1]–[2].

As referências “E-500” são identificadores internos deste papel didático. Não significam que foram criados papéis adicionais, nem fazem remissão a papéis de auditoria da companhia ou de PwC.

## Resultados, exceções, conclusão e limitações

**Resultados observados:** as cifras divulgadas para estoque circulante total e componente não circulante de terrenos somam aritmeticamente o total de estoques informado, R\$ 6.951.508 mil. A classe total de terrenos a incorporar, R\$ 5.678.238 mil, aumentou R\$ 1.090.415 mil em relação ao comparativo total de R\$ 4.587.823 mil (aprox. 23,8%). O ativo consolidado de R\$ 13.219.635 mil confere com o dado consolidado de 31/12/2025 apresentado na página da B3. A consistência entre essas apresentações dá suporte apenas à transcrição e coerência aritmética de informação pública. [3] [4]

**Exceções/distorções:** nenhuma distorção contábil foi identificada por esses procedimentos limitados. Isso não equivale a declarar inexistência de distorções. Não foram testados saldos, amostras ou divulgações contra fontes subjacentes; portanto, não há base para quantificar erro ou concluir sobre a adequação de reconhecimento, custo, titularidade, classificação ou recuperabilidade. Os aumentos observados são flutuações de dados publicados, não exceções de auditoria por si sós.

**Conclusão do PT:** a evidência pública obtida é relevante para documentar o montante divulgado, comparação entre períodos e consistência aritmética básica. Ela é insuficiente, por si só, para fundamentar conclusão de auditoria sobre existência, direitos e obrigações, integralidade, avaliação e alocação dos estoques, ou sobre o tratamento da receita imobiliária e contingências. Em conformidade com a NBC TA 500 (R1), antes de qualquer conclusão de auditoria sobre essas afirmações seriam necessários os procedimentos planejados, informação preparada pela entidade cuja precisão e integridade fossem avaliadas e evidência corroborativa adequada e suficiente. Este trabalho didático não emite opinião sobre as demonstrações financeiras e não substitui a auditoria independente divulgada pela companhia.

**Limitações:** trabalho de gabinete restrito às fontes públicas indicadas e às cifras de referência fornecidas para este exercício. Não houve comunicação com a companhia ou auditor, acesso a registros internos, inspeção, confirmação, entrevista, teste de detalhe, teste de controle, consulta jurídica, avaliação independente nem revisão de papéis de trabalho. A ausência dessas evidências limita a conclusão ao conteúdo e à consistência formal das divulgações públicas examinadas.

## Preparação e revisão

**Preparador:** matrícula didática EDU-AUD-001  
**Data:** 22/10/2026  
**Revisor:** ______________________________  
**Data da revisão:** ______________________

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC. NBC TA – de Auditoria Independente de Informação Contábil Histórica. Catálogo normativo. Consulta em 22/10/2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC. Resolução NBC TA 500 R1. Evidência de Auditoria. Publicada no DOU em 05/09/2016. PDF oficial, pp. 1–4; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA500%28R1%29.pdf>).
- **Ref. 3** — CVM. DIRECIONAL ENGENHARIA S.A. DFP de 31/12/2025, versão 1, protocolo 021350DFP311220250100155189-71, enviada em 09/03/2026. Tela do documento, quadro DFs Consolidadas / Balanço Patrimonial Ativo e bloco Pareceres e Declarações. Consulta em 22/10/2026; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3. DIRECIONAL ENGENHARIA S.A. Perfil do emissor DIRR3, código CVM 21350. Balanço Patrimonial Consolidado, comparativo em 31/12/2025. Consulta em 22/10/2026; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — DIRECIONAL ENGENHARIA S.A. RI. Central de Resultados. Consulta em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-501 — Estoques, litígios e informações por segmento

## Identificação do papel de trabalho

| Campo | Informação |
|---|---|
| Código / título | **PT-501 — Evidência de auditoria: considerações específicas para itens selecionados** |
| Entidade | DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações consolidadas |
| Período / data-base | Exercício encerrado em **31/12/2025** |
| Natureza | Papel de trabalho **didático**; não constitui documentação de auditoria efetivamente executada nem opinião independente |
| Norma | **NBC TA 501 — Evidência de Auditoria — Considerações Específicas para Itens Selecionados**, Resolução CFC nº 1.218/09, texto normativo aplicável alterado pela Revisão NBC 20 (2023), conforme cadastro do CFC. Aplicável a períodos iniciados em ou após 01/01/2010. O cadastro do CFC informa que a resolução está em vigor, não foi revogada e foi alterada pela Revisão NBC 20, publicada no DOU de 06/12/2023; a norma consta no índice oficial como NBC TA 501, sem designação “R1”. [1] [2] |
| Itens utilizados | NBC TA 501, itens **1–3** (alcance/objetivo); **4–8** (estoques); **9–12** (litígios e reclamações/representações); **13** (informações por segmento); aplicação e material explicativo **A1–A16**, **A17–A25** e **A26–A27**, respectivamente. O texto da Resolução 1.218/09 consultado traz esses números e requisitos; a Revisão NBC 20 é indicada aqui por ser a alteração listada pelo CFC. [1] [2] |
| Preparador | Matrícula didática **EDU-AUD-001** |
| Data de preparação | **22/10/2026** |
| Revisão | **____________________________** (em branco) |

> **Convenção de status usada neste PT.** “Realizado com evidência pública” significa apenas leitura/inspeção de informação acessível em fonte pública, nos limites descritos abaixo; não significa teste de auditoria sobre registros internos. “Planejado por falta de acesso” designa procedimento necessário que dependeria de acesso à companhia, seus registros ou terceiros. “Simulado para fins didáticos” identifica roteiro ou cálculo ilustrativo, sem execução sobre documentos subjacentes nem conclusão de auditoria.

## Objetivo, contas e processos

**Objetivo normativo.** Estruturar evidência apropriada e suficiente sobre (a) existência e condições de estoques; (b) totalidade de litígios e reclamações que envolvem a entidade; e (c) apresentação e divulgação de informação por segmentos, nos termos da estrutura de relatório financeiro aplicável (NBC TA 501, item 3). A norma é lida em conjunto com as demais NBC TAs pertinentes; este PT não substitui os procedimentos gerais de auditoria, nem normas sobre estimativas, evidência, grupos ou modificações de opinião. [1]

**Conta/processo prioritário — estoques.** Saldo consolidado de estoques e seus registros auxiliares, com atenção a terrenos a incorporar e a estoques circulantes, desde o inventário físico e a documentação de titularidade/custódia até a conciliação da contagem com o razão e a apresentação nas demonstrações. A base pública examinada indica estoques de **R\$ 6.951.508 mil**, dos quais **R\$ 5.678.238 mil** correspondem ao total de terrenos a incorporar, incluindo **R\$ 4.864.673 mil** não circulantes, e **R\$ 2.086.835 mil** a estoques circulantes. O total de ativos consolidado indicado é **R\$ 13.219.635 mil**. Esses valores são dados públicos para o exercício didático; as páginas relevantes da DFP integral foram examinadas, mas os saldos subjacentes e registros internos não foram obtidos. A B3 apresenta o ativo total consolidado em 31/12/2025 de R\$ 13.219.635 mil. [3] [4]

**Processos abrangidos pela NBC TA 501.** (i) contagem, corte, movimentação, custódia, compilação e conciliação de estoques; (ii) identificação, acompanhamento, contabilização e divulgação de litígios e reclamações; e (iii) determinação, consolidação, análise e divulgação da informação por segmento. Não se presume neste PT que existam estoques custodiados por terceiros, processos judiciais específicos, mais de um segmento operacional ou qualquer deficiência de controle.

## Afirmações e riscos considerados

| Área | Afirmação / objetivo pertinente | Riscos a avaliar — hipóteses, não constatações |
|---|---|---|
| Estoques, especialmente terrenos a incorporar | A NBC TA 501 exige evidência sobre **existência e condições** (itens 3(a) e 4). Também se considerariam, com procedimentos sob outras normas, direitos e obrigações, integridade, corte, exatidão, classificação e mensuração. | O peso relativo do saldo pode aumentar o risco de distorção relevante. A conta pode demandar juízo na alocação/capitalização de custos, corte, titularidade, classificação e avaliação de recuperabilidade; isso é **hipótese de risco**, não evidência de erro. A contagem pode ocorrer em múltiplos locais ou datas, ou certos estoques podem estar com terceiros; a ocorrência desses fatos precisa ser apurada. Terrenos podem demandar documentação registral e análise de restrições; não se afirma que existam pendências. |
| Litígios e reclamações | **Totalidade** de litígios e reclamações que possam gerar risco de distorção relevante (itens 3(b), 9–12), inclusive estimativas e divulgações correlatas. | Possível omissão de processos, contingências ou reclamações; informação incompleta da assessoria; classificação ou mensuração inconsistente com a evidência disponível. São riscos inerentes possíveis, não afirmações sobre processos concretos da Direcional. O caso informa que provisões para contingências foram PAA, mas o PAA, por si só, não comprova completude nem adequação de qualquer saldo. |
| Informações por segmento | Apresentação e divulgação conforme estrutura contábil aplicável (itens 3(c) e 13). | Possível identificação incompleta de segmentos, método de agregação/alocação inadequado, reconciliação inconsistente com os valores consolidados ou divulgação incompleta. Não se conclui, sem exame da nota e dos métodos da administração, quantos segmentos existem ou se há distorção. |

**Indicadores aritméticos para priorização (não são procedimentos substantivos nem validação independente dos saldos).** Com base exclusivamente nos dados públicos examinados: estoques equivalem a aproximadamente **52,6%** dos ativos consolidados; terrenos a incorporar totais correspondem a aproximadamente **81,7%** dos estoques e **43,0%** dos ativos; o total de terrenos a incorporar aumentou de R\$ 4.587.823 mil em 2024 para R\$ 5.678.238 mil em 2025, acréscimo de R\$ 1.090.415 mil (cerca de **23,8%**). Os cálculos são ilustrativos e não substituem teste dos lançamentos, composição, avaliação ou contagem. Comparativos: ativo consolidado 2024 de R\$ 10.067.406 mil; o componente não circulante de terrenos em 2024 era R\$ 3.888.979 mil. [3] [4]

## População, fontes e critérios

**Populações a obter da administração (não disponibilizadas para este trabalho).**

1. Cadastro completo dos estoques em 31/12/2025, por empreendimento, localização, natureza, quantidade/unidade, custo, condição, situação de obra e responsável pela custódia; reconciliação entre cadastro, razão e demonstrações; população e mapa de contagens físicas; registros de movimentações entre eventual data de contagem e a data-base; relação de itens mantidos por terceiros.
2. Relação completa de processos judiciais, administrativos, reclamações e demandas, por entidade do grupo, com situação, valor envolvido, avaliação da administração, documentação do jurídico interno e externo e conciliação com razão, provisões, despesas legais e notas explicativas.
3. Nota de segmentos, política e métodos utilizados, informações internas submetidas ao tomador de decisões operacionais, dados por segmento e conciliações/eliminações com as demonstrações consolidadas.

**Fontes públicas efetivamente consultadas.** A consulta CVM identifica a DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71, envio 09/03/2026 e PwC como auditor [3]. O PDF integral foi obtido diretamente no RI [6] e as páginas impressas foram examinadas: Nota 2.1.3 sobre segmentos p.44; Nota 5 sobre estoques p.69; Nota 16.2 sobre contingências pp.93–94; relatório PwC, PAA de contingências p.116. Também foram consultados o perfil B3 [4] e a Central de Resultados como índice institucional [5].

A página B3 identifica DIRECIONAL ENGENHARIA S.A. e mostra ativo consolidado de R\$13.219.635 mil em 31/12/2025 e R\$10.067.406 mil em 31/12/2024 [4]. A Central de Resultados é um índice dinâmico [5]; o PDF integral foi obtido pelo link direto da fonte institucional [6].

**Critérios e parâmetros de seleção planejados.** Relevância para as demonstrações; cobertura integral de localidades e entidades; risco e materialidade determinados pela equipe com base no planejamento completo; itens de maior valor e itens selecionados por amostragem; movimentações próximas ao encerramento; características de risco dos terrenos e de cada estoque; custódia de terceiros; processos ou reclamações com potencial de efeito relevante; e conciliação de dados de segmento com as demonstrações. Nenhuma materialidade, tamanho de amostra, lista de amostra ou limite de erro foi inventado neste PT. A definição quantitativa depende de materialidade e populações não fornecidas.

## Procedimentos e status

### Estoques

| Nº | Procedimento | Status e evidência / limite |
|---|---|---|
| E-01 | Consultar o registro público da DFP CVM para identificar companhia, período, versão, protocolo, data de envio, auditor e categorias das demonstrações apresentadas. | **Realizado com evidência pública.** Evidência: cabeçalho da página CVM informa DFP 31/12/2025 V1, protocolo e envio de 09/03/2026; consta PwC como auditor. Não valida saldos nem procedimentos de contagem da auditoria. [3] |
| E-02 | Comparar o ativo consolidado de 2025 e de 2024 com os dados econômico-financeiros publicados pela B3. | **Realizado com evidência pública.** A B3 apresenta os ativos totais de R\$ 13.219.635 mil e R\$ 10.067.406 mil, respectivamente. A comparação é de consistência entre dado-base e painel público, não teste da DFP completa. [4] |
| E-03 | Ler a Nota 5 e calcular os saldos/proporções de estoques e terrenos divulgados para priorização. | **Realizado com evidência pública.** Nota 5 p.69: estoques R\$6.951.508 mil; terrenos a incorporar totais R\$5.678.238 mil em 2025 e R\$4.587.823 mil em 2024; 81,7% dos estoques e 43,0% do ativo em 2025; variação anual de 23,8%. Cálculos aritméticos sobre divulgação, sem rastreamento ao razão. [6] |
| E-04 | Obter listagem completa de estoques e reconciliar saldos com razão, balancete, demonstrações e nota; testar integridade dos relatórios que suportam a população. | **Planejado por falta de acesso.** Depende de registros internos da companhia, cadastro item a item, razão e reconciliações; a leitura da nota pública não valida a população subjacente. |
| E-05 | Acompanhar contagem física, avaliar instruções da administração, observar a contagem, inspecionar itens e executar testes de contagem; testar a compilação dos resultados com os registros finais (itens 4(a)–(b); A1–A8). | **Planejado por falta de acesso.** Não houve presença ou observação em inventário, inspeção física, contagem de itens, teste de controles ou conciliação de contagem. Planejar cobertura e seleção conforme a população, locais e materialidade a obter. |
| E-06 | Se a contagem ocorrer em data diferente de 31/12/2025, testar movimentos entre a data de contagem e o encerramento; em caso de impossibilidade imprevista de comparecimento, planejar contagem alternativa e testes das transações intermediárias (itens 5–6; A9–A11). | **Planejado por falta de acesso.** Datas e circunstâncias da contagem não foram obtidas. Não se conclui que tenha havido impedimento ou contagem fora da data-base. |
| E-07 | Se presença for impraticável, desenhar procedimentos alternativos adequados; se insuficientes, avaliar efeito de limitação de alcance (item 7; A12–A14). | **Planejado por falta de acesso.** Não houve avaliação da praticabilidade na entidade, execução de alternativa ou conclusão sobre opinião. |
| E-08 | Identificar estoques relevantes sob custódia de terceiros; solicitar confirmação de quantidade/condição e/ou executar inspeção ou outro procedimento apropriado, conforme aplicável (item 8; A15–A16). | **Planejado por falta de acesso.** A existência de estoques com terceiros não foi constatada; primeiro obter a população e mapear a custódia. Não houve confirmação ou inspeção. |

### Litígios e reclamações

| Nº | Procedimento | Status e evidência / limite |
|---|---|---|
| L-01 | Ler a Nota 16.2 e o PAA de contingências do relatório público do auditor; registrar os saldos divulgados e delimitar o que não se pode concluir sem evidência jurídica/interna. | **Realizado com evidência pública.** Nota 16.2 pp.93–94 divulga provisão consolidada de R\$39.280 mil em 31/12/2025 (tributário 5, trabalhista 3.459, cível 35.816) e perdas possíveis sem provisão: trabalhista R\$38.847 mil, tributário R\$29.075 mil e cível R\$458.669 mil. O relatório PwC p.116 trata contingências como PAA. Isso não testa completude ou prognósticos jurídicos. [6] |
| L-02 | Indagar a administração, responsáveis pela governança e, conforme o caso, jurídico interno; revisar atas, correspondência com assessores jurídicos externos e contas de despesas legais para identificar litígios e reclamações (item 9; A17–A20). | **Planejado por falta de acesso.** Não foram realizadas entrevistas/indagações; não foram revisadas atas, correspondência, faturas, razão de despesas legais ou registros jurídicos. |
| L-03 | Havendo risco relevante ou indícios de litígios adicionais, preparar carta de indagação jurídica pela administração, enviada pelo auditor, solicitando resposta direta do assessor jurídico externo; avaliar alternativa apenas se comunicação for vedada (item 10; A21–A25). | **Planejado por falta de acesso.** Nenhuma carta foi enviada ou recebida, nenhum advogado foi contatado e nenhum procedimento alternativo foi executado. |
| L-04 | Solicitar representação formal da administração e, quando apropriado, da governança sobre litígios e reclamações conhecidos (item 12). | **Planejado por falta de acesso.** Não houve solicitação ou recebimento de representação formal. |

### Informações por segmento

| Nº | Procedimento | Status e evidência / limite |
|---|---|---|
| S-01 | Ler a política de segmentos divulgada e avaliar sua apresentação à luz da descrição pública da administração (item 13; A26–A27). | **Realizado com evidência pública.** Nota 2.1.3 p.44 informa que a administração usa as demonstrações consolidadas para decisões e identifica internamente um segmento, “Negócios Imobiliários”. A leitura não testa a composição dos relatórios ao principal tomador de decisões nem a completude do método. [6] |
| S-02 | Solicitar conciliação entre informação por segmento e valores consolidados, avaliar transferências/eliminações, alocação de ativos/custos e consistência entre períodos, conforme aplicável. | **Planejado por falta de acesso.** Depende das notas, informações gerenciais e demonstrações integrais. Não se presume qualquer estrutura ou quantidade de segmentos. |

## Evidências e referências cruzadas

| Referência | Fonte/evidência disponível | Uso neste PT |
|---|---|---|
| CVM-01 | Consulta de documentos CVM para a DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71; cabeçalho mostra data de envio 09/03/2026 e PwC como auditor. Página web sem número impresso. [3] | E-01; identificação do documento e do auditor. O conteúdo detalhado foi examinado no PDF direto do RI [6]. |
| B3-01 | Perfil oficial da DIRECIONAL ENGENHARIA S.A., seção “Dados Econômico-Financeiros — R\$ mil”, quadro “Balanço Patrimonial — Consolidado”, colunas 31/12/2025 e 31/12/2024; painel web **sem paginação**. [4] | E-02; comparação de ativo total informado. |
| RI-01 | Central de Resultados da Direcional, consultada em 22/10/2026, como índice web sem paginação [5]; DFP 4T25 V1 no link direto do RI [6], PDF com páginas impressas. | Fonte do exame da Nota 5 p.69, Nota 16.2 pp.93–94, Nota 2.1.3 p.44 e relatório PAA p.116. |
| N-01 | Resolução CFC nº 1.218/09, arquivo oficial “RES_1218.pdf”: texto da NBC TA 501, índice impresso na p. 3; requisitos e objetivo nos itens 1–13, pp. 4–6; aplicação A1–A27, pp. 6–12. [1] | Critério normativo dos procedimentos E-05–E-08, L-02–L-04 e S-01–S-02. |
| N-02 | Cadastro oficial de resoluções do CFC para 2009/001218 (situação e alteração) e índice das NBC TAs. Revisão NBC 20, publicada no DOU em 06/12/2023. Páginas web **sem paginação**. [2] | Verificação do status da norma e de sua alteração; identificação da versão aplicável. |

**Referência cruzada interna:** E-01/E-02 → CVM-01/B3-01; E-03/L-01/S-01 → PDF público [6]; E-04–E-08, L-02–L-04 e S-02 → dados e evidências internas ainda requeridas; N-01/N-02 → critérios. Não há papéis de suporte internos recebidos.

## Resultados, exceções e conclusão

**Resultados das verificações públicas.** A CVM identifica a DFP V1 e PwC [3]; B3 exibe ativo consolidado de R\$13.219.635 mil em 2025 e R\$10.067.406 mil em 2024 [4]. A leitura do PDF RI [6] confirmou saldos de estoques/terrenos (Nota 5 p.69), um segmento divulgado pela administração (Nota 2.1.3 p.44), provisões e perdas possíveis (Nota 16.2 pp.93–94) e o PAA correspondente (relatório PwC p.116). Nenhum desses cotejos substitui teste da população, registros ou assessoria jurídica.

**Base factual do estudo.** Conforme a DFP pública obtida e as páginas relevantes examinadas — sem acesso à evidência subjacente, aos registros internos ou ao arquivo privado da auditoria — estoques são R\$ 6.951.508 mil; terrenos a incorporar totais, R\$ 5.678.238 mil, incluindo R\$ 4.864.673 mil não circulantes; estoques circulantes, R\$ 2.086.835 mil; terrenos totais em 2024, R\$ 4.587.823 mil, incluindo R\$ 3.888.979 mil não circulantes; e os PAA são reconhecimento de receita imobiliária e provisões para contingências, com opinião sem ressalva. São referências para exercício didático, não exceções ou achados apurados pelo preparador. A opinião sem ressalva e os PAA não constituem prova de que cada procedimento deste PT tenha sido realizado, nem evidência suficiente para os objetivos da NBC TA 501.

**Exceções/achados.** Nenhuma exceção substantiva de auditoria foi testada ou identificada. Permanecem sem teste a completude da população de estoques, titularidade, contagem física, custódia de terceiros, arquivo integral de processos/correspondências jurídicas, prognósticos, registros internos de segmento e documentação da PwC. A divulgação pública da Nota 16.2 e do PAA não permite validar os valores nem a completude de processos.

**Conclusão didática.** A DFP pública permite examinar saldos e divulgações de estoques, contingências e segmento nas páginas identificadas, mas não fornece evidência apropriada e suficiente para concluir sobre existência/condições de estoques, totalidade de litígios/reclamações ou exatidão/completude da divulgação por segmento. O PT permanece **inconcluso quanto aos objetivos de auditoria** até execução dos procedimentos planejados com acesso apropriado. Não modifica, reinterpreta ou substitui o relatório PwC.

## Limitações e ressalvas de uso

Este documento foi produzido para treinamento a partir de fontes públicas. Não é papel da PwC, não reproduz documentação interna e não atesta que a auditoria independente tenha executado ou deixado de executar procedimento específico. Nenhuma confirmação externa foi solicitada ou recebida; nenhuma entrevista, inspeção física, observação ou teste de contagem ocorreu; não houve contato com advogados nem acesso a registros internos. Saldos, Nota 16.2, informação de segmento e PAA foram localizados no PDF público nas páginas citadas; a concordância com razão, completude de litígios e documentação suporte permanecem sem teste.

As interfaces web CVM, B3 e RI não fornecem numeração de página estável; o PDF oficial do RI tem páginas impressas citadas por número nos procedimentos. Valores monetários são expressos em **R\$ mil**. Não foi definida amostra de registros reais nem materialidade de auditoria para testar populações internas.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, Resolução nº 1.218/09 — NBC TA 501, Evidência de Auditoria — Considerações Específicas para Itens Selecionados; texto oficial, pp. 3–12, publicada em 03/12/2009, vigente para períodos iniciados desde 01/01/2010; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/RES_1218.pdf>).
- **Ref. 2** — CFC, Resolução 2009/001218 e índice oficial NBC TA — status em vigor, alterada pela Revisão NBC 20, DOU 06/12/2023; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001218>).
- **Ref. 3** — CVM, Consulta de documentos — Demonstrações Financeiras Padronizadas DIRECIONAL ENGENHARIA S.A., 31/12/2025 V1, protocolo 021350DFP311220250100155189-71, envio 09/03/2026; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3, DIRECIONAL ENGENHARIA S.A., Dados Econômico-Financeiros, Balanço Patrimonial Consolidado em R\$ mil, 31/12/2025 e 31/12/2024; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — Direcional Engenharia S.A., RI, Central de Resultados, consulta realizada em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 6** — RI Direcional, DFP 4T25 V1; Nota 2.1.3 p.44, Nota 5 p.69, Nota 16.2 pp.93–94, relatório PwC p.116; acesso em 22/10/2026; [abrir fonte](<https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2>).


---

# PT-505 — Confirmações externas

**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações contábeis consolidadas  
**Exercício:** encerrado em 31/12/2025  
**Norma:** NBC TA 505 — *Confirmações Externas*, aprovada pela Resolução CFC nº 1.219/09, aplicável a auditorias de períodos iniciados em ou após 01/01/2010. O cadastro oficial do CFC consultado em 22/10/2026 indica a resolução como vigente, não alterada e não revogada. Referências normativas principais: itens 1–16 e A1–A25; em especial itens 5–7, 8–9, 10–14, 15–16 e A1–A25. [1] [2]  
**Classificação do documento:** papel de trabalho didático elaborado exclusivamente com evidência pública; não integra nem pretende reproduzir o arquivo de auditoria da companhia ou da PwC.

## Objetivo, conta e processo

Avaliar, para fins didáticos, como procedimentos de confirmação externa poderiam fornecer evidência relevante e confiável sobre saldos e divulgações do consolidado em 31/12/2025. A NBC TA 505 define confirmação externa como resposta escrita recebida diretamente pelo auditor de terceiro e exige que o auditor controle informações a confirmar, escolha da parte confirmadora, conteúdo/endereço, envio e eventual segundo pedido (itens 5–7). [1]

O foco ilustrativo é o processo de aquisição, manutenção, classificação e avaliação dos **estoques imobiliários**, sobretudo terrenos a incorporar, e a confirmação de saldos relacionados com terceiros. A DFP consolidada pública apresenta ativo total de R\$ 13.219.635 mil e estoques de R\$ 6.951.508 mil em 31/12/2025; terrenos a incorporar totalizam R\$ 5.678.238 mil, dos quais R\$ 4.864.673 mil são não circulantes, e estoques circulantes totalizam R\$ 2.086.835 mil. Em 31/12/2024, ativo totalizava R\$ 10.067.406 mil e terrenos a incorporar totais, R\$ 4.587.823 mil, dos quais R\$ 3.888.979 mil não circulantes. Valores em R\$ mil. [3] [4]

A confirmação externa, por si só, não comprova necessariamente a existência física, avaliação ou classificação de terreno. Uma resposta de vendedor, instituição financeira, agente custodiante ou contraparte pode corroborar termos, saldos, garantias, direitos ou obrigações; deve ser combinada, conforme o risco e os critérios aplicáveis, com contratos, pagamentos, registros de imóveis, inspeção física e outros procedimentos substantivos. Nenhuma inspeção física foi executada neste trabalho.

## Afirmações e riscos

Afirmações relevantes para o estoque e transações associadas: **existência**, **direitos e obrigações**, **integralidade**, **avaliação/alocação**, **classificação e apresentação**, e **corte** das aquisições, pagamentos e transferências entre circulante e não circulante. Para saldos com bancos e contrapartes, seriam relevantes existência, integralidade, direitos/obrigações, exatidão e classificação.

A escala da classe e sua concentração em terrenos justificam atenção de auditoria: terrenos a incorporar totais representam aproximadamente 81,7% dos estoques e 43,0% do ativo total de 2025. O total de terrenos aumentou R\$ 1.090.415 mil (aproximadamente 23,8%) em relação a 2024, enquanto o ativo total aumentou R\$ 3.152.229 mil (aproximadamente 31,3%). São cálculos aritméticos sobre os saldos públicos citados, não testes de auditoria. [3] [4]

**Hipóteses de risco, não constatações:** títulos ou contratos incompletos/desatualizados; direitos, ônus, garantias, condições suspensivas ou compromissos não refletidos nos registros; divergências entre saldo contábil e confirmações de vendedores, instituições financeiras ou agentes; terrenos registrados em período ou classificação inadequados; e estimativas ou premissas de custo/recuperabilidade inadequadas. O crescimento/concentração não demonstra, por si, erro ou irregularidade.

O DFP público identifica como principais assuntos de auditoria (PAA) o reconhecimento de receita imobiliária e provisões para contingências e informa opinião sem ressalva. Isso contextualiza áreas de julgamento e risco, mas não equivale a evidência deste PT nem comprova que quaisquer confirmações específicas foram enviadas ou recebidas pela PwC. A NBC TA 505, item 1, não trata indagações relativas a litígios e reclamações, cobertas pela NBC TA 501; confirmações jurídicas sobre esses temas não são tratadas como procedimento concluído neste PT. [3]

## População, fontes e critérios

A população de auditoria necessária seria a relação completa, conciliada com o razão e o balancete consolidado, de terrenos e demais estoques, contrapartes, saldos, movimentos e compromissos relevantes em 31/12/2025. Seriam necessários também a composição por controlada/projeto, cadastro de contrapartes, documentação de propriedade e ônus, contratos, pagamentos subsequentes, conciliações e materialidade/limites de execução. **Esses registros internos não foram disponibilizados.** Assim, este PT não define população auditável, não seleciona amostra estatística, não extrapola resultados e não inventa saldos por contraparte.

A evidência pública consultada consiste em: (i) DFP CVM de 31/12/2025, versão 1, protocolo **021350DFP311220250100155189-71**, enviado em 09/03/2026 às 18:29:30, em especial dados consolidados, balanço, notas e relatório do auditor; (ii) página de dados econômico-financeiros consolidados da B3, que apresenta ativo total de R\$ 13.219.635 mil em 31/12/2025; (iii) central de resultados de RI, como canal público de divulgação; e (iv) texto e cadastro oficial do CFC da NBC TA 505. [1] [2] [3] [4] [5]

**Critérios para execução futura:** seleção baseada em risco e materialidade documentada; confirmação positiva dirigida a terceiros adequados; endereço e canal de resposta sob controle do auditor, com resposta diretamente ao auditor; autenticação da identidade e autoridade do respondente; acompanhamento de não respostas; investigação e avaliação de exceções; e procedimentos alternativos apropriados. Resposta negativa é menos persuasiva e, segundo item 15, não deve ser usada como único procedimento substantivo salvo quando presentes as condições normativas. Itens 7–16 e A1–A25 da NBC TA 505. [1]

## Procedimentos e evidências

| Procedimento | Classificação | Resultado / referência |
|---|---|---|
| Consulta ao cadastro e texto oficial do CFC para identificar edição aplicável, vigência e requisitos da NBC TA 505. | **Realizado com evidência pública** | Cadastro do CFC aponta Resolução CFC nº 1.219/09 vigente, sem alteração ou revogação; o PDF oficial contém o texto da norma e os itens referenciados. Não se trata de procedimento de confirmação sobre saldos da companhia. [1] [2] |
| Leitura dos dados públicos do DFP CVM informado: período, versão, protocolo/data de envio, balanço consolidado e informação pública sobre auditor e opinião/PAA. | **Realizado com evidência pública** | Identificados os saldos e divulgações resumidos neste PT, inclusive auditor PwC e opinião sem ressalva conforme o DFP. A consulta foi documental; não houve inspeção dos papéis da PwC nem verificação de documentos subjacentes. [3] |
| Comparação independente do ativo consolidado publicado pela CVM com a página B3 para 31/12/2025. | **Realizado com evidência pública** | Ambas as fontes exibem R\$ 13.219.635 mil para ativo total consolidado. É apenas consistência entre divulgações públicas, não confirmação externa independente obtida pelo auditor nem teste dos registros. [3] [4] |
| Recalcular variação do total de terrenos e do ativo total entre 2024 e 2025 e proporções dos terrenos em relação aos estoques e ativo de 2025. | **Realizado com evidência pública** | Aumento do total de terrenos: R\$ 1.090.415 mil, aproximadamente 23,8%; aumento do ativo: R\$ 3.152.229 mil, aproximadamente 31,3%; terrenos/estoques: aproximadamente 81,7%; terrenos/ativo: aproximadamente 43,0%. Recalculo aritmético sem teste de exatidão do dado-fonte ou de avaliação. [3] |
| Solicitar ao auditor/companhia razão, composição da população e materialidade; reconciliar a listagem integral de terrenos a incorporar com demonstrações e registros consolidados. | **Planejado por falta de acesso** | Não executado: não houve acesso à administração, ao auditor, ao razão, ao balancete ou a controles internos. Sem esse suporte, não foi possível determinar população, materialidade ou amostra. |
| Para itens selecionados após a etapa anterior, desenhar e enviar confirmações positivas a vendedores/alienantes e, conforme o caso, instituições financeiras, agentes custodiante/de garantias ou contrapartes, pedindo confirmação de saldos, condições contratuais, pagamentos, garantias, ônus, direitos e compromissos diretamente ao auditor. | **Planejado por falta de acesso** | Nenhuma solicitação foi preparada ou enviada; nenhum terceiro foi contatado e nenhuma resposta foi recebida. A escolha da parte confirmadora e dos dados a confirmar dependeria da natureza do saldo e de fontes externas apropriadas, nos termos do item 7. |
| Controlar expedição, endereçamento e devolução, autenticar cada resposta, enviar segundo pedido quando cabível e investigar toda diferença. Para não respostas, planejar procedimentos alternativos como inspeção de títulos/contratos, comprovantes de liquidação subsequente, extratos e registros externos pertinentes. | **Planejado por falta de acesso** | Não executado por inexistência de solicitações e acesso interno. Não houve avaliação de resposta não recebida, de exceção ou da confiabilidade de resposta. Itens 7, 10–14 e 16. |
| Exercício de treinamento: em uma confirmação hipotética de saldo de terreno, tratar diferença entre resposta e razão como exceção a investigar; comparar resposta obtida diretamente e documento de titularidade/ônus; tratar ausência de resposta como não resposta, não como concordância. | **Simulado para fins didáticos** | Cenário fictício, sem identificação de contraparte, valor, resposta, divergência real ou documento obtido. Demonstra aplicação dos itens 6, 10–14 e A11–A22; não constitui achado nem evidência sobre a companhia. |
| Procedimento hipotético diante de recusa da administração: indagar razões, avaliar validade/razoabilidade, reavaliar riscos e considerar procedimentos alternativos; avaliar implicações para auditoria e comunicação. | **Simulado para fins didáticos** | Não houve recusa real ou contato com a administração. Cenário ilustrativo dos itens 8–9 e A8–A10. |

## Referências cruzadas e arquivo de evidências

- **E-01 / [1]–[2]:** cadastro oficial CFC da resolução e PDF oficial da NBC TA 505. Base para identificação da versão e requisitos.
- **E-02 / [3]:** DFP CVM 31/12/2025 V1, protocolo 021350DFP311220250100155189-71. Base pública para período, versão, saldos, auditor, relatório/PAA. A interface consultada apresenta quadros online; não foi possível determinar uma paginação estável do arquivo a partir da visualização pública acessada. Para rastreabilidade, a referência é pelo nome do documento, protocolo, grupo “DFs Consolidadas”, quadro/nota/relatório e rubrica, e não por página presumida.
- **E-03 / [4]:** B3, página da companhia e quadro “Balanço Patrimonial – Consolidado”, data 31/12/2025. Corrobora publicamente apenas o ativo total indicado.
- **E-04 / [5]:** Central de Resultados do RI, consultada em 22/10/2026. Índice público de divulgação; não foi usada para afirmar um procedimento interno ou resposta de terceiro.

Não há cartas, e-mails de confirmação, respostas, registros de telefonema, evidência de autenticação, razão, conciliações ou arquivos de seleção/amostragem neste papel de trabalho. A classificação “realizado com evidência pública” aplica-se apenas às consultas e recálculos descritos na tabela.

## Resultados, exceções, conclusão e limitações

**Resultado documental:** os dados públicos de ativo total na CVM e na B3 são concordantes no montante de R\$ 13.219.635 mil em 31/12/2025. O DFP informado traz os saldos de estoques/terrenos descritos acima, identifica PwC como auditor, apresenta opinião sem ressalva e indica os PAA de reconhecimento de receita imobiliária e provisões para contingências. [3] [4] Não foi feita confirmação externa e, portanto, não foi obtida evidência de terceiro sobre existência, titularidade, completude, avaliação ou corte dos estoques nem sobre outros saldos.

**Exceções:** nenhuma exceção de confirmação foi identificada porque nenhuma solicitação foi enviada ou respondida. A concordância de divulgação entre CVM e B3 é apenas uma consistência pública; não elimina risco nem substitui confirmação. Não se conclui que os saldos estão corretos, que a auditoria da PwC incluiu determinada circularização, ou que não existam exceções ou distorções.

**Conclusão do PT didático:** os saldos e sua concentração apontam áreas apropriadas para planejar procedimentos de confirmação externa, especialmente como evidência corroborativa relativa a contrapartes, direitos, obrigações, garantias e condições dos terrenos, após acesso à população reconciliada e avaliação de risco/materialidade. Com as evidências disponíveis, **não é possível concluir sobre a suficiência ou adequação de confirmações externas para as afirmações contábeis**, nem sobre os saldos subjacentes. Qualquer conclusão de auditoria exigiria execução dos procedimentos planejados, avaliação de exceções e evidências adicionais apropriadas.

**Limitações expressas:** trabalho apenas didático, retrospectivo e restrito a informações públicas citadas; sem autorização ou comunicação com a companhia, PwC, bancos, vendedores, cartórios ou outros terceiros; sem acesso a controles, registros, contratos, papéis de auditoria, amostra, materialidade ou evidência de confirmações; sem entrevista, inspeção física, confirmação, teste substantivo ou validação de estimativas executados. As referências a riscos são hipóteses de planejamento, não constatações. Não se pretende emitir opinião ou assegurar as demonstrações financeiras.

## Preparação e revisão

**Preparador:** matrícula didática **EDU-AUD-001**  
**Data:** 22/10/2026  
**Revisão:** ______________________________  
**Data da revisão:** ________________________

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC. Resolução nº 1.219/09 — NBC TA 505, Confirmações Externas. PDF oficial, especialmente pp. 1 e 3–14, itens 1–16 e A1–A25, 2009.; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/RES_1219.pdf>).
- **Ref. 2** — CFC. Resoluções e Ementas — Resolução 2009/001219, NBC TA 505, situação de vigência, consulta em 22/10/2026.; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001219>).
- **Ref. 3** — CVM. DIRECIONAL ENGENHARIA S.A., DFP de 31/12/2025, versão 1, protocolo 021350DFP311220250100155189-71, enviada em 09/03/2026; quadros consolidados, notas e relatório do auditor, 2025. Paginação não indicada na visualização consultada.; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3. DIRECIONAL ENGENHARIA S.A., dados econômico-financeiros, Balanço Patrimonial Consolidado, 31/12/2025, consulta em 22/10/2026.; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — DIRECIONAL ENGENHARIA S.A. RI. Central de Resultados, consulta em 22/10/2026.; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-510 — Trabalhos iniciais — saldos iniciais

## Identificação e escopo

| Campo | Informação |
|---|---|
| Código / título | PT-510 — Trabalhos iniciais — saldos iniciais |
| Entidade / demonstrações | DIRECIONAL ENGENHARIA S.A. — demonstrações financeiras consolidadas |
| Período sob exame | Exercício encerrado em 31/12/2025 |
| Data de referência dos saldos iniciais | 01/01/2025, correspondentes, em regra, aos saldos finais de 31/12/2024 |
| Norma | NBC TA 510 (R1), *Trabalhos Iniciais — Saldos Iniciais*, texto oficial do CFC, publicado no DOU em 05/09/2016; aplicável a auditorias de períodos encerrados em ou após 31/12/2016. No índice oficial consultado em 22/10/2026 consta em vigor, sem revogação ou alteração posterior indicada. Itens principalmente aplicáveis: 1–13; material explicativo A1–A9. A norma deve ser lida com NBC TA 200, e, conforme o assunto, NBC TA 300, 315, 450, 500, 505, 540, 705 e 710. [1] [2] |
| Preparador | Matrícula didática EDU-AUD-001 |
| Data | 22/10/2026 |
| Revisor / data da revisão |  |
| Natureza | Papel de trabalho didático, construído com evidência pública. Não é papel de auditoria de campo nem documentação de auditoria efetivamente executada pela PwC ou por outro auditor. |

**Condição de aplicabilidade:** a NBC TA 510 rege um trabalho de auditoria inicial, definido no item 4(a) como aquele em que as demonstrações do período anterior não foram auditadas ou foram auditadas por auditor independente antecessor. A informação pública consultada identifica a PwC como auditora do DFP de 2025, mas não permite concluir, por si só, se 2025 foi primeiro exercício de auditoria da PwC, se houve auditor antecessor ou se a auditoria de 2024 foi por ela realizada. Para fins deste PT didático, a aplicação da NBC TA 510 é uma premissa de treinamento a validar em contratação e documentação; não é fato societário constatado. [3]

## Objetivo, contas e processo

**Objetivo normativo.** Obter evidência apropriada e suficiente sobre se os saldos iniciais contêm distorções que afetem relevantemente as demonstrações correntes e se as políticas contábeis apropriadas refletidas nos saldos iniciais foram aplicadas uniformemente em 2025, ou se eventuais mudanças foram adequadamente registradas, apresentadas e divulgadas (NBC TA 510, item 3). [2]

**Contas e divulgações em foco.** O foco didático é o saldo inicial de estoques imobiliários, em particular terrenos a incorporar, e as divulgações a respeito de contingências e compromissos existentes no início do exercício. Também se considera a leitura de todos os saldos iniciais e divulgações relevantes, pois a norma não limita a análise a uma conta específica. As provisões para contingências e o reconhecimento de receita imobiliária aparecem como assuntos-chave de auditoria no relatório de 2025 informado no DFP; isso orienta o risco do exercício corrente, mas não demonstra por si só que um saldo inicial esteja distorcido. [3]

**Processo a compreender e testar (planejado):** transição do balancete consolidado encerrado em 31/12/2024 para a abertura de 01/01/2025; consolidação e eliminações; formação, custo e baixa/transferência dos terrenos e estoques imobiliários; aplicação de políticas contábeis; e identificação, avaliação, atualização, reconhecimento e divulgação de contingências e compromissos. Nenhuma dessas rotinas internas foi acessada ou testada neste trabalho.

## Afirmações e riscos de distorção relevante

| Área | Afirmações relevantes | Riscos a avaliar — hipóteses, não constatações |
|---|---|---|
| Terrenos a incorporar / estoques imobiliários | Existência; direitos e obrigações; integralidade; avaliação e alocação; classificação e apresentação; corte | Hipótese de custo capitalizado indevido, alocação ou baixa incompleta, impairment não reconhecido, classificação inadequada entre circulante e não circulante ou direito de propriedade/controle não comprovado. A concentração do saldo aumenta a relevância potencial; não prova erro. |
| Demais estoques | Existência; integralidade; avaliação; corte e apresentação | Hipótese de custo de obra/projeto incorreto, obsolescência, transferência entre rubricas sem suporte ou reconhecimento inadequado de perda. Nenhuma foi observada em registros internos. |
| Contingências e compromissos existentes em 01/01/2025 | Integralidade; avaliação; obrigações; apresentação e divulgação | Hipótese de litígio ou compromisso existente não identificado, estimativa inicial desatualizada ou tratamento contábil/divulgação inadequado. A referência pública a provisões para contingências como PAA em 2025 torna o tema relevante para planejamento corrente, sem afirmar que havia erro ou evento não divulgado na abertura. |
| Uniformidade de políticas contábeis | Mensuração, reconhecimento, apresentação e divulgação | Hipótese de política de estoque, reconhecimento de receita imobiliária ou provisão alterada/aplicada sem tratamento adequado. A consistência não pode ser inferida apenas da comparação de totais publicados. |

A presença de PAA sobre reconhecimento de receita imobiliária e provisões para contingências no relatório do auditor referente a 2025 é evidência pública de que esses temas demandaram atenção de auditoria no exercício. Não é evidência de distorção nem substitui os procedimentos da NBC TA 510 sobre saldo inicial. [3]

## População, fontes e critérios

**População pretendida para auditoria completa:** todos os saldos contábeis existentes em 01/01/2025 e divulgações pertinentes a contingências e compromissos existentes naquela data, no consolidado da Companhia e controladas. A população quantitativa integral — balancete, razão, matriz de consolidação e subledgers — não foi disponibilizada. Portanto, os valores públicos abaixo são pontos de partida e não constituem população completa, nem base suficiente para amostragem.

**Dados públicos-base examinados:** DFP consolidada pública de 31/12/2025, versão 1, CVM, protocolo CVM n.º 021350DFP311220250100155189-71, data do documento 31/12/2025; o material de referência informa protocolo em 09/03/2026. O cadastro público identifica a auditora como PricewaterhouseCoopers Auditores Independentes Ltda. [3] A DFP reporta ativo consolidado de R\$ 13.219.635 mil em 31/12/2025 e R\$ 10.067.406 mil em 31/12/2024; estoques de R\$ 6.951.508 mil no encerramento de 2025, incluindo terrenos a incorporar totais de R\$ 5.678.238 mil, dos quais R\$ 4.864.673 mil são não circulantes, e estoques circulantes de R\$ 2.086.835 mil; terrenos a incorporar totais comparativos de R\$ 4.587.823 mil em 2024, dos quais R\$ 3.888.979 mil são não circulantes. Esses montantes são apresentados em milhares de reais; as páginas relevantes da DFP integral foram examinadas, sem acesso à evidência subjacente. [3] A B3 também apresenta ativo total consolidado de R\$ 13.219.635 mil em 31/12/2025. [4]

**Critérios de execução e avaliação:** NBC TA 510, itens 5–9 para procedimentos e evidência; itens 10–13 para consequências de limitação, distorção, inconsistência de políticas e opinião modificada do antecessor. Evidência planejada também deve atender à NBC TA 500. Comparativos devem ser tratados em conjunto com NBC TA 710. Avaliação de diferenças, se identificadas, deve seguir NBC TA 450; qualquer efeito no relatório observaria NBC TA 705. [2]

## Procedimentos, classificação e resultados

Legenda: **Realizado com evidência pública** = análise limitada a material publicamente disponível; **Planejado por falta de acesso** = procedimento necessário, ainda não executado porque os registros ou pessoas não foram disponibilizados; **Simulado para fins didáticos** = desenho hipotético de procedimento, sem execução e sem resultado atribuído.

| Ref. | Procedimento | Classificação | Evidência / resultado limitado |
|---|---|---|---|
| P510-01 | Consultar o cadastro oficial do CFC para identificar título, revisão, data de publicação, status e texto aplicável da norma. | Realizado com evidência pública | CFC identifica NBC TA 510 (R1), DOU 05/09/2016, e a página de resolução informa “em vigor: sim”, sem alteração ou revogação. Aplicabilidade normativa estabelecida; não valida a condição factual de auditoria inicial da Companhia. [1] [2] |
| P510-02 | Ler a DFP consolidada mais recente disponível para obter informação pública sobre comparativos, saldos iniciais relevantes, divulgações e relatório do auditor. | Realizado com evidência pública | Consulta ao registro CVM da DFP 2025 V1 e aos seus campos de DFs consolidadas, notas explicativas e pareceres/declarações. O DFP identifica PwC. Relatório apresenta opinião sem ressalva e PAA sobre reconhecimento de receita imobiliária e provisões para contingências conforme dados do documento público. Referência é o registro e as demonstrações/relatório correspondentes, não um número de página impresso que não foi validado na página HTML da CVM. [3] |
| P510-03 | Comparar analiticamente os valores publicados de ativos e do total de terrenos a incorporar em 2024 e 2025, sem tratar o comparativo como teste de saldo ou explicação de variação. | Realizado com evidência pública | Ativo consolidado: R\$ 10.067.406 mil (2024) versus R\$ 13.219.635 mil (2025), variação aritmética de R\$ 3.152.229 mil (31,3%). Total de terrenos a incorporar: R\$ 4.587.823 mil (2024) versus R\$ 5.678.238 mil (2025), variação de R\$ 1.090.415 mil (23,8%). O componente não circulante foi R\$ 3.888.979 mil em 2024 e R\$ 4.864.673 mil em 2025. Percentuais são cálculos do preparador sobre números publicados, arredondados a uma casa decimal. Não se investigou causa, não se definiu materialidade e nenhuma exceção de auditoria pode ser concluída dessa comparação isolada. [3] |
| P510-04 | Reconciliar o balancete final de 31/12/2024 com o balancete de abertura de 01/01/2025, incluindo eliminatórias e conversões do consolidado; rastrear diferenças e lançamentos de transição. | Planejado por falta de acesso | Requer razão, balancete, trilha de consolidação, lançamentos e relatórios dos sistemas. Nenhum desses arquivos foi obtido. Sem resultado. [2, item 6(a)] |
| P510-05 | Inspecionar papéis do auditor antecessor que suportam os saldos e divulgações iniciais; verificar também o relatório do antecessor e se eventual modificação continua relevante. | Planejado por falta de acesso | Não foram disponibilizados papéis de trabalho do auditor antecessor, autorização de acesso, comunicação com antecessor nem evidência de qual auditor examinou 2024. A DFP pública de 2025, por si, não dá acesso a papéis. Sem execução ou conclusão sobre antecessor. [2, itens 6(c)(i), 9 e 13] |
| P510-06 | Testar amostra de terrenos: concordar itens do cadastro de terrenos com escrituras/matrículas e contratos; conferir titularidade ou direitos, preço e custos capitalizados com documentação de origem; avaliar ônus, corte, baixas, transferências, perdas e classificação. | Planejado por falta de acesso | População, seleção, contratos, matrículas, comprovantes, composição de custo, avaliações e inspeção física não disponíveis. Nenhuma confirmação ou inspeção foi efetuada. [2, itens 6(c)(ii)–(iii)] |
| P510-07 | Obter e testar composição por projeto dos estoques de abertura; rastrear custos para documentos de suporte e testar movimentação subsequente pertinente ao saldo de abertura, inclusive baixas/vendas e reconhecimento de custos. | Planejado por falta de acesso | Subledger, balancetes por empreendimento, contratos, notas fiscais, memórias de custo, movimentos subsequentes e critérios de seleção não disponíveis. Nenhum item foi testado. [2, itens 6(c)(ii)–(iii)] |
| P510-08 | Para contingências e compromissos existentes na abertura, obter listagem jurídica, circularizações/retornos de assessores jurídicos, processos, atas e documentos subsequentes; avaliar completude, reconhecimento, mensuração, classificação e divulgação, separando fatos novos de condições preexistentes. | Planejado por falta de acesso | Não houve circularização, entrevista, consulta a processo em nome da Companhia ou inspeção de documentação interna. A menção pública a provisões como PAA não satisfaz a evidência de saldo inicial. [2, itens 1, 4(b) e 6] |
| P510-09 | Comparar políticas contábeis e divulgações de 2024 e 2025 para estoques, receita imobiliária e contingências; rastrear alterações a decisões, base normativa e lançamentos. | Planejado por falta de acesso | A leitura de demonstrações publicadas pode orientar o confronto, mas não demonstra a aplicação no razão nem justifica lançamentos. As políticas detalhadas e sua aplicação consistente não foram verificadas em fonte interna. [2, item 8] |
| P510-10 | Como exercício demonstrativo, selecionar hipoteticamente itens materiais de terrenos e contingências da abertura e executar rastreamento documental conforme P510-06 a P510-08, registrando cada evidência e resultado em subpapel. | Simulado para fins didáticos | Apenas roteiro de treinamento. Não se criou amostra real, não se recebeu evidência e não se atribuíram achados. Este procedimento simulado não pode ser confundido com teste realizado. |
| P510-11 | Avaliar a resposta de auditoria corrente sobre os riscos de abertura e se evidência do exercício corrente é relevante para saldos iniciais, conforme a natureza da conta e a asserção. | Planejado por falta de acesso | Não foram disponibilizados programa de auditoria corrente, testes ou evidências de 2025. Sem base para concluir que procedimentos correntes cobrem saldos iniciais. [2, item 6(c)(ii)] |

## Evidências e referências cruzadas

- **E510-1 — Norma:** página de normas de auditoria do CFC e registro oficial da NBC TA 510 (R1), com link para o PDF integral. A norma descreve como itens 5–9 os procedimentos e como itens 10–13 conclusões/relatórios; o PDF também traz os materiais A1–A9. Referência cruzada: P510-01 e critérios. [1] [2]
- **E510-2 — DFP consolidada:** CVM, DIRECIONAL ENGENHARIA S.A., DFP referente a 31/12/2025, versão 1, protocolo n.º 021350DFP311220250100155189-71. Consultar as seções “DFs Consolidadas”, “Balanço Patrimonial Ativo”, “Notas Explicativas” e “Pareceres e Declarações” no registro eletrônico. CVM exibe dados por tela/quadros; não atribuo número de página PDF porque não foi validada paginação fixa nessa visualização. Referência cruzada: P510-02 a P510-03 e população. [3]
- **E510-3 — Cadastro econômico-financeiro B3:** perfil da DIRECIONAL ENGENHARIA S.A., código CVM 21350, “Dados Econômico-Financeiros — R\$ — mil”, balanço patrimonial consolidado, coluna 31/12/2025. Apresenta ativo total de 13.219.635. O perfil corrobora a identificação da entidade e o dado de ativo total; não substitui a DFP e não suporta testes de detalhe. Referência cruzada: população. [4]
- **E510-4 — Relações com investidores:** Central de Resultados da Companhia, utilizada como canal oficial para demonstrações e documentos por exercício. Consulta realizada em 22/10/2026; a página dinâmica não foi usada para atribuir número de página a demonstrativos. Referência cruzada: origem alternativa de documentos da Companhia. [5]

**Paginação e unidades:** os demonstrativos consultados via CVM são quadros eletrônicos e as referências acima identificam seção, quadro e data, não uma página impressa. Quando uma cópia PDF com paginação estável for obtida para o arquivo de auditoria real, registrar número de página e preservar cópia/versionamento. Não se atribui página não confirmada. Valores monetários citados estão em R\$ mil, salvo indicação em contrário.

## Exceções, conclusão e limitações

**Exceções identificadas na evidência pública examinada:** nenhuma diferença aritmética foi identificada nos valores reproduzidos neste PT. Esse resultado é apenas uma recomputação de variações entre saldos publicados e não representa teste de transferência, existência, titularidade, mensuração, corte, completude ou uniformidade de políticas. Não foi identificada nem investigada uma distorção de saldo inicial. A opinião sem ressalva sobre a DFP de 2025 não substitui a evidência requerida por este PT nem elimina limitações do trabalho didático. [2] [3]

**Conclusão didática:** o material público permite identificar a versão normativa, o auditor reportado, os valores comparativos e os temas de atenção indicados no relatório de 2025. Não permite obter evidência apropriada e suficiente para concluir se os saldos iniciais de 01/01/2025 estavam livres de distorção relevante, se os saldos finais de 2024 foram corretamente transferidos, ou se políticas contábeis foram aplicadas uniformemente. Assim, **não se conclui sobre os objetivos do item 3 da NBC TA 510**. Em trabalho real, os procedimentos planejados devem ser executados e documentados. Se, mesmo após procedimentos adicionais apropriados, não for possível obter evidência apropriada e suficiente, o auditor deve avaliar o efeito no relatório, inclusive ressalva ou abstenção conforme o item 10; distorção material não corrigida ou política inconsistente demanda considerar opinião modificada nos termos dos itens 11–13 e da NBC TA 705. Não se está propondo opinião sobre a Companhia. [2]

**Limitações expressas:** (i) nenhum acesso a razão, balancete, consolidação, contratos, matrículas, documentos de custo, processos, pareceres jurídicos, atas ou comunicações internas; (ii) nenhuma confirmação externa, entrevista, inspeção física ou visita foi realizada; (iii) nenhum papel de trabalho de auditor antecessor examinado; (iv) nenhuma amostragem ou teste substantivo executado; (v) período de referência e cifras públicas não validam a totalidade da população; (vi) não se presume alteração de auditor, continuidade de auditor, distorção, deficiência de controle ou inadequação contábil a partir dos dados públicos; e (vii) qualquer cenário de auditoria inicial é premissa didática até confirmação documental. Fontes acessadas em 22/10/2026.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA — de Auditoria Independente de Informação Contábil Histórica, índice de normas, versão consultada em 2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, NBC TA 510 (R1), Trabalhos Iniciais — Saldos Iniciais, texto oficial, publicada em 2016; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA510%28R1%29.pdf>).
- **Ref. 3** — CVM, DIRECIONAL ENGENHARIA S.A., DFP 31/12/2025, versão 1, protocolo CVM 021350DFP311220250100155189-71, documento e quadros consolidados; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3, perfil de listagem DIRECIONAL ENGENHARIA S.A., dados econômico-financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — DIRECIONAL ENGENHARIA S.A., Relações com Investidores, Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-520 — Procedimentos analíticos

## Identificação, norma e itens

**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações consolidadas  
**Exercício:** encerrado em 31/12/2025  
**Código/título:** PT-520 — Procedimentos analíticos  
**Norma aplicável:** NBC TA 520, *Procedimentos Analíticos*, aprovada pela Resolução CFC nº 1.221/09, publicada no DOU em 04/12/2009. A ficha oficial do CFC consultada em 22/10/2026 informa que a resolução está em vigor, não foi alterada nem revogada. A norma aplica-se a auditorias de demonstrações contábeis de períodos iniciados a partir de 01/01/2010; portanto, é a versão identificada para o exercício de 2025. [1]  
**Itens normativos considerados:** 2–7; orientações A1–A3, A4–A16, A17–A19 e A20–A21. Os itens 3–4 tratam dos objetivos e da definição; o item 5 estabelece requisitos para procedimentos analíticos substantivos; o item 6 requer procedimentos analíticos perto do fim da auditoria para apoiar a conclusão geral; e o item 7 requer investigar diferenças relevantes ou incoerentes mediante indagação e evidência apropriada, além de outros procedimentos quando necessários. [1] [2]  
**Data de acesso das fontes:** 22/10/2026.

> Este é um papel de trabalho didático elaborado com informações públicas. Não é papel de trabalho da PwC, não integra seus arquivos de auditoria e não representa opinião ou asseguração independente.

## Objetivo, conta e processo

**Objetivo:** executar uma leitura analítica comparativa pública, em nível de demonstrações consolidadas, com foco em estoques e especialmente em terrenos a incorporar, considerando a dimensão do saldo, sua evolução entre 2024 e 2025 e sua proporção em relação ao ativo total. Identificar questões que, numa auditoria real, exigiriam expectativa mais precisa e investigação adicional. O exercício público não substitui os procedimentos requeridos para formar expectativa suficientemente precisa, avaliar confiabilidade dos dados e estabelecer diferença aceitável nos termos do item 5 da NBC TA 520.

**Conta/processo em foco:** estoques consolidados, com terrenos a incorporar como rubrica individual destacada; processo hipotético sob auditoria compreende aquisição e registro de terrenos, alocação a projetos, classificação circulante/não circulante e avaliação contábil. A existência, direitos, registros e controles desse processo não foram examinados internamente neste trabalho.

**Contexto público relacionado:** a DFP e o relatório do auditor independente informam PwC como auditor e opinião sem ressalva, e apresentam como principais assuntos de auditoria o reconhecimento de receita imobiliária e provisões para contingências, conforme relatório público examinado no PDF direto da DFP 4T25 V1 (pp. 115–117; S2 em FONTES.md). Esses assuntos são contexto de risco informado no relatório publicado; não constituem achado deste PT nem evidência de auditoria obtida aqui. Não se infere deles distorção em estoques. [3]

## Afirmações e riscos considerados

As afirmações relevantes para orientar procedimentos adicionais seriam existência, direitos e obrigações, integridade, avaliação e alocação, corte, classificação e apresentação. Não foram testadas por documentos internos, inspeção física ou confirmação externa.

O saldo de estoques é expressivo em relação ao ativo consolidado, e terrenos a incorporar é uma classe especialmente relevante dentro de estoques. Isso orienta uma **hipótese de risco**, não uma constatação: mensuração, alocação, classificação e suporte dos terrenos podem demandar atenção, por exemplo, diante de alterações no ritmo dos projetos ou em suas premissas de realização. Os dados públicos comparativos, isoladamente, não demonstram erro, perda, obsolescência, problema de titularidade ou inadequação de classificação.

A execução de testes substantivos sobre receita imobiliária e provisões para contingências não integra o escopo deste PT. O registro público de PAA apenas sinaliza temas que a auditoria reportada tratou como relevantes; não foi usado como substituto de evidência ou como prova sobre a conta de estoques. [3]

## População, fontes e critérios

**População observada:** informação financeira consolidada publicada para 31/12/2025 e comparativo de 31/12/2024 na DFP 2025, versão 1, da Companhia. A DFP foi protocolada em 09/03/2026, conforme o dado-base do caso. O registro CVM identifica a data-base 31/12/2025, DFP versão 1 e demonstrações consolidadas. [3] [4]

**Unidade e critério:** valores em R\$ mil; comparação de saldo contra saldo, com percentuais calculados pelo preparador usando valores publicados. Critério analítico apenas descritivo: variação interanual e proporção de saldos em relação ao ativo total e ao total de estoques em 2025. Não há orçamento público, expectativa independente documentada, limite quantitativo de diferença aceitável ou materialidade fornecidos para este exercício didático. Assim, não se trata de teste analítico substantivo com poder de detectar distorção relevante.

**Dados usados:** ativo consolidado de R\$ 13.219.635 mil em 2025 e R\$ 10.067.406 mil em 2024; estoques de R\$ 6.951.508 mil em 2025, dos quais terrenos a incorporar totais de R\$ 5.678.238 mil, incluindo R\$ 4.864.673 mil não circulantes, e R\$ 2.086.835 mil em estoques circulantes; terrenos a incorporar totais de R\$ 4.587.823 mil em 2024, incluindo R\$ 3.888.979 mil não circulantes. Valores reproduzidos da informação pública indicada e verificados no PDF integral e nos quadros consolidados/Nota 5 correspondentes; a estrutura CVM também está em R\$ mil e não possui paginação de documento PDF. [3] [4]

## Procedimentos e resultados

| ID | Procedimento e classificação | Evidência/resultados |
|---|---|---|
| A1 | **Realizado com evidência pública.** Comparar ativo total consolidado em 31/12/2025 com o comparativo de 31/12/2024. | R\$ 13.219.635 mil contra R\$ 10.067.406 mil: acréscimo de R\$ 3.152.229 mil, equivalente a **31,3%** (diferença aritmética calculada sobre o comparativo). A variação é observável; sua causa não é identificável apenas pelo saldo. [3] [4] |
| A2 | **Realizado com evidência pública.** Comparar terrenos a incorporar totais em 2025 com o saldo comparativo total de 2024. | R\$ 5.678.238 mil contra R\$ 4.587.823 mil: acréscimo de R\$ 1.090.415 mil, equivalente a **23,8%**. A classe cresceu em valor absoluto, mas sua taxa de crescimento ficou cerca de 7,5 pontos percentuais abaixo da variação do ativo total. Isto é uma comparação, não explicação causal nem conclusão de razoabilidade. [3] [4] |
| A3 | **Realizado com evidência pública.** Calcular a proporção do estoque e dos terrenos a incorporar totais em relação ao ativo total, e dos terrenos totais dentro do estoque total. | Em 2025: estoques/ativo total = **52,6%**; terrenos a incorporar totais/ativo total = **43,0%**; terrenos a incorporar totais/estoques = **81,7%**. R\$ 5.678.238 mil é a maior classe individual de estoques detalhada na Nota 5; R\$ 4.864.673 mil é o componente não circulante. Esses indicadores dimensionam exposição, não comprovam existência, titularidade ou valor recuperável. [3] [4] |
| A4 | **Realizado com evidência pública.** Observar isoladamente estoques circulantes publicados em 2025 em relação ao ativo total. | R\$ 2.086.835 mil equivalem a **15,8%** do ativo total de 2025. Não foi calculada variação interanual desta classe: o comparativo circulante de 2024 não integra os dados-base utilizados neste trabalho. [3] [4] |
| P1 | **Planejado por falta de acesso.** Construir expectativa analítica com dados mensais/trimestrais, aquisições e baixas de terrenos, situação de projetos e informação operacional pertinente, reconciliando as fontes às demonstrações auditadas. | Não executado. Nenhum dado interno, orçamento, razão contábil, cronograma de projetos ou base operacional foi disponibilizado. A confiabilidade, comparabilidade e controles dos dados não foram avaliados, como requer o item 5(b). A expectativa não foi desenvolvida nem avaliada quanto à precisão requerida pelo item 5(c); também não foi definido limiar de investigação nos termos do item 5(d). [1] |
| P2 | **Planejado por falta de acesso.** Investigar oscilações identificadas por indagação à administração e corroborar respostas com evidência apropriada; aplicar outros testes que a causa e os riscos exijam. | Não executado. Não houve entrevistas, solicitações à administração, exame de documentos, conciliações, confirmações externas ou inspeções físicas. Se realizado em auditoria, este passo atenderia à lógica do item 7; não se afirma aqui resposta, explicação ou corroborador obtido. [1] |
| P3 | **Planejado por falta de acesso.** Efetuar procedimentos analíticos perto do encerramento dos trabalhos, usando entendimento atualizado da entidade e o conjunto final das demonstrações, para apoiar a conclusão geral. | Não executado. Este trabalho não acompanhou uma auditoria, não teve acesso à compreensão do auditor sobre a entidade ou às demonstrações finais de auditoria e não forma conclusão geral segundo o item 6. [1] |
| S1 | **Simulado para fins didáticos; não executado.** Considerar, em um cenário hipotético de auditoria, a criação prévia de expectativa por movimentações de terrenos e dados não financeiros confiáveis e a comparação do realizado contra essa expectativa. | Sem valores simulados, sem limiar inventado e sem conclusão sobre a Companhia. O exercício apenas ilustra que uma expectativa suficientemente precisa, critérios de confiabilidade e tolerância de investigação precisariam ser estabelecidos antes de classificar diferença como aceitável ou exceção, conforme item 5. [1] |

## Evidências e referências cruzadas

- **REF-01 — CFC, Resolução nº 1.221/09, NBC TA 520, *Procedimentos Analíticos*.** Ficha da resolução informa publicação no DOU em 04/12/2009 e estado “em vigor”, sem alteração ou revogação. Texto oficial completo em PDF: itens 2–7 e orientações A1–A21. Para localização: item 2 e objetivo/definição, PDF oficial pp. 3–4; requisitos e exame dos resultados (itens 5–7), p. 5; aplicação e materiais explicativos, pp. 6–11. [1] [2]
- **REF-02 — CVM, DFP 2025, DIRECIONAL ENGENHARIA S.A., exercício findo em 31/12/2025, versão 1.** Consulta de informações financeiras no registro CVM, demonstrações consolidadas, quadro “Balanço Patrimonial Ativo”. Registro/data-base e quadros são navegáveis; a extração estruturada oficial CVM utilizada não tem páginas numeradas. Linhas identificadas por códigos de conta 1 (Ativo Total), 1.01.04 (Estoques) e 1.02.01.05.01 (Estoques de terrenos a incorporar); escala MIL. Para estoques circulantes, a linha 1.01.04; a classe não circulante aparece na hierarquia 1.02.01.05. [3] [4]
- **REF-03 — CVM, DFP 2025, relatório do auditor independente e PAA.** A interface HTML da CVM identifica o documento, mas não oferece paginação impressa estável. O relatório PwC foi lido no PDF direto da DFP 4T25 V1, pp. 115–117 (p. 116 para os PAA); a opinião sem modificação e os PAA de receita imobiliária e contingências são divulgações públicas, não evidência gerada por este trabalho. [3]
- **REF-04 — RI Direcional, Central de Resultados**, e **B3, perfil DIRECIONAL ENGENHARIA S.A.** Fontes públicas institucionais consultadas para localizar divulgações da companhia e conferir identificação e atividade principal. [5] [6]

**Rastreabilidade de cálculos:** A1 = (13.219.635 ÷ 10.067.406 − 1) × 100; A2 = (5.678.238 ÷ 4.587.823 − 1) × 100; A3 = 6.951.508 ÷ 13.219.635, 5.678.238 ÷ 13.219.635 e 5.678.238 ÷ 6.951.508; A4 = 2.086.835 ÷ 13.219.635. Valores arredondados a uma casa decimal. Aritmética refeita a partir dos saldos públicos; não foi recalculada a contabilidade subjacente.

## Exceções, conclusão e limitações

**Exceções identificadas:** nenhuma exceção de auditoria foi estabelecida. As variações e proporções acima são observações analíticas públicas e não foram comparadas com uma expectativa auditável ou tolerância formal. Por isso, não podem ser classificadas como erros, desvios, distorções ou conclusões de razoabilidade. Aumento dos saldos, isoladamente, não é evidência de anomalia.

**Conclusão didática:** a leitura pública indica que estoques representam 52,6% do ativo consolidado e terrenos a incorporar totais representam 43,0% do ativo e 81,7% dos estoques em 2025. Os saldos totais de terrenos cresceram 23,8% em relação a 2024, enquanto o ativo total cresceu 31,3%. A relevância quantitativa torna apropriado, em uma auditoria real, avaliar riscos e desenhar procedimentos adicionais. A evidência pública limitada deste papel, sem dados para uma expectativa suficientemente precisa, **não permite concluir** se estoques ou terrenos estão livres de distorção relevante, nem se o reconhecimento de receita, provisões ou demonstrações como um todo estão adequados.

**Limitações e salvaguardas:** não houve acesso a livros contábeis, contratos, escrituras, registros de propriedade, laudos, orçamento, dados operacionais, informações por projeto, previsões, controles internos, atas ou correspondência. Não houve confirmação externa, entrevista ou indagação, inspeção física, observação, recálculo do razão, teste de corte, teste de detalhes, avaliação de valor realizável líquido ou validação de premissas. Nenhum procedimento interno foi executado. As informações públicas foram usadas para análise descritiva e instrução; os registros oficiais estruturados não têm paginação PDF. O fato de a auditoria publicada ter opinião sem ressalva não substitui nem valida os procedimentos didáticos aqui descritos.

**Preparado por:** matrícula didática **EDU-AUD-001**  
**Data:** 22/10/2026  
**Revisão por:** ______________________________  
**Data da revisão:** ___________________________

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, Resolução 2009/001221, ficha NBC TA 520; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001221>).
- **Ref. 2** — CFC, Resolução 1.221/09, NBC TA 520, texto integral; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/RES_1221.pdf>).
- **Ref. 3** — CVM, DFP 2025 DIRECIONAL ENGENHARIA S.A., versão 1; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — CVM, Dados Abertos DFP 2025, demonstrações financeiras padronizadas; [abrir fonte](<https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip>).
- **Ref. 5** — Direcional, RI, Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 6** — B3, perfil de DIRECIONAL ENGENHARIA S.A.; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).


---

# PT-530 — Amostragem em auditoria

**Entidade/escopo de referência:** DIRECIONAL ENGENHARIA S.A. e controladas, demonstrações consolidadas encerradas em 31/12/2025. **Natureza:** exercício didático com população inteiramente sintética; não representa teste da Companhia nem trabalho da PwC. **Preparador:** matrícula didática EDU-AUD-001. **Data:** 22/10/2026. **Revisão:** campo em branco.

## Norma, objetivo e conta

**Norma:** NBC TA 530 — Amostragem em Auditoria, Resolução CFC nº 1.222/09, vigente para o exercício de 2025 segundo o cadastro oficial consultado. Itens 1–5 (objetivo/definições); 6–8 (desenho, tamanho e seleção); 9–11 (execução e itens sem evidência); 12–13 (causa de desvios/distorções); 14–15 (projeção e avaliação); aplicação A1–A23 e Apêndices 1 e 4. [1] [2]

**Objetivo deste PT:** documentar (i) conciliação de população sintética referente à rubrica integral de estoques com os saldos públicos da DFP e da Nota 5; (ii) seleção e execução de uma amostra aleatória e de uma seleção dirigida, ambas apenas sobre itens sintéticos; (iii) identificação de inconsistências implantadas; e (iv) limites da projeção monetária ilustrativa. A base não é razão, cadastro, contrato, unidade imobiliária, terreno ou registro real da Direcional. Os resultados não fornecem asseguração sobre as demonstrações de 2025.

**Conta de foco e materialidade:** Estoques é a maior rubrica individual do ativo consolidado, totalizando R\$6.951.508 mil em 31/12/2025 (BP pp.16–17; Nota 5, p.69). A Nota 5 discrimina imóveis concluídos de R\$99.063 mil, imóveis em construção de R\$1.174.207 mil e terrenos a incorporar de R\$5.678.238 mil. Terrenos são o maior componente (81,7% dos estoques; 43,0% do ativo), mas a população sintética abaixo cobre as três classes e concilia ao total da rubrica. Os estoques consolidados são R\$5.532.090 mil em 2024. A DFP integral pública e as páginas impressas pertinentes foram examinadas; a opinião e os PAA divulgados são contexto, não conclusão deste preparador. [3]–[6]

Como premissas didáticas coerentes com PT-320 e as planilhas: materialidade global = 0,75% do ativo total = R\$99.147.262; materialidade para execução = 70% da global = R\$69.403.084; materialidade específica de Estoques = 0,50% do saldo total = R\$34.757.540; claramente trivial = 5% da global = R\$4.957.363. Os percentuais são julgamentos simulados, não parâmetros da NBC TA nem materialidade estabelecida pela PwC.

## Afirmações e riscos

**Existência e direitos/obrigações.** Risco hipotético: cadastro sem suporte documental ou titularidade/condição jurídica não evidenciada. Em auditoria real, inspecionar contratos, matrículas, registros, pagamentos e documentos legais; confirmar ou inspecionar somente quando apropriado e autorizado.

**Avaliação e alocação.** Risco hipotético: custo ou capitalização incorretos; valor realizável líquido inferior ao contábil; dados de área ou avaliação desatualizados. Em auditoria real, reconciliar custo, testar apropriação, orçamento e premissas/VLR por empreendimento ou unidade e realizar análise de sensibilidade.

**Integridade.** Risco hipotético: população incompleta ou diferença entre cadastro, razão e demonstrações. Em auditoria real, validar a integridade da população e conciliá-la ao razão e à consolidação antes de selecionar itens.

**Classificação, apresentação e corte.** Risco hipotético: uso incorreto da classificação circulante/não circulante ou de datas e divulgações. Em auditoria real, testar documentos, política e critérios de realização próximos ao encerramento.

Os cenários acima não são constatações sobre estoques reais, controles ou conduta da administração. A relevância quantitativa de estoques orienta a prioridade, mas não demonstra distorção.

## População, fontes, unidade e método

**População sintética:** 500.000 registros distintos, cada um identificado por chave única `synthetic_item_id`, em `data/estoques_sinteticos.csv.gz`. São 420.000 posições sintéticas de terrenos, 75.000 unidades em construção e 5.000 unidades concluídas. A soma dos valores contábeis sintéticos é R\$6.951.508.000,00, exatamente igual ao saldo público consolidado de Estoques; diferença total: R\$0,00. As somas sintéticas por classe reconciliam, respectivamente, a R\$5.678.238.000,00, R\$1.174.207.000,00 e R\$99.063.000,00. A classificação sintética corrente soma R\$2.086.835.000,00 e a não corrente, R\$4.864.673.000,00. Os valores item a item, contratos, projetos, áreas, referências registrais e datas são inventados; a conciliação aritmética não valida qualquer registro real.

**Fontes societárias públicas examinadas:** DFP 4T25 V1 obtida diretamente no RI e consultada em conjunto com o registro CVM (NSD 155189) e o perfil B3. BP pp.16–17, DRE p.21, Nota 5 p.69, Nota 1.1 p.41 e relatório PwC pp.115–117. A leitura pública sustenta os fatos reportados, mas não substitui registros subjacentes. [3]–[6]

**Unidade amostral:** um item sintético individual da rubrica Estoques. **Amostra aleatória:** amostragem aleatória simples sem reposição por algoritmo de reservatório, semente fixa 20251232; cada registro tem a mesma chance teórica de seleção. **Seleção dirigida:** 200 maiores valores sintéticos, selecionados separadamente; houve uma unidade em comum com a SRS. A seleção dirigida não é probabilística nem projetável.

| Parâmetro do desenho ilustrativo para atributo binário | Cálculo/resultado |
|---|---:|
| Confiança e valor crítico aproximado | 95%; z = 1,96 |
| Proporção conservadora e precisão tolerável | p = 50%; ±5 pontos percentuais |
| n inicial, antes da correção finita | 384,16 |
| n com correção para N = 500.000 | 383,87; mínimo arredondado para cima = 384 |
| n aleatório executado | 1.000 registros (0,2% da população; 2,60 vezes o mínimo ilustrativo) |
| Seleção dirigida complementar | 200 maiores valores; não probabilística e não projetável |

Esse cálculo é apenas referencial didático para estimação de atributo em base sintética; não é desenho de auditoria de companhia real, não é seleção monetária proporcional à materialidade, não assegura detecção de distorção monetária e não substitui avaliação de risco, tolerância e população em trabalho efetivo.

## Procedimentos executados e planejados

| ID | Procedimento | Classificação obrigatória | Evidência/resultado |
|---|---|---|---|
| P1 | Ler a fonte normativa CFC e identificar vigência/itens pertinentes. | **Realizado com evidência pública** | Norma e itens registrados acima; sem avaliação do cumprimento por qualquer firma. [1] [2] |
| P2 | Inspecionar DFP pública e cotejar identidade/saldos publicados com RI/CVM/B3. | **Realizado com evidência pública** | Rubrica, classes, saldos e páginas citados no §1; sem tie-out a razão. [3]–[6] |
| P3 | Gerar a população sintética determinística, testar unicidade, recalcular a soma e reconciliar ao total de Estoques, às classes e aos saldos corrente/não corrente. | **Simulado para fins didáticos** | 500.000/500.000 IDs únicos; total de R\$6.951.508.000,00; reconciliação total, por classe e por classificação: diferença R\$0,00. Resultados em `analysis/PT530_resultados.json`. |
| P4 | Selecionar sem reposição 1.000 itens por SRS com semente 20251232 e exportar os itens. | **Simulado para fins didáticos** | `analysis/amostra_aleatoria_1000.csv`; seleção reproduzível em `scripts/analyze_synthetic_inventory.py`. |
| P5 | Selecionar os 200 maiores valores para teste dirigido separado da SRS. | **Simulado para fins didáticos** | `analysis/amostra_direcionada_top200.csv`; 200 IDs únicos; sobreposição de uma unidade com a SRS. Não projetar ao restante. |
| P6 | Aplicar regras de teste aos 500.000 registros e confrontar detecções com o registro conhecido das inconsistências implantadas. | **Simulado para fins didáticos** | Cinco categorias reproduzidas exatamente; zero falsos positivos e zero falsos negativos na população sintética conhecida. Ver §5. |
| P7 | Contar achados na SRS e estimar shortfall sintético de VLR, com erro amostral ilustrativo e intervalo aproximado. | **Simulado para fins didáticos** | Cinco ocorrências categóricas na amostra; projeção e intervalo no §5. Não extrapolável à Companhia. |
| P8 | Em auditoria real, obter cadastro analítico, comprovar integridade, reconciliar a razão, definir risco/tolerância, selecionar e testar itens reais e projetar distorções somente para população pertinente. | **Planejado por falta de acesso** | Nenhum cadastro, razão, título, contrato, custo por empreendimento, confirmação ou população real foi recebido; portanto não houve amostra de registros da Direcional. |

Não foram realizadas confirmação externa, entrevista, inspeção física, observação/contagem de estoque, consulta a registros internos ou teste de sistema. A base sintética é a única população efetivamente amostrada.

## Resultados, exceções e avaliação

### Teste da população sintética versus registro de injeções

| Categoria sintética | Injetadas | Detectadas | Não detectadas | Inesperadas | Correspondência exata |
|---|---:|---:|---:|---:|---|
| Documento dominial incompleto | 200 | 200 | 0 | 0 | Sim |
| Área inválida | 150 | 150 | 0 | 0 | Sim |
| VLR sintético abaixo do valor contábil | 500 | 500 | 0 | 0 | Sim |
| Incompatibilidade de classificação | 250 | 250 | 0 | 0 | Sim |
| Avaliação sintética desatualizada | 300 | 300 | 0 | 0 | Sim |

As cinco categorias foram implantadas em estratos disjuntos (1.400 itens no total). Zero não detectadas/inesperadas significa apenas que as regras reproduziram as injeções conhecidas na população artificial. Não é achado, teste ou inferência sobre a Direcional.

### Resultados da amostra aleatória simples

| Categoria encontrada na SRS (n = 1.000) | Itens sintéticos |
|---|---:|
| Documento dominial incompleto | 0 |
| Área inválida | 1 |
| VLR abaixo do valor contábil | 1 |
| Incompatibilidade de classificação | 1 |
| Avaliação desatualizada | 2 |

A seleção aleatória identificou cinco exceções sintéticas. A SRS não capturou todas as injeções existentes; a comparação com o registro integral de injeções demonstra risco de não detecção por amostragem. O resultado não mede taxa de erro real da Companhia.

### Projeção monetária sintética e conclusão sobre exceções

A soma dos shortfalls de VLR dos itens da SRS foi expandida linearmente por N/n. Estimativa ilustrativa de shortfall na população sintética: **R\$454.595,00**. O intervalo aproximado de 95%, calculado com desvio-padrão amostral e correção de população finita, é **R\$0,00 a R\$1.344.710,64**. O shortfall total efetivamente implantado na população foi **R\$1.191.323,15**. A diferença entre estimativa e valor implantado evidencia incerteza amostral; o valor real está dentro do intervalo. O estimador e o intervalo são didáticos e não são adequados para inferir distorção de Estoques da Direcional.

**Exceções da Companhia:** nenhuma foi identificada, pois não houve teste de item, registro, controle, título, custo ou VLR real. As exceções acima são todas simuladas e intencionalmente implantadas. A inexistência de achados reais neste PT decorre da falta de acesso a dados internos, não prova ausência de distorções.

## Arquivo e referências cruzadas

**Arquivos reproduzíveis:**

- População, registro das injeções e dicionário: `data/estoques_sinteticos.csv.gz`, `data/injection_register.json` e `analysis/dicionario_variaveis.csv`.
- Amostras e resultados: `analysis/amostra_aleatoria_1000.csv`, `analysis/amostra_direcionada_top200.csv`, `analysis/excecoes_detectadas_sinteticas.csv` e `analysis/PT530_resultados.json`.
- Planilha editável de amostragem/conciliação: `analysis/papel_amostragem_conciliacao.xlsx`.
- Código: `scripts/generate_synthetic_inventory.py` e `scripts/analyze_synthetic_inventory.py`.
- Valores-fonte e páginas: `FONTES.md`, IDs S1–S2.
- Referências cruzadas: PT-300/315 (risco), PT-320 (materialidade), PT-330 (resposta), PT-450 (distorções) e PT-500/501/540 (evidência, estoque e estimativas).

## Conclusão e limitações

A população sintética de Estoques foi gerada determinística e sem identificadores repetidos. Ela contém itens das três classes divulgadas, conciliou exatamente ao saldo público de R\$6.951.508.000,00 e às classes, e foi submetida a teste integral, SRS sem reposição e seleção dirigida. A execução detectou exatamente as cinco classes de inconsistências implantadas na população artificial; a amostra aleatória de 1.000 itens encontrou cinco ocorrências sintéticas e ilustra risco amostral. Essa evidência é adequada apenas para demonstrar o método com dados artificiais. **Não foi amostrado nem testado qualquer item real da Direcional e não há base para concluir sobre existência, direitos, avaliação, alocação, integridade, classificação ou saldo das demonstrações.** O trabalho não emite opinião ou asseguração e não modifica a opinião pública da PwC.

## Referências

[1] CFC, índice oficial das NBC TAs: https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/. Acesso em 22/10/2026.

[2] CFC, publicação oficial compilada NBC TA 200–810, NBC TA 530 a partir da p.335: https://cfc.org.br/wp-content/uploads/2018/04/Publicacao_NBC_TA_AUDITORIA.pdf. Acesso em 22/10/2026.

[3] CVM/RAD, DFP Direcional Engenharia S.A., 31/12/2025, V1, NSD 155189: https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1. Acesso em 22/10/2026.

[4] B3, perfil DIRECIONAL ENGENHARIA S.A., dados econômico-financeiros consolidados: https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br. Acesso em 22/10/2026.

[5] RI Direcional, Central de Resultados: https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/. Acesso em 22/10/2026.

[6] RI Direcional, DFP 4T25 V1, PDF integral: https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2. BP pp.16–17; DRE p.21; Nota 5 p.69; relatório PwC pp.115–117. Acesso em 22/10/2026.


---

# PT-540 — Auditoria de estimativas contábeis e divulgações relacionadas

**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações consolidadas  
**Exercício/data-base:** exercício encerrado em 31/12/2025  
**Código/título:** PT-540 — Auditoria de estimativas contábeis e divulgações relacionadas  
**Norma:** NBC TA 540 (R2), *Auditoria de Estimativas Contábeis, Inclusive do Valor Justo, e Divulgações Relacionadas*, Resolução CFC de 17/10/2019, publicada no DOU em 23/10/2019. O cadastro oficial do CFC indica a norma em vigor e não alterada nem revogada na data de acesso deste papel. Para o exercício de 2025, esta é a versão identificada como aplicável. Parágrafos centrais considerados: 1–7 (alcance, objetivo, definições); 8–19 (avaliação de riscos); 20–29 (respostas aos riscos e métodos, dados, premissas, incerteza e estimativa pontual/faixa); 30–32 (avaliação de razoabilidade, divulgações e indicadores de possível viés); 33–35 (representações, comunicação e documentação). Referência normativa oficial e situação consultadas em 22/10/2026. [1] [2]

> **Natureza e limite do documento:** papel de trabalho exclusivamente didático, preparado com fontes públicas examinadas. Não é parte do arquivo de auditoria da PwC nem de qualquer auditor independente. Não houve acesso a razão contábil, subrazões, contratos, matrículas, laudos, modelos, atas, cartas de assessores jurídicos ou outros registros internos. Nada neste PT declara que foram executadas confirmações, entrevistas, inspeções físicas, observação de controles ou testes sobre registros internos. As conclusões abaixo são limitadas à leitura de informação pública e ao desenho didático de procedimentos.

## 1. Objetivo, contas e processo

**Objetivo.** Demonstrar como, em uma auditoria didática, seriam identificadas e respondidas as áreas de estimativa contábil e respectivas divulgações com potencial de distorção relevante, nos termos da NBC TA 540 (R2), e documentar separadamente o que foi verificado em informação pública, o que permanece planejado por falta de acesso e o que é apenas simulado para ensino. Não se emite opinião nem conclusão de asseguração sobre as demonstrações financeiras.

**Conta/processo focal.** Estoques imobiliários consolidados, com atenção à mensuração e recuperabilidade de terrenos a incorporar, cuja rubrica foi informada como a maior rubrica individual do ativo. Processos correlatos considerados para planejamento: reconhecimento de receita imobiliária e provisões para contingências, ambas apontadas como Principais Assuntos de Auditoria (PAA) no relatório do auditor da DFP, conforme fato-base e documento público informado. O fato de figurarem como PAA não constitui, por si só, evidência de erro ou de inadequação contábil. [3]

**Enquadramento didático.** A NBC TA 540 requer que o auditor compreenda como a administração identifica a necessidade de estimativas, como as desenvolve e como seleciona métodos, premissas e dados, avalie risco inerente — inclusive incerteza de estimativa, complexidade, subjetividade e outros fatores — e desenhe respostas proporcionais aos riscos. O auditor também avalia a razoabilidade das estimativas e divulgações e considera possíveis indicadores de viés da administração. Este PT usa esses requisitos para estruturar procedimentos, mas não afirma que os passos planejados ocorreram na auditoria real. [1] [2]

## 2. Afirmações e riscos de distorção relevante

As afirmações a seguir são **riscos/hipóteses de auditoria a investigar**, não constatações sobre a companhia.

### 2.1 Estoques imobiliários e terrenos a incorporar

- **Mensuração, valorização e alocação:** hipótese de risco de que custos atribuídos a terrenos, projetos ou unidades não sejam suportados, alocados de forma consistente ou reduzidos quando o valor realizável líquido eventualmente ficar abaixo do custo. A magnitude do saldo divulgado torna essa área prioritária para resposta; não se conclui que haja perda ou erro.
- **Existência e direitos/obrigações:** hipótese de risco quanto à existência dos terrenos e aos direitos da entidade sobre eles, considerando a natureza imobiliária da rubrica. Isso exigiria, entre outros, títulos, contratos e registros de propriedade, não acessados neste trabalho.
- **Completude e corte:** hipótese de risco quanto à inclusão apropriada de aquisições, custos elegíveis, obrigações associadas e movimentos de encerramento do exercício.
- **Classificação e divulgação:** hipótese de risco de classificação entre circulante e não circulante, descrição das políticas e divulgações pertinentes. Os dados públicos consultados não permitem validar a composição analítica do saldo.

### 2.2 Receita imobiliária e provisões para contingências — áreas indicadas como PAA

- **Receita imobiliária:** hipótese de risco nas premissas e julgamentos usados para reconhecer receita ao longo do tempo ou em momento específico, incluindo mensuração do avanço, preço/contraprestação, custos estimados para conclusão, corte e divulgação, conforme a política efetivamente adotada. O conteúdo do modelo e as evidências de suporte não foram acessados. A referência a PAA é atribuída ao relatório de auditoria da DFP, não a uma conclusão deste PT.
- **Provisões para contingências:** hipótese de risco quanto à completude da população de processos, avaliação da probabilidade de saída de recursos, mensuração do valor e prazo, e suficiência de divulgações. Não foram consultados assessores jurídicos ou processos individuais; nenhuma provisão foi confirmada ou recalculada.

**Fatores de risco inerente — avaliação preliminar apenas.** A escala dos saldos divulgados e a natureza de incorporação/construção indicam que volatilidade de custo, prazos de projetos, condições dos terrenos, mudanças de mercado ou decisões de desenvolvimento poderiam afetar estimativas. São exemplos de fatores a investigar, não fatos atribuídos à Direcional. Complexidade, subjetividade e incerteza de estimativa para cada rubrica não podem ser classificadas definitivamente sem modelos, dados, premissas e processo da administração. Não se atribui nível de risco significativo nem se fixa materialidade, pois faltam materialidade do trabalho, granularidade por estimativa e entendimento interno requerido pelos itens 8–19 da NBC TA 540 (R2). [1] [2]

## 3. População, fontes e critérios

**População pública examinada.** Informações consolidadas de 31/12/2025 e comparativo de 31/12/2024 da DFP CVM identificada como versão 1 (V1), protocolo `021350DFP311220250100155189-71`, documento datado de 31/12/2025 e enviado em 09/03/2026. A tela da CVM identifica o auditor como PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. [3]

**Valores públicos considerados (R\$ mil).** Conforme o BP consolidado e a Nota 5 da DFP 4T25 V1 lidos no PDF direto do RI (pp. 16–17 e 69; fonte S2 em FONTES.md):

- Ativo total consolidado em 31/12/2025: **R\$ 13.219.635 mil**; comparativo em 31/12/2024: **R\$ 10.067.406 mil**.
- Estoques em 31/12/2025: **R\$ 6.951.508 mil**.
- Terrenos a incorporar totais em 31/12/2025: **R\$ 5.678.238 mil**, dos quais **R\$ 4.864.673 mil** são não circulantes; comparativo total em 31/12/2024: **R\$ 4.587.823 mil**, dos quais **R\$ 3.888.979 mil** são não circulantes.
- Estoques circulantes: **R\$ 2.086.835 mil**.

Os números são apresentados em milhares de reais conforme solicitado e sua composição não foi conciliada com balancetes internos. A página do registro CVM informa documento, versão, datas, auditor e quadros; o quadro eletrônico não oferece paginação impressa estável na visualização consultada. Por isso, as referências são pelo nome do documento e do quadro/área, sem atribuição de página não verificada. [3]

**Fontes societárias admitidas.** O fato societário e financeiro deste PT é referenciado a documentos/páginas da CVM, B3 e RI da companhia. A B3 identifica a companhia como DIRECIONAL ENGENHARIA S.A., código CVM 21350, ticker DIRR3 e atividade principal envolvendo incorporação, construção e comercialização de imóveis e serviços de engenharia. Essa descrição é contexto, não evidência de saldos ou estimativas. [4] A Central de Resultados do RI foi consultada como portal institucional; seu extrator é dinâmico e não expõe o arquivo no corpo, mas o PDF integral público foi obtido diretamente e as páginas relevantes foram examinadas. Não houve acesso à evidência subjacente ou ao arquivo privado de auditoria. [5]

**Critérios de auditoria/contábeis para a execução planejada.** NBC TA 540 (R2), demais NBC TA aplicáveis e políticas contábeis/divulgações constantes da DFP; para as questões contábeis específicas, o auditor do trabalho confirmaria a estrutura de relatório financeiro e os pronunciamentos contábeis efetivamente aplicáveis, inclusive critérios de estoques, receita e provisões. Não se presume neste PT uma política ou premissa da administração além das informações públicas expressamente identificadas.

**Populações internas necessárias, não disponibilizadas.** Para execução substantiva seriam necessários, conforme aplicável: cadastro completo dos terrenos e empreendimentos; composição de estoques e movimentações; razão/subrazão e conciliações; custo acumulado e orçamento/custo para conclusão por projeto; modelos e premissas de valor realizável; contratos de aquisição, documentação de titularidade e obrigações; relatório de evolução de obra e memória de cálculo de receita; relação completa de litígios e contingências; avaliações jurídicas; atas, aprovações e versões dos modelos; e memória das divulgações. Sem isso, não se pode afirmar integridade de população nem definir amostra.

## 4. Procedimentos e evidências

Cada procedimento recebe uma das classificações requeridas. “Realizado com evidência pública” significa somente leitura/checagem documental de informação disponível publicamente para este PT didático; não significa teste de auditoria sobre registros primários. “Planejado por falta de acesso” é procedimento a executar em trabalho com autorização e acesso. “Simulado” é atividade didática sem dado de companhia, seleção real ou resultado de auditoria.

### 4.1 Procedimentos realizados com evidência pública

| Ref. | Procedimento e classificação | Evidência/resultado público |
|---|---|---|
| P1 | **Realizado com evidência pública:** leitura da identificação da DFP e validação de data-base, versão e protocolo no registro da CVM. | DFP Direcional Engenharia S.A., 31/12/2025, V1, documento datado 31/12/2025 e enviado 09/03/2026; protocolo exibido na CVM `021350DFP311220250100155189-71`. A tela identifica PwC como auditor. Referência cruzada: E1. [3] |
| P2 | **Realizado com evidência pública:** transcrição dos saldos publicados no BP/Nota 5 do PDF integral da DFP para ativo consolidado, estoques, terrenos a incorporar e comparativos, mantendo unidade em R\$ mil. | Valores listados na seção 3, atribuídos ao quadro de DFs Consolidadas/Balanço Patrimonial Ativo e às notas da DFP CVM; não houve conciliação com registros internos. Referência cruzada: E1. [3] |
| P3 | **Realizado com evidência pública:** cálculo analítico simples dos valores relativos e variações ano a ano a partir dos montantes da seção 3. | Estoques/ativo total 2025 = 6.951.508 ÷ 13.219.635 = **52,58%**; terrenos totais/ativo total 2025 = 5.678.238 ÷ 13.219.635 = **42,96%**; terrenos totais/estoques = **81,68%**; crescimento nominal do total de terrenos de 2024 para 2025 = (5.678.238 − 4.587.823) ÷ 4.587.823 = **23,77%**; crescimento do ativo total = (13.219.635 − 10.067.406) ÷ 10.067.406 = **31,31%**. Cálculos próprios, não saldos adicionais reportados. Não foi definida expectativa de auditoria nem investigada variação por projeto. E1. [3] |
| P4 | **Realizado com evidência pública:** leitura da identificação cadastral da companhia na B3 para apoiar o enquadramento setorial e de atividade. | B3 apresenta Direcional Engenharia S.A., código CVM 21350, DIRR3 e atividade de incorporação/construção/comercialização de imóveis e serviços de engenharia. Não constitui teste de estimativa. E2. [4] |
| P5 | **Realizado com evidência pública:** leitura das áreas identificadas como PAA no relatório público do auditor, incorporado à DFP (pp. 115–117, especialmente p. 116). | Reconhecimento de receita imobiliária e provisões para contingências; opinião sem modificação conforme relatório público lido. A leitura de opinião sem ressalva não substitui evidência substantiva deste PT e não significa que o PT reexecutou os procedimentos de PwC. E1. [3] |

### 4.2 Procedimentos planejados por falta de acesso

Os itens abaixo são planos e não foram executados neste trabalho.

| Ref. | Procedimento planejado | Objetivo/afirmações e documentação a obter |
|---|---|---|
| P6 | Obter entendimento, com administração e responsáveis pelo processo, do fluxo de identificação, aprovação, contabilização e revisão das estimativas; mapear papéis, sistemas, controles e especialistas. | NBC TA 540, itens 8–12. Reuniões/entrevistas e inspeção de evidência de controle não realizadas. Avaliar risco inerente e de controle em conjunto com NBC TA 315; determinar respostas em conformidade com NBC TA 330. |
| P7 | Obter a listagem integral de estoques e terrenos por empreendimento, conciliar total ao razão e demonstrações e testar integridade, exatidão e classificação da população. Selecionar itens segundo materialidade e risco após obter a base. | Existência, completude, mensuração, classificação e apresentação. Conciliar circulante/não circulante e movimentações; investigar itens materiais e lançamentos manuais. Seleção ainda não definida porque não há universo, materialidade ou documentação. |
| P8 | Para terrenos selecionados, inspecionar contratos e documentos de titularidade/obrigações, conferir preço e custos elegíveis a comprovantes e registros, e avaliar alocação de custos a terrenos/projetos. | Direitos, existência e mensuração. Não alegar confirmação de propriedade ou inspeção documental nesta etapa; seriam procedimentos futuros, sujeitos à evidência obtida. |
| P9 | Avaliar métodos, dados e premissas de recuperabilidade/valor realizável dos terrenos e estoques; comparar premissas com informação observável disponível e recalcular modelo em amostra, incluindo sensibilidade a preço de venda, custos, prazo e absorção somente se relevantes no modelo efetivamente usado. | NBC TA 540, itens 20–29. Avaliar incerteza de estimativa e divulgações conforme itens 10–11 e 19. Considerar fatos posteriores relevantes conforme item 24 sem substituir evidência da data-base. Pressupostos acima são campos a investigar, não premissas constatadas da Companhia. |
| P10 | Para receita imobiliária, obter política contábil, contratos e memórias por empreendimento/unidade; testar critérios de reconhecimento, entradas do modelo, avanço/medição, custos estimados e corte antes/depois de 31/12/2025. Confrontar premissas e divulgações com evidência apropriada. | Ocorrência, exatidão, completude, corte e mensuração, conforme o modelo e política em uso. Não há amostra, cálculos ou evidência executada neste PT. |
| P11 | Obter lista integral de contingências, circularizar/solicitar resposta diretamente aos assessores jurídicos quando autorizado, inspecionar respostas, documentos dos casos e pagamentos/eventos posteriores; testar completude, avaliação e cálculo por caso. | Completude, mensuração, classificação e divulgação. Confirmações externas, consultas jurídicas e inspeção de processos não foram executadas. |
| P12 | Avaliar divulgações de estimativas e incerteza e documentar indicadores de possível viés da administração por estimativa e no conjunto, inclusive mudanças de método ou seleção assimétrica de premissas. Obter representações formais apropriadas ao final do trabalho. | NBC TA 540, itens 30–35. Avaliações, comunicações com governança e representações formais não foram obtidas. Representação da administração não substituiria outra evidência necessária. |

### 4.3 Procedimentos simulados para fins didáticos

- **S1 — Simulado:** exercício de desenho de resposta para terrenos a incorporar: em uma auditoria real, a população por projeto seria reconciliada ao razão, itens de maior risco selecionados e custos e premissas de recuperação testados. Nenhum projeto foi selecionado e nenhum custo, direito ou valor recuperável foi testado neste exercício didático.
- **S2 — Simulado:** exercício de cenário para sensibilidade: elaborar faixa de resultados razoavelmente possível variando premissas efetivamente usadas pela administração e comparar a faixa com valor registrado/divulgação, quando aplicável. Nenhuma premissa ou faixa foi calculada; qualquer número hipotético seria inadequado sem modelo e suporte, portanto não se inserem valores simulados.
- **S3 — Simulado:** exercício de resposta para contingências: compilar processos, obter avaliação jurídica e confrontar conclusões com provisão/divulgações. Não se simulou processo, probabilidade, valor nem confirmação jurídica; não existe resultado fictício.

## 5. Evidências e referências cruzadas

- **E1 — DFP CVM consolidada:** DIRECIONAL ENGENHARIA S.A., Demonstrações Financeiras Padronizadas, data-base 31/12/2025, versão 1, protocolo 021350DFP311220250100155189-71, envio em 09/03/2026. Quadros de “DFs Consolidadas” e “Balanço Patrimonial Ativo”, notas explicativas e relatório do auditor. Referência eletrônica sem paginação impressa estável na tela consultada; não se atribui número de página. Apoia P1–P3 e, segundo o fato-base do relatório da DFP, P5. [3]
- **E2 — Perfil da companhia na B3:** página Direcional Engenharia S.A., código CVM 21350, ticker DIRR3, consultada em 22/10/2026. Apoia somente P4 e contexto societário/setorial. [4]
- **E3 — Portal de RI:** Central de Resultados da Direcional, consultada em 22/10/2026. Serve como referência ao portal institucional; o extrator da página não exibe o arquivo no corpo, mas o PDF integral público foi obtido por link oficial e suas páginas relevantes foram examinadas. [5]
- **E4 — Norma:** CFC, NBC TA 540 (R2), resolução de 17/10/2019, publicação no DOU de 23/10/2019, cadastro oficial consultado em 22/10/2026. Apoia o enquadramento, os requisitos citados e a versão normativa. [1] [2]

## 6. Resultados, exceções e conclusão

**Resultado limitado da leitura pública.** O registro da CVM identifica DFP V1 da Direcional Engenharia S.A. de 31/12/2025, enviada em 09/03/2026, e auditor PwC. As páginas relevantes da DFP pública integral foram examinadas: ativo consolidado de R\$ 13.219.635 mil, estoques de R\$ 6.951.508 mil, terrenos a incorporar totais de R\$ 5.678.238 mil, dos quais R\$ 4.864.673 mil não circulantes, e estoques circulantes de R\$ 2.086.835 mil; o total de terrenos era R\$ 4.587.823 mil em 2024, dos quais R\$ 3.888.979 mil não circulantes, e o ativo total era R\$ 10.067.406 mil. Receita imobiliária e provisões para contingências são os PAA indicados, e a opinião foi sem ressalva. Os cálculos analíticos em P3 mostram concentração quantitativa relevante do saldo divulgado, mas não identificam distorção. Não houve acesso à evidência subjacente, aos registros internos ou ao arquivo privado da auditoria. [3]

**Exceções/limitações.** Não foram disponibilizados dados para avaliar integridade da população, construir amostra, testar controles, recalcular estimativas, examinar documentos de titularidade, confirmar saldos, circularizar advogados, entrevistar administração, inspecionar fisicamente terrenos ou projetos, revisar modelos de gestão ou avaliar estimativas individualmente. Por conseguinte, não há exceção de auditoria apurada nem ausência de erro concluída. Não se pode concluir sobre adequação dos saldos, razoabilidade de estimativas, suficiência de provisões, reconhecimento de receita ou adequação de divulgações. Não se atribuem afirmações de existência, confirmação ou inspeção executadas.

**Conclusão didática.** À luz somente dos dados públicos identificados, estoques — especialmente terrenos a incorporar — devem receber atenção de planejamento por sua magnitude e natureza estimativa. Receita imobiliária e provisões para contingências também integram as áreas a considerar por estarem identificadas como PAA no relatório da DFP. Esses elementos sustentam risco/hipótese e desenho de procedimentos adicionais, não uma constatação de distorção nem conclusão de auditoria. A avaliação final sob NBC TA 540 (R2) depende dos procedimentos planejados P6–P12, de evidência apropriada e suficiente e da consideração conjunta de materialidade, riscos e estrutura de relatório financeiro. Este papel didático não modifica nem reexpressa a opinião do auditor independente.

## 7. Preparação e revisão

**Preparador:** matrícula didática **EDU-AUD-001**  
**Data:** **22/10/2026**  
**Revisor:** ______________________________  
**Data da revisão:** _______________________  
**Conclusão/referência da revisão:** __________________________________________

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA de Auditoria Independente de Informação Contábil Histórica, listagem de normas, acesso em 22/10/2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, NBC TA 540 R2, Resolução de 17/10/2019 e cadastro da norma, acesso em 22/10/2026; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2019/NBCTA540%28R2%29&arquivo=NBCTA540%20%28R2%29.doc>).
- **Ref. 3** — CVM, DIRECIONAL ENGENHARIA S.A., DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71, quadros consolidados, notas e relatório do auditor, envio em 09/03/2026; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3, perfil de companhia listada, DIRECIONAL ENGENHARIA S.A., DIRR3, código CVM 21350, acesso em 22/10/2026; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — Direcional Engenharia S.A., RI, Central de Resultados, acesso em 22/10/2026; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-550 — Partes relacionadas

**Entidade:** DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações contábeis consolidadas  
**Exercício:** encerrado em 31/12/2025  
**Código/título:** PT-550 — Partes relacionadas  
**Norma:** NBC TA 550 — Partes Relacionadas, itens 1–28 e aplicação A1–A50, com ênfase nos itens 9–28, Resolução CFC nº 1.224/09, vigente para períodos iniciados em ou após 01/01/2010. O cadastro oficial do CFC a indica vigente e alterada pela Revisão NBC20, publicada em 06/12/2023, em decorrência da NBC TA 600 (R2). Base normativa consultada: texto oficial CFC em PDF, versão publicada; ver referências [1] e [2].  
**Data de acesso das fontes:** 22/10/2026  
**Preparador:** EDU-AUD-001 (matrícula didática) — 22/10/2026  
**Revisor:** ____________________________________ (em branco)

> **Natureza do documento:** papel de trabalho exclusivamente didático, preparado com dados públicos acessíveis e premissas factuais fornecidas no enunciado. Não representa auditoria, asseguração, revisão ou validação das demonstrações financeiras. Nenhum acesso interno, confirmação, entrevista, inspeção física ou procedimento de auditoria sobre livros e documentos da Companhia foi executado.

## 1. Objetivo, conta e processo

**Objetivo.** Modelar procedimentos pertinentes à NBC TA 550 para identificar, avaliar e responder a riscos de distorção relevante decorrentes de relacionamentos e transações com partes relacionadas, e avaliar, em tese, sua contabilização e divulgação nas demonstrações consolidadas de 2025. A Norma atribui ao auditor o objetivo de obter entendimento suficiente dos relacionamentos e transações para reconhecer fatores de risco de fraude, concluir se as demonstrações são afetadas e obter evidência de que a identificação, contabilização e divulgação atendem à estrutura aplicável (itens 9–10 e 25–26; [1], pp. 4–8).

**Conta/processo abrangido.** Todas as contas, classes de transações, saldos, compromissos e divulgações da controladora e controladas que possam envolver partes relacionadas; identificação de partes e beneficiários, consolidação/eliminações, aprovações e divulgação. A atenção didática é ampliada para estoques imobiliários e terrenos para incorporação, mas não se presume que tenham sido transacionados com partes relacionadas. A DFP identificada é a Demonstração Financeira Padronizada consolidada de 31/12/2025, V1, protocolada na CVM em 09/03/2026; a tela RAD/CVM indica PwC como auditor [3].

## 2. Afirmações e riscos

**Afirmações relevantes:** completude das partes e operações; ocorrência/existência dos saldos e transações; exatidão, mensuração e classificação; corte; autorização/aprovação; apresentação e divulgação, incluindo natureza do relacionamento, montantes, saldos/compromissos e condições exigidas pela estrutura contábil aplicável. A consideração de materialidade deve atender ao valor e também à natureza do relacionamento (NBC TA 550, item 25 e A46–A47; [1], pp. 12–13).

**Riscos inerentes — hipóteses para planejamento, não constatações:**

- Possível omissão de parte ou transação relacionada não identificada pela administração, inclusive por estruturas societárias, influência significativa ou controle comum não observáveis nos recortes públicos (itens 11–15 e 21–22). A informação de acionistas publicada pela B3 é limitada a posições divulgadas e não constitui, isoladamente, mapa completo de partes relacionadas [5].
- Possível distorção de completude, ocorrência, mensuração, corte ou divulgação de transações significativas fora do curso normal. A NBC TA 550 requer tratá-las como risco significativo e examinar fundamento econômico, termos, contabilização, divulgação e aprovação (itens 18 e 23; [1], pp. 10–12). Não há evidência pública aqui examinada de que tais operações ocorreram.
- Hipótese de risco acrescido em operações com terrenos, incorporações, sociedades de propósito específico, permutas, adiantamentos ou financiamentos entre entidades do grupo e terceiros relacionados, se existentes. A hipótese decorre da relevância quantitativa da rubrica reportada, não de evidência de contraparte relacionada. Segundo os fatos públicos examinados, o ativo consolidado foi R\$ 13.219.635 mil, estoques R\$ 6.951.508 mil, dos quais terrenos a incorporar totais R\$ 5.678.238 mil (incluindo R\$ 4.864.673 mil não circulantes) e estoques circulantes R\$ 2.086.835 mil; em 2024, ativo R\$ 10.067.406 mil e terrenos a incorporar totais R\$ 4.587.823 mil (componente não circulante R\$ 3.888.979 mil). As páginas relevantes da DFP integral foram examinadas; não houve acesso à evidência subjacente ou aos registros internos. A B3 publica o ativo total consolidado 2025 de R\$ 13.219.635 mil [5].
- Hipótese de risco de influência dominante, conluio ou burla de controles para distorção fraudulenta, a avaliar apenas com evidência apropriada (itens 19 e A29–A30). Não é conclusão sobre a Companhia.
- O PAA informado no enunciado refere-se a reconhecimento de receita imobiliária e provisões para contingências; não demonstra por si só risco ou transação com parte relacionada. Deve ser usado como contexto para coordenação com os papéis de trabalho de receita/estimativas, sem inferir partes relacionadas.

**Risco específico preliminar:** elevado quanto à completude da identificação e à divulgação, sujeito à obtenção de registros internos. A alta materialidade relativa dos estoques e terrenos reforça a relevância da análise das contrapartes, mas não permite concluir que o risco de partes relacionadas esteja efetivamente presente nem quantificar distorção. A classificação final e significância permanecem pendentes de materialidade global/de execução e evidência da auditoria completa.

## 3. População, fontes e critérios

**População pretendida (não disponibilizada):** cadastro de partes relacionadas e beneficiários finais; estrutura legal e consolidação do grupo; razão geral e subrazões completos de controladora e controladas; transações e saldos com contrapartes; contratos/alterações; atas de acionistas, conselho e comitês; aprovações; confirmações externas e correspondência jurídica/bancária; declarações formais da administração; e divulgações das demonstrações. A população deveria abranger o exercício integral, 01/01–31/12/2025, e saldos/compromissos na data-base.

**Fontes públicas consideradas:**

1. Registro da DFP no RAD/CVM, documento 155189: empresa, data-base, versão, protocolo, envio e auditor [3]. A interface CVM é dinâmica e não oferece paginação impressa estável; ela foi usada para metadados, não como substituta do PDF examinado.
2. PDF integral DFP 4T25 V1 obtido diretamente pela Central de Resultados do RI [7]. Foram examinados o balanço (pp.16–17), Nota 5 (p.69), Nota 6 — Partes relacionadas (pp.70–71) e relatório do auditor (pp.115–117). A leitura pública confirma as divulgações referidas neste PT, mas não testa completude contra registros internos.
3. Página B3 da DIRECIONAL ENGENHARIA S.A.: identificação da companhia, atividade, quadro econômico-financeiro e ativo total consolidado 2025 de R\$ 13.219.635 mil [5]. A posição acionária divulgada limita-se aos acionistas acima dos limiares nela indicados; não constitui mapa completo de partes relacionadas.
4. Central de Resultados do RI como índice institucional [4], e texto oficial CFC NBC TA 550 e cadastro de vigência/alteração [1–2].

**Critérios:** NBC TA 550, especialmente itens 11–19 (avaliação de risco), 20–24 (respostas), 25 (avaliação contábil e divulgação), 26 (representações formais), 27 (governança), 28 (documentação), A8–A28 e A29–A50; estrutura contábil aplicável brasileira referida pela DFP. A Nota 6 foi examinada nas páginas impressas 70–71; não foram obtidos cadastro interno, razão, contratos nem evidência para concluir sobre completude ou adequação de todas as relações/transações.

## 4. Procedimentos

| Procedimento e referência | Status | Evidência/limite |
|---|---|---|
|Inspecionar o registro RAD/CVM para identificar entidade, DFP consolidada, data-base, V1, data de envio e auditor indicado; documentar referência da fonte.|**Realizado com evidência pública**|A tela do documento 155189 identifica DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71, envio 09/03/2026 e PwC [3]. Inspeção apenas da página pública, sem reauditoria do parecer ou relatório de auditoria.| 
|Confrontar o ativo total consolidado 2025 publicado no perfil B3 com o fato-base do enunciado.|**Realizado com evidência pública**|B3 lista R\$ 13.219.635 mil em 31/12/2025 [5]; a confirmação é limitada à apresentação do dado pela B3, sem rastrear ao razão ou PDF da DFP.| 
|Ler a DFP integral e confrontar estoques/terrenos, comparativos, Nota 6 de partes relacionadas, PAA e opinião com as páginas impressas correspondentes.|**Realizado com evidência pública**|PDF RI examinado: balanço pp.16–17; Nota 5 p.69; Nota 6 pp.70–71; relatório PwC pp.115–117. A leitura confirma saldos e divulgações públicas, mas não constitui teste de completude, concordância com razão ou reexecução do trabalho da PwC. [7]| 
|Obter da administração relação integral de partes relacionadas, natureza dos vínculos e transações; indagar outros empregados pertinentes e entender controles de identificação, registro, divulgação, autorização e aprovação (itens 13–14).|**Planejado por falta de acesso**|Requer cadastro, entrevistas/indagações e documentação interna não disponibilizados. Não realizado.| 
|Discutir na equipe os riscos de omissão, influência dominante, fraude e transações incomuns; compartilhar a informação sobre partes relacionadas com a equipe de grupo (itens 12, 17–19; A9–A13).|**Planejado por falta de acesso**|Não houve equipe de auditoria nem comunicação de grupo nesta atividade didática. Considerar, em auditoria real, solicitações aos auditores dos componentes conforme NBC TA 600 aplicável.| 
|Cruzar a relação fornecida pela administração com cadastro societário, declarações de conflito, atas, livros societários e documentos públicos CVM/B3/RI; testar completude e vínculos até beneficiário final.|**Planejado por falta de acesso**|Não foram disponibilizados cadastro interno, declarações ou atas completas. O quadro acionário B3 é apenas fonte pública parcial; não foi tratado como população completa.| 
|Inspecionar razão, contratos, confirmações bancárias/jurídicas, atas e outros registros para buscar relações/transações não informadas; investigar acordos incomuns e determinar natureza e possível vínculo relacionado (itens 15–16, 21–22).|**Planejado por falta de acesso**|Os itens normativos orientam o trabalho, mas esses registros e confirmações não foram obtidos; nenhuma confirmação foi solicitada ou recebida.| 
|Selecionar amostra com base em risco de transações/saldos identificados; inspecionar contratos, aprovações, racionalidade econômica, contabilização, divulgação, exatidão e corte; testar eliminações de consolidação (itens 20–23).|**Planejado por falta de acesso**|Não há razão, listagem de transações, contratos, tamanho de população ou materialidade para seleção. Nenhuma amostra foi selecionada nem testada.| 
|Para terrenos/estoques, rastrear movimentos e saldos por empreendimento/contraparte, documentos de aquisição ou permuta, registros de titularidade, valores e partes, eliminando relações intragrupo quando apropriado.|**Planejado por falta de acesso**|A magnitude reportada motiva a proposta, mas não houve inspeção física, documental ou teste de saldo. Nenhum terreno foi observado ou confirmado.| 
|Avaliar divulgações de vínculos, transações, saldos e termos segundo a estrutura aplicável; obter representações formais e comunicar questões significativas à governança (itens 25–27).|**Planejado por falta de acesso**|Não foram obtidos registros internos completos, carta de representação ou documentação de governança. A Nota 6 pública foi lida, mas não testada contra essas evidências. Não houve solicitação ou comunicação.| 
|Aplicar cenário didático de transação relevante fora do curso normal, sem afirmar ocorrência: inspecionar contrato, motivação econômica, aprovação e contabilização, e avaliar resposta a risco significativo/fraude.|**Simulado para fins didáticos**|Simulação de desenho de procedimento baseada nos itens 18, 19 e 23. Não constitui teste nem evidência sobre fato real da Companhia.| 

## 5. Evidências e referências cruzadas

- **E-01 — registro DFP/CVM:** [3], protocolo indicado acima; a tela RAD/CVM identifica DFP 31/12/2025 V1, envio e PwC como auditor, mas não oferece paginação impressa estável. O documento integral foi obtido no RI e examinado separadamente, conforme E-04/E-05 e [7].
- **E-02 — perfil B3:** [5], “Dados Econômico-Financeiros — Balanço Patrimonial — Consolidado”, colunas 31/12/2025 e 31/12/2024. O ativo total é R\$13.219.635 mil e R\$10.067.406 mil, respectivamente. Estoques/terrenos e Nota 6 têm evidência direta adicional em [7].
- **E-03 — RI:** [4] é o índice institucional; dele foi obtido o PDF DFP 4T25 V1 em [7]. Páginas impressas da fonte direta: BP pp.16–17, Nota 5 p.69, Nota 6 pp.70–71 e relatório do auditor pp.115–117.
- **E-04 — norma:** [1], Resolução CFC 1.224/09/NBC TA 550, PDF oficial de 22 páginas; identificação e índice no início, itens 9–28 nas pp. 5–13; [2] cadastro CFC da revisão NBC20.
- **E-05 — Nota 6, partes relacionadas:** DFP direta do RI [7], pp.70–71. No consolidado, a Nota 6.1 apresenta ativos de R\$92.922 mil (2025) e R\$71.054 mil (2024), passivos de R\$214.534 mil (2025) e R\$101.094 mil (2024), mútuos/contas correntes com empreendimentos, dividendos a receber da Riva e fretamento de aeronaves da ALVG por R\$1.488 mil em 2025. A p.71 apresenta remuneração total da administração e Conselho Fiscal de R\$23.020 mil (2025) e R\$15.560 mil (2024). São divulgações examinadas, não saldos reconciliados nem evidência de completude.
- **Referências cruzadas de auditoria (propostas; não existentes como pastas de trabalho executadas):** PT-315/550 para avaliação de risco; PT-240 para fraude; PT-330/500 para resposta e evidência; PT-600 para consolidação/componentes; PT-450 para distorções; PT-700 para conclusão/opinião. Números são rótulos didáticos, não evidência de documentação de auditoria real.

## 6. Resultados, exceções, conclusão e limitações

**Resultados de procedimentos realizados.** A consulta ao RAD/CVM confirmou a identificação da DFP V1 e PwC [3]; o perfil B3 apresenta ativo consolidado de R\$13.219.635 mil em 31/12/2025 [5]. A leitura da DFP integral do RI [7] confirmou os saldos de estoques/terrenos (BP pp.16–17 e Nota 5 p.69), a Nota 6.1 (pp.70–71) e a identificação dos PAA/opinião no relatório PwC (pp.115–117). A Nota 6 divulga, entre outros, ativos/passivos consolidados com partes relacionadas e fretamento da ALVG. O exame foi documental e público: nenhum saldo foi rastreado ao razão, e nenhuma relação não divulgada foi pesquisada em bases internas.

**Exceções/pendências.** Não disponíveis para este trabalho: lista completa da administração, organograma/beneficiários finais, razão e lançamentos, contratos e aditivos, atas/aprovações, confirmações, representação formal, políticas e evidência de controles. A Nota 6 pública foi examinada, mas não se testou sua completude contra tais registros. Não houve exceção substantiva identificada; ausência de achado neste escopo não equivale a ausência de partes ou transações omitidas.

**Conclusão didática.** A evidência pública examinada sustenta que a DFP divulga, na Nota 6 (pp.70–71), determinados relacionamentos, saldos e transações e, no relatório PwC (pp.115–117), os PAA e a opinião publicada. Isso não é evidência apropriada e suficiente para concluir sobre completude de partes/transações, exatidão dos saldos, condições de mercado, autorizações, eliminações ou adequação integral da divulgação. Em trabalho real, a conclusão deste PT permaneceria **pendente** até obtenção e teste dos registros subjacentes e procedimentos complementares.

**Limitações e salvaguardas.** Esta é uma auditoria didática simulada, não relatório de auditor independente. A DFP integral pública foi examinada nas páginas indicadas, mas não houve entrevista, confirmação externa, inspeção física, consulta a razão, teste de controle, amostragem de registros reais, teste substantivo, solicitação de representação ou comunicação com governança. O papel não verifica a completude da Nota 6 e não reexecuta procedimentos da PwC. Fatores sem suporte foram tratados somente como hipóteses de risco; nenhum risco hipotético foi convertido em achado.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, Resolução nº 1.224/09, NBC TA 550 — Partes Relacionadas, texto oficial, PDF de 22 páginas; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/RES_1224.pdf>).
- **Ref. 2** — CFC, cadastro oficial da Resolução 2009/001224 e situação de vigência; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2009/001224>).
- **Ref. 3** — CVM, DIRECIONAL ENGENHARIA S.A., DFP 31/12/2025 V1, protocolo 021350DFP311220250100155189-71, tela do documento; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — Direcional Engenharia, RI, Central de Resultados e acesso a documentos financeiros; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 5** — B3, DIRECIONAL ENGENHARIA S.A., perfil e Dados Econômico-Financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 6** — CFC, Revisão NBC20, publicada em 06/12/2023, alteração normativa decorrente da NBC TA 600 (R2); [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?codigo=2023/NBC20>).
- **Ref. 7** — RI Direcional, DFP 4T25 V1; BP pp.16–17, Nota 5 p.69, Nota 6 pp.70–71 e relatório PwC pp.115–117; acesso em 22/10/2026; [abrir fonte](<https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2>).


---

# PT-560 — Eventos subsequentes

## Identificação, norma e itens

**Código:** PT-560  
**Título:** Eventos subsequentes — auditoria didática das demonstrações contábeis consolidadas  
**Entidade:** Direcional Engenharia S.A. e controladas  
**Exercício:** encerrado em 31/12/2025  
**Data de acesso/execução didática:** 22/10/2026  
**Preparador:** matrícula didática EDU-AUD-001  
**Revisor:** ____________________________________  
**Data da revisão:** __________________

**Norma aplicável ao período:** NBC TA 560 (R1) — *Eventos Subsequentes*, Resolução CFC 2016/NBCTA560(R1), publicada no DOU em 05/09/2016. Na página oficial do CFC consultada em 22/10/2026 a R1 consta como vigente, não alterada e não revogada. É a versão identificada para este papel de trabalho sobre o exercício de 2025. A norma tem vigência para auditorias de períodos iniciados em ou após 01/01/2010. [1] [2]

**Itens considerados:** NBC TA 560 (R1), itens 1–5 (alcance, tipos de evento, objetivo e definições); 6–9 (procedimentos até a data do relatório do auditor e representação formal); 10–13 (fatos conhecidos após o relatório e antes da divulgação das demonstrações); e 14–17 (fatos conhecidos após a divulgação). Materiais explicativos considerados para desenhar os testes: A1–A10, A11–A17 e A18–A20. A norma distingue a data das demonstrações, a data de aprovação, a data do relatório do auditor e a data de divulgação; essas datas não são intercambiáveis. [2]

## Objetivo, contas e processo

Obter, no contexto de um exercício didático, evidência apropriada e suficiente para avaliar se os eventos entre 31/12/2025 e a data do relatório do auditor que exigiam ajuste ou divulgação foram identificados e refletidos nas demonstrações consolidadas; e definir a resposta apropriada a fatos relevantes que possam ter chegado ao conhecimento do auditor após o relatório, conforme a janela e as condições dos itens 10–17 da NBC TA 560 (R1). Este documento não representa auditoria executada nem expressa opinião sobre as demonstrações financeiras.

**Processo em foco:** identificação, avaliação, ajuste/apresentação e divulgação de eventos subsequentes; leitura de atas e informações financeiras intermediárias; consulta à administração e, quando apropriado, aos responsáveis pela governança; obtenção de representação formal; avaliação de fatos conhecidos após o relatório ou após a divulgação.

**Contas e divulgações de interesse para a seleção de risco:** estoques imobiliários — com destaque para terrenos a incorporar —, provisões e divulgações de contingências, reconhecimento de receita imobiliária e demais rubricas potencialmente afetadas por fatos subsequentes. A seleção é orientada por relevância aparente e julgamentos contábeis, e **não** implica que tenha sido identificada distorção.

## Afirmações e riscos

Afirmações pertinentes: **integridade** de eventos e divulgações; **avaliação e alocação** de estimativas, provisões e ativos; **existência/ocorrência** de condições e transações; **corte** entre períodos; e **apresentação e divulgação** adequada de eventos que demandem ajuste ou divulgação.

A DFP pública integral de 2025, obtida no RI e examinada nas páginas relevantes, apresenta ativo consolidado de R\$13.219.635 mil, estoques de R\$6.951.508 mil, terrenos a incorporar totais de R\$5.678.238 mil, dos quais R\$4.864.673 mil são não circulantes, e estoques circulantes de R\$2.086.835 mil. O comparativo é ativo consolidado de R\$10.067.406 mil e terrenos a incorporar totais de R\$4.587.823 mil em 2024, dos quais R\$3.888.979 mil são não circulantes. Por cálculo aritmético sobre esses dados, os terrenos totais representam aproximadamente 81,7% dos estoques e 43,0% do ativo consolidado de 2025. Esses percentuais são apenas análise de contexto, não limiar de materialidade. Não houve acesso à evidência subjacente, aos registros internos ou ao arquivo privado da auditoria. [3] [4]

A DFP pública integral foi obtida no RI e o relatório do auditor foi examinado nas pp. 115–117 (p. 116 para PAA). Ele identifica PAA de reconhecimento de receita imobiliária e provisões para contingências e contém opinião sem modificação. São informações do relatório publicado que orientam a pesquisa de fatos posteriores, não uma conclusão autônoma deste PT nem reexecução dos procedimentos da PwC. A interface HTML da CVM identifica a PwC como auditora, mas não oferece paginação impressa; ver S2 em FONTES.md. [3]

**Riscos considerados — hipóteses, não constatações:** (i) evento não registrado ou divulgação incompleta; (ii) evidência posterior que confirme condição já existente em 31/12/2025, inclusive para estimativas de receita, estoque/terreno ou contingências; (iii) evento não ajustável cuja natureza ou estimativa de efeito demande divulgação; (iv) incorreta distinção entre condição existente na data-base e condição que surgiu depois; (v) fato relevante conhecido após o relatório, mas antes da divulgação, não comunicado ou não tratado adequadamente; e (vi) fato conhecido após a divulgação que, se conhecido na data do relatório, poderia ter levado a alteração do relatório. A dimensão dos estoques e os PAA tornam esses temas relevantes para planejamento, mas, isoladamente, não demonstram erro, deterioração, litígio ou evento subsequente.

## População, fontes e critérios

**População de auditoria a obter internamente:** todos os eventos e transações ocorridos de 01/01/2026 até a data do relatório do auditor independente; fatos conhecidos entre a data do relatório e a data de divulgação das demonstrações; e, para a resposta limitada dos itens 14–17, fatos que chegassem ao conhecimento do auditor após a divulgação. A data exata do relatório, da aprovação das demonstrações e da primeira disponibilização pública conjunta do relatório e das demonstrações deve ser confirmada no documento original e nos registros de emissão. O protocolo da DFP em 09/03/2026 é uma data de envio informada para o formulário, não substitui por si só essas três datas normativas. [2] [3]

**Fontes públicas examinadas:** (a) registro/página CVM da DFP indicada, DFP de 31/12/2025, V1, informada como protocolada em 09/03/2026; (b) perfil de companhia da B3 para Direcional Engenharia S.A., inclusive dados econômico-financeiros consolidados; (c) páginas e documentos de Relações com Investidores da companhia para informações financeiras e comunicados societários; e (d) texto e cadastro oficiais da NBC TA 560 (R1) no CFC. Os fatos societários neste PT são referidos somente a documentos CVM, B3 ou RI da companhia. [1] [2] [3] [4] [5] [6]

**Critérios de classificação dos procedimentos:**

- **Realizado com evidência pública:** exame de fonte pública identificada e registro restrito do que ela efetivamente mostra. Não equivale a confirmação independente da completude da população nem a trabalho de auditoria com acesso à entidade.
- **Planejado por falta de acesso:** procedimento requerido ou apropriado que depende de administração, governança, sistemas, atas não publicadas, documentos de suporte ou papéis de auditoria não disponíveis neste exercício didático.
- **Simulado para fins didáticos:** exercício hipotético de aplicação do critério, sem representar evento, saldo, procedimento ou conclusão da Direcional.

**Critério técnico:** itens 6–9 da NBC TA 560 (R1) para a janela até a data do relatório; itens 10–13 para fato conhecido após o relatório e antes da divulgação; itens 14–17 para fato conhecido após a divulgação. Para classificar eventos, a equipe deve apurar quando a condição subjacente surgiu e quando foi conhecida, e não apenas a data da notícia ou do documento. A avaliação de ajuste ou divulgação deve seguir a estrutura contábil aplicável e ser corroborada nos demonstrativos e notas efetivamente emitidos. [2]

## Procedimentos, status e evidências

| Ref. | Procedimento e classificação | Evidência/referência cruzada | Resultado / alcance |
|---|---|---|---|
| P-01 | **Realizado com evidência pública.** Consultar o cadastro do CFC para identificar versão, vigência e itens da NBC TA 560 (R1). | E-01: cadastro oficial CFC, resolução 2016/NBCTA560(R1), e E-02: PDF oficial CFC, texto NBC TA 560 (R1), especialmente itens 1–17 e A1–A20. | O cadastro informa publicação em 05/09/2016 e status vigente, não alterada e não revogada na consulta de 22/10/2026. Os itens aplicáveis estão listados acima. Não é evidência sobre a execução dos controles da companhia. [1] [2] |
| P-02 | **Realizado com evidência pública, com alcance limitado.** Consultar o perfil B3 e confrontar o ativo consolidado de 31/12/2025 com o dado-base informado para a DFP. | E-03: perfil B3, seção “Dados Econômico-Financeiros — Balanço Patrimonial — Consolidado”. | A página B3 exibe ativo total consolidado de R\$13.219.635 mil em 31/12/2025. Os saldos de estoques e terrenos foram lidos no PDF direto da DFP (BP pp. 16–17; Nota 5 p. 69, S2 em FONTES.md), sem conciliação a razão nem teste de lançamentos, existência ou avaliação. [4] |
| P-03 | **Realizado com evidência pública, limitado a documentos localizados.** Consultar a página CVM indicada para identificar informações de arquivamento e o auditor divulgado para a DFP. | E-04: página CVM do documento/formulário da companhia, DFP de 2025 referida no escopo. | O trecho público retornado identifica PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA. como auditor. A interface CVM não oferece paginação estável; a DFP pública integral foi obtida por canal oficial e suas páginas relevantes foram examinadas. Data de protocolo 09/03/2026 e versão V1 foram confrontadas com a identificação pública; não houve acesso à evidência privada da auditoria. [3] |
| P-04 | **Realizado com evidência pública; busca direcionada, não abrangente.** Consultar comunicados/atas publicados pela RI e identificar eventos noticiados em 2026 que demonstrem a necessidade de determinar a janela temporal correta. | E-05: Ata de Reunião do Conselho de Administração de 13/10/2026, itens 4–5; E-06: Comunicado ao Mercado de 13/10/2026 sobre modificação de oferta; E-07: Comunicado ao Mercado de 16/10/2026 sobre participação acionária relevante. | A ata de 13/10/2026 registra rerratificação de emissão de debêntures e operação de CRI; entre seus termos, descreve valor total de R\$250 milhões para a emissão de debêntures, sujeito às condições ali previstas. O comunicado de 13/10/2026 trata da oferta de CRI lastreados em créditos devidos pela Direcional e informa montante inicial de R\$200 milhões. São instrumentos e termos distintos, conforme os documentos. O comunicado de 16/10/2026 informa que a participação agregada da Driehaus Capital Management LLC passou a aproximadamente 4,7805% em 15/10/2026. São documentos públicos datados de 2026, posteriores ao protocolo da DFP informado no escopo. A leitura confirma apenas que os documentos existem e o que neles está escrito. Não demonstra que essas condições existiam em 31/12/2025 nem que eram conhecidas antes do relatório ou da divulgação da DFP; por isso, não são classificados como eventos ajustáveis de 2025. Sua relevância para nota ou demonstração específica de 2025 não foi testada. [5] [6] [7] |
| P-05 | **Planejado por falta de acesso.** Obter entendimento e testar os procedimentos da administração para identificar eventos subsequentes, inclusive responsáveis, periodicidade, fontes de informação e escalonamento ao conselho. | E-08: solicitar políticas, fluxos, evidência de revisão e controles de fechamento. | Não executado. A página pública não permite observar desenho ou operação dos controles internos. |
| P-06 | **Planejado por falta de acesso.** Indagar administração e, quando apropriado, responsáveis pela governança sobre eventos que possam afetar as demonstrações, com perguntas específicas sobre receita imobiliária, distratos, estoques/terrenos, contingências e compromissos relevantes. | E-09: roteiro de indagação; ata ou registro de respostas a obter. | Não executado. Não houve entrevista, confirmação ou contato com representantes da companhia. |
| P-07 | **Planejado por falta de acesso.** Ler atas de acionistas, conselho e administração após 31/12/2025 até a data do relatório; indagar matérias cujas atas ainda não estejam disponíveis. | E-10: conjunto completo de atas e calendário a solicitar; E-05 é apenas ata pública de 13/10/2026 e fora da janela presumida da DFP protocolada em março. | Não executado para a população temporal relevante. A ata pública de outubro não substitui leitura completa de atas nem prova inexistência de outros eventos. |
| P-08 | **Planejado por falta de acesso.** Ler últimas demonstrações intermediárias disponíveis até a data do relatório e reconciliar com eventos posteriores identificados. | E-11: ITR/intermediária e documentos de suporte a obter. | Não executado. O perfil B3 traz dados consolidados resumidos para 30/06/2026, mas essa página não substitui a leitura da ITR integral nem prova qual era a última informação disponível na data do relatório. [4] |
| P-09 | **Planejado por falta de acesso.** Obter a representação formal da administração e, quando apropriado, dos responsáveis pela governança de que todos os eventos que requerem ajuste ou divulgação foram ajustados ou divulgados. | E-12: carta de representação conforme NBC TA 580 a obter. | Não executado; nenhuma representação foi solicitada ou obtida. [2] |
| P-10 | **Planejado por falta de acesso.** Obter a DFP completa, o relatório assinado do auditor, as notas, as datas de aprovação e divulgação; ler nota de eventos subsequentes e avaliar tratamento e consistência com fontes internas e públicas. | E-13: DFP e relatório completos; reconciliação nota a nota e datas formais. | A DFP pública integral foi obtida e as páginas relevantes foram lidas. Permanece não executado o procedimento de reconciliação com fontes internas, confirmação de datas formais e acesso ao relatório/arquivo privado da auditoria; não houve acesso à evidência subjacente. As referências à opinião sem ressalva e aos PAA descrevem o relatório público, não procedimentos deste PT. |
| P-11 | **Simulado para fins didáticos, sem fato da companhia.** Se um documento recebido após 31/12/2025 indicasse que uma obrigação relativa a condição já existente em 31/12/2025 se tornou provável ou mensurável, rastrear a evidência à provisão/divulgação e avaliar se o tratamento é consistente com a estrutura contábil aplicável. | E-14: exemplo hipotético; não é evidência nem constatação relativa à Direcional. | Nenhum documento ou evento real da companhia foi usado neste exercício hipotético. |
| P-12 | **Simulado para fins didáticos, sem fato da companhia.** Se um evento originado após 31/12/2025 fosse material, avaliar se é não ajustável e se a natureza e o efeito financeiro estimado, ou a impossibilidade de estimá-lo, requerem divulgação. | E-15: exemplo hipotético; não é evidência nem constatação relativa à Direcional. | Nenhum documento ou evento real da companhia foi usado neste exercício hipotético. |
| P-13 | **Planejado por falta de acesso.** Estabelecer cobertura da população completa entre 31/12/2025 e a data do relatório do auditor, documentar a conclusão de eventos previamente identificados em outros ciclos de auditoria e estender os procedimentos o mais próximo possível da data do relatório. | E-16: listagens de transações subsequentes, atas, razão, assessoria jurídica e datação dos testes a obter. | Não executado. Busca pública direcionada não equivale à cobertura exigida pelos itens 6–7 nem sustenta conclusão de completude. [2] |
| P-14 | **Planejado por falta de acesso.** Se fato com potencial de afetar o relatório fosse conhecido após sua data e antes da divulgação, discutir com administração/governança, avaliar necessidade de alteração e a resposta prevista nos itens 10–13. Se conhecido depois da divulgação, avaliar a resposta dos itens 14–17 apenas se atendidos seus pressupostos. | E-17: protocolo de investigação e decisão de resposta; depende de fato identificado e de documentos completos. | Não executado; não se identificou, nesta revisão pública limitada, fato que permita afirmar que esses procedimentos de resposta foram acionados. A ausência de identificação na busca limitada não prova inexistência do fato. [2] |

## Evidências e referências cruzadas

**E-01/E-02 — Norma:** Conselho Federal de Contabilidade, cadastro oficial “NBC TA — de Auditoria Independente de Informação Contábil Histórica”, linha NBC TA 560 (R1); e PDF “NBC TA 560 (R1) — Eventos Subsequentes”. Para o texto normativo, as referências de página são substituídas aqui pelos itens numerados da norma: 1–17 e A1–A20, que são os localizadores estáveis do CFC. Ano/ato: 2016; Resolução CFC 2016/NBCTA560(R1), DOU 05/09/2016. [1] [2]

**E-03 — B3:** B3, “DIRECIONAL ENGENHARIA S.A. — Dados Econômico-Financeiros — Balanço Patrimonial — Consolidado”, linha de 31/12/2025. A página HTML não tem paginação impressa. Mostra ativo total consolidado de R\$13.219.635 mil. [4]

**E-04 — CVM/DFP:** CVM, página de gerenciamento/documento associada ao número sequencial 155189, utilizada no escopo como referência à DFP de 31/12/2025, versão 1, envio/protocolo informado de 09/03/2026. A página HTML identifica o auditor, mas não oferece paginação estável; a DFP pública integral foi obtida e as páginas relevantes examinadas. Os valores, PAA e opinião foram conferidos no PDF público, sem acesso à evidência subjacente ou ao arquivo privado. [3]

**E-05 — RI:** Direcional Engenharia S.A., “Ata de Reunião do Conselho de Administração realizada em 13 de outubro de 2026”, itens 4, 5 e 5.1; documento público em RI, sem paginação confiável na visualização consultada. A ata trata de emissão de debêntures/CRI e respectiva oferta. [5]

**E-06 — RI:** Direcional Engenharia S.A., “Comunicado ao Mercado de Modificação da Oferta Pública de Distribuição de Certificados de Recebíveis Imobiliários da 335ª emissão da Riza Securitizadora S.A., lastreados em créditos imobiliários devidos pela Direcional Engenharia S.A.”, datado de 13/10/2026. Documento público em RI, sem paginação confiável na visualização consultada. Informa valor total inicialmente de R\$200.000.000 e modificações nas condições/crono­grama da oferta. [6]

**E-07 — RI:** Direcional Engenharia S.A., “Comunicado ao Mercado — Alienação de Participação Acionária Relevante”, de 16/10/2026. Documento público em RI, sem paginação confiável na visualização consultada. Informa alteração da participação acionária reportada pela Driehaus Capital Management LLC para aproximadamente 4,7805% em 15/10/2026. [7]

**E-08 a E-17:** Solicitações/documentos internos ainda não obtidos ou cenários hipotéticos explicitamente identificados na tabela. Não constituem evidência de auditoria disponível.

## Resultados, exceções, conclusão e limitações

**Resultado dos procedimentos públicos:** foi identificado o texto oficial da NBC TA 560 (R1) e consultados dados públicos de B3, CVM e RI. A B3 confirma o ativo consolidado em 31/12/2025 de R\$13.219.635 mil. A página CVM identifica PwC como auditor. A pesquisa direcionada de RI localizou documentos societários de outubro de 2026 sobre alteração de condições de oferta de CRI/debêntures e mudança de participação acionária reportada por investidor. Esses documentos são fatos de 2026 conforme suas próprias datas e conteúdo, não evidência de condição existente na data-base. A DFP pública integral foi obtida e as páginas relevantes foram lidas; ela reporta PAA de receita imobiliária e provisões para contingências e opinião sem ressalva. Esses elementos são fatos do relatório público, não procedimentos deste PT.

**Exceções e pendências:** não se observou exceção de auditoria comprovada, pois não houve acesso à população completa, aos controles, às atas internas completas, à administração, às representações formais, ao suporte jurídico-contábil, nem aos papéis de trabalho. A DFP pública integral e o relatório público foram obtidos e lidos nas páginas relevantes; permanecem pendentes a reconciliação com evidência interna, confirmação de datas formais, indagações, representação, exame completo de atas/intermediárias e avaliação de eventos para fins de ajuste/divulgação. Essa ausência de exceção observada não significa que eventos ou erros não existam.

**Conclusão didática:** com base exclusivamente nos procedimentos marcados como realizados, **não é possível concluir** se todos os eventos subsequentes relevantes do exercício encerrado em 31/12/2025 foram identificados, ajustados ou divulgados, nem se a evidência de auditoria é apropriada e suficiente para essa conclusão. Não há conclusão de auditoria nem opinião sobre a Direcional neste PT. A execução completa requer os procedimentos planejados e evidência apropriada e suficiente. O material simulado é apenas ilustrativo e não deve ser apresentado como procedimento executado ou evento da companhia.

**Limitações:** (1) a interface CVM é dinâmica e não oferece paginação impressa estável; a DFP pública integral foi obtida por canal oficial e as páginas relevantes foram examinadas. (2) Saldos, PAA e tipo de opinião foram reextraídos da DFP pública para este papel, sem conciliação com registros internos. (3) A página B3 corrobora o ativo total, mas não os saldos de estoques. (4) A revisão pública de comunicados é direcionada e não substitui procedimentos de auditoria. (5) Não houve entrevista, confirmação externa, inspeção física, acesso interno, revisão de contratos ou processo, nem comunicação com a PwC, administração ou governança. (6) Não foi verificada a necessidade contábil de reconhecer ou divulgar eventos de 2026 nas demonstrações de 2025.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC. NBC TA de Auditoria Independente de Informação Contábil Histórica. Cadastro consultado em 22 outubro 2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC. NBC TA 560 R1 Eventos Subsequentes. Resolução publicada em 2016; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA560%28R1%29.pdf>).
- **Ref. 3** — CVM. Página de gerenciamento da DFP de Direcional Engenharia S.A. Número sequencial 155189; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3. Direcional Engenharia S.A. Perfil e dados econômico-financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — Direcional Engenharia S.A. Ata do Conselho de Administração de 13 outubro 2026; [abrir fonte](<https://filemanager-cdn.mziq.com/published/ada9bc2c-f7d0-4359-9eaf-851b679ab788/f4b8b064-726a-4f17-91f8-a6829aa82d66>).
- **Ref. 6** — Direcional Engenharia S.A. Comunicado ao Mercado de 13 outubro 2026 sobre modificação de oferta; [abrir fonte](<https://filemanager-cdn.mziq.com/published/ada9bc2c-f7d0-4359-9eaf-851b679ab788/b827990a-1252-42d4-94b8-cedcbc341872>).
- **Ref. 7** — Direcional Engenharia S.A. Comunicado ao Mercado de 16 outubro 2026 sobre participação acionária relevante; [abrir fonte](<https://filemanager-cdn.mziq.com/published/ada9bc2c-f7d0-4359-9eaf-851b679ab788/15fa5da0-e732-4b16-b364-0f264c093d07>).


---

# PT-570 — Continuidade operacional

## Identificação do trabalho

| Campo | Registro |
|---|---|
| Código / título | **PT-570 — Continuidade operacional** |
| Entidade / demonstrações | DIRECIONAL ENGENHARIA S.A. e controladas — demonstrações financeiras **consolidadas** |
| Exercício | Encerrado em **31/12/2025** |
| Norma aplicável | **NBC TA 570 — Continuidade Operacional**, redação aprovada pela Resolução CFC nº 2016/NBCTA570, publicada no DOU em 04/07/2016. Aplicável a auditorias de demonstrações de períodos encerrados em ou após 31/12/2016 (item 8). Esta é a redação pertinente ao exercício de 2025. A NBC TA 570 (R1), publicada em 25/09/2026, tem aplicação para períodos iniciados em ou após 01/01/2027; portanto, não rege este exercício. [1] [2] [3] |
| Itens normativos focais | NBC TA 570 (2016): itens **6–7, 9–20 e 21–24**; aplicação e outros materiais explicativos **A3–A18 e A19–A25**. A seleção cobre responsabilidade e objetivo do auditor, avaliação de riscos e revisão da avaliação da administração, período mínimo, eventos subsequentes à avaliação, procedimentos adicionais se identificados indicadores, evidência e conclusão, divulgação e implicações para o relatório. Para consistência de documentação, considerar também NBC TA 230. [1] |
| Referência da informação financeira | DFP — Demonstrações Financeiras Padronizadas de 31/12/2025, **Versão 1**, protocolada na CVM em 09/03/2026, conforme base pública indicada para este trabalho. Documento correspondente disponível no RI; demonstrações consolidadas e notas/relatório do auditor são referenciados abaixo por página impressa da DFP. [4] [5] |
| Auditor independente indicado na DFP | PricewaterhouseCoopers Auditores Independentes Ltda. (PwC). Relatório assinado em 09/03/2026. [4] |
| Data de acesso / elaboração didática | **22/10/2026** |
| Preparador | **EDU-AUD-001** (matrícula didática) |
| Revisor |  |

> **Natureza deste papel:** peça exclusivamente didática, baseada em informação pública consultada. Não é arquivo de auditoria da companhia, não documenta trabalho executado pelo auditor independente e não constitui opinião de auditoria. Não houve entrevista, confirmação externa, inspeção física, consulta à administração ou acesso a livros, previsões, atas, correspondência ou papéis internos.

## Objetivo, conta e processo

**Objetivo.** Estruturar a avaliação didática da adequação da base contábil de continuidade operacional utilizada pela administração nas demonstrações consolidadas, identificar se as informações públicas indicam eventos ou condições que poderiam levantar dúvida significativa, e definir procedimentos necessários para obter evidência apropriada e suficiente. O objetivo normativo inclui concluir sobre a adequação da base e sobre a existência de incerteza relevante, não prever a capacidade futura da entidade. A ausência de menção a incerteza relevante em relatório público não garante continuidade futura. (NBC TA 570, itens 6–9.) [1]

**Conta/processo abrangido.** Avaliação transversal do grupo, com foco na base contábil, projeções de liquidez e financiamento, geração de caixa e realização de ativos; divulgações correlatas; e classificação, mensuração e apresentação das demonstrações consolidadas. Não se trata de auditoria autônoma dos estoques, receitas ou contingências. Essas rubricas entram como contexto para a avaliação do grupo, sem substituir os respectivos papéis de trabalho.

## Afirmações e riscos avaliados para planejamento

Continuidade operacional não é uma afirmação isolada de saldo. Para este PT são relevantes: **base de preparação e apresentação/divulgação** (uso apropriado da base, suficiência e clareza da nota); **completude** de eventos, obrigações e incertezas relevantes; **classificação** corrente/não corrente e vencimentos; e **avaliação** dos ativos e passivos quando planos ou cenários possam alterar a realização/liquidação no curso normal dos negócios.

| Fator / risco de auditoria didático | Base observada e qualificação |
|---|---|
| Concentração relevante em estoques imobiliários, inclusive terrenos a incorporar, e possível dependência de lançamento, construção e venda de empreendimentos para realização do valor e geração de caixa. Risco hipotético de sensibilidade a prazos, custos, demanda, preço, financiamento à produção e repasses. | A DFP pública integral apresenta estoque consolidado de R\$ 6.951.508 mil; terrenos a incorporar totais de R\$ 5.678.238 mil, dos quais R\$ 4.864.673 mil são não circulantes; estoques circulantes somam R\$ 2.086.835 mil. Os dados, por si só, **não demonstram** dificuldade de liquidez, perda de valor, impedimento a lançamentos ou incapacidade de continuidade. [4, p. 16–17; 5, p. 69] |
| Variação dos saldos de ativo e do total de terrenos em 2025 versus 2024. Risco hipotético de estimativas excessivamente otimistas quanto a absorção, cronograma de lançamento, custo total e realização de terrenos. | Ativo consolidado: R\$ 13.219.635 mil em 2025 versus R\$ 10.067.406 mil em 2024; terrenos a incorporar totais: R\$ 5.678.238 mil versus R\$ 4.587.823 mil. A variação do ativo é aproximadamente **31,3%** e a do total de terrenos aproximadamente **23,8%**. O componente não circulante foi R\$ 4.864.673 mil em 2025 versus R\$ 3.888.979 mil em 2024. São comparações aritméticas de saldos publicados, não indicadores autossuficientes de deterioração ou estresse financeiro. [4, p. 16–17; 5, p. 69] |
| Julgamentos e estimativas ligados ao reconhecimento de receita imobiliária e aos custos orçados das obras; provisões para contingências. | A DFP identifica reconhecimento de receita imobiliária e provisões para contingências entre os principais assuntos de auditoria (PAA). PAA é assunto de auditoria significativo, não constatação de risco à continuidade nem evidência de incerteza relevante. Os riscos de premissas e estimativas são hipóteses para procedimentos adicionais, não achados deste PT. [4, p. 115] |
| Suficiência da avaliação da administração e do horizonte temporal. | A Nota 1.1 afirma que a administração avaliou a capacidade para “o próximo exercício”, declara conforto com a posição financeira e operacional e ausência de conhecimento de incerteza significativa que possa pôr a capacidade operacional em risco. Não foi possível examinar a avaliação subjacente, o horizonte explicitamente coberto, suas premissas ou documentação suporte. A expressão publicada, isoladamente, não permite concluir se a análise satisfaz o mínimo de doze meses após 31/12/2025 requerido pelo item 13 da NBC TA 570. [4, p. 41; 1, item 13] |
| Fatores macroeconômicos potencialmente adversos. | A Nota 1.1 menciona que a companhia acompanha cenário político, políticas econômicas, taxa de juros, inflação e conflitos externos. Não quantifica exposição, probabilidade ou efeito. São fatores reconhecidos pela administração, mas não são aqui tratados como prova de pressão efetiva sobre caixa ou operação. [4, p. 41] |

## População, fontes e critérios

**População pública examinada.** DFP 2025 V1 — demonstrações consolidadas, notas explicativas e relatório de auditoria; página da CVM identificada no enunciado; Central de Resultados do RI e arquivo anual; e página cadastral/econômico-financeira da B3. As demonstrações consolidadas são o nível do escopo; a NBC TA 570 requer consideração da entidade e, quando aplicável, do grupo como um todo.

**Fontes primárias permitidas para fatos societários.** CVM, B3 e RI da companhia. Para norma, texto e cadastro oficial do CFC. Nenhuma fonte jornalística ou de terceiros foi utilizada como evidência societária.

**Critérios.** NBC TA 570, redação aplicável a 2025, com ênfase nos itens 6, 9–20 e 21–24: (i) identificar eventos/condições potencialmente relevantes e revisar a avaliação da administração (itens 10–12); (ii) cobrir ao menos doze meses desde a data das demonstrações se a avaliação da administração for menor (item 13); (iii) considerar informações relevantes conhecidas e eventos subsequentes à avaliação (itens 14–15); (iv) se surgirem indicadores, obter evidência adicional e avaliar planos e fatores mitigadores (itens 16–18); (v) concluir sobre base e incerteza relevante, e sobre divulgação e relatório (itens 19–24). A responsabilidade da administração pela avaliação não substitui a do auditor (itens 4–6). [1]

## Procedimentos e situação

### Realizados com evidência pública

| Ref. | Procedimento e natureza da evidência | Resultado documentado |
|---|---|---|
| P-01 | Consulta ao cadastro oficial CFC para fixar a versão: leitura da NBC TA 570 de 2016 e do registro da revisão aprovada em 2026. Procedimento documental público. | NBC TA 570 (2016), item 8, aplica-se a exercícios encerrados desde 31/12/2016; NBC TA 570 (R1) tem vigência para períodos iniciados em/apos 01/01/2027. A revisão de 2026 não altera o critério deste PT para o exercício 2025. [1] [2] [3] |
| P-02 | Inspeção documental pública da DFP 2025 V1: confronto do balanço consolidado e comparação dos saldos publicados de 2025 e 2024. Não houve teste de razão, conciliação com balancete ou teste de titularidade/valoração. | Ativo total e saldos de estoque/terrenos conforme seção “Riscos”. Na apresentação consolidada, R\$ 4.864.673 mil de terrenos a incorporar aparecem no ativo não circulante; a informação pública também identifica R\$ 2.086.835 mil de estoques circulantes. Valores em R\$ mil. [4, p. 16–17] |
| P-03 | Leitura da Nota 1.1 da DFP sobre continuidade operacional. | A administração relata avaliação para o próximo exercício, conforto com posição financeira e operacional, não conhecimento de incerteza significativa e preparação sob a base de continuidade. Trata-se de representação divulgada pela administração; este procedimento não verificou sua sustentação. [4, p. 41] |
| P-04 | Leitura da nota de estimativas críticas e do relatório do auditor para compreender os PAA públicos. | PAA incluem reconhecimento de receita imobiliária e provisões para contingências; relatório do auditor sobre as demonstrações consolidadas contém opinião sem ressalva. O relatório é evidência pública do que o auditor reportou, não evidência dos procedimentos subjacentes deste PT nem validação independente dos prognósticos da administração. [4, p. 57 e 115–117] |
| P-05 | Consulta às páginas públicas da B3 e CVM para identidade da emissora/atividade e identificação do auditor na DFP/CVM. | B3 identifica Direcional Engenharia S.A., código CVM 21350, DIRR3 e atividade principal de incorporação, construção e comercialização de imóveis e serviços de engenharia. A página da CVM identifica PwC como auditor. [5] [6] |
| P-06 | Consulta à Central de Resultados do RI e ao arquivo DFP anual 2025, cruzando sua identificação/título com a DFP V1. | Arquivo do RI contém DFP de 31/12/2025, versão 1, com 123 páginas numeradas no documento; relatório de auditoria datado de 09/03/2026. RI e CVM são fontes documentais, não evidência de acesso aos registros internos. [4] [7] |

### Planejados por falta de acesso

Os itens abaixo são **planejamento, não procedimentos realizados**. Requerem autorização e evidência interna ou terceiros sob controle apropriado; não foram executados neste trabalho didático.

| Ref. | Procedimento planejado | Propósito / critério |
|---|---|---|
| PP-01 | Obter da administração a avaliação formal de continuidade operacional para o grupo e componentes, sua data de preparação/aprovação, horizonte, versões, premissas, planos e documentação suporte; comparar o período coberto ao requisito de pelo menos doze meses após 31/12/2025, caso a avaliação seja menor. | NBC TA 570, itens 10, 12–14. Confirmar a extensão temporal com evidência, sem inferir suficiência a partir da expressão “próximo exercício”. |
| PP-02 | Obter orçamento, fluxo de caixa projetado e projeções de liquidez por período e entidade, conciliar saldos iniciais relevantes com contabilidade auditada, verificar consistência matemática, premissas com histórico/contratos e dados realizados posteriores, e testar cenários de sensibilidade (vendas, ritmo de lançamento, custo e prazo de obra, inflação, juros, repasses e recebimentos). Avaliar necessidade de cenários combinados. | Itens 16–18, 20. Examinar robustez dos planos e possíveis mitigadores; dados e conclusões dependem de evidência que não está no domínio público consultado. |
| PP-03 | Inspecionar contratos e extratos de financiamentos e outras fontes de capital: vencimentos, covenants, garantias, cláusulas de aceleração, renovações/refinanciamentos, disponibilidade e restrições de caixa; confirmar diretamente saldos/termos selecionados com financiadores se apropriado. | Itens 16–18. Identificar déficits de financiamento e avaliar se mitigadores são factíveis e suficientemente sustentados. Nenhuma confirmação foi solicitada ou recebida. |
| PP-04 | Obter posição de caixa e equivalentes, aplicações e restrições, cronogramas de recebimentos e pagamentos, compromissos de terrenos/obras, compras, dividendos e necessidades de capital de giro; testar reconciliações e vencimentos por sociedade do grupo. | Itens 12, 16–18. Avaliar capacidade de cumprir obrigações no curso normal; não presumir que saldo de ativo total equivale a liquidez. |
| PP-05 | Obter evidência sobre cronograma, aprovações, condições resolutivas e compromissos dos empreendimentos relevantes; confrontar pressupostos de lançamento, vendas, estoque, repasse e custo com documentos e eventos subsequentes. Examinar se há ativos comprometidos, não disponíveis ou dependentes de eventos incertos. | Itens 14 e 16–18. O elevado saldo de terrenos apenas orienta a seleção de itens, não comprova risco de continuidade. |
| PP-06 | Obter relação completa de processos, contingências, garantias, reclamações, obrigações e correspondência jurídica; solicitar atualização a assessores jurídicos, avaliar pagamentos/exposições e a inclusão de premissas relevantes nos fluxos de caixa, resguardadas as regras de confirmação externa. | Itens 14–16. A provisão destacada como PAA não permite inferir resultado de litígios, materialidade futura ou saída de caixa. |
| PP-07 | Indagar administração e responsáveis pela governança sobre eventos/condições até a data do relatório de auditoria, examinar atas, decisões, planos de recuperação/financiamento e comunicações pertinentes; cotejar fatos conhecidos após a avaliação com a projeção. | Itens 11, 14–16. Nenhuma entrevista, indagação ou inspeção de ata foi efetuada. |
| PP-08 | Se evidência revelar evento ou condição potencialmente relevante, ampliar procedimentos sobre viabilidade dos planos, fatores mitigadores e divulgação; avaliar se existe incerteza relevante, se a base continua apropriada e as implicações para opinião/relatório. | Itens 16–24. Escalonamento condicionado a evidência ainda não obtida; não há neste PT conclusão de ocorrência. |

### Simulados para fins didáticos

| Ref. | Exercício simulado (não executado como teste da companhia) | Limitação |
|---|---|---|
| S-01 | Discussão hipotética de sensibilidade: atraso de lançamentos/repasses, queda na velocidade de vendas, aumento de custo de construção e juros e atraso de recebíveis; avaliar qualitativamente se e como esses choques poderiam pressionar caixa ou alterar a realização de terrenos e empreendimentos. | Não foi preparado modelo, não foram inseridos dados da companhia nem calculado impacto, folga de caixa ou probabilidade. Não é cenário informado pela administração, evento observado, projeção ou evidência de risco concretizado. Serve somente para ilustrar PP-02 e PP-05. |
| S-02 | Exemplo de decisão didática: se uma previsão interna demonstrasse déficit de caixa em horizonte pertinente e o plano mitigador dependesse de refinanciamento sem evidência de disponibilidade, verificar se a conclusão e as divulgações estariam suficientemente suportadas. | Premissas inteiramente hipotéticas; nenhum déficit, refinanciamento malsucedido ou divulgação inadequada foi constatado na Direcional por este PT. |

## Evidências e referências cruzadas

| ID | Evidência pública / referência cruzada | Localização no documento |
|---|---|---|
| E-01 | DFP 2025 V1 — demonstrações consolidadas, ativo, estoques e terrenos a incorporar. Valores em R\$ mil. | DFP, páginas impressas **16–17 de 123**. Ver P-02 e riscos. [4] |
| E-02 | DFP 2025 V1 — Nota 1.1, continuidade operacional e declaração da administração sobre próximo exercício. | DFP, página impressa **41 de 123**. Ver P-03. [4] |
| E-03 | DFP 2025 V1 — estimativas críticas; reconhecimento de receita de unidades imobiliárias em construção e provisões para riscos. | DFP, página impressa **57 de 123**. Ver P-04. [4] |
| E-04 | DFP 2025 V1 — relatório independente e PAA, inclusive reconhecimento de receita e provisões para contingências; opinião sem ressalva. | DFP, páginas impressas **115–117 de 123**. Relatório assinado em 09/03/2026. Ver P-04. [4] |
| E-05 | Registro normativo oficial CFC para NBC TA 570 (2016) e cópia oficial do texto. | Cadastro da Resolução 2016/NBCTA570 e PDF integral; item 8 trata da vigência. Ver P-01. [1] [2] |
| E-06 | Registro e texto oficial da NBC TA 570 (R1), publicação de 25/09/2026, vigência para períodos iniciados a partir de 01/01/2027. | Cadastro e PDF oficial; item 8 / cláusula de vigência. Ver P-01. [3] |
| E-07 | CVM — página do documento/companhia indicada para DFP; identifica PricewaterhouseCoopers Auditores Independentes Ltda. | Registro público CVM no endereço indicado. Ver P-05. [6] |
| E-08 | B3 — cadastro público da companhia, código CVM 21350, código DIRR3 e atividade principal. | Página “DIRECIONAL ENGENHARIA S.A.”. Ver P-05. [5] |
| E-09 | RI — Central de Resultados e arquivo anual da DFP 2025. | Documento “DFP — Demonstrações Financeiras Padronizadas — 31/12/2025 — DIRECIONAL ENGENHARIA S.A., Versão 1”. Ver P-06. [4] [7] |

## Resultados, exceções e conclusão

**Resultados públicos observados.** A administração divulgou que avaliou continuidade para o “próximo exercício”, afirmou estar confortável com sua posição financeira e operacional, não ter conhecimento de incerteza significativa que pudesse pôr em risco sua capacidade operacional e ter preparado as demonstrações pela base de continuidade (Nota 1.1, p. 41). O balanço consolidado mostra ativo total de R\$ 13.219.635 mil, estoque de R\$ 6.951.508 mil, com terrenos a incorporar totais de R\$ 5.678.238 mil, dos quais R\$ 4.864.673 mil não circulantes, e estoques circulantes de R\$ 2.086.835 mil; os comparativos de 2024 são R\$ 10.067.406 mil para ativo e R\$ 4.587.823 mil para terrenos totais, dos quais R\$ 3.888.979 mil não circulantes (pp. 16–17; Nota 5, p. 69). A DFP assinala PAA sobre reconhecimento de receita imobiliária e provisões para contingências, e o relatório público expressa opinião sem ressalva (pp. 115–117). Esses fatos contextualizam o planejamento, mas não substituem evidência da avaliação, projeções ou capacidade de financiamento. [4]

**Exceções / itens em aberto.** Nenhuma exceção de auditoria foi estabelecida, pois não foram testados registros internos nem obtida evidência de auditoria da companhia. A principal limitação observável é que as informações públicas não permitem avaliar: horizonte exato da avaliação divulgado como “próximo exercício”; conteúdo e premissas do plano de negócios; fluxos de caixa, liquidez disponível e restrita; vencimentos/covenants; viabilidade de planos mitigadores; e eventos subsequentes considerados pela administração. Não se conclui que tais informações faltam na documentação da administração; apenas não foram acessadas por este trabalho.

**Conclusão didática.** Com base **somente nas evidências públicas acima**, a administração divulgou o uso da base de continuidade e a conclusão de conforto para o próximo exercício, e o relatório PwC publicado contém opinião sem ressalva. O material público consultado **não oferece evidência suficiente para este preparador concluir independentemente** se a avaliação da administração cobriu, no mínimo, doze meses após 31/12/2025, se suas premissas e mitigadores são razoáveis, nem se existe ou não incerteza relevante. Portanto, conclusão de auditoria substantiva sobre continuidade operacional fica **em aberto, condicionada à execução dos procedimentos PP-01 a PP-08 e à documentação de evidência apropriada e suficiente**. Não se identificou nem se afirma evento adverso, dificuldade financeira, ameaça à continuidade ou distorção; riscos descritos sem suporte permanecem hipóteses para planejamento. A opinião sem ressalva da PwC é registrada como fato do relatório público e não é reproduzida ou reemitida por este PT.

**Limitações.** Papel elaborado à distância e para fins didáticos, a partir de fontes públicas acessadas em 22/10/2026. Os procedimentos marcados como realizados limitam-se à leitura/consulta documental pública. Não foram executados confirmações, entrevistas, inspeções, reexecuções, análises de dados internos, verificação de orçamento, obtenção de carta de representação, reuniões de governança ou avaliação do trabalho de componentes. Não há opinião, certificação, recomendação de crédito ou garantia de continuidade presente/futura.

## Aprovação

| Função | Identificação | Data | Assinatura |
|---|---|---|---|
| Preparador | **EDU-AUD-001 — matrícula didática** | **22/10/2026** |  |
| Revisor |  |  |  |

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA 570 – Continuidade Operacional, redação da Resolução 2016/NBCTA570, texto integral, itens 6–24, versão aplicável a 2025; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA570.pdf>).
- **Ref. 2** — CFC, Resolução 2016/NBCTA570, publicada no DOU em 04/07/2016, cadastro e situação normativa; [abrir fonte](<https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo=2016/NBCTA570>).
- **Ref. 3** — CFC, NBC TA 570 (R1), aprovada em 17/09/2026, publicada em 25/09/2026, vigência para períodos iniciados em ou após 01/01/2027; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA570%28R1%29.pdf>).
- **Ref. 4** — Direcional Engenharia S.A., DFP – Demonstrações Financeiras Padronizadas de 31/12/2025, Versão 1, arquivo publicado no RI em 09/03/2026, 123 páginas impressas; [abrir fonte](<https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2>).
- **Ref. 5** — B3, DIRECIONAL ENGENHARIA S.A., página cadastral e informações econômico-financeiras; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 6** — CVM, página pública de informações da companhia/documento, auditor PRICEWATERHOUSECOOPERS AUDITORES INDEPENDENTES LTDA; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 7** — Direcional Engenharia S.A., RI, Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-580 — Representações formais

**Entidade:** DIRECIONAL ENGENHARIA S.A. — demonstrações contábeis consolidadas  
**Data-base:** exercício encerrado em 31/12/2025  
**Norma e itens:** NBC TA 580 (R1), *Representações Formais*, especialmente itens 1–20, A1–A27 e Apêndice 2; interação com NBC TA 210, conforme itens 10 e 11. Texto oficial CFC identificado como NBC TA 580 (R1), publicada no DOU em 05/09/2016, com as alterações posteriores indicadas pelo CFC (Revisão NBC 03/2019, incluindo Apêndices 1 e 2). Aplicável ao exercício de 2025. [1] [2]

**Natureza do papel:** papel didático de planejamento e documentação baseada apenas em informação pública. Não é arquivo de auditoria da PwC nem atesta a execução de auditoria ou obtenção de carta de representação.

## Objetivo, conta e processo

Documentar o planejamento da obtenção e avaliação de representações formais da administração e, quando apropriado, dos responsáveis pela governança, para a auditoria das demonstrações consolidadas de 2025. Busca-se obter declarações escritas de responsáveis com conhecimento apropriado, datadas tão próximo quanto praticável e não depois da data do relatório do auditor, cobrindo todas as demonstrações e períodos referidos nesse relatório (NBC TA 580, itens 6, 9, 14 e 15). As representações são evidência necessária, mas, isoladamente, não constituem evidência apropriada e suficiente nem substituem outros procedimentos (item 4). [2]

**Conta/processo abrangido:** responsabilidade da administração pela elaboração e apresentação das demonstrações consolidadas, integridade das informações fornecidas e registro integral das transações; complementos escritos direcionados às estimativas, divulgações e afirmações relevantes que o auditor determine necessárias. No planejamento didático, maior atenção é dirigida aos estoques — em particular terrenos a incorporar — e aos temas destacados como principais assuntos de auditoria (PAA): reconhecimento de receita imobiliária e provisões para contingências. Esses focos não significam que as representações, por si, validem saldos, premissas ou conclusões de auditoria.

## Afirmações e riscos considerados

| Área | Afirmações / responsabilidade relacionadas | Risco ou hipótese para orientar a solicitação — não é constatação |
|---|---|---|
| Demonstrações consolidadas como um todo | Elaboração conforme a estrutura de relatório financeiro aplicável e apresentação adequada, quando pertinente; integralidade das informações e das transações (itens 10–12). | Risco de carta incompleta, assinada por pessoa sem responsabilidade ou conhecimento apropriados, ou incompatível com as demais evidências. |
| Estoques, inclusive terrenos a incorporar | Existência, direitos e obrigações, integralidade, mensuração/avaliação, classificação e divulgação. | A concentração de valores em terrenos pode elevar a exposição a riscos de classificação, titularidade, custo atribuível, recuperabilidade e divulgação. São riscos possíveis a avaliar por evidência própria, não erros identificados. |
| Receita imobiliária — PAA público | Ocorrência, competência/corte, mensuração e apresentação da receita e divulgações correlatas. | Complexidade de contratos, estágio de execução, premissas ou corte podem criar risco de distorção relevante; nada neste papel constata distorção ou falha. |
| Provisões e contingências — PAA público | Integralidade, existência/obrigação, mensuração, classificação e divulgação. | A avaliação pode depender de estimativas, informações jurídicas ou eventos posteriores; uma declaração genérica não elimina a necessidade de evidência apropriada. |
| Informações fornecidas / eventos e compromissos | Acesso acordado, integralidade dos registros e das informações comunicadas ao auditor (item 11); outras declarações específicas, se necessárias (item 13). | Pode haver risco de informação ou transação não comunicada. Não foi possível verificar internamente sua existência ou ausência. |

**Indicadores públicos de escopo, em R\$ mil:** a DFP pública integral obtida no RI e examinada nas páginas relevantes informa ativo total de 13.219.635; estoques de 6.951.508, incluindo terrenos a incorporar totais de 5.678.238 (dos quais 4.864.673 não circulantes) e estoques circulantes de 2.086.835. Para 2024, informa ativo total de 10.067.406 e terrenos a incorporar totais de 4.587.823 (dos quais 3.888.979 não circulantes). O perfil da B3 também exibe ativo consolidado de 13.219.635 para 31/12/2025, em sua tabela econômica em R\$ mil. As quantias são parâmetros de seleção de risco e não foram reconciliadas a balancetes ou registros internos. [3] [4]

## População, fontes e critérios

**População planejada:** responsáveis apropriados pela elaboração e apresentação das demonstrações consolidadas de 2025, selecionados segundo responsabilidade e conhecimento (itens 8–9 e A2–A6); demonstrações consolidadas e períodos abrangidos pelo relatório; e declarações específicas selecionadas a partir dos riscos e de requisitos de outras NBC TAs. A identificação nominal de signatários, estrutura societária completa, lista de componentes e carta efetivamente obtida não estão disponíveis neste trabalho didático.

**Fontes públicas consultadas:**

- **PUB-01 — CVM:** registro público da DFP de Direcional Engenharia S.A., documento sequencial 155189, protocolo 021350DFP311220250100155189-71, exercício 31/12/2025, versão 1; a tela identifica PwC como auditor. Os quadros da DFP são apresentados eletronicamente e a tela não possui paginação fixa; a DFP pública integral foi obtida diretamente no RI e as páginas relevantes foram examinadas. Referências detalhadas: BP pp.16–17, DRE p.21, Nota 5 p.69 e relatório PwC pp.115–117. [3]
- **PUB-02 — B3:** perfil de DIRECIONAL ENGENHARIA S.A., código CVM 21350, seção “Dados Econômico-Financeiros — R\$ - mil”, balanço consolidado, coluna 31/12/2025. Fonte pública auxiliar para identidade e ativo total consolidado. Página web dinâmica, sem página impressa. [4]
- **PUB-03 — RI da companhia:** Central de Resultados, seção de informações financeiras, com seletor anual e acesso aos documentos divulgados pela companhia. A página de entrada não foi usada para confirmar cifras específicas de 2025. [5]
- **NORM-01 — CFC:** registro oficial da NBC TA 580 (R1) e PDF oficial do texto normativo. No PDF do CFC, os itens e aplicação estão nas páginas do próprio arquivo; para citação operacional: itens 1–20, PDF pp. 2–4; aplicação e outros materiais, itens A1–A27, PDF pp. 5–9; Apêndices 1 e 2, PDF pp. 10–13 (paginação do arquivo). A página de registro identifica a publicação, vigência e alterações. [1] [2]

**Critérios:** texto da NBC TA 580 (R1), incluindo itens 4 e 6 e requisitos 9–20, com ênfase em itens 9–15 e resposta dos itens 16–20; consistência da data, forma, signatários, abrangência e conteúdo; compatibilidade com demais evidências e resposta a omissões ou contradições. A carta deve refletir a descrição de responsabilidades estabelecida nos termos do trabalho (item 12). Para afirmações adicionais, solicitar apenas as consideradas necessárias ou exigidas por outras normas (item 13), usando o Apêndice 2 como exemplo, não como carta automaticamente suficiente.

## Procedimentos e status

Legenda: **Realizado — evidência pública** significa leitura/inspeção de fonte pública, não procedimento de auditoria interna. **Planejado — falta de acesso** significa etapa a executar em trabalho real, sem execução declarada. **Simulado — didático** significa conteúdo demonstrativo, não evidência obtida.

| ID / status | Procedimento | Resultado documentável neste papel |
|---|---|---|
| P01 — **Realizado — evidência pública** | Consultar o registro CVM indicado e identificar documento, companhia, referência a DFP V1, auditor indicado e acesso aos quadros consolidados. | Tela pública identifica DFP de 31/12/2025, versão 1 e PwC. A interface CVM não oferece paginação estável; a DFP pública integral foi obtida e as páginas relevantes do balanço e relatório foram examinadas. Não foi feita inspeção de livros, papéis da PwC ou comprovante de protocolo fora do conteúdo público. [3] |
| P02 — **Realizado — evidência pública** | Consultar a página da B3 e cotejar identificação pública e ativo total consolidado de 31/12/2025 com a base de escopo. | A página da B3 mostra DIRECIONAL ENGENHARIA S.A., código CVM 21350, ativo consolidado de R\$ 13.219.635 mil em 31/12/2025. Não confirma saldos de estoque, terrenos, carta de representação ou seus suportes. [4] |
| P03 — **Realizado — evidência pública** | Consultar página oficial do CFC e norma NBC TA 580 (R1), identificando versão, vigência e requisitos. | A norma aplicável está identificada como NBC TA 580 (R1), com publicação DOU de 05/09/2016 e alteração de apêndices em 2019 conforme registro CFC. Foram usados, em particular, itens 4, 6, 9–15 e 16–20. [1] [2] |
| P04 — **Planejado — falta de acesso** | Obter a carta assinada pelo diretor-presidente/diretor financeiro ou equivalentes com responsabilidade e conhecimento apropriados; avaliar necessidade de assinatura de responsáveis pela governança. Confirmar aderência dos signatários aos termos do trabalho e dos quadros consolidados. | Não executado: nenhuma entrevista, solicitação, confirmação ou carta interna foi acessada ou obtida. Na execução, documentar signatários, competência, data, entidades/escopo consolidados e cobertura de todos os períodos do relatório. (Itens 9, 12, 14 e 15.) |
| P05 — **Planejado — falta de acesso** | Solicitar declarações escritas de que a administração cumpriu sua responsabilidade pela elaboração e apresentação das demonstrações; forneceu todas as informações e acesso acordado; e registrou/refletiu todas as transações. | Não executado. Confrontar a redação com NBC TA 210 e a carta/termos reais do trabalho; não substituir essa declaração pela disponibilidade pública de uma DFP. (Itens 10–12.) |
| P06 — **Planejado — falta de acesso** | Considerar, conforme evidências e exigências aplicáveis, declarações adicionais sobre integralidade das informações de estoques/terrenos, contratos e premissas de receita imobiliária, processos e contingências, garantias, compromissos, partes relacionadas, eventos subsequentes e informações relevantes não divulgadas. | Não executado. Definir conteúdo após avaliação dos procedimentos e requisitos aplicáveis; obter evidência corroborativa e não tratar declaração como substituto de testes, confirmação jurídica, inspeção física ou procedimentos sobre estimativas. (Item 13; Apêndice 2.) |
| P07 — **Planejado — falta de acesso** | Conferir data da carta (tão próxima quanto praticável e não posterior à data do relatório), período abrangido, destinatário e forma escrita; avaliar resposta a alterações/omissões e comparar declarações com outras evidências e inconsistências identificadas. | Não executado. Data do relatório e carta não foram verificadas neste trabalho; não presumir uma data. Se houver contradição, investigar e reavaliar confiabilidade; se houver recusa, aplicar itens 16–20 e avaliar consequência na opinião. |
| P08 — **Simulado — didático** | Elaborar lista de conferência e minuta-esqueleto da carta para orientar eventual solicitação. | Simulação apenas: a minuta deve reproduzir responsabilidades dos termos do trabalho, incluir confirmações dos itens 10–11 e tópicos adicionais aprovados após avaliação de riscos. Não é declaração da administração, não foi enviada nem assinada e não constitui evidência. |

### Minuta-esqueleto simulada — não enviada / não assinada

> À PwC, em conexão com a auditoria das demonstrações contábeis consolidadas da DIRECIONAL ENGENHARIA S.A. relativas ao exercício findo em 31 de dezembro de 2025, nós, na qualidade de responsáveis apropriados e com base em nosso melhor conhecimento após as indagações consideradas necessárias, confirmaríamos: (1) que cumprimos as responsabilidades por elaboração e apresentação das demonstrações conforme descritas nos termos do trabalho e a estrutura de relatório financeiro aplicável; (2) que fornecemos as informações e os acessos acordados; e (3) que todas as transações foram registradas e refletidas nas demonstrações. Declarações adicionais seriam incluídas apenas após definição, conforme os riscos e as normas aplicáveis. Esta minuta é uma simulação didática e não afirma que tais fatos foram declarados pela administração.

## Evidências e referências cruzadas

- **PUB-01:** metadados públicos da DFP CVM V1 e identificação do auditor na tela do documento; quadros eletrônicos de DFs consolidadas, sem página fixa. Ver ressalva de acesso em P01. [3]
- **PUB-02:** perfil B3, identificação societária e coluna 31/12/2025 de balanço consolidado; sem paginação impressa. [4]
- **PUB-03:** página da Central de Resultados do RI, usada como localizador de publicações, não como fonte de cifra específica neste papel. [5]
- **NORM-01:** NBC TA 580 (R1), principalmente itens 4, 6, 9–20 e Apêndice 2; páginas do PDF referidas na seção de critérios. [1] [2]
- **PAA e opinião:** o relatório público PwC da DFP, lido nas pp. 115–117, destaca reconhecimento de receita imobiliária e provisões para contingências como PAA e apresenta opinião sem ressalva. Trata-se de informação sobre o relatório público, não de reexecução, validação ou endosso das conclusões da PwC. A carta de representações não é prova suficiente isoladamente para os saldos ou PAA. [3]

## Resultados, exceções, conclusão e limitações

**Resultado dos procedimentos públicos:** a consulta ao perfil B3 corroborou o nome/código da companhia e o ativo consolidado de 31/12/2025 de R\$ 13.219.635 mil. A tela do registro CVM identifica DFP V1 e PwC. Os demais montantes e o conteúdo de PAA/opinião foram localizados na DFP pública integral e nas páginas relevantes; isso não implica reexecução de procedimentos nem conciliação com registros internos. Não foi localizada nem acessada carta de representação ou evidência privada da auditoria.

**Exceções:** não há exceção de auditoria identificada neste trabalho. A indisponibilidade de evidência interna é limitação de escopo didático, não evidência de que a administração deixou de fornecer representações, nem indício de distorção. Nenhum procedimento de confirmação, entrevista, inspeção física, teste de transação, exame de contrato, consulta a assessores jurídicos ou inspeção de papéis de auditoria foi executado.

**Conclusão didática:** os indicadores públicos justificam que a solicitação formal cubra o conjunto das demonstrações consolidadas e seja planejada com atenção adicional aos estoques/terrenos, receita imobiliária e provisões/contingências. Com a evidência disponível não é possível concluir que as representações requeridas foram solicitadas, recebidas, confiáveis ou suficientes, nem concluir sobre saldos ou afirmações. Em trabalho real, a conclusão deste PT dependeria de obtenção da carta escrita e de confronto com evidências apropriadas. Se as representações dos itens 10–11 não forem fornecidas, ou se forem não confiáveis, observar requisitos e efeitos dos itens 16–20, inclusive abstenção de opinião nas situações do item 20.

**Limitações:** papel estritamente didático, elaborado a partir de fontes públicas delimitadas e da base factual indicada para o exercício. O acesso público não revela as solicitações, cartas, comunicações, respostas, papéis de trabalho ou evidência interna do auditor. A informação da opinião sem ressalva não permite inferir os procedimentos realizados para suportá-la. Cifras em reais mil; não inventadas nem substituídas por estimativas. Referências CVM sem número de página foram descritas como quadros eletrônicos sem paginação fixa; nenhuma página não verificada é atribuída.

---

**Preparador:** matrícula didática **EDU-AUD-001**  
**Data de preparação:** **22/10/2026**  
**Revisor:** ____________________________________  
**Data da revisão:** ______________________________

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA de Auditoria Independente — relação oficial, versão consultada em 2026; [abrir fonte](<https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>).
- **Ref. 2** — CFC, NBC TA 580 R1 — Representações Formais, texto oficial e apêndices, PDF consolidado; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBCTA580%28R1%29.pdf>).
- **Ref. 3** — CVM, DFP DIRECIONAL ENGENHARIA S.A., exercício 31/12/2025, V1, protocolo 021350DFP311220250100155189-71; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3, perfil de DIRECIONAL ENGENHARIA S.A., código CVM 21350, dados econômico-financeiros consolidados; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — DIRECIONAL ENGENHARIA S.A., RI, Central de Resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).


---

# PT-600 — Considerações especiais — auditoria das demonstrações contábeis de grupos

**Entidade:** DIRECIONAL ENGENHARIA S.A. — demonstrações contábeis consolidadas  
**Exercício:** encerrado em 31/12/2025  
**Código/título:** PT-600 — NBC TA 600 (R2), *Considerações especiais — auditorias de demonstrações contábeis de grupos, incluindo o trabalho dos auditores dos componentes*  
**Preparador:** matrícula didática **EDU-AUD-001**  
**Data:** 22/10/2026  
**Revisor:** ____________________________________  
**Data da revisão:** ____________________________  
**Natureza:** papel de trabalho didático, baseado exclusivamente em documentos públicos identificados e em procedimentos de leitura/recalculo efetuados sobre esses dados. Não constitui relatório de auditoria nem evidência de que procedimentos do auditor independente foram reexecutados.

## Norma, escopo e objetivo

Aplicada como referência normativa a **NBC TA 600 (R2)**, aprovada em 25/10/2023. O item 12 torna-a aplicável às auditorias de demonstrações de grupos para períodos iniciados em ou após 01/01/2024; portanto, é a versão pertinente ao exercício de 2025. O texto oficial do CFC registra a norma como vigente e não revogada. A página do CFC lista publicação no DOU em 06/12/2023, enquanto a edição oficial do DOU identifica a publicação certificada em 16/11/2023, edição 217, seção 1, p. 134; para a referência da publicação, este PT adota os dados da edição do DOU. A diferença entre a data indicada no índice do CFC e a edição do DOU fica registrada, sem efeito sobre a data de vigência expressa no item 12. [1] [2]

**Itens-chave da NBC TA 600 (R2):** 12–13 (vigência e objetivos); 14–15 (definições de grupo, componente, auditor do grupo e risco de agregação); 16–21 (responsabilidade, aceitação, acesso e contratação); 22–29 (estratégia, plano e envolvimento dos auditores de componentes); 30–34 (entendimento do grupo, identificação e avaliação dos riscos); 35–36 (materialidade); 37–44 (respostas aos riscos); 45–48 (comunicações e avaliação do trabalho dos auditores de componentes); 49–52 (eventos subsequentes e suficiência/adequação da evidência); 53 (relatório); 54–59 (comunicações e documentação). Referência por página no PDF oficial do CFC: item 12–13, p. 5; item 22, p. 8; itens 33–36, p. 11; item 37, p. 12; itens 45–48, p. 13–14; itens 51–53, p. 15; item 59, p. 16. [1]

**Objetivo deste PT:** documentar, em ambiente didático e sob a ótica do auditor do grupo, as considerações de auditoria pertinentes aos estoques consolidados, com foco em terrenos a incorporar, e as interações com o processo de consolidação, o reconhecimento de receita imobiliária e as provisões para contingências. O objetivo normativo do auditor do grupo é avaliar riscos de distorção relevante e obter evidência apropriada e suficiente, inclusive avaliando o trabalho de auditores de componentes quando envolvidos, para formar opinião sobre as demonstrações do grupo (itens 13 e 51–52). Este documento não pretende formar ou emitir tal opinião.

## Conta, processo e base pública

**Conta/processo principal:** estoques consolidados em 31/12/2025 e fluxo de informações financeiras incluído nas demonstrações consolidadas. A DFP pública integral examinada, de 31/12/2025, versão 1, protocolada em 09/03/2026, informa: ativo consolidado de **R\$ 13.219.635 mil**; estoques de **R\$ 6.951.508 mil**, compreendendo terrenos a incorporar totais de **R\$ 5.678.238 mil** (dos quais **R\$ 4.864.673 mil** não circulantes) e estoques circulantes de **R\$ 2.086.835 mil**. Para 2024, os valores comparativos são ativo de **R\$ 10.067.406 mil** e terrenos a incorporar totais de **R\$ 4.587.823 mil** (dos quais **R\$ 3.888.979 mil** não circulantes). Os valores são saldos publicados, não saldos verificados por este PT contra registros internos. A página da B3 apresenta o ativo total consolidado de 31/12/2025 em R\$ 13.219.635 mil e o de 31/12/2024 em R\$ 10.067.406 mil, ambos em R\$ mil. [3] [4] [7]

A partir somente desses valores, foram feitos recálculos aritméticos: estoques representam aproximadamente **52,6%** do ativo consolidado; terrenos a incorporar totais representam aproximadamente **81,7%** dos estoques e **43,0%** do ativo; o total de terrenos aumentou **R\$ 1.090.415 mil**, ou aproximadamente **23,8%**, frente a 2024; o ativo total aumentou aproximadamente **31,3%**. O componente não circulante de terrenos aumentou de R\$ 3.888.979 mil para R\$ 4.864.673 mil. Percentuais arredondados a uma casa decimal. Esses cálculos são comparações analíticas públicas e não testes de avaliação, existência, titularidade ou completude.

A DFP pública integral examinada reporta a **PwC** como auditor, PAA relativos a reconhecimento de receita imobiliária e provisões para contingências e opinião sem ressalva. A interface CVM confirma PwC e lista seções, mas não oferece paginação estável; as páginas relevantes do PDF foram lidas. Esses fatos descrevem o relatório público, não conclusões deste PT, e não afastam riscos nos saldos. Não houve acesso à evidência subjacente, registros internos ou arquivo privado da auditoria. [3] [4] [7]

## Afirmações e riscos considerados

Os riscos abaixo são **hipóteses/áreas de atenção para planejamento**, baseadas no peso dos estoques e dos terrenos, no tipo de atividade divulgado pela B3 e nos PAA divulgados. Não são constatações de distorção, deficiência, fraude, litígio incorretamente provisionado ou falha de controle. [3] [4]

| Área/afirmações relevantes | Risco hipotético a avaliar no grupo | Base e classificação |
|---|---|---|
| Estoques e terrenos a incorporar: existência, direitos e obrigações, avaliação/alocação, completude, corte, classificação e apresentação/divulgação. | Pelo peso relativo dos estoques e dos terrenos, há risco potencial de erro de mensuração ou alocação de custos, classificação entre circulante/não circulante, reconhecimento/corte, obsolescência ou redução ao valor realizável líquido; direitos sobre terrenos e compromissos poderiam exigir suporte documental. Nada disso foi constatado. | Saldo publicado e recálculos analíticos; risco hipotético, não conclusão. [3] [4] |
| Reconhecimento de receita imobiliária: ocorrência, exatidão, competência/corte, completude e apresentação/divulgação. | PAA publicado torna o tema relevante para a auditoria; podem existir riscos inerentes associados a julgamento de contratos, progresso/obrigações de desempenho, custos a incorrer, distratos e conciliação entre dados operacionais e contábeis. Esta lista descreve possibilidades a testar, não fatos específicos conhecidos. | PAA relatado na DFP; hipóteses a testar. [3] |
| Provisões e contingências: completude, mensuração/avaliação, corte e divulgação. | PAA publicado torna relevante examinar integridade da população de casos, avaliação de probabilidade e estimativa, eventos posteriores e consistência da divulgação; não se afirma haver contingência omitida ou estimativa inadequada. | PAA relatado na DFP; hipóteses a testar. [3] |
| Consolidação e agregação: completude do perímetro, exatidão, corte, consistência de políticas, eliminações intragrupo e risco de agregação. | Como se trata de demonstração consolidada, há risco potencial de informações de componentes não serem capturadas ou harmonizadas corretamente, ou distorções individualmente pequenas se agregarem. A composição efetiva, os componentes selecionados e os ajustes não foram disponibilizados para este exercício didático. | Aplicação condicional da NBC TA 600; composição e processo internos não verificados. [1] |
| Trabalho de auditor de componente, se houver. | Risco potencial de insuficiente envolvimento, supervisão, comunicação bilateral ou avaliação da competência/capacidade do auditor do componente; não há confirmação pública aqui de quantos auditores/componentes foram usados nem da extensão de seu trabalho. | Não inferido a partir da identificação pública da PwC como auditor das demonstrações. [1] [3] |

## População, fontes e critérios

**População pretendida para auditoria completa:** registros de estoque por projeto/empreendimento e por item (inclusive terrenos a incorporar), informações financeiras dos componentes definidos pelo auditor do grupo, reconciliações e lançamentos de consolidação, além das populações de contratos/receitas e processos/contingências que suportam os PAA. **Limitação:** tais listagens, bases, população completa e documentos internos não foram acessados. Os saldos consolidados divulgados são apenas população documental pública agregada e não foram tratados como substituto de população de auditoria.

**Fontes públicas consultadas:** DFP CVM 31/12/2025 V1, protocolo informado de 09/03/2026, e PDF integral direto do RI, com demonstrações consolidadas, notas e relatório do auditor; página de informações da companhia na B3; central de resultados e documentos entregues à CVM no RI da companhia; NBC TA 600 (R2) no repositório do CFC e publicação certificada do DOU. Fatos societários e financeiros da companhia neste PT limitam-se às fontes CVM/B3/RI indicadas. [1] [2] [3] [4] [5] [6] [7]

**Critérios normativos e de seleção propostos:** itens 22–24 e 30–34 da NBC TA 600 (R2): o auditor do grupo estabelece/atualiza estratégia e plano, determina componentes/unidades e recursos necessários, entende o grupo e seu processo de relatório/consolidação, identifica e avalia riscos e define o envolvimento dos componentes. A seleção e o trabalho não devem ser inferidos automaticamente a partir de pessoas jurídicas; deve-se considerar a forma como o grupo gera e agrega informações, a materialidade, a relevância financeira e qualitativa, riscos e possibilidades de agregação. Itens 35–36 requerem materialidade do grupo e materialidade de desempenho dos componentes, quando aplicável, com limite de comunicação de distorções. Não se definiu benchmark, materialidade monetária, limiar de amostragem ou número de componentes neste PT, pois não há documentação de planejamento, razão financeira para tais parâmetros, nem acesso à população completa. [1]

## Procedimentos e resultados

A etiqueta de status qualifica cada procedimento: **Realizado — evidência pública** significa leitura/recalculo de informação já publicada, não reexecução dos procedimentos PwC; **Planejado — falta de acesso** descreve procedimento necessário caso se conduza auditoria com autorização e documentação; **Simulado — fins didáticos** descreve desenho ilustrativo sem executar teste sobre saldos/indivíduos reais.

| Status | Procedimento e vínculo a item NBC TA 600 (R2) | Evidência/resultado |
|---|---|---|
| **Realizado — evidência pública** | Leitura da ficha CVM indicada para a DFP, identificando o auditor divulgado como PwC e as áreas do formulário eletrônico disponíveis. Itens 13, 53 e 59. | O registro CVM confirma a identificação pública do auditor. A interface CVM não oferece paginação estável; a DFP pública integral foi obtida e as páginas relevantes foram examinadas. Não foi obtida confirmação direta da PwC, nem documentação de auditoria. [3] [7] |
| **Realizado — evidência pública** | Leitura das informações de balanço consolidado disponíveis na página B3 e comparação do ativo total de 2025/2024 com os valores-base da DFP indicados para este trabalho. Itens 30, 33–34. | Ativo consolidado de R\$ 13.219.635 mil em 31/12/2025 e de R\$ 10.067.406 mil em 31/12/2024, conforme B3; valores coincidem com a base pública deste PT. Comparação de consistência entre divulgações, não conciliação com razão ou balancete. [4] |
| **Realizado — evidência pública** | Recálculo de percentuais e variações de estoques/terrenos a partir dos saldos publicados na DFP e na B3. Itens 33–36. | Estoques/ativo ≈52,6%; terrenos totais/estoques ≈81,7%; terrenos totais/ativo ≈43,0%; crescimento do total de terrenos ≈23,8%; ativo total ≈31,3%. O componente não circulante cresceu 25,1%. Cálculos descritos no escopo e reproduzíveis pelos saldos exibidos. Não foram estabelecidos limiares de investigação nem materialidade formal. [3] [4] [7] |
| **Realizado — evidência pública** | Leitura da DFP pública para identificar auditor, opinião e PAA, e exame das páginas relevantes do relatório independente e das demonstrações/notas. Itens 13, 33 e 53. | A DFP integral foi obtida no RI e as páginas impressas 115–117 foram lidas (PAA p.116); opinião sem modificação e PAA de reconhecimento de receita e contingências. Fato público, não avaliação de papéis de trabalho privados nem conciliação com evidência subjacente. [3] [7] |
| **Planejado — falta de acesso** | Obter organograma societário, lista completa de entidades/unidades de negócio, pacote de consolidação, mapas de eliminação, políticas e fechamento; entender processo e selecionar componentes/unidades segundo risco, relevância e agregação. Itens 22, 30–34. | Não executado. DFP consolidada não fornece, por si só, a população interna completa, mapeamento de processo, nem a base documentada da seleção. [1] |
| **Planejado — falta de acesso** | Determinar materialidade global e por componente, tolerância/limite de comunicação e cobertura projetada após obter informações desagregadas e compreender riscos. Itens 35–36. | Não executado. Nenhuma materialidade ou limite foi inventado. [1] |
| **Planejado — falta de acesso** | Se auditores de componentes estiverem envolvidos, avaliar independência, competência e capacidade, confirmar cooperação e escopo, transmitir instruções, dirigir/supervisionar/revisar, estabelecer comunicações bidirecionais e resolver diferenças significativas. Itens 23–29, 45–48 e 59. | Não executado. Não houve comunicação, confirmação, entrevista ou revisão de arquivo de auditor de componente neste PT. [1] |
| **Planejado — falta de acesso** | Obter listagem analítica integral de terrenos/estoques; rastrear amostra baseada em população documentada para documentos de aquisição e evidência de direitos, custos capitalizados, aprovação, localização, estágio do empreendimento, corte, custo a incorrer e valor realizável líquido; testar itens selecionados também da documentação à listagem. | Não executado. Sem registro auxiliar, escritura/contratos, custo de projeto ou acesso físico, não é possível concluir existência, titularidade, mensuração, classificação ou completude. NBC TA 600 itens 33–44, conforme riscos identificados. [1] |
| **Planejado — falta de acesso** | Avaliar receitas e provisões relacionadas aos PAA por meio de teste de contratos e cálculos de reconhecimento, confronto a bases operacionais, custos estimados e distratos; inspecionar documentos jurídicos e solicitar evidências externas quando aplicável; avaliar eventos subsequentes e divulgação. | Não executado. Não houve confirmação de advogado/cliente, entrevista, inspeção de contrato interno, recálculo por empreendimento ou busca documentada de eventos após a data-base. Itens 37–50. [1] |
| **Planejado — falta de acesso** | Testar o processo de consolidação: conciliar pacotes com demonstrações dos componentes, recalcular consolidação, testar eliminações e saldos/transações intragrupo, políticas consistentes e lançamentos manuais, e avaliar suficiência global de evidência. Itens 30–34, 37–44 e 51–52. | Não executado. Sem balancetes, pacotes de consolidação, confirmações intragrupo ou trilha de lançamentos não há base para concluir sobre o processo. [1] |
| **Simulado — fins didáticos** | Desenhar uma matriz de risco priorizando terrenos por magnitude relativa, com colunas para afirmações, controles, procedimentos substantivos, auditor responsável, evidência e conclusão; desenhar amostragem estratificada a partir da listagem real quando obtida, com seleção orientada por risco e cobertura dos itens individualmente significativos. Itens 33–44. | Apenas desenho conceitual. Não se definiu nem se selecionou amostra real; não se atribuiu quantidade a uma população inexistente neste arquivo, e nenhuma conclusão foi simulada como resultado observado. [1] |
| **Simulado — fins didáticos** | Esboçar fluxo de consolidação: mapear componentes → documentar materialidade → receber comunicação do componente → avaliar qualidade/adequação do trabalho → testar ajustes/eliminações → acumular distorções → concluir sobre evidência agregada. Itens 22–29 e 45–52. | Fluxo ilustrativo, não descrição do processo efetivamente usado pela Direcional/PwC. [1] |

## Evidências e referências cruzadas

- **E-01 / PT-600:** publicação certificada da NBC TA 600 (R2), itens 12–13 e requisitos 22–59. Documento: *Norma Brasileira de Contabilidade, NBC TA 600 (R2), de 25 de outubro de 2023*. PDF CFC, páginas indicadas acima; DOU, 16/11/2023, edição 217, seção 1, p. 134. [1] [2]
- **E-02 / PT-600:** DFP consolidada CVM 31/12/2025 V1 (protocolo informado 09/03/2026): consulta ao formulário confirma auditor PwC e lista seções; a interface não oferece paginação estável. A DFP pública integral foi obtida diretamente no RI, e as páginas relevantes foram examinadas. Saldos de estoques/terrenos, opinião e PAA foram lidos no PDF público, sem acesso à evidência subjacente ou arquivo privado. [3] [7]
- **E-03 / PT-600:** B3, perfil DIRECIONAL ENGENHARIA S.A., seção “Dados Econômico-Financeiros — Balanço Patrimonial — Consolidado”, linhas “Ativo Total”, colunas 31/12/2025 e 31/12/2024; valor em R\$ mil, conforme página. Sem número de página (página web). [4]
- **E-04 / PT-600:** RI, Central de Resultados; acesso à área pública de demonstrações/resultados. Documento-alvo deste procedimento: DFP 2025; a página é um catálogo web e não apresenta paginação própria. [5]
- **E-05 / PT-600:** RI, “Documentos Entregues à CVM”; catálogo de documentos da companhia. Referência à DFP anual 2025 e outros documentos no site não substitui o arquivo CVM citado em E-02. Página web, sem paginação própria. [6]
- **E-06 / PT-600:** recálculos independentes de razão simples e variação percentual a partir dos valores publicados; fórmulas: estoque/ativo, terrenos/estoque, terrenos/ativo e variação de saldo (2025−2024)/2024. Resultados arredondados a uma casa decimal. Não inclui procedimento sobre registros-fonte.
- **E-07 / PT-600:** RI Direcional, DFP 4T25 V1, PDF direto. Páginas impressas examinadas: balanço pp.16–17; Nota 5 p.69; Nota 6 pp.70–71; Nota 16.2 pp.93–94; relatório independente pp.115–117. Os cotejos são documentais; não houve acesso a livros ou papéis privados. [7]

## Exceções, conclusão e limitações

**Exceções/achados de auditoria:** nenhuma exceção de auditoria foi identificada por teste substantivo neste PT, pois testes substantivos e de controles não foram realizados. As leituras públicas e os recálculos não revelaram inconsistência aritmética nos valores comparáveis utilizados, mas isso não é evidência sobre suporte, direitos, existência, avaliação, completude ou corte. Os PAA e a concentração de estoques são indicadores para direcionar trabalho, não achados de distorção.

**Conclusão didática:** a relevância quantitativa dos estoques e terrenos justifica incluí-los entre as áreas prioritárias da auditoria de grupo, com avaliação de afirmações de existência, direitos, mensuração, classificação e divulgação, além de ligação com o processo de consolidação. Os PAA divulgados sobre receitas imobiliárias e contingências são relevantes para entender o perfil de risco da auditoria publicada. Com base apenas em evidência pública e procedimentos analíticos limitados, **não é possível concluir** se os estoques estão corretamente reconhecidos/mensurados, se o perímetro e a consolidação estão completos, se os riscos foram respondidos adequadamente, ou se a evidência do auditor do grupo e dos componentes é suficiente. Nenhuma opinião de auditoria é expressa por este papel didático.

**Limitações expressas:** nenhum acesso a razão, balancetes, contratos, escrituras, documentação de terreno, sistema contábil, pacote de consolidação, atas ou documentação jurídica, inventário físico ou papéis de trabalho; nenhuma confirmação externa; nenhuma entrevista com administração, auditor, advogado ou componente; nenhuma inspeção física; nenhum procedimento da PwC reexecutado; nenhuma amostra real selecionada. A DFP integral pública de 2025 foi obtida no RI e as páginas impressas relevantes foram examinadas (Nota 5 p.69, Nota 6 pp.70–71, Nota 16.2 pp.93–94 e relatório do auditor pp.115–117); o registro CVM confirma metadados, mas não oferece paginação impressa estável. Não houve acesso ao arquivo privado da auditoria nem à evidência subjacente. Não se atribui número de página não conferido. As hipóteses de risco permanecem hipóteses, não afirmações sobre eventos ou controles da companhia.

## Referências


**Fontes citadas neste papel:**

- **Ref. 1** — CFC, NBC TA 600 R2, texto oficial em PDF, 2023, 70 páginas; [abrir fonte](<https://www1.cfc.org.br/sisweb/SRE/docs/NBC%20TA%20600%20%28R2%29.pdf>).
- **Ref. 2** — Diário Oficial da União, NBC TA 600 R2, edição 217, seção 1, página 134, 16 de novembro de 2023; [abrir fonte](<https://www.in.gov.br/en/web/dou/-/norma-brasileira-de-contabilidade-nbc-ta-600-r2-de-25-de-outubro-de-2023-523235416>).
- **Ref. 3** — CVM, DFP Direcional Engenharia, exercício encerrado em 31 de dezembro de 2025, versão 1, protocolo informado de 9 de março de 2026, formulário eletrônico; [abrir fonte](<https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=155189&CodigoTipoInstituicao=1>).
- **Ref. 4** — B3, perfil DIRECIONAL ENGENHARIA S.A., informações e dados econômico-financeiros consolidados, acesso em 22 de outubro de 2026; [abrir fonte](<https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/21350/DIRR/overview?language=pt-br>).
- **Ref. 5** — RI Direcional, Central de Resultados, catálogo de demonstrações e resultados; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/central-de-resultados/>).
- **Ref. 6** — RI Direcional, Documentos Entregues à CVM, catálogo público de documentos; [abrir fonte](<https://ri.direcional.com.br/informacoes-financeiras/documentos-entregues-a-cvm/>).
- **Ref. 7** — RI Direcional, DFP 4T25 V1, PDF integral; páginas impressas citadas no PT; [abrir fonte](<https://api.mziq.com/mzfilemanager/v2/d/ada9bc2c-f7d0-4359-9eaf-851b679ab788/184f5357-c3a8-12a9-3a85-cdb268303bcb?origin=2>).

