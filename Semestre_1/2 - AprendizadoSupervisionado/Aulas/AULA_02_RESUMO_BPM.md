# AULA 2 — BUSINESS PERFORMANCE MANAGEMENT (BPM)

## Disciplina: Aprendizado de Máquina Supervisionado — Graduação em IA (FMU)

---

## 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Supervisionado
**Aula:** 2 — Business Performance Management (BPM)
**Fonte:** *Introdução à Inteligência de Negócios* — Aline Zanin, SAGAH (Soluções Educacionais Integradas), capítulo "Business performance management (BPM)"

### Objetivos de aprendizagem (conforme o capítulo)
- Explicar os conceitos de estratégia, plano e monitoramento.
- Aplicar medidas de desempenho.
- Analisar metodologias de BPM.

**Observação de contexto:** esta aula muda de eixo em relação à Aula 1 (que tratou de Machine Learning propriamente dito) — o foco passa a ser gestão e inteligência de negócios (BI), um domínio de apoio à decisão que frequentemente fornece o contexto/dados para os modelos de aprendizado de máquina.

---

## 2. Resumo e Contextualização

**BPM (business performance management)**, ou gerenciamento do desempenho do negócio, é uma ferramenta de suporte à tomada de decisão. Ele abrange um conjunto de processos, metodologias, métricas e aplicações criadas para medir o desempenho geral de uma empresa, ajudando gestores a converter estratégias em planos e objetivos, e depois monitorar o desempenho em relação a esses objetivos.

O capítulo situa o BPM dentro de um conjunto maior de ferramentas com o mesmo propósito, mas nomes diferentes conforme a empresa criadora: **corporate performance management (CPM)** e **enterprise performance management (EPM)**.

> **BPM Standard Group** define BPM como "uma estrutura destinada a organizar, automatizar e analisar as metodologias de negócios, bem como as métricas, os processos e os sistemas, visando a induzir o desempenho geral da empresa" (TURBAN *et al.*, 2009).

Pontos importantes de definição:
- O BPM **faz parte** das estratégias de *business intelligence* (BI), mas não se limita a isso.
- O BPM **não é** uma tecnologia ou *software* de ERP (*enterprise resources planning*).
- Segundo Chicaleski (2008), o BPM "pode ser definido como a união de componentes, como orçamento, planejamento, [BI], integração de dados, previsões e simulações".

---

## 3. Conceitos Fundamentais e Explicações

### 3.1 Ciclo do BPM (Figura 1, Turban et al., 2009, p. 195)

O ciclo é dividido em dois grandes eixos:
- **Eixo da estratégia** → estratégias e planos
- **Eixo da execução** → monitoramento, ação e ajustes

Conectados ao centro por **dados integrados**.

```
                    ESTRATÉGIA
        1. Fazer estratégias    2. Plano
     (planos estratégicos,     (planos, orçamentos,
      mapas estratégicos)       cenários, projetos)
                    ↕
              Dados integrados
                    ↕
     (ofertas e ações          (alertas, relatórios/
      de agentes, previsões     análise, painéis)
      e métodos)
        4. Agir e ajustar      3. Monitorar
                    EXECUÇÃO
```

**1. Estratégias** — respondem a "para onde queremos ir no futuro?". Geralmente formalizadas em um **planejamento estratégico** (mapa de ações para atingir objetivos em um período). Estratégias podem apresentar **lacunas** (gaps entre o planejado e o executado), causadas por 4 fatores principais:

| Causa da lacuna | Descrição |
|---|---|
| **Visão** | Poucos funcionários conhecem a estratégia/visão da empresa, dificultando decisões alinhadas |
| **Pessoas** | Remuneração motiva a curto prazo, mas não alinha o colaborador à visão da empresa |
| **Gerenciamento** | Gestores nem sempre identificam os problemas principais, dispersando esforços |
| **Recursos** | Equipes superestimam o orçamento disponível e não conseguem executar a estratégia |

**2. Planos** — respondem a "como chegaremos até lá?". O plano operacional converte estratégia em metas, táticas, recursos e resultados esperados. Pode ser:
- **Centrado em táticas** — práticas para atender aos objetivos do planejamento estratégico.
- **Centrado em orçamentos** — ações planejadas visando ao lucro final.

