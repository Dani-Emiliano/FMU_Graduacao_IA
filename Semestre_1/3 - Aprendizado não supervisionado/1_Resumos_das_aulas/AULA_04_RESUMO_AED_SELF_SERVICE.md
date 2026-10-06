# AULA 4 — ANÁLISE EXPLORATÓRIA DE DADOS (REVISÃO) E SELF-SERVICE ANALYTICS

## APRENDIZADO DE MÁQUINA NÃO SUPERVISIONADO (262GGR6044A) — Graduação em IA, FMU

---

## 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Não Supervisionado (262GGR6044A)
**Aula:** 4 — "Unidade 4"
**Livros-base:**
- *Preparação e Análise Exploratória de Dados* — Rafael Gastão Coimbra Ferreira, capítulo "Análise exploratória de dados" (SAGAH).
- *Analytics para Big Data* — Juliane Adelia Soares, capítulo "Self-service analytics" (SAGAH).

**Objetivos de aprendizagem da Unidade:**
- Definir o processo de análise exploratória de dados.
- Descrever as etapas da análise exploratória.
- Reconhecer a importância da análise exploratória.
- Reconhecer o papel do autoatendimento na análise de dados.
- Aplicar técnicas de busca de insights.
- Apontar estratégias de autoatendimento.

**Como ler este arquivo:** o conteúdo está separado em três tipos, sempre identificados:
- **Material acadêmico:** o que consta nos capítulos, infográficos e atividade da unidade.
- **Observações da Dani:** suas interpretações e dúvidas.
- **Complementação:** explicações, exemplos e cuidados acrescentados para estudo. **Não são do livro nem do professor.**

---

## 2. Resumo e Contextualização

A Unidade 4 tem dois blocos:

1. **Análise exploratória de dados (AED):** é **o mesmo capítulo** já estudado na Aula 4 de *Aquisição e Preparação de Dados* (262GGR6046A). Por isso aparece aqui **em modo revisão**: o conteúdo completo está em `AULA_4_ANALISE_EXPLORATORIA_COMPLETO.md` e no notebook daquela disciplina. Esta aula registra só o que é **novo** (seção 3).
2. **Self-service analytics (análise de autoatendimento):** conteúdo novo e foco da aula. Trata de como usuários de negócio analisam dados com autonomia, sem depender de uma equipe de TI, e dos desafios e estratégias para isso funcionar (seções 4 a 6).

**Ligação entre os blocos:** a AED garante a qualidade dos dados para qualquer análise. No autoatendimento, esse cuidado sai das mãos de especialistas e passa a depender de usuários de negócio e de governança. É por isso que a qualidade de dados reaparece como estratégia central do capítulo de self-service.

---

## 3. AED em modo revisão: o que é novo nesta unidade

### 3.1 O que se repete (não registrado de novo)

Pirâmide dados → informação → conhecimento → sabedoria; AED × estatística clássica e bayesiana; classificação das variáveis (discreta, contínua, nominal, ordinal); etapas (coleta, organização, tratamento, análise, apresentação e interpretação); missing values; outliers; normalização; análise univariada, multivariada e correlação; tabular × gráfica; qualidade de dados em projetos de ML.
**Ver:** `AULA_4_ANALISE_EXPLORATORIA_COMPLETO.md` (disciplina anterior).

### 3.2 Detalhes do capítulo com pouca ou nenhuma presença no registro anterior *(material acadêmico)*

| Detalhe | O que o capítulo diz |
|---|---|
| **Exemplo do KNN** | Em uma variável "sexo" com valores M, F e **10**, o valor 10 está fora da escala. Se não for corrigido, o algoritmo (KNN) não acha boa relação nos dados e o resultado no treino é ruim |
| **Análise separada só com outliers** | Abordagem útil para investigar casos extremos, com exemplos do capítulo: desempregados que sempre pedem seguro-desemprego, alunos que só tiram nota máxima, empresas com alto lucro em tempo de alta inflação, fraudes |

### 3.3 Infográfico: técnicas de tratamento de valores ausentes *(material acadêmico)*

O infográfico "Tratamento de dados na AED" apresenta duas saídas para dados ausentes:
1. **Recorrer ao processo que gera a informação** e tentar recuperá-la.
2. **Substituir por um valor (imputation)**, com cinco formas:

