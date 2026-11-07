# AULA 02 — SQL e Índices: Material Prático

**Disciplina:** Banco de Dados Não Relacional (262GGR6387A) · **Aula 02 (Unidade 2)**
**Arquivo complementar de:** `AULA_02_RESUMO_SQL_INDICES_AGREGACAO_CONSULTAS.md`

## Como usar
- Blocos organizados para futura compilação em Jupyter Notebook (cada bloco `sql` = uma célula).
- **Origem:** consultas e dados vêm do material (Paes, Pichetti, Andrade). Os **tipos de dados dos `CREATE TABLE`** não constam do material e foram **escolhidos aqui (complementação)**. Datas em formato ISO (`AAAA-MM-DD`).
- **Validação:** as partes de agregação/agrupamento/junção/subconsulta (seções 1 e 2) foram **executadas** (em SQLite) e os resultados **batem com os impressos no material**. A seção 3 (índices) é específica do **PostgreSQL** e **não foi executada** (sem servidor PostgreSQL no ambiente).
- Onde a consulta impressa no material estava incompleta, aparece a versão **corrigida (complementação)** com comentário.

---

## 1. Funções de agregação e agrupamento — tabelas de demonstração

### 1.1 `paciente_demo` (COUNT, SUM, AVG, MIN, MAX e NULL)
> No material chama-se `paciente`; aqui `paciente_demo` para não colidir com o `paciente` da clínica (seção 2).

```sql
CREATE TABLE paciente_demo (
  cpf    VARCHAR(11) PRIMARY KEY,
  nome   VARCHAR(60),
  cidade VARCHAR(40),
  sexo   CHAR(1),
  idade  INTEGER
);
INSERT INTO paciente_demo VALUES
 ('11111111111','JULIA SANTOS','RIO DE JANEIRO','F',35),
 ('22222222222','MARIA OLIVEIRA',NULL,'F',30),
 ('33333333333','JOÃO DA SILVA',NULL,'M',25),
 ('44444444444','CARLOS FERREIRA','NITERÓI','M',28);
```

```sql
SELECT COUNT(*)      FROM paciente_demo;   -- 4  (todas as linhas)
SELECT COUNT(cidade) FROM paciente_demo;   -- 2  (ignora NULL)
SELECT SUM(idade)    FROM paciente_demo;   -- 118
SELECT AVG(idade)    FROM paciente_demo;   -- 29.5
SELECT MIN(idade)    FROM paciente_demo;   -- 25
SELECT MAX(idade) AS MaiorIdade FROM paciente_demo;   -- 35 (alias com AS)
```

### 1.2 `estudante` (GROUP BY, WHERE + GROUP BY, HAVING)

```sql
CREATE TABLE estudante (
  cpf    VARCHAR(11) PRIMARY KEY,
  nome   VARCHAR(60),
  cidade VARCHAR(40),
  sexo   CHAR(1),
  idade  INTEGER
);
INSERT INTO estudante VALUES
 ('55555555555','GABRIELA ALVES','RIO DE JANEIRO','F',22),
 ('66666666666','HELENA LIMA','RIO DE JANEIRO','F',28),
 ('77777777777','ANDRÉ TORRES','RIO DE JANEIRO','M',32),
 ('88888888888','MIGUEL FERREIRA','NITERÓI','M',26);
```

```sql
-- Estudantes por cidade
SELECT cidade, COUNT(*) FROM estudante GROUP BY cidade;
-- RIO DE JANEIRO 3 | NITERÓI 1

-- Com WHERE (filtra ANTES de agrupar)
SELECT cidade, COUNT(*) FROM estudante WHERE idade < 30 GROUP BY cidade;
-- RIO DE JANEIRO 2 | NITERÓI 1

-- Com HAVING (filtra DEPOIS de agrupar)
SELECT cidade, COUNT(*) FROM estudante GROUP BY cidade HAVING COUNT(*) > 1;
-- RIO DE JANEIRO 3
```

### 1.3 `atletas` (infográfico)

