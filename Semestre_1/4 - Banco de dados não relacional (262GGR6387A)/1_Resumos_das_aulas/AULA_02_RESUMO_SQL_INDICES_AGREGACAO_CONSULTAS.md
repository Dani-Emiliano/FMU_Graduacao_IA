# AULA 02 — SQL: Funções de Agregação e Agrupamento, Consultas Complexas e Índices

## 1. Identificação e objetivos

| Item | Informação |
|------|------------|
| **Disciplina** | Banco de Dados Não Relacional (262GGR6387A) |
| **Curso** | Graduação em Inteligência Artificial — FMU |
| **Aula / Unidade** | Aula 02 (Unidade 2) |
| **Tema** | Funções de agregação e agrupamento em SQL; consultas complexas (junção, ordenação, aninhamento, correlacionamento); índices em banco de dados (PostgreSQL) |
| **Material acadêmico** | Infográfico *Funções de agregação e agrupamento de dados em SQL*; capítulo *Funções de agregação e agrupamento de dados em SQL* (PAES, C. A. — *Consultas em Banco de Dados*, SAGAH); Infográfico *Consultas complexas em SQL*; capítulo *Consultas complexas em SQL* (PICHETTI, R. F. — *Banco de Dados*, SAGAH); Infográfico *Índices em banco de dados*; capítulo *Índices em banco de dados* (ANDRADE, G. L. — *Consultas em Banco de Dados*, SAGAH); Dicas do Professor; Saiba mais |

### Objetivos de aprendizagem (da Unidade)
- Definir o conceito de **índices** em banco de dados e identificar suas principais vantagens.
- **Criar, excluir e aplicar** índices em consultas SQL.
- Identificar e utilizar **funções de agregação e agrupamento** de dados em SQL.
- Desenvolver consultas utilizando **junção, agregação e ordenação**.
- Produzir consultas avançadas empregando **aninhamento e correlacionamento**.

> **Nota de contexto:** esta unidade trata do modelo **relacional/SQL** (exemplos em PostgreSQL, com menções a MySQL, Oracle e SQL Server). Na disciplina, funciona como a "linha de base" relacional para a comparação com o NoSQL feita na Aula 01 (ver §6).

---

## 2. Resumo e contextualização

À medida que o volume de dados cresce, consultar de forma **rápida, organizada e eficiente** vira requisito. A unidade apresenta três blocos que se encadeiam:

1. **Resumir dados** — funções de **agregação** (COUNT, SUM, AVG, MIN, MAX) e **agrupamento** (GROUP BY, HAVING): analisam *grupos de linhas* em vez de linhas individuais.
2. **Combinar e comparar dados** — **consultas complexas**: junções (JOIN), ordenação (ORDER BY), **subconsultas aninhadas** e **correlacionadas**, além do tratamento de valores **NULL** (lógica de três valores).
3. **Acelerar a busca** — **índices**: estruturas de dados auxiliares que organizam os registros em disco para otimizar a recuperação, com custo de espaço e de escrita.

As três partes se conectam por um ponto: **a mesma consulta pode ser escrita de várias formas**, e escolher bem a estrutura (agrupamento, subconsulta, índice) muda o resultado e o desempenho.

---

## 3. Conceitos fundamentais e explicações

### 3.1 Funções de agregação

**Definição.** Função de agregação é um procedimento que calcula **um único valor de resultado a partir de um conjunto de valores de entrada** (documentação do PostgreSQL, citada por Paes). Pode ser usada onde se usaria uma constante, na declaração do atributo do `SELECT` (Silberschatz, Korth e Sudarshan, 1999). Funções "padrão" (Mannino, 2008): **COUNT, SUM, AVG, MAX, MIN**.

```sql
SELECT <função de agregação> FROM nomeTabela;
SELECT <função de agregação> FROM nomeTabela WHERE ... ;   -- WHERE opcional
```

Sintaxe geral (Manzano, 2017, citado por Pichetti): `NOME_FUNÇÃO ([ALL | DISTINCT] expressão)` — `ALL` aplica a função a todos os valores; `DISTINCT` aplica a ação **uma única vez a cada valor distinto**.

| Função | O que faz | Tipo de coluna | **Quando usar** | Exemplo (material) | Exemplo real *(complementação)* |
|--------|-----------|----------------|-----------------|--------------------|----------------------------------|
| **COUNT(\*)** | Conta **todas as linhas** do resultado (inclui nulos) | Qualquer | Medir volume de dados / nº de ocorrências | `SELECT COUNT(*) FROM paciente;` → 4 | Total de pedidos do dia |
| **COUNT(coluna)** | Conta só as linhas com valor **não nulo** na coluna | Qualquer | Saber quantos registros têm o campo preenchido | `COUNT(cidade)` → 2 (dois pacientes têm `null`) | Quantos clientes informaram e-mail |
| **COUNT(DISTINCT col)** | Conta **valores distintos** | Qualquer | Evitar contagem repetida | `COUNT(distinct a.idProcedimento)` | Nº de produtos diferentes vendidos |
| **SUM** | Soma os valores | **Numérica** (inteira/decimal) | Totais (faturamento, quantidades) | `SUM(idade)` → 118; `SUM(preco)` → 370,00 | Receita do mês |
| **AVG** | Média dos valores | **Numérica** | Valor típico de um conjunto | `AVG(idade)` → 29,50 | Ticket médio |
| **MIN** | Menor valor | Numérica (e `DATE`/`TIME`, ver nota) | Mínimo / mais antigo | `MIN(idade)` → 25 | Menor preço praticado |
| **MAX** | Maior valor | Numérica (e `DATE`/`TIME`) | Máximo / mais recente | `MAX(idade)` → 35 | Maior venda do mês |

**Pontos do material:**
- **`COUNT(*)` × `COUNT(coluna)`**: com `*` entram todas as linhas; com a coluna, só as que têm valor válido (não nulo).
- **NULL** em SQL significa **vazio/sem valor**: não é zero e não é branco. Valores `NULL` são descartados quando as funções de agregação são aplicadas a uma coluna (Elmasri e Navathe, 2011).
- **`DISTINCT`** pode acompanhar `COUNT`, `AVG` e `SUM` (Paes).
- **`MAX` e `MIN`** também funcionam com domínios não numéricos que tenham **ordenação total** (ex.: `DATE`, `TIME`) (Elmasri e Navathe, 2011).
- Podem ser aplicadas a **conjunto ou multiconjunto** de valores.
- **Alias com `AS`**: o nome da coluna do resultado refere-se à função usada; `AS` dá um "apelido": `SELECT MAX(idade) AS MaiorIdade FROM paciente;`.
- Com `WHERE`, os resultados passam a considerar só as linhas filtradas: `SELECT SUM(Salario), MAX(Salario), MIN(Salario), AVG(Salario) FROM COLABORADOR;` (ou restringindo por departamento).

### 3.2 Agrupamento de dados: GROUP BY e HAVING

**Ideia.** Agrupar é "ajuntar" linhas segundo um critério (analogia do material: bolas de cores diferentes formando ajuntamentos por tom). O agrupamento **divide o resultado e gera uma linha para cada grupo** (documentação Microsoft, citada por Paes). As funções de agrupamento **selecionam um conjunto de linhas para uso das funções de agregação**; a cada grupo, a agregação é executada e o resultado apresentado (Infográfico).

| Cláusula | Função | Quando é aplicada |
|----------|--------|-------------------|
| **GROUP BY** | Forma **grupos de linhas** com mesmo valor no(s) atributo(s) indicado(s) para executar as funções agregadas | Sobre as linhas geradas pela seleção (`WHERE`) |
| **HAVING** | Impõe uma **condição de seleção sobre os grupos** resultantes do `GROUP BY` | Depois do agrupamento (processamento como subconsulta) |