| Técnica | Como funciona (infográfico) | Quando usar *(complementação)* | Exemplo teórico | Exemplo real |
|---|---|---|---|---|
| **Educated guessing** | Infere o valor ausente pelo padrão existente nos dados. Pouco utilizada | Quando há conhecimento de especialista e poucos casos | Idade ausente inferida pelo ano de formatura | Um analista que conhece o cliente completa o campo "porte da empresa" |
| **Average imputation** | Usa a média da coluna (das observações com valor) | Variável numérica, poucos ausentes, sem muitos outliers (com outliers, a **mediana** é mais segura) | Renda ausente = média das rendas | Pesquisa de satisfação com nota de 0 a 10 faltando em 3% das linhas |
| **Common-point imputation** | Valores ausentes viram valores padrão ou os que mais se repetem | Variáveis **categóricas** (moda) | Estado civil ausente = "casado" (o mais frequente) | Campo "forma de pagamento" vazio recebe a forma mais usada |
| **Regression substitution** | Modelo de regressão múltipla estima o valor ausente | Quando a variável tem forte relação com outras | Peso ausente estimado pela altura e idade | Preço de imóvel ausente estimado por área, quartos e bairro |
| **Multiple imputation** | Estende a regressão, identificando correlações com os valores ausentes | Quando a ausência é relevante e se quer refletir a incerteza da imputação | Várias versões preenchidas da base, analisadas em conjunto | Pesquisa de saúde com muitas respostas em branco |

Além da imputação, o capítulo cita a opção de **descartar** o registro com valor ausente e o exemplo da **repetição do último valor** (útil em séries ao longo do tempo).

**Quando cada opção pesa (complementação):**

| Situação | Tendência de escolha | Cuidado |
|---|---|---|
| Poucos ausentes, aleatórios | Descartar ou imputar com média/mediana | Descartar muito reduz a amostra |
| Muitos ausentes numa coluna | Avaliar remover a coluna ou imputar por modelo | Imputar por média reduz a variância e pode enviesar |
| Categórica | Moda ou categoria "não informado" | "Não informado" pode ser informação por si só |
| Série temporal | Repetir o último valor ou interpolar | Longos períodos sem leitura distorcem a série |
| Ausência com motivo (ex.: pessoa constrangida em informar renda) | Investigar o motivo antes de imputar | A ausência pode estar ligada ao próprio valor |

### 3.4 Falha de edição no infográfico *(observação)*

Sob o título **"Tratamento de outliers"**, o infográfico traz o texto sobre pessoas que se sentem constrangidas e não respondem determinadas questões, e sobre "preencher a informação faltante". Esse texto trata de **valores ausentes**, não de outliers. A definição de outlier ("valor atípico, grande afastamento dos demais") aparece no mesmo bloco, mas misturada com isso.

### 3.5 Imagine que... *(complementação)*

- **Imagine que** você tem uma pesquisa com a coluna *renda* ausente em 30% das linhas, porque muitas pessoas não quiseram informar.
- **Será tratado por** análise do motivo da ausência e, se for razoável imputar, mediana ou regressão (com uma coluna indicadora "renda ausente").
- **Porque** descartar 30% da amostra empobrece a análise, e imputar a média apaga o fato de que a ausência pode estar ligada ao próprio valor (quem tem renda muito alta ou muito baixa evita responder).

### 3.6 Material prático: imputação em Python *(complementação, testado)*

```python
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame({
    "renda":        [3200, np.nan, 4100, 2800, np.nan, 5200],
    "estado_civil": ["casado", "solteiro", None, "casado", "casado", None],
    "temp_c":       [21.5, np.nan, np.nan, 22.1, 22.4, np.nan],
})

print(df.isna().sum())                  # quantos ausentes por coluna
print((df.isna().mean() * 100).round(1))  # % de ausentes por coluna

d = df.copy()
d["renda"] = d["renda"].fillna(d["renda"].median())         # numérica: mediana (robusta a outliers)
d["estado_civil"] = d["estado_civil"].fillna(d["estado_civil"].mode()[0])  # categórica: moda
d["temp_c"] = d["temp_c"].ffill()                           # série: repete o último valor

# Equivalente com scikit-learn (útil dentro de Pipeline, evitando vazamento de dados):
num = SimpleImputer(strategy="median").fit_transform(df[["renda"]])
cat = SimpleImputer(strategy="most_frequent").fit_transform(df[["estado_civil"]])
```
Resultado do teste: `renda` ausente vira 3650 (mediana), `estado_civil` ausente vira "casado" e `temp_c` repete 21,5 e 22,4.

**Regra de ouro:** em projetos supervisionados, ajuste o imputador **só no treino** e apenas aplique no teste (como na PCA da Aula 3).

---

## 4. Self-service analytics: conceito e importância

### 4.1 Contexto: volume de dados *(material acadêmico)*

O capítulo cita o relatório *Data Never Sleeps 9.0* (DOMO, 2021), com a estimativa de dados gerados **por minuto em 2020**:

| Plataforma | Volume por minuto |
|---|---|
| Facebook | cerca de 240 mil fotos compartilhadas |
| Twitter | cerca de 575 mil tweets |
| Instagram | cerca de 65 mil fotos |
| YouTube | cerca de 694 mil horas de vídeo |
| Netflix | cerca de 452 mil horas assistidas |
| TikTok | cerca de 167 milhões de vídeos assistidos |

Essas coleções são **big data**: volume, velocidade e variedade tão grandes que dificultam armazenar, gerenciar, processar e analisar com bancos e ferramentas tradicionais (Bahga e Madisetti, 2019).