```sql
CREATE TABLE atletas (
  codigo  INTEGER PRIMARY KEY,
  nome    VARCHAR(40),
  peso    NUMERIC(5,1),
  altura  NUMERIC(3,2),
  esporte VARCHAR(20)
);
INSERT INTO atletas VALUES
 (10,'GABRIEL',80,1.79,'VOLEI'),
 (20,'MARIANA',57,1.67,'FUTEBOL'),
 (30,'JULIA',80,1.70,'FUTEBOL');

SELECT esporte, COUNT(*) FROM atletas GROUP BY esporte;
-- VOLEI 1 | FUTEBOL 2
SELECT esporte, COUNT(*) FROM atletas GROUP BY esporte HAVING COUNT(*) > 1;
-- FUTEBOL 2
```

### 1.4 `colaborador` (tabela de grupos do capítulo de Pichetti — colunas visíveis na figura)

```sql
CREATE TABLE colaborador (
  pnome   VARCHAR(30),
  cpf     VARCHAR(11) PRIMARY KEY,
  salario NUMERIC(10,2),
  dnr     INTEGER
);
INSERT INTO colaborador VALUES
 ('Diego','12345678966',3000,5),
 ('Paulo','33344455566',2000,5),
 ('Ana','66677788899',10000,5),
 ('Lia','98765432199',7500,4),
 ('Jorge','98798798798',4500,4),
 ('João','87687687676',6000,4),
 ('Regina','54545454545',15000,1);

SELECT dnr, COUNT(*), AVG(salario) FROM colaborador GROUP BY dnr;
-- 5 | 3 | 5000 ; 4 | 3 | 6000 ; 1 | 1 | 15000
```

---

## 2. Estudo de caso — Clínica Médica "Felizes por Viver"

### 2.1 Esquema e dados (reconstruídos das tabelas do material)

```sql
CREATE TABLE procedimento (
  codigo    INTEGER PRIMARY KEY,
  descricao VARCHAR(40),
  preco     NUMERIC(10,2)
);
CREATE TABLE paciente (
  cpf   VARCHAR(11) PRIMARY KEY,
  nome  VARCHAR(60),
  email VARCHAR(60),
  idade INTEGER
);
CREATE TABLE medico (
  crm   VARCHAR(10) PRIMARY KEY,
  nome  VARCHAR(60),
  email VARCHAR(60)
);
CREATE TABLE consulta (
  id          INTEGER PRIMARY KEY,
  data        DATE,
  hora        TIME,
  crmmedico   VARCHAR(10) REFERENCES medico(crm),
  cpfpaciente VARCHAR(11) REFERENCES paciente(cpf),
  situacao    VARCHAR(10) CHECK (situacao IN ('agendada','realizada','cancelada'))
);
CREATE TABLE atendimento (
  idconsulta     INTEGER REFERENCES consulta(id),
  idatendimento  INTEGER,
  idprocedimento INTEGER REFERENCES procedimento(codigo),
  PRIMARY KEY (idconsulta, idatendimento)
);
```

```sql
INSERT INTO procedimento VALUES
 (1,'CONSULTA',150.00),(2,'APLICAÇÃO INJEÇÃO',60.00),(3,'CURATIVO',40.00),(4,'REVISAO EXAMES',80.00);
INSERT INTO paciente VALUES
 ('10101010101','ANTONIO MANOEL','amanoel@fviver.com.br',67),
 ('20202020202','MARIA JOAQUINA','mjoaquina@fviver.com.br',70),
 ('30303030303','JULIA SILVA','jsilva@fviver.com.br',80);
INSERT INTO medico VALUES
 ('567890','MARCELO ARAÚJO','maraujo@fviver.com.br'),
 ('234891','ALEXANDRE SOUZA','asouza@fviver.com.br'),
 ('167384','JUNIA TRINDADE','jtrindade@fviver.com.br');
INSERT INTO consulta VALUES
 (1,'2020-01-10','08:00','567890','10101010101','realizada'),
 (2,'2020-01-10','10:00','234891','30303030303','realizada'),
 (3,'2020-01-15','08:00','567890','30303030303','realizada'),
 (4,'2020-02-12','14:00','567890','10101010101','realizada'),
 (5,'2020-02-20','16:00','234891','20202020202','realizada'),
 (6,'2020-03-10','09:00','167384','30303030303','realizada'),
 (7,'2020-03-25','19:00',NULL,'20202020202','agendada'),
 (8,'2020-03-27','09:00',NULL,'10101010101','cancelada');
INSERT INTO atendimento VALUES
 (1,1,1),(1,2,2),(2,1,2),(3,1,3),(3,2,2),(4,1,4),(5,1,1),(6,1,2);
```