```sql
-- GROUP BY
SELECT nomeAtributo, <função de agregação> FROM nomeTabela
GROUP BY nomeAtributo;

-- GROUP BY com WHERE (WHERE filtra ANTES de agrupar)
SELECT nomeAtributo, <função de agregação> FROM nomeTabela
WHERE ........
GROUP BY nomeAtributo;

-- HAVING (filtra DEPOIS de agrupar)
SELECT nomeAtributo, funçãoDeAgregacao FROM nomeTabela
GROUP BY nomeAtributo
HAVING condição;
```

**Regras e observações do material:**
- O atributo usado na projeção do `SELECT` deve estar representado no `GROUP BY` (ex.: `SELECT cidade, AVG(idade) FROM estudante GROUP BY cidade;`).
- É possível usar **todas as funções agregadas** com `GROUP BY`; pode-se agrupar por mais de um atributo (`GROUP BY Projnumero, Projnome`).
- Se houver `NULL` no atributo de agrupamento, é criado **um grupo separado** para todas essas linhas (Elmasri e Navathe, 2011).
- Os **resultados parciais** do processamento não aparecem ao usuário: o processamento é interno e o armazenamento, em memória.
- Condição de junção pode ser usada junto com `GROUP BY`: agrupamento e funções são aplicados **depois da junção** das tabelas.

**Exemplo-base do material (tabela `estudante`, 4 linhas: 3 no Rio de Janeiro, 1 em Niterói):**

| Consulta | Resultado |
|----------|-----------|
| `SELECT cidade, COUNT(*) FROM estudante GROUP BY cidade;` | RIO DE JANEIRO = 3; NITERÓI = 1 |
| `... WHERE idade < 30 GROUP BY cidade;` | RIO DE JANEIRO = 2; NITERÓI = 1 |
| `... GROUP BY cidade HAVING COUNT(*) > 1;` | RIO DE JANEIRO = 3 |

**Exemplo do infográfico (tabela `atletas`):** `SELECT count(*) FROM atletas GROUP BY esporte;` → VÔLEI 1, FUTEBOL 2; com `HAVING count(*) > 1` fica só FUTEBOL 2 (o infográfico também mostra o `SELECT` com a coluna `esporte` junto ao `count`).

### 3.3 Ordem conceitual de avaliação e `WHERE` × `HAVING`

Uma consulta pode ter até **seis cláusulas**; **somente `SELECT` e `FROM` são obrigatórias**; termina com `;`.

| Cláusula | Papel |
|----------|-------|
| `SELECT` | Lista os atributos a recuperar |
| `FROM` | Tabelas úteis à consulta e suas relações |
| `WHERE` | Condições de seleção das tuplas e **condições de junção** |
| `GROUP BY` | Atributos de agrupamento |
| `HAVING` | Condição sobre os **grupos** selecionados |
| `ORDER BY` | Ordem de exibição do resultado |

**Ordem conceitual** (Elmasri e Navathe, 2011, p. 86): avalia-se primeiro `FROM` (identifica tabelas e materializa junções), depois `WHERE` (seleciona e junta tuplas), depois `GROUP BY` e `HAVING`; **`ORDER BY` é aplicado no final**, para classificar o resultado.

| | `WHERE` | `HAVING` |
|---|---------|----------|
| Atua sobre | **Tuplas individuais** (ou tuplas de junção) | **Grupos** criados pelo `GROUP BY` |
| Momento | **Antes** do agrupamento | **Depois** do agrupamento |
| **Quando usar** | Restringir quais linhas entram na conta | Restringir quais grupos aparecem no resultado (condição sobre agregação) |

**Armadilha explicada no material:** combinar `WHERE` + `HAVING` na mesma consulta pode gerar resultado diferente do esperado. A consulta **incorreta** pretende "departamentos com mais de 5 funcionários, cada um com salário > R$ 5.000", mas `WHERE` roda primeiro e já restringe as tuplas a quem ganha mais de 5.000; só então `HAVING COUNT(*) > 5` é aplicado. Solução: **consulta aninhada**, que consulta primeiro os departamentos com mais de cinco funcionários e depois filtra por salário (ver §3.5 e §4.3).

**Flexibilidade × confusão:** existem várias formas de escrever a mesma consulta (vantagem: escolher a técnica mais confortável; desvantagem: confusão sobre qual é a "correta" para cada situação). O ideal é o usuário **especificar corretamente** a consulta e deixar ao SGBD a escolha de como executá-la com eficiência.

### 3.4 Junções e ordenação

| Junção | Comportamento | **Quando usar** |
|--------|---------------|-----------------|
| **Junção por igualdade em `WHERE`** (`FROM A, B WHERE A.chave = B.chave`) | Iguala **chave primária** com **chave estrangeira** | Forma usada nos exemplos de Paes (estudo de caso da clínica) |
| **`INNER JOIN` / `JOIN ... ON`** | Junção interna: a tupla só entra se **combinar com a outra relação** | Quando só interessam registros presentes nas duas tabelas |
| **`NATURAL JOIN`** | Cada par de atributos de junção é incluído **apenas uma vez** na relação resultante; se os nomes dos atributos não coincidem, é possível **renomeá-los** antes | Quando as colunas de junção têm o mesmo nome nas duas tabelas |
| **`LEFT OUTER JOIN`** | **Toda tupla da tabela da esquerda** aparece; sem correspondência, preenche com nulos | Manter todos os registros da esquerda, mesmo sem par |
| **`RIGHT OUTER JOIN`** | **Toda tupla da tabela da direita** aparece; sem correspondência, preenche com nulos | Manter todos os registros da direita |

- Se o resultado da junção for nulo para uma das relações, a tupla é excluída (nas junções internas).
- **`ORDER BY`** define a ordem de exibição (ex.: `ORDER BY Pnome, Unome`).
- Junção pode ser **combinada com agregação** (ex.: soma/máx/mín/média dos salários do departamento "Compras" via `JOIN`).

### 3.5 Subconsultas: aninhamento e correlacionamento

**Consulta aninhada** = bloco `SELECT-FROM-WHERE` **completo dentro da cláusula `WHERE`** de outra consulta. A de fora é a **consulta externa**; a embutida é a **subconsulta** (Elmasri e Navathe, 2011). Segundo Ramakrishnan e Gehrke, é um dos recursos mais poderosos da SQL.

| Conceito | Regra do material | **Quando usar** |
|----------|-------------------|-----------------|
| **Subconsulta com `IN`** | A subconsulta devolve um conjunto/multiconjunto de tuplas; a externa testa se o valor pertence a ele | Comparar um valor com **um conjunto** de valores |
| **Subconsulta com `=`** | Se a subconsulta retorna **um único atributo e uma única tupla** (valor único), pode-se usar `=` em vez de `IN` | Comparação com um valor escalar (ex.: `MIN(idade)`) |
| **Aninhamento em vários níveis** | As consultas podem estar aninhadas em vários níveis | Perguntas compostas |
| **Ambiguidade de nomes** | Referência a atributo **não qualificado** refere-se à relação declarada na **consulta mais interna** (regra semelhante ao escopo de variáveis em linguagens de programação) | Evitar erros: criar **variáveis de tupla (aliases)** para todas as referências |
| **Consulta correlacionada** | Uma condição do `WHERE` da subconsulta **referencia um atributo de uma relação declarada na consulta externa**; a interna é avaliada **uma vez para cada tupla** da externa | Quando a comparação depende da linha corrente da consulta externa |

> Toda consulta escrita com blocos aninhados `SELECT-FROM-WHERE` usando `=` ou `IN` **sempre pode ser definida com uma única consulta em bloco** (Elmasri e Navathe, 2011).