### 4.2 Análise de dados e autoatendimento *(material acadêmico)*

- **Análise de dados (data analytics)**, segundo Zhang (2017): definir metas e as perguntas que os dados devem responder → coletar → inspecionar → interpretar, separando os "bits úteis" para apoiar a decisão, descobrir tendências e **confirmar ou refutar ideias** existentes.
- **Self-service analytics (análise de autoatendimento):** ferramentas **prontas para uso**, com as quais usuários finais interagem e configuram, **filtrando, classificando, analisando e visualizando** dados **sem envolver** TI ou especialistas em análise (Myers e Kogan, 2021).
- **Mudança de paradigma:** de plataformas **governadas e centradas em TI** para plataformas **descentralizadas**, em que o usuário de negócio lida com recursos analíticos de autoatendimento e descoberta de dados.
- Segundo Daradkeh e Al-Dwairi (2017), é uma inovação que torna os usuários mais autossuficientes, estende o alcance das ferramentas de analytics e libera a TI para recursos mais avançados. O capítulo cita a **redução de cerca de 47% nas solicitações de atendimento**.

**Motivadores para adotar (Daradkeh e Al-Dwairi, 2017):**
1. Necessidade de constantes mudanças nos negócios.
2. Incapacidade da TI de atender novos requisitos de forma imediata.
3. Necessidade de organizações mais analíticas.
4. Acesso lento às informações.

### 4.3 Vantagens, benefícios e desafios *(material acadêmico)*

**Quatro vantagens (Imhoff e White, 2011):**

| Vantagem | Ideia central |
|---|---|
| **Resultados simples de interpretar** | Ambiente simples para descobrir, acessar e compartilhar; painéis personalizáveis; definições de negócio claras; linhagem de dados rastreada e documentada |
| **Ferramentas fáceis de usar** | Usuários acessam informações, escolhem relatórios e criam análises sozinhos, sem depender de TI |
| **Soluções de data warehouse mais rápidas** | Implantação alternativa (ex.: SaaS) para reduzir custos, melhorar o *time-to-value* e dar desempenho e escalabilidade |
| **Fácil acesso à fonte de dados** | Nem tudo precisa estar no DW. Dados externos (meteorológicos, geográficos, demográficos) e de vários tipos (estruturados, não estruturados, semiestruturados) integrados sem suporte da TI |

**Sete benefícios (Castro, 2016):**

| Benefício | Ideia central |
|---|---|
| Usuários orientam suas próprias análises | Acesso simplificado a várias fontes, em tempo real, de várias perspectivas |
| Liberação das equipes de TI | TI deixa de gerar relatórios sob demanda e foca prioridades de maior valor |
| Análises mais coerentes e ágeis | Dados integrados e atualizados criam uma "**versão única da verdade**" |
| Navegação pelos relatórios | Aprofundar detalhes, filtrar por período, isolar problemas e oportunidades |
| Redução da "fadiga decisória" | Painéis-resumo convertem informação em ação rápida |
| Redução de custos | Menos especialistas; SaaS troca investimento inicial por assinatura mensal e escala conforme os usuários |
| Alteração da cultura empresarial | De reativa para preventiva/proativa; melhor percepção de custos reais e de preços |

**Três desafios (Castro, 2016):**

| Desafio | O que pode acontecer |
|---|---|
| **Resultados analíticos imprecisos** | Fontes e formatos variados, conjuntos incompletos ou erros não corrigidos; usuários trabalhando com **versões diferentes dos mesmos dados** ou preparando-os de formas distintas, gerando informação inconsistente |
| **Segurança de dados e privacidade** | Amplo acesso sem política forte permite acesso indevido a dados confidenciais e violação de regulamentos de privacidade |
| **Implementações não controladas** | Sem monitoramento centralizado e supervisão especializada, o ambiente fica desordenado: dados inconsistentes, ferramentas diferentes e custos excessivos |

---

## 5. Níveis de autoatendimento *(material acadêmico: Alpar e Schulz, 2016)*

O autoatendimento varia conforme a tarefa. Na Figura 1 do capítulo, **quanto maior a autossuficiência do usuário, maior a necessidade de conhecimento** (e de suporte do sistema).

| Nível | O que o usuário faz | Quem prepara | Limite |
|---|---|---|---|
| **1. Uso de informações** | Acessa relatórios existentes ou só define parâmetros; relatórios e painéis que permitem "**perfurar em qualquer lugar**" (drill: do agregado ao detalhe por caminhos predefinidos) | Especialistas de BI | Adequado a usuários casuais e a insights básicos; pouco flexível para percepções individuais profundas; restrito ao que o BI preparou |
| **2. Criação de informações** | Acessa dados no nível **desagregado** mais baixo e cria relatórios e visualizações; faz análises avançadas (preditivas, mineração de texto) com funções analíticas prontas | Ferramentas criam visualizações virtuais sem exigir SQL | Risco de selecionar dados com trechos incorretos ou agregados, por não entender a relação dos dados por trás |
| **3. Criação de recursos de informação** | Usa **novas fontes sem pré-processamento** e as combina temporariamente com dados corporativos; monta **mashups** (arrastar e soltar componentes reutilizáveis num painel) | Componentes preparados pela TI | Exige mais conhecimento e é onde o risco de inconsistência cresce |