### 2.2 Consultas com função de agregação

```sql
-- Quantidade de pacientes
SELECT COUNT(*) FROM paciente;                        -- 3

-- Maior idade (devolve o VALOR, não o paciente)
SELECT MAX(idade) FROM paciente;                      -- 80

-- [Corrigida] Qual paciente tem a maior idade? (complementação)
SELECT nome, idade FROM paciente
WHERE idade = (SELECT MAX(idade) FROM paciente);      -- JULIA SILVA, 80

-- Média de idade dos pacientes atendidos por ALEXANDRE SOUZA
-- [Corrigida: o material imprime p.cpf = c.cpf e m.cpf = c.cpf, incompatível com as colunas]
SELECT AVG(p.idade)
FROM paciente p, medico m, consulta c
WHERE p.cpf = c.cpfpaciente AND m.crm = c.crmmedico
  AND m.nome = 'ALEXANDRE SOUZA';                     -- 75

-- Faturamento de janeiro/2020 (junção em 3 tabelas)
SELECT SUM(p.preco)
FROM procedimento p, consulta c, atendimento a
WHERE a.idconsulta = c.id AND p.codigo = a.idprocedimento
  AND c.data >= '2020-01-01' AND c.data <= '2020-01-31';   -- 370.00 (150+60+60+40+60)
```

### 2.3 Consultas com função de agrupamento

```sql
-- Consultas por situação
SELECT situacao, COUNT(*) FROM consulta GROUP BY situacao;
-- agendada 1 | realizada 6 | cancelada 1

-- Consultas realizadas por CRM
SELECT crmmedico, COUNT(*) FROM consulta
WHERE situacao = 'realizada' GROUP BY crmmedico;
-- 567890 3 | 234891 2 | 167384 1

-- Menor idade de paciente por médico
SELECT m.nome, MIN(p.idade)
FROM paciente p, medico m, consulta c
WHERE p.cpf = c.cpfpaciente AND m.crm = c.crmmedico
GROUP BY m.nome;
-- MARCELO ARAÚJO 67 | ALEXANDRE SOUZA 70 | JUNIA TRINDADE 80
```

```sql
-- Linhas (atendimentos) por médico
-- [Corrigida: o material omite "medico m" no FROM e a junção c.crmmedico = m.crm]
SELECT m.nome, COUNT(*)
FROM procedimento p, medico m, consulta c, atendimento a
WHERE a.idconsulta = c.id AND p.codigo = a.idprocedimento AND c.crmmedico = m.crm
GROUP BY m.nome;
-- MARCELO ARAÚJO 5 | ALEXANDRE SOUZA 2 | JUNIA TRINDADE 1

-- Só médicos com mais de um procedimento (HAVING)
SELECT m.nome, COUNT(*)
FROM procedimento p, medico m, consulta c, atendimento a
WHERE a.idconsulta = c.id AND p.codigo = a.idprocedimento AND c.crmmedico = m.crm
GROUP BY m.nome
HAVING COUNT(*) > 1;
-- MARCELO ARAÚJO 5 | ALEXANDRE SOUZA 2

-- COUNT(*) × COUNT(DISTINCT)
-- [Corrigida como acima] O material rotula COUNT(*) como "qtdeConsultas", mas conta atendimentos
SELECT m.nome,
       COUNT(*)                         AS qtdeAtendimentos,   -- 5 | 2 | 1
       COUNT(DISTINCT a.idprocedimento) AS qtdeProc,           -- 4 | 2 | 1
       COUNT(DISTINCT c.id)             AS qtdeConsultas       -- 3 | 2 | 1  (complementação)
FROM procedimento p, medico m, consulta c, atendimento a
WHERE a.idconsulta = c.id AND p.codigo = a.idprocedimento AND c.crmmedico = m.crm
GROUP BY m.nome;
```