**Subconsulta com função de agregação (Paes):** "nome do paciente mais novo": `SELECT nome FROM paciente WHERE idade IN (SELECT MIN(idade) FROM paciente);` — a subconsulta retorna 67 (menor idade) e a externa compara a idade de cada paciente com esse valor → **ANTONIO MANOEL**. Equivalente com `=`: `WHERE idade = (SELECT MIN(idade) FROM paciente);`.

### 3.6 Valores NULL e lógica de três valores

- **NULL** identifica valores faltantes: **desconhecidos, não disponíveis ou não aplicáveis**. Cada `NULL` é considerado **diferente** de qualquer outro.
- Por isso a SQL usa **lógica de três valores**: `TRUE`, `FALSE` e `UNKNOWN` (quando um `NULL` participa de uma comparação, o resultado é `UNKNOWN`).
- Para testar nulos usam-se **`IS NULL` / `IS NOT NULL`**; comparar com `=` não é apropriado.

**Quadro 1 (Elmasri e Navathe, 2011) — conectivos lógicos:**

| AND | TRUE | FALSE | UNKNOWN |
|-----|------|-------|---------|
| **TRUE** | TRUE | FALSE | UNKNOWN |
| **FALSE** | FALSE | FALSE | FALSE |
| **UNKNOWN** | UNKNOWN | FALSE | UNKNOWN |

| OR | TRUE | FALSE | UNKNOWN |
|----|------|-------|---------|
| **TRUE** | TRUE | TRUE | TRUE |
| **FALSE** | TRUE | FALSE | UNKNOWN |
| **UNKNOWN** | TRUE | UNKNOWN | UNKNOWN |

| NOT | Resultado |
|-----|-----------|
| TRUE | FALSE |
| FALSE | TRUE |
| UNKNOWN | UNKNOWN |

### 3.7 Índices em banco de dados

#### 3.7.1 Conceito e vantagens
- **Analogia do material:** buscar um tema em um livro percorrendo todas as páginas seria lento; o **índice do livro** indica a página. O índice de banco de dados é semelhante, exceto que é usado para encontrar **linhas específicas de uma tabela** (Price, 2009).
- **Definição formal:** *"Um índice é uma estrutura de dados que organiza registros de dado em disco para otimizar determinados tipos de operações de recuperação. Um índice nos permite recuperar de forma eficiente todos os registros que satisfaçam às condições de pesquisa nos campos de chave de pesquisa do índice"* (Ramakrishnan e Gehrke, 2008, p. 228).
- Os índices contêm **ponteiros para a tabela** com os dados reais (busca e recuperação mais rápidas e eficientes).
- **Vantagem principal:** consulta otimizada.
- **Desvantagens:** demora maior na **inserção** de registros (é preciso atualizar o índice) e **sobrecarga** no sistema de banco de dados como um todo → devem ser usados **com sensatez** (PostgreSQL, 2020; Price, 2009).

**Quando criar um índice e em qual coluna:**

| Critério | Regra do material |
|----------|-------------------|
| Quando criar | Quando a consulta recupera **um pequeno número de linhas** de uma tabela grande; regra geral: **10% ou menos** do total de linhas (Price, 2009) |
| Boa candidata | Coluna da **chave primária** (geralmente numérica, facilita a indexação — Barbosa e Freitas, 2018); coluna com **valor exclusivo por linha** (ex.: matrícula do aluno) |
| Má candidata | Coluna com **poucos valores distintos** (ex.: sexo: feminino/masculino) |
| Múltiplas colunas | Índices podem ser criados sobre **várias colunas**, não só uma (Price, 2009) |

> **Fique atento (material):** em banco relacional, a chave primária é uma coluna (ou combinação) de valores **únicos** por linha. Boas práticas sugerem que corresponda a um valor **numérico** para facilitar o índice; ao definir uma PK **não se está definindo nenhum caminho de acesso**, e sim apenas uma **restrição de integridade** (unicidade) (Heuser, 2009).

> Explicação simples com tabela hipotética 5×5 e desenho: ver **Anexo A (§7)**. Comparativo entre algoritmo (Árvore B, *hash*) e classificação (agrupado, primário, secundário): ver **Anexo B (§8)**.

#### 3.7.2 Índices agrupados, primários e secundários

| Termo | Definição do material |
|-------|----------------------|
| **Agrupado (clustered)** | Índice sobre uma coluna é agrupado se a organização dos registros de dados é **igual ou parecida com a ordenação das entradas do índice**; caso contrário, é **não agrupado**. Na prática raramente acontece, pois ordenar os dados conforme sua atualização é muito custoso |
| **Primário / ordenado** | Índice sobre a coluna da **chave primária** (registros ordenados pela PK) |
| **Secundário** | Contempla os demais tipos de índice (a definição "não está bem delimitada na literatura" — Ramakrishnan e Gehrke, 2008) |
| **No PostgreSQL** | **Todos os índices são ditos secundários**; o índice é armazenado **separadamente** dos registros da tabela indexada (chamada de **pilha/heap**) (PostgreSQL, 2020) |

#### 3.7.3 Estrutura de dados do índice

| Estrutura | Como funciona (material) | Característica |
|-----------|--------------------------|----------------|
| **Hashing** | Aplica uma função *hash* à **chave de pesquisa** para saber a qual ***bucket*** (página primária + páginas adicionais encadeadas) o registro pertence. Inserção coloca o registro no *bucket* apropriado; a consulta aplica o *hash* e examina as páginas do *bucket*. Pode recuperar a página em **1 ou 2 E/S** de disco | Só serve para **igualdade**. A chave de pesquisa pode ser qualquer sequência de uma ou mais colunas, não precisa ser única |
| **Árvore** | Registros dispostos de forma **ordenada** em estrutura hierárquica; cada nó é uma página física; o nível **folha** (L1, L2, L3...) contém os registros | Localiza com eficiência registros em um **intervalo** de valores |
| **B-tree** | Árvore **balanceada pela altura**: todos os caminhos do nó raiz até o nó folha têm o mesmo comprimento | Suportada por muitos SGBD, como o PostgreSQL |

**Figura 1 (Ramakrishnan e Gehrke, 2008):** índice *hash* sobre `idade` com índice auxiliar sobre `salário` (pares `<salário, rid>`, em que `rid` = *record id*, ponteiro para o registro). A função `h` do exemplo converte a chave em binário e usa os **dois bits menos significativos** como identificador do *bucket*.

**Figura 2:** os mesmos registros indexados por árvore sobre `idade`. A pesquisa começa na raiz e segue ponteiros: o ponteiro à direita de um valor `k` aponta para subárvore com valores **≥ k**; à esquerda, valores **< k**. Para `33 < idade < 44`: raiz → direita do nó 12 → direita do nó 19 → esquerda do nó 44.

#### 3.7.4 Tipos de índice no PostgreSQL

Por padrão, o PostgreSQL cria índices **B-tree**; cada tipo usa um **algoritmo diferente** e é indicado para determinado tipo de consulta sobre determinado tipo de dado. Antes de escolher o tipo e as colunas, deve-se perguntar **qual consulta será necessária**.