**Ajuste usuário-ferramenta:** depende das **tarefas**, **demandas de informação**, **habilidades de computador** e **habilidades analíticas**. Usuários de uma mesma função podem ter necessidades e habilidades diferentes, então não precisam ser agrupados só por função.

### 5.1 Quando usar cada nível *(complementação)*

| Nível | Quando usar | Exemplo teórico | Exemplo real |
|---|---|---|---|
| **1** | Perfil casual; perguntas já previstas pelo BI | Consultar o painel de vendas do mês e filtrar por região | Gerente abre o painel oficial de indicadores e filtra por unidade |
| **2** | Perfil com noção de dados; perguntas não previstas, sobre dados já estruturados | Cruzar vendas com campanhas no nível de pedido | Analista de marketing cria um relatório novo sobre a base de pedidos sem pedir à TI |
| **3** | Perfil avançado e governança madura; exploração com fontes novas | Combinar a base corporativa com dados externos de clima | Área comercial junta metas (planilha) com vendas corporativas num painel |

---

## 6. Estratégias em self-service analytics *(material acadêmico: Halper, 2020)*

| # | Estratégia | O que o capítulo diz |
|---|---|---|
| 1 | **Foco na gestão de mudança** | Criar mentalidade orientada a dados leva tempo (evangelização, treinamento). Duas abordagens: ter um **defensor de peso** (executivo com orçamento e influência) e achar **métricas que importam** para cada função |
| 2 | **Ferramentas modernas de BI** | Insights mais rápidos, sem codificar. Recursos: **consumerização** (foco no usuário final), colaboração, linguagem natural e **inteligência aumentada** (sugestões de visualização, insights automáticos). **O treinamento continua sendo necessário** |
| 3 | **Alfabetização em dados** | Pensamento crítico com dados, fundamentos de estatística (média, mediana) e **comunicação com dados** (narrativa, público-alvo, boas visualizações) |
| 4 | **Garantia de dados confiáveis** | Parceria entre negócio e TI; **camada de modelagem semântica** (visão virtualizada das fontes, sem replicar); qualidade (precisos, oportunos e razoáveis: padronização, desduplicação, verificação de discrepantes e ausentes, consistência); **metadados** e **catálogo de dados** |
| 5 | **Equilíbrio entre autoatendimento e governança** | Governança = políticas, regras e responsabilidades. Responsabilidade **compartilhada** entre negócio e TI, sem regras demais nem de menos: controle de acesso, padronização de termos, coordenação, métricas de qualidade, regras de compartilhamento, segurança e privacidade |

**Fechamento do capítulo:** para evitar os desafios, cada organização deve partir de uma **estratégia de BI bem planejada**: arquitetura sólida, padrões de tecnologia, governança, programas de treinamento e política de governança de dados.

---

## 7. BI tradicional × Self-service BI *(material acadêmico: infográfico)*

| Dimensão | BI tradicional | Self-service BI |
|---|---|---|
| **Configuração de TI** | Envolvimento constante de especialistas de TI e dados; vários componentes, cada um exigindo especialistas | TI usada só na implementação; menos pessoal especializado para manter |
| **Agilidade** | Acesso restrito à TI e a especialistas; oportunidades presas em ciclos de consultas e relatórios de **uma semana a um mês** | Análises, relatórios e insights **em tempo real** pelos usuários; testam tendências e correlações, modelando dados |
| **Dados** | Deve **estruturar** os dados antes de usá-los | Dados de várias fontes e **vários formatos** |
| **Comunicação** | Responde o que já aconteceu ou está acontecendo; recursos limitados de relatórios sob demanda | Relatórios preditivos e prescritivos, além dos históricos; vários recursos sob demanda |
| **Gestão de dados** | Equipe especializada garante limpeza, armazenamento e segurança, além da governança | **Exige política de governança** para limpeza, armazenamento, modelagem e privilégios de acesso |

**Conclusão do infográfico:** o self-service oferece mais vantagens e facilidades, mas no tradicional a **qualidade dos dados é mais controlada**. O **recomendado é usar as duas soluções em conjunto**: BI tradicional para o passado e o presente; self-service para perguntas em tempo real e sobre o futuro.

### 7.1 Quando usar cada abordagem *(complementação)*