### 2.4 Subconsulta

```sql
SELECT nome FROM paciente
WHERE idade IN (SELECT MIN(idade) FROM paciente);     -- ANTONIO MANOEL

-- Equivalente (subconsulta com valor único)
SELECT nome FROM paciente
WHERE idade = (SELECT MIN(idade) FROM paciente);
```

---

## 3. Índices — PostgreSQL (não executados; sintaxe e exemplos do material)

### 3.1 Sintaxe e variações

```sql
CREATE INDEX nome ON tabela (coluna);                          -- B-tree (padrão)
CREATE INDEX nome ON tabela USING HASH   (coluna);
CREATE INDEX nome ON tabela USING GIN    (coluna);             -- coluna tsvector
CREATE INDEX nome ON tabela USING GIST   (coluna);
CREATE INDEX nome ON tabela USING SPGIST (coluna);
CREATE INDEX nome ON tabela USING BRIN   (coluna) WITH (pages_per_range = 128);

CREATE INDEX nome ON tabela (coluna1, coluna2);                -- múltiplas colunas
CREATE INDEX nome ON tabela (coluna NULLS FIRST);              -- ordenado (só B-tree)
CREATE INDEX nome ON tabela (coluna DESC NULLS LAST);
CREATE UNIQUE INDEX nome ON tabela (coluna);                   -- único (só B-tree)
CREATE INDEX nome ON tabela (lower(coluna));                   -- funcional
CREATE INDEX nome ON tabela (idade) WHERE idade >= 50 AND idade <= 80;   -- parcial
CREATE INDEX CONCURRENTLY nome ON tabela (coluna);             -- não bloqueia gravações

DROP INDEX nome;
EXPLAIN SELECT * FROM tabela WHERE coluna = constante;
ANALYZE tabela;
ANALYZE tabela (coluna);
```

### 3.2 Exemplo 1 — Hash e B-tree

```sql
CREATE TABLE exemplo1 (nome varchar, idade integer);
INSERT INTO exemplo1 VALUES
 ('Bruna',26),('Carla',41),('Deiva',78),('Fernando',20),('Gilberto',24),('Ilmo',34);

CREATE INDEX id_indice_hash ON exemplo1 USING HASH (idade);
SELECT * FROM exemplo1 WHERE idade = 20;                       -- só igualdade

CREATE INDEX id_indice_B ON exemplo1 (idade);
SELECT * FROM exemplo1 WHERE idade >= 30 AND idade <= 80;      -- Carla 41, Deiva 78, Ilmo 34
```

### 3.3 Exemplo 2 — Dados geométricos

```sql
CREATE TABLE exemplo2 (ponto point);
INSERT INTO exemplo2 VALUES
 ('(0,1)'),('(0,2)'),('(0,6)'),('(1,1)'),('(1,2)'),('(2,1)'),
 ('(3,2)'),('(4,9)'),('(5,1)'),('(6,8)'),('(7,9)');

CREATE INDEX ponto_index_gist  ON exemplo2 USING GIST   (ponto);
CREATE INDEX ponto_index_spgist ON exemplo2 USING SPGIST (ponto);

SELECT * FROM exemplo2 ORDER BY ponto <-> point '(0,1)' LIMIT 6;
-- (0,1) (0,2) (1,1) (1,2) (2,1) (3,2)
```

### 3.4 Exemplo 3 — Múltiplas colunas e índice funcional