| Tipo | Característica (material) | Operadores / suporte | **Quando usar** | Exemplo do material |
|------|---------------------------|----------------------|-----------------|---------------------|
| **B-tree (Árvore B)** | **Padrão** quando o tipo não é definido; indexa **todos os tipos de dados**; usada em igualdade, **intervalos** e predicados nulos; recupera dados **classificados em ordem** | `<`, `<=`, `=`, `>=`, `>` | Uso geral; consultas por **intervalo**; ordenação | `idade >= 30 AND idade <= 80` |
| **Hash** | Suportado a partir da versão 10 (infográfico); só **comparações simples de igualdade** | `=` | Busca por **valor exato** | `idade = 20` |
| **GIN** | Acelera consultas em **estruturas complexas** (matrizes, pesquisa em texto completo); útil quando **vários valores** mapeiam para uma linha da tabela; consulta ~**3× mais rápida** que GiST (infográfico). Coluna deve ser `tsvector` | `<@`, `@>`, `=`, `&&` | **Texto completo** / arrays com foco em velocidade de leitura | índice sobre `titulo \|\| ' ' \|\| corpo` |
| **GiST** | **Dados geométricos** bidimensionais (ex.: `point`) e texto completo; ~**3× menor** que GIN e ~**10× mais rápido de atualizar** (infográfico). Coluna `tsvector` ou `tsquery` | `<<`, `&<`, `&>`, `>>`, `<<\|`, `&<\|`, `\|&>`, `\|>>`, `@>`, `<@`, `~=`, `&&` | Dados geométricos; texto com muita atualização; busca por **vizinhos mais próximos** (`<->`) | 6 pontos mais próximos de `(0,1)` |
| **SP-GiST** | Similar ao GiST; projetado para **tipos complexos definidos pelo usuário**; exige mais conhecimento técnico (infográfico) | `<<`, `>>`, `~=`, `<@`, `<^`, `>^` | Ex.: indexar dois pontos em um plano | `USING SPGIST (ponto)` |
| **BRIN** | Para **tabelas muito grandes** em que colunas têm **correlação natural com a localização física**; parâmetro `pages_per_range` (blocos por entrada; **padrão 128**); suportado a partir da v9.5; consulta **mais lenta que B-tree**, mas **ocupa menos espaço** | — | **Big data** / tabelas gigantes (ex.: campo de data) | `USING BRIN (data) WITH (pages_per_range = 128)` |

> **Fique atento (material):** o PostgreSQL oferece muitos operadores de seleção — `=` igual, `<>` diferente, `<`, `>`, `<=`, `>=`, `@>` contém o elemento, `<@` elemento contido por, `&&` sobreposição, `<<` estritamente à esquerda de, `>>` estritamente à direita de, `&<` não se estende à direita de, `&>` não se estende à esquerda de, `-|-` adjacente a, `+` união, `*` interseção, `-` diferença.

#### 3.7.5 Criação, variações e exclusão

```sql
-- Sintaxe básica (B-tree por padrão)
CREATE INDEX nome ON tabela (coluna);

-- Com tipo explícito
CREATE INDEX nome ON tabela USING TIPO (coluna);

-- Exclusão
DROP INDEX nome;
```

| Variação | Comando (material) | Observação | **Quando usar** |
|----------|--------------------|-----------|-----------------|
| **Múltiplas colunas** | `CREATE INDEX nome ON tabela (coluna1, coluna2, ...);` | Só **B-tree, GiST, GIN e BRIN** (PostgreSQL 12.2); até **32 colunas** | Buscas que filtram por várias colunas juntas |
| **Ordenado** | `... (coluna NULLS FIRST);` / `... (coluna DESC NULLS LAST);` | Só **B-tree**; opções `ASC`, `DESC`, `NULLS FIRST`, `NULLS LAST`; por padrão nulos ficam **por último** | Consultas com `ORDER BY` frequente |
| **Único (UNIQUE)** | `CREATE UNIQUE INDEX nome ON tabela (coluna [, ...]);` | Só **B-tree**; garante **unicidade** da coluna (ou da combinação) | Impor unicidade |
| **Funcional** | `CREATE INDEX nome ON tabela (lower(coluna));` | Índice é o resultado de uma **função** aplicada a colunas; `lower` aplica-se a cadeia de caracteres (ex.: `varchar`) e converte para minúsculas | Buscas sem diferenciar maiúsculas/minúsculas |
| **Parcial** | `CREATE INDEX nome ON tabela (idade) WHERE idade >= 50 AND idade <= 80;` | Índice sobre um **subconjunto** definido por predicado condicional (após `WHERE`); evita indexar **valores comuns**, reduz o índice e acelera consultas e atualizações. Pode ser combinado com `UNIQUE` | Quando poucas linhas são as mais acessadas (ex.: pedidos não faturados) |
| **`CONCURRENTLY`** | `CREATE INDEX CONCURRENTLY nome ON tabela (coluna);` | A criação de índice **bloqueia inserções, exclusões e atualizações** na tabela; `CONCURRENTLY` constrói **sem bloquear gravações** | Tabelas em produção com escrita contínua (ex.: vendas) |
| **`COLLATE`** | `CREATE INDEX collate_index ON exemplo4 (conteudo);` | Um índice só suporta **um agrupamento (collation) por coluna**; vários agrupamentos exigem vários índices | Consultas com regras de ordenação diferentes |

#### 3.7.6 Verificar o uso de índices
- **`EXPLAIN`** examina o uso do índice em uma consulta individual: `EXPLAIN SELECT * FROM tabela WHERE coluna = constante;`.
- **`ANALYZE`** coleta **estatísticas** sobre a distribuição dos valores na tabela para **estimar o nº de linhas** retornadas. Sem parâmetros, examina **todas as tabelas** do banco atual; com parâmetro, só a tabela desejada: `ANALYZE tabela;` ou `ANALYZE tabela (coluna);`.

---

## 4. Exemplos, aplicações e material prático

> Os scripts completos (DDL, dados, consultas e versões corrigidas) estão no arquivo complementar **`AULA_02_SQL_INDICES_PRATICO.md`**.

### 4.1 Estudo de caso: Clínica Médica "Felizes por Viver" (Paes)

Clínica **hipotética** geriátrica, funciona 7 dias/semana × 24 h, com atendimentos de emergência e de rotina. O paciente é registrado na entrada; registra-se uma **consulta** (que também pode ser **agendada**); os médicos registram os **atendimentos**, classificando-os pelos **procedimentos** realizados.

**Modelo (Figura 1 — ER):**

| Entidade | Atributos | Relacionamento |
|----------|-----------|----------------|
| `paciente` | CPF (PK), nome, e-mail, idade | paciente **comparece** à consulta (1,1)–(0,n) |
| `medico` | CRM (PK), nome, e-mail | médico **atende** a consulta (1,1)–(0,n) |
| `consulta` | ID (PK), data, hora, CRM do médico (FK), CPF do paciente (FK), situação ∈ {agendada, realizada, cancelada} | consulta **realiza** atendimento (1,1)–(0,n) |
| `atendimento` | ID da consulta (PK/FK), ID do atendimento (PK), ID do procedimento (FK) | atendimento **usa** procedimento (0,n)–(1,1) |
| `procedimento` | código (PK), descrição, preço | — |

**Dados:** `procedimento` — 1 CONSULTA 150,00; 2 APLICAÇÃO INJEÇÃO 60,00; 3 CURATIVO 40,00; 4 REVISÃO EXAMES 80,00. `paciente` — ANTONIO MANOEL (67), MARIA JOAQUINA (70), JULIA SILVA (80). `medico` — MARCELO ARAÚJO, ALEXANDRE SOUZA, JUNIA TRINDADE. `consulta` — 8 linhas (6 realizadas, 1 agendada, 1 cancelada; as duas últimas sem médico). `atendimento` — 8 linhas.

### 4.2 Consultas do estudo de caso e resultados