| Situação | Tendência | Exemplo teórico | Exemplo real |
|---|---|---|---|
| Números **oficiais**, auditados ou regulatórios | BI tradicional (centralizado) | Balanço e relatórios regulatórios | Indicador financeiro enviado à diretoria ou a órgãos externos |
| Exploração rápida, perguntas novas e departamentais | Self-service | "Por que as vendas caíram na região Sul?" | Time comercial investiga uma queda sem abrir chamado |
| Prototipar uma visão para depois oficializar | Self-service, depois promover ao BI | Painel piloto de uma área | Protótipo de painel validado e depois assumido pela TI |
| Modelos preditivos críticos | Ciência de dados com apoio de TI | Modelo de risco de crédito | Modelo de churn em produção |

> O infográfico afirma que o self-service responde perguntas "sobre o futuro". Isso depende da ferramenta e da competência do usuário. Ferramentas oferecem recursos preditivos, mas **interpretá-los e validá-los** exige conhecimento estatístico (ligação com a estratégia 3, alfabetização em dados).

---

## 8. Ferramentas citadas no material *(material acadêmico)*

| Ferramenta | Onde aparece |
|---|---|
| **Alteryx** | "Saiba mais": live com especialista, descrita como ferramenta de análise de dados self-service que gera insights visuais analíticos |
| **Microsoft Power BI Desktop** | "Saiba mais": artigo que usa uma solução de BI self-service com dados do Facebook para apoiar decisões |
| **Tableau, Power BI, Sisense e QlikView** | "Saiba mais": artigo que compara as quatro ferramentas para ajudar a escolher a que atende melhor cada negócio |

A **Dica do Professor** (vídeo) apresenta "algumas das principais ferramentas de self-service analytics". **Não acessei o vídeo** (ver seção 12).

---

## 9. Análise crítica: observações da Dani e leitura do material

> Esta seção registra o que a Dani pensa e confronta com o capítulo. Cada linha identifica a origem.

| # | Observação da Dani | O que o capítulo diz | Complementação / ponto de atenção |
|---|---|---|---|
| 1 | O modelo parece ser um **data lake** com as áreas de negócio estruturando as próprias análises, sem alta dependência da TI e **sem ETL, executando um ELT** | **Não menciona data lake nem ELT.** Fala de data warehouse, camada de modelagem semântica, catálogo de dados e mashups. O nível 3 (novas fontes sem pré-processamento) é o que mais se aproxima | Self-service define **quem** analisa, não **onde** os dados ficam: funciona sobre DW, lake ou camada semântica. A transformação **não desaparece**: muda de lugar e de mãos (seção 10) |
| 2 | Isso gera um **desafio de governança de dados** | Confirma: é desafio (imprecisão, segurança, implementação não controlada) e é a **estratégia 5**; as estratégias 4 e 5 tratam de dados confiáveis e governança | A governança é pré-condição, não complemento |
| 3 | Ser capacitado em uma ferramenta como Power BI **não faz de alguém um analista de dados** e algumas ineficiências são propagadas | Reconhece em parte: "o treinamento não é dispensável", alfabetização em dados (estratégia 3) e o risco de usuários selecionarem dados incorretos ou agregados. Mas também afirma que o modelo **"abole a necessidade de vasta mão de obra especializada"** e reduz custos | **Tensão interna do capítulo:** a estratégia 4 (dados confiáveis) depende justamente de especialistas e de TI. Ferramenta fácil não equivale a competência analítica |
| 4 | Análise em cima de **planilha Excel gerada manualmente é ponto de risco alto** | Coerente com o desafio de "versões diferentes dos mesmos dados" e com o benefício da "versão única da verdade" | Faltam **linhagem, versionamento, validação e reprodutibilidade**. Planilha manual como fonte é o caso típico de nível 3 sem governança |
| 5 | A teoria é **problemática em empresas grandes**, com gestão já definida e, segundo a Dani, de gerações X e Y | A estratégia 1 trata da cultura: defensor executivo e métricas relevantes. O capítulo não faz recorte por geração | O ponto de fundo (preparo da liderança para decidir com dados) é legítimo. Como argumento, é mais sólido formular por **papel e letramento em dados** (verificáveis) do que por geração (generalização difícil de sustentar) |
| 6 | O capítulo é otimista demais | — | Fontes majoritariamente de **literatura de mercado** (TDWI) e uma dissertação; a cifra de 47% vem de **um único estudo (2017)**, e não foi verificada aqui |

**Dúvidas em aberto (Dani):**
- Em um ambiente real, onde termina o autoatendimento seguro e começa o "ETL informal"?
- Que critérios definem quando uma análise feita por usuário de negócio deve ser promovida a um indicador oficial?

*(Respostas parciais estão nas seções 10 e 11.)*

---

## 10. Complementação: onde fica a transformação (ETL × ELT) e arquitetura típica

> Seção de complementação. O capítulo não trata de ELT.

### 10.1 ETL × ELT