**3. Monitoramento** — garante que o plano operacional ocorre conforme esperado. Desafio principal: definir **o quê** e **como** monitorar de forma que agregue valor.

**4. Agir e ajustar** — sem plano de ação/ajuste, estratégia, plano e monitoramento perdem utilidade. Toda divergência identificada no monitoramento deve gerar ação imediata.

### 3.2 Medidas de Desempenho — Quadro 1 (conceitos básicos)

| Conceito | Definição | Exemplo |
|---|---|---|
| **Métrica** | Marcação de um fator monitorado; ponto de registro/controle | Altura — 1,80 m; faturamento — 2 milhões |
| **Medida** | Quantidade de registros de um valor/desempenho, por acumulação | 30 clientes por dia (média); 200 mil *likes* até hoje (total) |
| **Indicador** | Fator qualitativo/quantitativo que expressa realização ou mudança; pode agregar várias medidas | 30% a mais de clientes no último ano; 10 graus de diferença entre cidades |

**Relação entre os três (Figura 2, Lawrence, 2019):**
Métrica = **marcação** (registra um valor) → Medida = **acúmulo** → Indicador = **variação** em comparação com outros cenários.

### 3.3 Sistema de Medida de Desempenho

Conjunto de estratégias de medição de desempenho. Características de um bom sistema:
- Concentra-se em fatores cruciais.
- Mistura passado, presente e futuro.
- Equilibra necessidades de acionistas, funcionários, parceiros, fornecedores e demais interessados.
- Tem metas baseadas em pesquisa e realidade, não arbitrárias.

> Segundo Simons (2002, *apud* Turban *et al.*, 2009, p. 206): sistemas de medida de desempenho "auxiliam os gerentes a rastrear as implementações de estratégia de negócios comparando os resultados reais com metas estratégicas e objetivos [...] geralmente engloba métodos sistemáticos de união de metas de negócios com relatórios de retorno periódicos que indicam progresso contra metas."

**3 etapas para criar um sistema de medida de desempenho:**
1. **Definição e detalhamento de indicadores** — etapa mais importante; define quais indicadores serão monitorados.
2. **Implementação de um sistema de informação** — envolve 3 níveis:
   - *Interface do usuário* (navegador, planilhas, ERP)
   - *Tecnologias capacitadoras* (ex.: *dashboards* de BI)
   - *Bancos de dados* (estruturados ou repositórios de planilhas)
3. **Uso e revisão do sistema** — melhorias e adequações contínuas à realidade da empresa.

### 3.4 Metodologias de BPM

#### Balanced Scorecard (BSC)

Modelo de sistema de gestão baseado em um *cockpit* de indicadores que orienta a condução da empresa a partir de múltiplas perspectivas.

**2 premissas básicas:**
1. Indicadores financeiros isoladamente não explicam sucesso/fracasso.
2. Gestores precisam de informação em tempo adequado.

**4 perspectivas do BSC** (Figura 3, Turban et al., 2009, p. 211):

| Perspectiva | Pergunta-chave |
|---|---|
| **Financeira** | Para ter sucesso financeiro, como deveríamos aparecer para nossos acionistas? |
| **Cliente** | Para alcançar nossa visão, como deveríamos aparecer para nossos clientes? |
| **Processos internos de negócios** | Para satisfazer acionistas e clientes, em que processos devemos nos superar? |
| **Aprendizado e crescimento** | Para alcançar nossa visão, como sustentamos nossa capacidade de mudar e melhorar? |

Todas as 4 perspectivas giram em torno do centro: **visão e estratégia** da empresa. Cada perspectiva usa uma matriz com 4 colunas: **Objetivos, Medidas, Metas, Iniciativas**.

**Exemplo do capítulo:**
- Objetivo: aumentar as vendas.
- Medidas: comparação matemática das vendas com o mesmo período do ano anterior.
- Meta: ser a empresa que mais vende no segmento X no ano 2022.
- Iniciativas: aumentar divulgação da marca; vender produtos da marca Y.