| Necessidade | Consulta (como no material) | Resultado | Conceito |
|-------------|-----------------------------|-----------|----------|
| Quantidade de pacientes | `SELECT COUNT(*) FROM paciente;` | 3 | COUNT, 1 tabela |
| Maior idade | `SELECT MAX(idade) FROM paciente;` | 80 | MAX |
| Média de idade dos pacientes atendidos pelo médico ALEXANDRE SOUZA | `SELECT AVG(idade) FROM PACIENTE p, MEDICO m, CONSULTA c WHERE ...` (junção PK=FK + filtro por nome) | 75 | AVG + junção em 3 tabelas |
| Faturamento de janeiro/2020 | `SELECT SUM(preco) FROM procedimento p, consulta c, atendimento a WHERE a.idconsulta = c.id AND p.codigo = a.idProcedimento AND data >= ... AND data <= ...` | **370,00** (= 150+60+60+40+60) | SUM + junção + filtro de período |
| Consultas por situação | `SELECT situacao, COUNT(*) FROM consulta GROUP BY situacao;` | agendada 1; realizada 6; cancelada 1 | GROUP BY |
| Consultas realizadas por CRM | `SELECT crmmedico, COUNT(*) FROM consulta WHERE situacao = "realizada" GROUP BY crmmedico;` | 567890 → 3; 234891 → 2; 167384 → 1 | WHERE + GROUP BY |
| Paciente de menor idade por médico | `SELECT m.nome, MIN(idade) FROM paciente p, medico m, consulta c WHERE p.cpf = c.cpfpaciente AND m.crm = c.crmmedico GROUP BY m.nome;` | MARCELO 67; ALEXANDRE 70; JUNIA 80 | MIN + GROUP BY + junção |
| Médicos que usaram **mais de um procedimento** | `... GROUP BY m.nome HAVING COUNT(*) > 1;` | Agrupado: MARCELO 5; ALEXANDRE 2; JUNIA 1. Com HAVING: **MARCELO 5; ALEXANDRE 2** | HAVING |
| Qtde de consultas **e** de procedimentos **distintos** por médico | `COUNT(*) AS qtdeConsultas, COUNT(DISTINCT a.idProcedimento) AS qtdeProc ... GROUP BY m.nome` | MARCELO 5 / 4; ALEXANDRE 2 / 2; JUNIA 1 / 1 | COUNT DISTINCT |
| Paciente mais novo | `... WHERE idade IN (SELECT MIN(idade) FROM paciente);` | ANTONIO MANOEL | Subconsulta |

*(Os pontos em que a consulta impressa não bate com o esquema estão na §5.)*

### 4.3 Exemplos do capítulo *Consultas complexas* (Pichetti — esquema Elmasri e Navathe)

```sql
-- Funções de agregação (resumo dos salários)
SELECT SUM(Salario), MAX(Salario), MIN(Salario), AVG(Salario) FROM COLABORADOR;

-- COUNT com junção e filtro
SELECT COUNT(*) FROM COLABORADOR, DEPARTAMENTO
WHERE Dnr = dnumero AND Dnome = 'Faturamento';

-- GROUP BY: nº do departamento, nº de colaboradores e salário médio
SELECT Dnr, COUNT(*), AVG(Salario) FROM COLABORADOR GROUP BY Dnr;

-- GROUP BY com condição de junção (nº, nome do projeto e nº de colaboradores)
SELECT Projnumero, Projnome, COUNT(*) FROM PROJETO, TRABALHA_EM
WHERE Projnumero = Pnr GROUP BY Projnumero, Projnome;

-- JOIN com ORDER BY
SELECT Pnome, Unome, Endereco
FROM (COLABORADOR JOIN DEPARTAMENTO ON Dnr = Dnumero)
WHERE Dnome = 'Compras' ORDER BY Pnome, Unome;

-- NATURAL JOIN com renomeação de atributos
SELECT Pnome, Unome, Endereco
FROM (COLABORADOR NATURAL JOIN (DEPARTAMENTO AS DEP (Dnome, Dnr, Cpf_gerente)))
WHERE Dnome = 'Compras' ORDER BY Pnome, Unome;

-- Junção + agregação
SELECT SUM(Salario), MAX(Salario), MIN(Salario), AVG(Salario)
FROM (COLABORADOR JOIN DEPARTAMENTO ON Dnr = Dnumero) WHERE Dnome = 'Compras';

-- Consulta aninhada (IN + OR): projetos com funcionário "Silva" como gerente ou trabalhador
SELECT DISTINCT Projnumero FROM PROJETO
WHERE Projnumero IN (SELECT Projnumero FROM PROJETO, DEPARTAMENTO, FUNCIONARIO
                     WHERE Dnum = Dnumero AND Cpf_gerente = Cpf AND Unome = 'Silva')
   OR Projnumero IN (SELECT Pnr FROM TRABALHA_EM, FUNCIONARIO
                     WHERE Fcpf = Cpf AND Unome = 'Silva');

-- Aninhada correlacionada + aliases (colaboradores com dependente de mesmo nome e sexo)
SELECT C.Pnome, C.Unome FROM COLABORADOR AS C
WHERE C.Cpf IN (SELECT D.Ccpf FROM DEPENDENTE AS D
                WHERE C.Pnome = D.Nome_dependente AND C.Sexo = D.Sexo);
```

**Tabela de grupos (figura do material):** colaboradores por `Dnr` — Dnr 5: salários 3.000 / 2.000 / 10.000 → COUNT 3, AVG 5.000; Dnr 4: 7.500 / 4.500 / 6.000 → COUNT 3, AVG 6.000; Dnr 1: 15.000 → COUNT 1, AVG 15.000.

**Consulta incorreta × correta (WHERE + HAVING):**
```sql
-- INCORRETA (como no material): WHERE roda antes e distorce o HAVING
SELECT Dnome, COUNT(*) FROM DEPARTAMENTO, COLABORADOR
WHERE Dnumero = Dnr AND Salario > 5.000
GROUP BY Dnome; HAVING COUNT(*) > 5;

-- CORRETA (ideia do material): consultar primeiro os departamentos com mais de 5 funcionários
-- e depois filtrar departamento + salário (consulta aninhada com HAVING na subconsulta)
SELECT Dnumero, COUNT(*) FROM DEPARTAMENTO, COLABORADOR
WHERE Dnumero = Dnr AND Salario > 5000
  AND Dnr IN (SELECT Dnr FROM COLABORADOR GROUP BY Dnr HAVING COUNT(*) > 5)
GROUP BY Dnumero;   -- (reescrita equivalente; ver §5, item 7)
```

### 4.4 Exemplos de índices (Andrade — PostgreSQL)