| Aspecto | ETL | ELT |
|---|---|---|
| **Onde transforma** | Antes de carregar, em uma área intermediária (staging) | Depois de carregar, dentro do destino (DW, lake ou lakehouse) |
| **Dado bruto** | Em geral não fica disponível no destino | Fica guardado e disponível |
| **Quando usar** | Regras estáveis, dados estruturados, governança forte, destino com pouca capacidade de processamento | Grandes volumes e dados variados, necessidade de reprocessar, destino com muita capacidade |
| **Exemplo teórico** | Carga noturna de vendas para um DW dimensional, já limpa e padronizada (Aula 2 da disciplina anterior) | Carregar logs e arquivos brutos em um lake e transformar sob demanda |
| **Exemplo real** | Consolidação financeira mensal com regras contábeis | Telemetria de aplicações guardada bruta e preparada para cada análise |
| **Relação com self-service** | Entrega dados prontos, com menos liberdade | Dá mais liberdade de exploração, mas **exige curadoria** para que cada usuário não transforme do seu jeito |

**Ponto-chave para a dúvida 1 da Dani:** em ambos os casos alguém **precisa transformar**. A diferença é **quando** e **quem**. No self-service sem governança, o usuário transforma na própria ferramenta (por exemplo, no Power Query ou em planilhas), criando um **ETL informal** ("*shadow* ETL"), sem padrão, documentação ou reprodutibilidade. Isso conecta com a observação da disciplina anterior de que cerca de 80% de um projeto de ETL é a definição das regras de transformação, que é uma análise gerencial e não técnica.

### 10.2 Arquitetura típica de self-service com governança

```
Fontes (sistemas, planilhas, APIs, arquivos)
        │
        ▼
Ingestão  →  Armazenamento (DW / data lake / lakehouse)
        │
        ▼
Camada semântica certificada (métricas e definições únicas) + Catálogo de dados e metadados
        │
        ▼
Ferramentas de autoatendimento (painéis, relatórios, exploração)
        │
        ▼
Usuários de negócio ── supervisionados por ── Governança (acesso, qualidade, linhagem, treinamento)
```
Corresponde às estratégias 4 e 5 do capítulo: camada de modelagem semântica, metadados, catálogo e governança compartilhada.

### 10.3 Salvaguardas para reduzir o risco *(checklist)*

| Salvaguarda | Risco que reduz |
|---|---|
| Conjuntos de dados **certificados** como fonte oficial | Versões diferentes dos mesmos dados |
| Métricas definidas **uma única vez** na camada semântica | Dois painéis com faturamento diferente |
| **Linhagem** e catálogo (de onde veio, quem criou, quando) | Análise sem rastreabilidade |
| Controle de acesso e classificação de dados sensíveis | Exposição de dados confidenciais e violação de privacidade |
| Versionamento e revisão de painéis críticos | Erros propagados e decisões com número errado |
| Treinamento **por nível** de autoatendimento (seção 5) | Usuário operando acima da própria competência |
| Processo para **promover** uma análise de área a indicador oficial | Indicador "paralelo" virando referência sem validação |
| Proibir fonte manual sem registro para números oficiais | Planilha manual como base de decisão |

---

## 11. Cenários de vida real: "Imagine que..." *(complementação)*

**1. Fila na TI**
- **Imagine que** o financeiro precisa de um relatório de vendas por região para amanhã e a fila de relatórios da TI está em três semanas.
- **Será analisado por** self-service nível 1 ou 2, sobre um conjunto de dados certificado.
- **Porque** o ganho de agilidade é o principal motivador do modelo e, com a fonte certificada, o risco de inconsistência fica baixo.

**2. Planilha de metas + base corporativa**
- **Imagine que** a área comercial quer juntar sua planilha própria de metas com as vendas da base corporativa.
- **Será analisado por** nível 3 (mashup), **com a planilha registrada como fonte** e revisão do painel antes de circular.
- **Porque** é o nível de maior flexibilidade e também o de maior risco de versões divergentes (desafio 1 do capítulo). A planilha manual sem registro é o ponto de risco apontado na seção 9.

**3. Dois painéis, dois números**
- **Imagine que** a diretoria recebe dois painéis com faturamentos diferentes para o mesmo mês.
- **Será resolvido por** métricas padronizadas numa camada semântica e um catálogo que indique a fonte oficial.
- **Porque** cada área aplicou filtros e regras próprias aos mesmos dados, exatamente o desafio de "resultados analíticos imprecisos".

**4. Antes de adotar a ferramenta**
- **Imagine que** uma empresa grande quer liberar uma ferramenta de BI de autoatendimento a todos os gerentes.
- **Será conduzido por** gestão de mudança (patrocinador executivo, métricas relevantes), treinamento por perfil e governança definida **antes** da liberação.
- **Porque** a ferramenta fácil, sozinha, não gera competência analítica (estratégias 1, 3 e 5).

