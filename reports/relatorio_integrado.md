# Dossiê didático de auditoria independente

## Direcional Engenharia S.A. — exercício encerrado em 31 de dezembro de 2025

**Preparador:** EDU-AUD-001 (matrícula didática, não atribuída a pessoa real)  
**Data:** 22 de outubro de 2026  
**Revisor:** campo não preenchido — nenhuma revisão de terceiro foi simulada.  
**Moeda:** reais; nas demonstrações, em geral R$ mil.  
**Classificação:** material didático baseado em informação pública e dados sintéticos.

> **Aviso:** Este trabalho não é auditoria contratada nem opinião independente sobre as demonstrações da Direcional. Não houve acesso a livros auxiliares, contratos, títulos, controles, sistemas, extratos, atas, confirmações externas ou instalações. As informações do emissor e o relatório PwC são apresentados como fatos/documentos públicos, sem apropriar os procedimentos do auditor da companhia. Procedimentos que exigiriam evidência interna estão marcados como planejados por falta de acesso; o único teste em população de grande porte foi feito sobre dados sintéticos expressamente identificados.

## 1. Objetivo, escopo e premissas

O dossiê organiza o planejamento didático para a NBC TA Estrutura Conceitual e as NBC TAs 200 a 600 aplicáveis ao roteiro. A população financeira analisada é o exercício de 2025, com comparativos de 2024 e, quando divulgado na DFP, 2023. A pesquisa de eventos subsequentes foi estendida até 22/10/2026. Foram utilizados documentos públicos da CVM, B3 e da área de RI da companhia para fatos corporativos. Endereços, exercícios, datas de acesso, páginas e limites estão no **Apêndice B — Fontes públicas**; versões e cobertura das normas estão no **Apêndice A — Matriz de cobertura das normas**.

O trabalho contém três classes de procedimento, sem confundi-las: **realizado com evidência pública**, quando o procedimento foi executado sobre a DFP/ITR/comunicados; **planejado por falta de acesso**, quando depende de evidência interna ou confirmação e não foi executado; e **simulado para fins didáticos**, para os testes sobre a base artificial. A documentação de cada papel especifica código, objetivo, afirmações, riscos, população, método, referência, conclusão, limitações, preparador/data e campo de revisão.

## 2. Conclusão executiva

A conta selecionada para a base de dados é **Estoques**, a maior rubrica individual do ativo consolidado: R$6.951.508 mil na Nota 5 de 2025. A conta compreende terrenos a incorporar (R$5.678.238 mil, 81,7% dos estoques e 43,0% do ativo), imóveis em construção (R$1.174.207 mil) e imóveis concluídos (R$99.063 mil). A predominância de terrenos orienta os riscos específicos de direitos/títulos, contratos de permuta, existência, ônus, classificação e mensuração pelo custo e valor realizável líquido; obras em andamento também envolvem capitalização de custos e estimativas para completar.

A DRE consolidada mostra receita de R$4.343.008 mil, crescimento de 29,7% sobre 2024, e resultado antes de tributos de R$1.078.495 mil, crescimento de 36,1%. O relatório PwC emitido sobre 2025 apresenta opinião sem modificação e parágrafo de ênfase sobre a política de reconhecimento da receita de unidades imobiliárias em construção; os principais assuntos de auditoria descritos são o reconhecimento de receita e provisões para contingências. Essa opinião pertence à PwC; este dossiê não reexecutou os testes nem emite opinião.

A triagem prioriza: (i) estoques de terrenos e custo/valor realizável; (ii) reconhecimento de receita de construção pelo progresso físico/financeiro e estimativas de custo para completar; (iii) recebíveis/distratos e perdas esperadas; (iv) dívida, liquidez, swaps, covenants e fluxos de caixa; (v) provisões e partes relacionadas; e (vi) perímetro e consolidação de SPEs/SCPs/empreendimentos. A administração declara não conhecer incerteza significativa de continuidade; a declaração e as métricas públicas não substituem a obtenção e teste independente de projeções, vencimentos, covenants, restrições de caixa e cenários.

Há ainda uma **inconsistência cronológica aparente**: a Nota 1 informa aprovação das demonstrações pelo Conselho em 10/03/2026, enquanto o relatório PwC está datado de 09/03/2026. Sem ata, assinaturas eletrônicas e versão final, o efeito é indeterminado; o procedimento apropriado é esclarecer a sequência com evidência formal. Não se conclui irregularidade nem se altera a opinião pública.

## 3. Procedimentos e evidência obtida

### Realizado com evidência pública

Foram identificados e conciliados, no limite dos demonstrativos publicados: a identidade da companhia (Direcional Engenharia S.A., DIRR3), totais consolidados e comparativos, nota de estoques, receita e resultado, saldos de partes relacionadas, política de continuidade, principais assuntos de auditoria, opinião PwC, dívida e posição líquida divulgadas pela administração, eventos subsequentes e documentos pós-período. A comparação da DFP com a ficha da B3 não indicou alteração de denominação empresarial ou ticker no exercício de 2025; essa conclusão limita-se às fontes públicas examinadas. A Nota 5 foi reconciliada aritmeticamente; o balanço publicado foi comparado aos quadros de resultados do RI e à ficha da B3. As tabelas editáveis preservam valores-base, fórmulas, limites de investigação e fonte.