| # | Tabela / situação | Comandos (material) | Resultado / ideia |
|---|-------------------|--------------------|-------------------|
| 1 | `exemplo1(nome varchar, idade integer)` — 6 pessoas (Bruna 26, Carla 41, Deiva 78, Fernando 20, Gilberto 24, Ilmo 34) | `CREATE INDEX id_indice_hash ON exemplo1 USING HASH (idade);` → `SELECT * FROM exemplo1 WHERE idade = 20;` · `CREATE INDEX id_indice_B ON exemplo1 (idade);` → `... WHERE idade >= 30 AND idade <= 80;` | *Hash*: só igualdade. B-tree: igualdade **e intervalo** → retorna Carla (41), Deiva (78), Ilmo (34) |
| 2 | `exemplo2(ponto point)` — 11 pontos 2D | `CREATE INDEX ponto_index_gist ON exemplo2 USING GIST (ponto);` e `... USING SPGIST (ponto);` → `SELECT * FROM exemplo2 ORDER BY ponto <-> point '(0,1)' LIMIT 6;` | Índice GiST para achar os **6 pontos mais próximos** de (0,1): (0,1), (0,2), (1,1), (1,2), (2,1), (3,2) |
| 3 | `exemplo3(nome, sobrenome, maior float, menor float)` — vendedores | `CREATE INDEX index_multi ON exemplo3 (maior, menor);` · `CREATE INDEX index_f ON exemplo3 ((nome \|\| ' ' \|\| sobrenome));` → `... WHERE (nome \|\| ' ' \|\| sobrenome) = 'Joana Lopes';` | **Múltiplas colunas** e índice **funcional** (retorna Joana Lopes, 3900 / 450) |
| 4 | Tabela `pedidos` (faturados e não faturados; os **não faturados** são poucos e os mais acessados) | `CREATE INDEX nfaturado_indice ON pedidos (num_pedidos) WHERE faturado IS NOT TRUE;` · versão `CONCURRENTLY` · para tabela com milhares de registros: `USING BRIN (data) WITH (pages_per_range = 128)` | **Índice parcial** só nas linhas não faturadas; `CONCURRENTLY` para não bloquear inserções; com milhares de registros o parcial deixa de compensar → **BRIN** sobre a data |
| 5 | `exemplo4(id integer, conteudo varchar COLLATE "x")` | `CREATE INDEX collate_index ON exemplo4 (conteudo); SELECT * FROM exemplo4 WHERE conteudo > 10;` · índice adicional com `COLLATE "y"` | O índice usa o agrupamento da coluna por padrão; outro agrupamento exige **outro índice** |
| 6 | `exemplo6(id integer, titulo tsvector, corpo tsvector)` — 8 livros | `CREATE INDEX indice_gin ON exemplo6 USING GIN ((titulo \|\| ' ' \|\| corpo));` → `SELECT * FROM exemplo6 WHERE (titulo \|\| ' ' \|\| corpo) = 'Dear John ...';` | **Busca em texto completo** com GIN (ou GiST) → retorna o livro 4 (*Dear John*) |

### 4.5 Cenários de aplicação *(complementação — exemplos ilustrativos elaborados para estudo; não fazem parte do material da FMU)*

> Formato: "Imagine que você tem este problema ___, será analisado por tal metodologia ___, porque ___".

| # | Problema | Metodologia / recurso | Porque |
|---|----------|----------------------|--------|
| 1 | Imagine que você tem **uma tabela de clientes com milhões de linhas e consultas por faixa de idade (30 a 80 anos)** | **Índice B-tree** sobre `idade` | B-tree suporta intervalos e ordenação; *hash* só atenderia igualdade |
| 2 | Imagine que você tem **buscas exatas por número de pedido** em uma tabela enorme | **Índice hash** (ou B-tree) sobre o número do pedido | Consulta só por igualdade; *hash* vai direto ao *bucket* |
| 3 | Imagine que você tem **um campo de descrição de produtos onde o usuário pesquisa por palavras** | **Índice GIN** sobre `tsvector` | GIN é voltado a texto completo e a valores múltiplos por linha, com leitura mais rápida |
| 4 | Imagine que você tem **uma tabela de pedidos em que só 2% estão "não faturados" e são os mais consultados** | **Índice parcial** (`WHERE faturado IS NOT TRUE`) | Índice menor, consultas e atualizações mais rápidas |
| 5 | Imagine que você tem **bilhões de registros de log inseridos em ordem cronológica** | **Índice BRIN** sobre a data | Correlação natural com a localização física; ocupa pouco espaço |
| 6 | Imagine que você quer **indexar a coluna "sexo" (2 valores)** | **Não indexar** | Pouca variedade de valores: a consulta recuperaria muito mais que ~10% das linhas |
| 7 | Imagine que você precisa **saber quantas consultas existem por situação** | **`COUNT(*)` + `GROUP BY situacao`** | Resumo por grupo de linhas |
| 8 | Imagine que você só quer **ver os médicos que usaram mais de um procedimento** | **`GROUP BY` + `HAVING COUNT(*) > 1`** | A condição é sobre o resultado da agregação, que só existe após o agrupamento |
| 9 | Imagine que você precisa **departamentos com mais de 5 funcionários e só contar quem ganha > R$ 5.000** | **Consulta aninhada** (`IN` + subconsulta com `HAVING`) | `WHERE` roda antes do `HAVING`; a subconsulta separa as duas condições |
| 10 | Imagine que você precisa **funcionários com dependente do mesmo nome e sexo** | **Subconsulta correlacionada** com aliases | A condição da interna depende da linha da externa |
| 11 | Imagine que você precisa **listar todos os departamentos, mesmo os sem funcionários** | **`LEFT OUTER JOIN`** | Mantém toda tupla da tabela da esquerda; preenche com nulos |
| 12 | Imagine que você precisa **achar registros sem e-mail preenchido** | **`IS NULL`** | `NULL` é diferente de qualquer valor; `=` resultaria em `UNKNOWN` |
| 13 | Imagine que você criou um índice e **quer saber se a consulta o está usando** | **`EXPLAIN`** (e `ANALYZE` para as estatísticas) | Mostra o uso do índice na consulta |

---

## 5. Pontos de atenção (inconsistências e limitações do material)

> Sinalizados conforme a regra de não alterar silenciosamente o conteúdo acadêmico. Os resultados impressos das consultas da clínica foram **conferidos executando** os dados do material; os resultados batem.