**5. Aplicação profissional (sugestão, não é conteúdo da aula)**
- **Imagine que** a gestão de demandas e portfólio quer acompanhar tempo de ciclo, envelhecimento (aging) e status das demandas, com dados vindos de ferramentas como Azure DevOps ou Jira Align.
- **Será analisado por** um conjunto de dados certificado (definições únicas de "demanda concluída" e "tempo de ciclo") e painéis de autoatendimento nos níveis 1 e 2 para as áreas, com o nível 3 restrito a quem tem treinamento.
- **Porque** os indicadores de portfólio sustentam decisões executivas: um número divergente entre painéis compromete a governança que o próprio modelo deveria apoiar.

---

## 12. Anexos

### Anexo A: Vídeo "Análise de dados em Python" *(material do professor, não assistido)*

| Item | Informação |
|---|---|
| Link | https://www.youtube.com/embed/W_Bz7M91R1Q |
| Descrição na plataforma | "Aprenda como realizar a análise de dados usando o frame da Anaconda, que permite programar em Python em Linguagem R." |
| Onde aparece | "Saiba mais" da AED (Aula 4). O mesmo vídeo já consta no notebook da disciplina anterior |
| Status | **Não assistido por mim** (acesso bloqueado neste ambiente). O conteúdo abaixo não deriva do vídeo |
| Observação da Dani | Considerou o conteúdo interessante e quer registrá-lo como anexo |

**Atenção a uma divergência:** o notebook anterior descreve o vídeo como prática com Pandas, NumPy e Matplotlib. Essa descrição foi escrita sem assistir ao vídeo e não coincide com o texto da plataforma (Anaconda). Vale ajustar assim que o conteúdo for conferido.

**Se quiser aprofundar:** envie a transcrição ou suas notas do vídeo que eu incorporo ao anexo.

### Anexo B: Anaconda em uma página *(complementação, não deriva do vídeo)*

O **Anaconda** é uma distribuição de Python e R para ciência de dados. Reúne o interpretador, o gerenciador de pacotes e ambientes **conda**, o **Jupyter** e muitas bibliotecas científicas já instaladas (como NumPy e Pandas). A frase da plataforma ("Python em Linguagem R") provavelmente se refere à possibilidade de trabalhar com as duas linguagens no mesmo ambiente.

| Opção | Quando usar | Exemplo |
|---|---|---|
| **Anaconda / conda** | Quer tudo pronto, usa Python e R, ou depende de bibliotecas científicas com dependências nativas difíceis de instalar | Estudar ciência de dados com Jupyter, Pandas e scikit-learn sem montar o ambiente à mão |
| **venv + pip** (usado no how-to da Aula 3) | Projetos leves, ambiente mínimo, integração simples com o VS Code | O pacote `aula03_vscode/` |

> **Cuidado em uso corporativo:** os termos de licença do Anaconda podem exigir licença paga para uso em empresas. Confira os termos atuais antes de instalar em ambiente de trabalho. Há alternativas, como `venv` e canais comunitários do conda.

### Anexo C: Links do material (não acessados)

| Material | Link (conforme o PDF) |
|---|---|
| Dica do Professor, AED (vídeo) | `fast.player.liquidplatform.com/pApiv2/embed/cee29914fad5b594d8f5918df1e801fd/aa7477e89ad9a349713e602cacc1a8df` |
| Prof. Álvaro Caldas: estatística e AED (vídeo) | https://www.youtube.com/embed/84JiM5UYswk |
| Dica do Professor, self-service (vídeo) | `fast.player.liquidplatform.com/pApiv2/embed/cee29914fad5b594d8f5918df1e801fd/007aa3f45a4b491a72c827cf787a4bfe` |
| Alteryx: live com especialista (vídeo) | https://www.youtube.com/embed/cCN5SpedEdI |
| Power BI Desktop com dados de mídia social (artigo) | http://periodicos.faex.edu.br/index.php/e-Locucao/article/view/212/164 |
| Avaliação de ferramentas de BI para visualização (artigo) | https://www.researchgate.net/profile/Isabel-Pedrosa/publication/344723939_Evaluation_and_Analysis_of_Business_Intelligence_Data_Visualization_Tools/links/6065a3f1299bf1252e1d857e/Evaluation-and-Analysis-of-Business-Intelligence-Data-Visualization-Tools.pdf |

---

## 13. Atividade 4 (A4): gabarito

> A plataforma não mostra o gabarito. As questões desta A4 são **equivalentes** às da Aula 4 de *Aquisição e Preparação de Dados* (mesmos temas; o registro anterior guardou os enunciados de forma resumida, então a redação pode variar), e o registro de lá indica as respostas abaixo. **Confirme na plataforma antes de reaproveitar:** um trecho de chat daquela disciplina menciona "8/10", enquanto o notebook e a memória registram 5/5.