### Planejado por falta de acesso

Não foram realizados circularização de bancos, clientes, advogados ou fornecedores; inspeção física de terrenos/obras; exame de matrícula, escritura, contrato ou laudo interno; entrevista da administração; walkthrough; observação de controles; teste de lançamentos contábeis no razão; recálculo de POC usando orçamento/medições; verificação de pagamentos posteriores ou acesso à TI. Esses procedimentos foram desenhados por ciclo, riscos e afirmações, mas dependem de autorização e fornecimento de evidência interna. Nenhuma solicitação foi enviada em nome da companhia ou de uma firma.

### Simulado para fins didáticos

A população `data/estoques_sinteticos.csv.gz` tem 500.000 itens sintéticos distintos: 420.000 terrenos, 75.000 unidades em construção e 5.000 unidades concluídas. O valor contábil soma exatamente R$6.951.508.000,00, conciliando por classe com a Nota 5 e entre circulante (R$2.086.835.000,00) e não circulante (R$4.864.673.000,00). A amostra aleatória simples sem reposição contém 1.000 itens, semente 20251232; uma seleção dirigida independente contém os 200 maiores saldos e tem uma unidade em comum com a SRS. O desenho estatístico é apenas ilustrativo e não valida saldo real nem substitui desenho amostral profissional.

Cinco grupos de exceções foram implantados para testar a detecção: documentação incompleta (200), áreas inválidas (150), sinais de valor realizável líquido inferior ao saldo (500), classificações divergentes (250) e avaliações antigas (300). O programa identificou exatamente todas as exceções artificiais conhecidas. A amostra de 1.000 detectou cinco ocorrências (0, 1, 1, 1 e 2, respectivamente). O shortfall implantado de VLR na base foi R$1.191.323,15; a projeção amostral sintética é R$454.595,00, com intervalo ilustrativo de 95% de R$0,00 a R$1.344.710,64. Nenhum desses valores representa a Direcional.

## 4. Materialidade e análise financeira

Como julgamento didático, foi adotado benchmark de 0,75% do ativo consolidado (R$13.219.635 mil): materialidade global de R$99.147.262; materialidade para execução de 70% (R$69.403.084); materialidade específica para Estoques de 0,50% do saldo (R$34.757.540); e limiar claramente trivial de 5% da global (R$4.957.363). Esses percentuais não são prescritos como regra pela NBC TA 320 e não correspondem à materialidade fixada pela PwC; devem ser revistos após a análise de erros, volatilidade, usuários e resultados finais.

A comparação anual indica variação de ativos de 31,3%, estoques de 25,7%, terrenos a incorporar de 23,8%, receita de 29,7%, resultado antes de tributos de 36,1% e empréstimos e financiamentos de 78,0% (2024 para 2025). São sinais para explicação e testes, não distorções por si só. A dívida líquida divulgada passou de posição de caixa líquido de R$68,2 milhões em 2024 a dívida líquida de R$532,6 milhões em 2025. A administração vincula o movimento ao pagamento de R$804 milhões em dividendos extraordinários no encerramento. Cerca de 90% do endividamento divulgado é de longo prazo, com prazo médio de 64 meses; a geração de caixa operacional informada para 2025 foi de R$104 milhões, após efeitos não operacionais líquidos positivos de R$779 milhões. As métricas reforçam foco em previsões, fluxo de caixa, covenants, restrições, vencimentos e decisões de distribuição, sem provar insuficiência de caixa ou incerteza material.

## 5. Eventos subsequentes e atualização de riscos

O ITR de 30/06/2026 reporta ativo consolidado de R$14.628.318 mil, terrenos a incorporar de R$6.345.109 mil e ajuste a NRV em estoques de R$4.310 mil (2025: R$4.165 mil). A nota informa capitalização líquida de juros de R$65.902 mil no semestre, R$48.217 mil ainda nos estoques de unidades não vendidas. A prévia operacional de 3T26 (não auditada) informa queda de vendas contratadas, lançamentos inferiores ao trimestre anterior, distratos acima do normal, geração operacional de caixa de R$228 milhões e geração contábil de R$10 milhões. A companhia também emitiu R$150 milhões de debêntures em 25/09/2026, encerrando a oferta em 05/10, e divulgou participação acionária de 4,7805% da Driehaus em 16/10, sem intenção declarada de alterar controle/administração.

Esses eventos são considerados para atualizar a avaliação de continuidade, liquidez, estoque e eventos subsequentes. Em regra, eventos que surgiram após a data-base não ajustam 2025; deve-se verificar se fornecem evidência sobre condições já existentes em 31/12/2025 e se há divulgação necessária. Os dados do 3T26 são preliminares e explicitamente não auditados. A emissão de CRI de R$437,5 milhões em 04/03/2026 é divulgada na Nota 26 como evento subsequente e deve ser tratada conforme a natureza do evento e as condições da data-base.

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