1. **Esquema da clínica inconsistente com o modelo (Paes, Figura 1 × tabelas):** o ER mostra `CPFMEDICO (fk)` em `consulta` e `CPF (pk)` em `medico`, mas as tabelas usam **CRM** (`CRMMEDICO` / `CRM (PK)`). A consulta da média de idade de ALEXANDRE SOUZA está impressa com `p.cpf = c.cpf and m.cpf = c.cpf`, que **não corresponde às colunas** das tabelas (`c.cpfpaciente`, `m.crm = c.crmmedico`); usa também aspas duplas em `"ALEXANDRE SOUZA"` (o padrão SQL é aspas simples). O resultado (75) está certo para a lógica pretendida.
2. **Consultas com `HAVING` e agrupamento por médico estão incompletas:** nas consultas de "médicos com mais de um procedimento" e de "qtdeConsultas/qtdeProc", o `SELECT` usa `m.nome` e o `GROUP BY m.nome`, mas a tabela `medico m` **não aparece no `FROM`** e falta a condição de junção `c.crmmedico = m.crm`. Há também uma **vírgula sobrando** após `GROUP BY m.nome,` antes do `HAVING`. As tabelas de resultado estão corretas (conferido), então o texto da consulta parece ter perdido linhas.
3. **Rótulo `qtdeConsultas` impreciso:** `COUNT(*)` conta as **linhas da junção** (atendimentos), não consultas. Para MARCELO ARAÚJO o resultado é 5, mas ele fez **3 consultas** (1, 3 e 4); as 5 linhas são atendimentos. *Complementação:* para contar consultas reais usaria `COUNT(DISTINCT c.id)` (confirmado na execução: MARCELO 3, ALEXANDRE 2, JUNIA 1).
4. **"Paciente com a maior idade":** o texto pede o **paciente**, mas `SELECT MAX(idade) FROM paciente;` devolve apenas o **valor** (80), não quem é. O mesmo vale para o rótulo "o paciente com menor idade, atendido por médico", em que o resultado traz a menor idade **por médico**. *Complementação:* para obter o nome, usaria subconsulta (`WHERE idade = (SELECT MAX(idade) FROM paciente)`).
5. **`paciente` com duas estruturas:** na seção de agregação, `paciente` tem (CPF, NOME, CIDADE, SEXO, IDADE); no estudo de caso da clínica, (CPF, NOME, E-MAIL, IDADE). São tabelas diferentes com o mesmo nome. Outro detalhe: a coluna do resultado de `COUNT(cidade)` está rotulada como `COUNT(*)`.
6. **Consulta de faturamento:** o texto diz "junção entre `procedimento` e `consulta`", mas a consulta junta **três** tabelas (`procedimento`, `consulta`, `atendimento`). As datas estão como `"01/01/2020"` (texto); o formato de data depende do SGBD (*complementação:* o formato ISO `AAAA-MM-DD` é o mais portável).
7. **Capítulo Pichetti (consulta "correta"):** o texto impresso da consulta correta parece ter erros de transcrição: `AND (SELECT Dnr IN FROM COLABORADOR GROUP BY DnR HAVING COUNT(*) > 5);` — `IN` fora de lugar, parênteses desencontrados, `DnR` com grafia diferente de `Dnr`. A ideia explicada é `Dnr IN (SELECT Dnr FROM COLABORADOR GROUP BY Dnr HAVING COUNT(*) > 5)`, que foi a forma usada acima (reescrita marcada). A consulta "incorreta" tem ainda `;` sobrando após `GROUP BY Dnome` e `Salario>5.000` com ponto como separador de milhar (em SQL, `5000`). O texto junta `Dnumero=Dnr` e, na explicação, usa `Dnumero` na projeção.
8. **Nomes de tabelas e colunas variam no capítulo:** `COLABORADOR` (maior parte) × `FUNCIONARIO` (exemplo da consulta aninhada); `Niome_dependente` (provável erro de `Nome_dependente`); `Cpf_gerente`, `Fcpf`, `Ccpf` sem esquema completo no material.
9. **Exemplo de `HAVING` em projetos:** o texto descreve a situação "projetos com mais de dois colaboradores" e explica o `HAVING`, mas **não mostra o código** da consulta com `HAVING`.
10. **Junções externas:** `LEFT/RIGHT OUTER JOIN` são **descritos**, mas o material não traz exemplo de código; os exemplos usam `JOIN ... ON` e `NATURAL JOIN`.
11. **Capítulo de índices (Andrade) — erros de redação/código:** no Exemplo 3 a consulta é `WHERE maior = 100 AND menor = 9`, mas a tabela tem `menor = 90` para Fernando (provável erro de digitação); o texto fala em criar índice B-tree "sobre o índice `id_indice_B`", enquanto o código cria sobre a coluna `idade`; nas opções de ordenação aparece `NULL FIRST` (o comando correto é `NULLS FIRST`); no Exemplo 4 há `faturado` / `faturados` e `num_pedidos` / `num_pedido` alternando; um `CREATE INDEX * ON pedidos USING BRIN ...` tem um `*` no lugar do nome do índice; no Exemplo 5 aparecem `exemplo4` e `exemplo`, e `conteudo` e `content`.
12. **Busca textual no Exemplo 6:** o material compara o `tsvector` com `=` e uma string. *Complementação:* em PostgreSQL a busca de texto completo costuma usar `@@` com `to_tsquery`; o material não explica essa parte. O índice GIN também é descrito como exigindo `tsvector`.
13. **Hash "a partir da versão 10":** o infográfico afirma que o *hash* é suportado a partir da v10. *Complementação (não consta do material):* o tipo existia antes, mas só a partir da v10 passou a ser seguro contra falhas (registrado no log de transações); vale confirmar com o professor.
14. **Infográfico "Cláusulas e funções":** na imagem, o par `MAX`/`MIN` parece mostrar `SELECT MAX (valor) FROM produto;` duas vezes (o segundo deveria ser `MIN`); o infográfico de agrupamento traz o rótulo `HAVING32` (provável marca de nota de rodapé). O texto do infográfico é pequeno; a leitura pode ter imprecisões.
15. **Referência:** Ramakrishnan e Gehrke, *Sistemas de gerenciamento de banco de dados*, 3. ed., aparece como **2008** no capítulo de índices e **2011** no de consultas complexas.
16. **Material não acessível:** os conteúdos por **QR code / link** (vídeo da Dica do Professor sobre `COUNT`, vídeo da Dica "Consultas complexas", vídeo da Dica "Índices", vídeos e links do *Saiba mais*, documentação MySQL, audiodescrições) **não foram lidos**. Os livros do *Saiba mais* (Oracle 11g SQL, SQL Server 2012, p. 122–127 de consultas aninhadas e p. 298–303 de junções) também não foram acessados.
17. **Atividade 2 (A2):** conforme sua preferência, as questões e respostas **não** foram incluídas neste arquivo.
18. **Índices (execução):** os comandos de índice são específicos do PostgreSQL e **não foram executados** (não havia servidor PostgreSQL no ambiente); os resultados exibidos são os impressos no material.

---

## 6. Referências e conexões

### Conexões com a Aula 01 *(complementação — conceitos explicados na Aula 01; aqui apenas ponteiros)*

| Conceito desta aula | Conexão com a Aula 01 |
|---------------------|----------------------|
| Banco relacional / SQL / chave primária e integridade | Aula 01 **§3.1** (modelo relacional, ACID, normalização) e **§3.8** (SQL × NoSQL). Esta unidade aprofunda o lado relacional da comparação |
| `GROUP BY` + funções de agregação (resumir grupos de linhas) | Aula 01 **§3.4** (consultas *scatter/gather* e **MapReduce**: `map` por nó + `reduce` para o resultado final) — ideia semelhante de agrupar e resumir, em contexto distribuído |
| Agregações rápidas por coluna | Aula 01 **§3.4** (layout **colunar** favorece operações sobre colunas) e **§3.6** (bancos colunares para consultas analíticas) |
| Índices *hash* / *buckets* e B-tree | Aula 01 **§3.4** (`hash(o) mod n`, hash consistente para sharding; árvores **LSM**). O *hash* do índice organiza *buckets* dentro de **uma** tabela; o *hash* de sharding distribui dados entre **nós** de um cluster — objetivos diferentes |
| Busca por igualdade em índice *hash* | Aula 01 **§3.6** (chave/valor: acesso por chave, O(1)) |
| `JOIN`s e custo | Aula 01 **§3.1** (joins são caros em hardware) e **§3.6** (grafos: *joins* recursivos viram **travessias**) |
| `NULL` e esquema rígido | Aula 01 **§3.8** (relacional com *schema* rígido × NoSQL sem *schema*) |
| Trade-off do índice (acelera leitura, custa escrita e espaço) | Aula 01 **§3.2** e **§3.5** (NoSQL troca garantias por escala) — mesma lógica de *trade-off* |

### Aplicação profissional *(complementação)*
- **Azure SQL / PostgreSQL gerenciado e Cosmos DB:** entender índices, agregações e planos de execução (`EXPLAIN`) apoia decisões de arquitetura de dados em nuvem, relevante em soluções com Azure; o *Azure Cosmos DB* já foi mencionado na Aula 01 (§6).
- **Governança e relatórios:** consultas com `GROUP BY`/`HAVING` são a base de indicadores e relatórios de demanda e portfólio (contagem por status, soma por área, média por período).