| Q | Tema | Resposta | Justificativa (capítulo) |
|---|---|---|---|
| 1 | Principal etapa da análise: organizar, resumir, calcular e visualizar | **A) Análise exploratória de dados** | Definição de Stankevix citada no capítulo |
| 2 | Valores de compra com grande afastamento da série (fraude em cartão) | **B) Outliers** | Valor que foge do padrão. Em fraude, o outlier é exatamente o que se busca |
| 3 | Fatos que ocorrem de forma sincronizada (pão e satisfação) | **C) Correlação** | Dois acontecimentos, não necessariamente causais, que tendem a ocorrer juntos |
| 4 | Opção que sugere um tipo de apresentação | **D) Gráfico** | O capítulo cita duas formas: tabular e gráfica |
| 5 | O que saber para escolher a técnica de imputação | **E) O tipo do dado faltante** | "As técnicas de imputação dependem do tipo de dado faltante" |

**Pegadinhas:**
- **Q4:** "Infográfico" (E) aparece como alternativa, mas o capítulo só reconhece duas formas de apresentação (tabular e gráfica). Resposta pelo texto: **Gráfico**.
- **Q5:** "O motivo do dado faltante" (B) parece razoável e, na prática, o motivo também importa (seção 3.3). Mas a resposta que o capítulo sustenta é o **tipo** do dado faltante.
- **Q2:** a alternativa E traz um ponto e vírgula no lugar do ponto final ("Quantitativo;"), erro de edição sem efeito sobre a resposta.

---

## 14. Referências e Conexões com Outros Conteúdos

**Referências do capítulo de AED:**
- BONAT, W. H.; KRAINSKI, E. T.; MAYER, F. P. *Introdução à análise exploratória de dados.* Material de aula, UFPR, 2020.
- CAPÍTULO 1: análise exploratória de dados. [S. l., 2011].
- MEDRI, W. *Análise exploratória de dados.* Londrina: UEL, 2011.
- NAVIDI, W. *Probabilidade e estatística para ciências exatas.* Porto Alegre: AMGH, 2012.
- NUNES, C. E. *Aula3 Carlos: dado, informação, conhecimento e sabedoria.* 2015.
- STANKEVIX, G. *Análise exploratória de dados.* [S. l.], 2020.
- Leituras recomendadas: MACHADO, F. N. R. *Projeto de data warehouse: uma visão multidimensional.* São Paulo: Érica, 2000; VIALI, L. *Série estatística multivariada: introdução.* [199-?].

**Referências do capítulo de self-service analytics:**
- ALPAR, P.; SCHULZ, M. *Self-service business intelligence.* Marburg: Springer, 2016.
- BAHGA, A.; MADISETTI, V. *Big data analytics: a hands-on approach.* 2019.
- CASTRO, J. M. L. T. *Tendências de business intelligence: SSBI como foco principal de estudo.* Dissertação, NOVA Information Management School, Lisboa, 2016.
- DARADKEH, M.; AL-DWAIRI, R. M. Self-service business intelligence adoption in business enterprises. *International Journal of Enterprise Information System*, v. 13, n. 3, p. 65–85, 2017.
- DOMO. *Data never sleeps 9.0.* 2021.
- HALPER, F. *Five strategies for creating a culture of self-service for analytics and business intelligence.* TDWI, 2020.
- IMHOFF, C.; WHITE, C. *Self-service business intelligence: empowering users to generate insights.* TDWI, 2011.
- MYERS, N. E.; KOGAN, G. *Self-service data analytics and governance for managers.* Wiley, 2021.
- ZHANG, A. *Data analytics: practical guide to leveraging the power of algorithms, data science, data mining, statistics, big data and predictive analysis to improve business, work, and life.* 2017.

> As referências acima são as listadas nos capítulos. Esta aula não consultou as fontes originais.

**Conexões com a disciplina anterior (Aquisição e Preparação de Dados — 262GGR6046A):**
- **Aula 4 (AED):** é o mesmo capítulo; esta aula só acrescenta o infográfico de imputação e detalhes pontuais (seção 3).
- **Aula 2 (ETL):** a seção 10 retoma ETL, staging, DW e OLAP, e os contrasta com ELT e self-service.
- **Aula 1 (dados abertos e conectados), conexão sugerida:** catálogo de dados, metadados e camada semântica se aproximam das ideias de dados conectados (identificação e vínculo entre fontes).
- **Aula 3 (normalização):** a padronização de termos e de escala é parte das técnicas de qualidade de dados da estratégia 4.

**Conexões internas à disciplina (Aprendizado Não Supervisionado):**
- **Aula 1:** big data (5 Vs) e qualidade de dados; o self-service é uma resposta organizacional ao volume e à variedade.
- **Aula 2:** os gráficos multivariados (heatmap, scatter, densidade) são os recursos que as ferramentas de autoatendimento oferecem ao usuário.
- **Aula 3:** outliers, imputação e padronização antecedem a PCA; sem dados confiáveis, a redução de dimensionalidade herda os erros.

**Conexões com Aprendizado Supervisionado:**
- **Aula 1 (pré-processamento) e Aula 2 (BPM):** painéis e indicadores de desempenho são o produto típico do autoatendimento, e a qualidade dos dados continua sendo pré-condição para o aprendizado de máquina.
