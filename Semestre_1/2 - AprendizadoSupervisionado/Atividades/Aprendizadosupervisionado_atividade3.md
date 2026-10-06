Ao iniciar o pré-processamento de um texto em linguagem natural, iniciamos com a **tokenização**.

O seu objetivo é facilitar a análise de um fluxo de texto, então ele quebra esse fluxo de texto em frases, palavras ou outros elementos chamados tokens.

Após a tokenização, temos a etapa de limpeza dos dados. Para a limpeza, existem diversas técnicas e ferramentas; no capítulo, as apresentadas como essenciais são a remoção de stopwords e de pontuação, porém outras, como padronização de caracteres e correção de erros de digitação, também aparecem como importantes e opcionais.

Objetivo da PLN: Identificar etapas executadas pela aluna em cada aula.

Frase: Daniela leu o livro para depois faser o trabalho.

Etapa 1: Tokenização

`["Daniela", "leu", "o", "livro", "para", "depois", "faser", "o", "trabalho", "."]`

Etapa 2: Limpeza

* Remoção de stopwords (removidos: "o", "para", "depois", "o"):  
  `["Daniela", "leu", "livro", "faser", "trabalho", "."]`
* Remoção de pontuação (removido o "."):  
  `["Daniela", "leu", "livro", "faser", "trabalho"]`
* Opcional incluída: correção de erros de digitação ("faser" → "fazer"):  
  `["Daniela", "leu", "livro", "fazer", "trabalho"]`
* Padronização em minúsculas ("Daniela" → "daniela"):  
  `["daniela", "leu", "livro", "fazer", "trabalho"]`

Texto final após o pré-processamento:

`daniela leu livro fazer trabalho`

Nota: "depois" foi removido, conforme exemplo no capítulo. Para este objetivo em específico, a ordem das atividades não importa. O objetivo é identificar as etapas e não sequenciá-las.