O ponto focal do BSC é o **equilíbrio**: financeiro x não financeiro, interno x externo, quantitativo x qualitativo, curto x longo prazo.

#### Six Sigma

Estratégia de gestão **quantitativa** (usa estatística) e **estruturada** (metodologia específica), focada na melhoria de processos já existentes.

**3 objetivos principais:**
1. Redução de custos.
2. Otimização de produtos e processos.
3. Incentivo à satisfação do cliente.

Fornece meios para medir/monitorar processos-chave ligados à lucratividade e acelerar melhoria de desempenho (TURBAN *et al.*, 2019). Foco principal: satisfação do cliente via redução de defeitos.

**Duas metodologias, cada uma com 5 fases (Periard, 2012):**

**DMADV** (para *novos* processos/produtos):
1. *Define goals* — definir objetivos alinhados a cliente e gestão.
2. *Measure and identify* — mensurar características críticas para a qualidade.
3. *Analyze* — desenvolver e projetar alternativas.
4. *Design details* — projetar detalhes e otimizar (fase mais longa, exige muitos testes).
5. *Verify the design* — executar pilotos, implementar produção, entregar ao proprietário do processo.

**DMAIC** (para *melhorar* processos existentes):
1. *Define the problem* — a partir de opiniões de clientes e objetivos da empresa.
2. *Measure key aspects* — aspectos principais do projeto atual.
3. *Analyze the data* — relação causa e efeito.
4. *Improve the process* — melhorar/otimizar com base na análise.
5. *Control* — assegurar correção de desvios futuros.

**BSC x Six Sigma:** a escolha depende da afinidade da equipe e do foco desejado. Six Sigma foca em resultados/cliente e exige base organizacional sólida; BSC identifica oportunidades de melhoria alinhadas aos objetivos estratégicos (VASQUES, 2019).

---

## 4. Exemplos, Aplicações e Material Prático

- **Exemplo de matriz BSC** (perspectiva financeira): Objetivo "aumentar vendas" → Medida "comparação com mesmo período do ano anterior" → Meta "ser líder no segmento X em 2022" → Iniciativas "aumentar divulgação da marca, vender produtos da marca Y".
- **Aplicação de Six Sigma citada no capítulo:** monitoramento de gastos com luz, diárias de viagem, telefone etc.
- Links complementares citados no capítulo (não verificados nesta sessão): vídeo sobre BSC e vídeo sobre Six Sigma (Canal Instituto Montanari; Canal Grupo Voitto).

---

## 5. Minhas Observações e Dúvidas

*(Espaço reservado — nenhuma observação registrada até o momento para esta aula.)*

---

## 6. Referências e Conexões com Outros Conteúdos

### Referência principal
ZANIN, Aline. **Introdução à Inteligência de Negócios** — capítulo "Business performance management (BPM)". SAGAH.

### Referências citadas no capítulo
- CHICALESKI, P. M. D. *O que é business performance management?* 2008.
- LAWRENCE, C. *Qual a diferença entre métrica, medida e indicador?* 2019.
- PERIARD, G. *Seis sigma: o que é e como funciona.* 2012.
- SIMONS, R. *Performance measurement and control systems for implementing strategy.* Upper Saddle River, NJ: Prentice Hall, 2002.
- TURBAN, E. *et al. Business intelligence: um enfoque gerencial para a inteligência do negócio.* Porto Alegre: Bookman, 2009.
- VASQUES, R. C. *Balanced Scorecard (BSC), CMMI e Six Sigma, como construir altos níveis de maturidade e desempenho.*

### Conexões com outras disciplinas/aulas
- **Aula 1 (Aprendizado de Máquina):** troca de eixo — de um conteúdo técnico/algorítmico (ML) para um conteúdo de gestão/BI. O BPM é o tipo de contexto de negócio que consome os resultados de modelos de AM (ex.: um indicador do BSC pode ser alimentado por uma predição de ML).
- **Aquisição e Preparação de Dados:** o conceito de "dados integrados" no centro do ciclo do BPM dialoga com o ETL já estudado (extração/integração de dados de múltiplas fontes para consolidar indicadores).

---

**Status:** Aula 2 documentada.