### Referências acadêmicas (do material)
- PAES, C. A. *Consultas em Banco de Dados*. SAGAH. Capítulo: *Funções de agregação e agrupamento de dados em SQL*.
- PICHETTI, R. F. *Banco de Dados*. SAGAH. Capítulo: *Consultas complexas em SQL*.
- ANDRADE, G. L. *Consultas em Banco de Dados*. SAGAH. Capítulo: *Índices em banco de dados*.
- Citadas nos capítulos (seleção): AGGREGATE Functions — *PostgreSQL 12.2 Documentation* (2020); AGREGAÇÃO — Dicio (2020); MANNINO, M. V. (2008); SELECT – GROUP BY – Transact-SQL, Microsoft Docs (2019); SILBERSCHATZ, A.; KORTH, H. F.; SUDARSHAN, S. (1999); ELMASRI, R.; NAVATHE, S. B. (2011); MANZANO, J. A. N. G. (2017); RAMAKRISHNAN, R.; GEHRKE, J. (2008/2011); BARBOSA, F. F. M.; FREITAS, P. H. C. (2018); HEUSER, C. A. (2009); JUBA, S.; VOLKOV, A. (2019); PRICE, J. (2009); SANTANA, R.; SILVA, R. *PostgreSQL BRIN índices como uma solução para Big Data* (InfoQ, 2019).
- **Leituras recomendadas pelo capítulo de Paes:** AMADEU (2014); DATE (2004); GARCÍA-MOLINA; ULLMAN; WIDOM (2008); HEUSER (2009); MEDEIROS (2013); RAMAKRISHNAN; GEHRKE (2008); SETZER; SILVA (2005).
- **Sugestões do professor (conteúdos não acessados):** *Modelagem e desenvolvimento de banco de dados*; *Oracle Database 11g SQL*; *Microsoft SQL Server 2012 – passo a passo*; vídeo *Funções agregadas*; livro de *consultas aninhadas* (p. 122–127) e de *consultas avançadas com SQL* (p. 298–303); documentação MySQL de funções de agregação; vídeo *Breve introdução sobre índices* (Heap, Clustered, Nonclustered); *Vinte e cinco dicas e boas práticas de banco de dados para desenvolvedores*; vídeo *Guia de otimização de consultas em PostgreSQL com casos reais*; *Indexes in PostgreSQL* (série de artigos em inglês); monografia *Armazenamento e manipulação de dados espaciais no PostgreSQL/PostGIS*; link citado no capítulo de Pichetti: https://qrgo.page.link/P115X.

---

## 7. Anexo A — Minha dúvida: índice em linguagem simples *(pedido da Dani; complementação, não faz parte do material da FMU)*

**Pedido original:** explicar o índice de forma fácil, com uma tabela hipotética 5×5 (nome, idade, endereço, estudo, sexo), representar o índice por nome e criar uma representação visual.

**Ideia em uma frase:** o índice é um **sumário ordenado** (como o índice de um livro): em vez de ler a tabela inteira, você consulta uma lista curta e ordenada que diz **em qual linha** está o dado.

**Tabela `pessoa` (5 linhas × 5 colunas, na ordem em que foi gravada):**

| # | nome | idade | endereço | estudo | sexo |
|---|------|-------|----------|--------|------|
| 1 | Carla | 41 | Rua das Flores, 120 | Superior | F |
| 2 | Bruno | 26 | Av. Brasil, 45 | Médio | M |
| 3 | Ana | 34 | Rua Sete, 300 | Pós-graduação | F |
| 4 | Diego | 29 | Rua do Sol, 88 | Superior | M |
| 5 | Elisa | 52 | Praça Central, 10 | Fundamental | F |

**Índice sobre `nome`** (estrutura separada, **ordenada A→Z**, só com o nome e o ponteiro para a linha):

| nome | ponteiro |
|------|----------|
| Ana | linha 3 |
| Bruno | linha 2 |
| Carla | linha 1 |
| Diego | linha 4 |
| Elisa | linha 5 |

**Busca `WHERE nome = 'Diego'`:**

| | Sem índice | Com índice |
|---|-----------|------------|
| Como busca | Lê a tabela linha a linha (1, 2, 3, 4...) | Procura na lista ordenada: "Diego → linha 4" e vai direto à linha 4 |
| Em 5 linhas | Diferença pequena | Diferença pequena |
| Em 1 milhão de linhas | Pode ter de ler **tudo** | Ordem de **~20 comparações** (log₂ de 1 milhão) + 1 leitura da linha (ordem de grandeza; o B-tree real tem outros detalhes) |

**Por que a lista é ordenada?** Porque ordenada dá para "pular" para a metade certa (como procurar um nome na agenda), em vez de conferir um por um. Com índice B-tree (padrão do PostgreSQL), isso também permite **intervalos** (`nome BETWEEN 'A' AND 'C'`); com *hash*, só igualdade (ver §3.7.4).

**O custo (do material):** o índice é **uma estrutura a mais**: ocupa espaço e, a cada novo registro na tabela, o índice também precisa ser atualizado (inserção mais lenta). Por isso se indexa a coluna que é muito consultada, e não todas.

**Por que `nome` e não `sexo`?** `sexo` só tem 2 valores (F/M): um índice recuperaria metade da tabela e quase não ajudaria (regra do material: bom índice quando recupera ~10% ou menos das linhas). `nome` tem valores variados → boa candidata.

```sql
CREATE INDEX idx_pessoa_nome ON pessoa (nome);       -- cria o índice (B-tree, padrão)
SELECT * FROM pessoa WHERE nome = 'Diego';           -- consulta que pode usar o índice
EXPLAIN SELECT * FROM pessoa WHERE nome = 'Diego';   -- mostra se o índice foi usado
DROP INDEX idx_pessoa_nome;                          -- exclui o índice
```

> Nota: em uma tabela de apenas 5 linhas o PostgreSQL pode ignorar o índice e ler a tabela direto (é mais barato); o ganho aparece em tabelas grandes.

**Representação visual** (arquivo `INDICE_POR_NOME_VISUAL.svg`: índice à esquerda, tabela à direita, setas do índice para as linhas e o caminho de "Diego" destacado):

![Índice por nome](INDICE_POR_NOME_VISUAL.svg)

---

## 8. Anexo B — Minha dúvida: diferença entre Árvore B, hash, agrupado, primário e secundário *(pedido da Dani; síntese com base no material, organizada em tabela)*

Os cinco termos aparecem juntos, mas respondem a perguntas diferentes: os dois primeiros dizem **como o índice organiza e busca** os dados (algoritmo); os três últimos dizem **como o índice é classificado** (onde fica guardado e sobre qual coluna foi criado).

| Termo | Categoria | O que é | Quando usar / quando se aplica |
|-------|-----------|---------|--------------------------------|
| **Árvore B (B-tree)** | Algoritmo | Estrutura hierárquica e ordenada, balanceada (todos os caminhos da raiz até a folha têm o mesmo comprimento). É o tipo **padrão** do PostgreSQL | Uso geral: igualdade, **intervalo** (`idade >= 30 AND idade <= 80`) e dados em **ordem**. É o único que aceita índice único (`UNIQUE`) e ordenado (`ASC`/`DESC`, `NULLS FIRST`/`LAST`) |
| **Hash** | Algoritmo | Aplica uma função *hash* à chave para achar direto o ***bucket*** onde o registro está | Só **igualdade** (`matricula = 123`). Não serve para `<`, `>` ou intervalos |
| **Agrupado (clustered)** | Classificação | Os registros da tabela estão **na mesma ordem** (ou parecida) das entradas do índice; caso contrário, é **não agrupado** | Na prática é raro: manter a tabela ordenada a cada atualização é muito custoso |
| **Primário (ordenado)** | Classificação | Índice criado sobre a coluna da **chave primária**, com registros ordenados por ela | Quando o acesso é pela chave primária (boa candidata: valor único e, em geral, numérico) |
| **Secundário** | Classificação | Índice guardado **separado** da tabela; contempla os demais tipos de índice | Caso do PostgreSQL: **todos** os índices são secundários, armazenados fora dos registros da tabela (a "pilha"/*heap*) |

**Como diferenciar:**
- Se o texto fala em **como o índice busca** (hierarquia, *buckets*, tipo de consulta aceita), é Árvore B ou *hash*.
- Se fala em **onde o índice fica guardado** ou **sobre qual coluna foi criado**, é agrupado, primário ou secundário.
- Índice guardado **fora** da tabela é o oposto do agrupado e, no PostgreSQL, é o **secundário**.

> **Ressalva do material:** a definição de índice primário e secundário "não está bem delimitada na literatura" (Ramakrishnan e Gehrke, 2008). A regra específica do PostgreSQL (todo índice é secundário e fica separado da tabela) é a referência segura.