```sql
CREATE TABLE exemplo3 (nome varchar, sobrenome varchar, maior float, menor float);
INSERT INTO exemplo3 VALUES
 ('Ana','Monteiro',5000,1000),('Fernando','Fagundes',100,90),('Flaviele','Oliveira',4500,100),
 ('Gilberto','Moraes',1400,180),('Igor','Soares',3300,150),('Ilmo','Da Silva',3400,100),
 ('João','Lima',2400,100),('Joana','Lopes',3900,450);

-- Material: "menor = 9" (provável erro; na tabela Fernando tem menor = 90)
SELECT nome FROM exemplo3 WHERE maior = 100 AND menor = 90;
CREATE INDEX index_multi ON exemplo3 (maior, menor);

CREATE INDEX index_f ON exemplo3 ((nome || ' ' || sobrenome));
SELECT * FROM exemplo3 WHERE (nome || ' ' || sobrenome) = 'Joana Lopes';   -- Joana Lopes 3900 450
```

### 3.5 Exemplo 4 — Pedidos faturados (índice parcial, CONCURRENTLY, BRIN)

```sql
-- Nomes de colunas uniformizados (o material alterna faturado/faturados e num_pedido/num_pedidos) — complementação
CREATE INDEX nfaturado_indice ON pedidos (num_pedidos) WHERE faturado IS NOT TRUE;
SELECT * FROM pedidos WHERE faturado IS NOT TRUE AND num_pedidos < 10000;
SELECT * FROM pedidos WHERE faturado IS NOT TRUE AND montante > 5000.00;

-- Sem bloquear inserções
CREATE INDEX CONCURRENTLY nfaturado_indice ON pedidos (num_pedidos) WHERE faturado IS NOT TRUE;

-- Tabela com milhares de registros: BRIN sobre a data
-- (o material imprime "CREATE INDEX * ON ..."; o "*" é um nome de índice faltando)
CREATE INDEX idx_pedidos_data_brin ON pedidos USING BRIN (data) WITH (pages_per_range = 128);
```

### 3.6 Exemplo 5 — COLLATE

```sql
CREATE TABLE exemplo4 (id integer, conteudo varchar COLLATE "x");
CREATE INDEX collate_index ON exemplo4 (conteudo);
SELECT * FROM exemplo4 WHERE conteudo > 10;

CREATE INDEX collate_index_y ON exemplo4 (conteudo COLLATE "y");
SELECT * FROM exemplo4 WHERE conteudo > 10 COLLATE "y";
```
> O material usa `exemplo4` na criação e `exemplo` no segundo índice, e `content` no lugar de `conteudo` — grafia uniformizada aqui. `"x"` e `"y"` são nomes ilustrativos de agrupamentos.

### 3.7 Exemplo 6 — Busca em texto

```sql
CREATE TABLE exemplo6 (id integer, titulo tsvector, corpo tsvector);
-- 8 livros: The Lucky One, The Last Song, The Best of Me, Dear John,
--           See Me, Every Breath, The Notebook, A Walk to Remember

CREATE INDEX indice_gin ON exemplo6 USING GIN ((titulo || ' ' || corpo));
SELECT * FROM exemplo6 WHERE (titulo || ' ' || corpo) = 'Dear John ...';   -- livro 4
```

### 3.8 Tabela hipotética `pessoa` (explicação do índice por nome — complementação)

```sql
CREATE TABLE pessoa (
  nome     VARCHAR(40),
  idade    INTEGER,
  endereco VARCHAR(60),
  estudo   VARCHAR(20),
  sexo     CHAR(1)
);
INSERT INTO pessoa VALUES
 ('Carla', 41,'Rua das Flores, 120','Superior','F'),
 ('Bruno', 26,'Av. Brasil, 45','Médio','M'),
 ('Ana',   34,'Rua Sete, 300','Pós-graduação','F'),
 ('Diego', 29,'Rua do Sol, 88','Superior','M'),
 ('Elisa', 52,'Praça Central, 10','Fundamental','F');

CREATE INDEX idx_pessoa_nome ON pessoa (nome);
SELECT * FROM pessoa WHERE nome = 'Diego';
EXPLAIN SELECT * FROM pessoa WHERE nome = 'Diego';   -- em 5 linhas o PostgreSQL pode preferir ler a tabela direto
```

Visual: `INDICE_POR_NOME_VISUAL.svg`.
