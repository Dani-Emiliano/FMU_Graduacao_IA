# HOW-TO — Identificar outliers e executar PCA no VS Code

**Aula 3 — Aprendizado de Máquina Não Supervisionado (262GGR6044A)**

Tempo estimado: 20 a 30 minutos (a primeira vez).

> **Está com a PCA "nebulosa"?** Rode primeiro o `pca_exemplo_imoveis.py` (mesmo ambiente, 7 células curtas) e leia a seção 3.9.0 do `.md` da Aula 3. Depois volte ao script principal.
Resultado: um script que roda célula por célula, gera 3 gráficos na pasta `saidas/` e imprime as tabelas que você precisa para interpretar.

> **Este material é complementação.** O capítulo da aula usa o dataset Boston Housing. Aqui uso o dataset **Wine** (vem junto com o scikit-learn, funciona offline e não tem os problemas do Boston, explicados na seção 8). O método é o mesmo do capítulo (IQR, box-plot, Mahalanobis) e o script foi **testado** (os números da seção 5 são resultados reais da execução).

---

## 1. O que você vai fazer

| Etapa | O que o script faz | Conceito da aula |
|---|---|---|
| 1–2 | Carrega o dataset e desenha box-plots | Box-plot e visualização de outliers |
| 3 | Marca outliers pelo IQR (cercas de 1,5× e 3×) | Método do intervalo interquartil |
| 4 | Calcula a distância de Mahalanobis (clássica e robusta) | Outliers multivariados |
| 5 | Compara remover × limitar (clip) × manter | Decidir remover ou não |
| 6 | Faz a PCA "na mão" com NumPy e confere com o scikit-learn | Metodologia da PCA, passo a passo |
| 7 | Scree plot, variância acumulada, critério de Kaiser, cargas | Quantos componentes manter |
| 8 | Projeta em PC1 × PC2 e desenha o biplot | Interpretar a PCA |
| 9 | Injeta 3 linhas com erro e mede o estrago na PCA | Por que tratar outliers antes da PCA |
| 10 | Compara um modelo com e sem PCA (Pipeline) | PCA no aprendizado supervisionado |
| 11 | Mede o erro de reconstrução | O que se perde ao descartar componentes |

---

## 2. Pré-requisitos

1. **Python 3.10 ou superior.** Baixe em python.org. No Windows, marque **"Add python.exe to PATH"** no instalador.
2. **VS Code** instalado.
3. Extensões do VS Code (ícone de quadradinhos na barra lateral, ou `Ctrl+Shift+X`):
   - **Python** (Microsoft)
   - **Jupyter** (Microsoft), necessária para rodar célula por célula

Verifique no terminal:
```bash
python --version
```
Se aparecer algo como `Python 3.12.x`, está certo. No macOS/Linux, use `python3`.

---

## 3. Passo a passo

### 3.1 Criar a pasta do projeto
1. Crie uma pasta, por exemplo `aula03`.
2. No VS Code: **File → Open Folder** e escolha a pasta.
3. Copie para dentro dela os dois arquivos entregues: `aula03_outliers_pca.py` e `requirements.txt`.

### 3.2 Abrir o terminal do VS Code
Atalho: ``Ctrl+` `` (tecla crase, abaixo do Esc). Confirme que o caminho mostrado é o da pasta `aula03`.

### 3.3 Criar o ambiente virtual (isola as bibliotecas deste projeto)

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
Se der erro de "execução de scripts desabilitada", use o Prompt de Comando (cmd) no lugar do PowerShell:
```bat
.venv\Scripts\activate.bat
```
(Alternativa: liberar scripts só para o seu usuário com `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. Isso muda uma configuração do Windows, então só faça se concordar.)

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Quando funcionar, o terminal mostra `(.venv)` no início da linha.

### 3.4 Instalar as bibliotecas
```bash
pip install -r requirements.txt
```
Instala: `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib` e `seaborn`.

### 3.5 Escolher o interpretador no VS Code
1. `Ctrl+Shift+P`, digite **Python: Select Interpreter**.
2. Escolha o que termina em `.venv` (algo como `.\.venv\Scripts\python.exe`).

### 3.6 Executar

**Opção A — célula por célula (recomendado para estudar):**
1. Abra `aula03_outliers_pca.py`.
2. Acima de cada `# %%` aparece **Run Cell**. Clique, ou posicione o cursor e use `Shift+Enter`.
3. Na primeira vez, o VS Code pode pedir para instalar o **ipykernel**: aceite. (Se preferir, rode `pip install ipykernel`.)
4. Os resultados e gráficos aparecem na janela **Interactive**.

**Opção B — arquivo inteiro:**
- Botão ▶ no canto superior direito, ou no terminal:
```bash
python aula03_outliers_pca.py
```
Cada gráfico abre em uma janela e o script só continua quando você a fecha. Os arquivos também ficam salvos em `saidas/`.

> Rode as células **em ordem**: as seguintes usam variáveis criadas pelas anteriores.

---

## 4. O que cada célula faz e como ler o resultado

### Células 1–2 — Carregar e olhar os dados
- Confirme `Formato: (178, 13)` e que não há valores ausentes.
- Nos box-plots, **pontos isolados além dos bigodes** são outliers pela regra de 1,5 × IQR.
- Veja que as variáveis têm escalas muito diferentes (`proline` na casa dos 700, `hue` perto de 1). É por isso que a PCA exige padronização.

### Célula 3 — IQR
Para cada coluna: `limite_inf = Q1 − 1,5×IQR` e `limite_sup = Q3 + 1,5×IQR`. Tudo fora disso é outlier.
- A tabela `resumo` mostra limites, quantidade e percentual por coluna.
- A saída "Outliers EXTREMOS (3 × IQR)" lista quem passa das cercas externas.
- `identificar_outliers(df["malic_acid"])` devolve valores **e índices**, igual à função do capítulo.

### Célula 4 — Mahalanobis
Olha as variáveis **em conjunto**: uma linha pode ter cada valor "normal" e uma combinação incomum.
- Corte: quantil 0,975 da qui-quadrado com p graus de liberdade (aqui, 24,74).
- Compara a versão clássica (usa média e covariância da amostra) com a robusta (`MinCovDet`).

### Célula 5 — Decidir e tratar
Compara três estratégias lado a lado: remover linhas, limitar valores (`clip`) ou manter. O script **não decide por você**.

### Células 6–8 — PCA
- **Célula 6** repete a metodologia do capítulo: padronizar → matriz de covariância → autovalores/autovetores → ordenar → variância explicada → projetar. As duas últimas linhas confirmam que sua conta na mão bate com o scikit-learn (`True`/`True`).
- **Célula 7** mostra o scree plot e a variância acumulada, e imprime as **cargas** (peso de cada variável em cada componente).
- **Célula 8** projeta cada vinho em PC1 × PC2. A cor da classe é só para você enxergar a separação: **a PCA não usa o rótulo**.

### Célula 9 — O estrago dos outliers
Adiciona 3 linhas com valores 8 desvios-padrão acima da média e refaz a PCA. Compare as três linhas da tabela.

### Célula 10 — PCA no fluxo supervisionado
Treina uma regressão logística sem PCA, com 2 componentes e mantendo 95%. O ponto-chave: scaler e PCA ficam **dentro do `Pipeline`**, para serem ajustados só com os dados de treino.

### Célula 11 — Reconstrução
Mostra que o erro ao descartar componentes é exatamente a soma dos autovalores descartados.

---

## 5. Resultados reais (para você conferir se rodou certo)

Valores obtidos na execução de teste (Python 3.12, scikit-learn 1.8). Pequenas diferenças na última casa decimal podem ocorrer entre versões.

**Outliers (IQR, 1,5×):**

| Variável | Qtde de outliers | % |
|---|---|---|
| malic_acid | 3 | 1,7 |
| ash | 3 | 1,7 |
| alcalinity_of_ash | 4 | 2,2 |
| magnesium | 4 | 2,2 |
| proanthocyanins | 2 | 1,1 |
| color_intensity | 4 | 2,2 |
| hue | 1 | 0,6 |
| demais 6 variáveis | 0 | 0 |

- **17 de 178 linhas (9,6%)** têm pelo menos um outlier.
- **Nenhum** outlier extremo (3 × IQR).
- `malic_acid`: índices 123, 137 e 173 (5,80, 5,51 e 5,65).

**Mahalanobis (corte MD² = 24,74):**

| Versão | Outliers |
|---|---|
| Clássica | 12 |
| Robusta (MinCovDet) | 51 (inclui os 12 da clássica) |

IQR e Mahalanobis robusta concordam em 14 linhas. Maiores distâncias robustas: linhas 121, 69, 95, 110 e 96.

**PCA (dados padronizados):**

| Componente | Autovalor | Variância explicada | Acumulada |
|---|---|---|---|
| PC1 | 4,73 | 36,2% | 36,2% |
| PC2 | 2,51 | 19,2% | 55,4% |
| PC3 | 1,45 | 11,1% | 66,5% |
| PC4 | 0,92 | 7,1% | 73,6% |
| PC5 | 0,86 | 6,6% | 80,2% |
| ... | ... | ... | ... |
| PC10 | 0,25 | 1,9% | 96,2% |

- Componentes para ≥ 95%: **10**. Critério de Kaiser: **3**. Cotovelo do scree plot: perto de **3 a 4**.
- Cargas de PC1: `flavanoids` (0,42), `total_phenols` (0,39), `od280/od315` (0,38), com sinal oposto em `nonflavanoid_phenols` (−0,30) e `malic_acid` (−0,25).
- Cargas de PC2: `color_intensity` (0,53), `alcohol` (0,48), `proline` (0,36).

**Efeito de outliers na PCA:**

| Base | Linhas | PC1 | PC1+PC2 | Cosseno do PC1 vs. original |
|---|---|---|---|---|
| original | 178 | 36,2% | 55,4% | 1,000 |
| com 3 linhas erradas | 181 | 32,2% | 50,7% | 0,992 |
| erradas removidas (3×IQR) | 178 | 36,2% | 55,4% | 1,000 |

**Modelo com e sem PCA (regressão logística):**

| Modelo | Componentes | Acurácia (validação cruzada) | Acurácia no teste |
|---|---|---|---|
| Sem PCA | 13 | 0,984 | 0,981 |
| PCA, 2 componentes | 2 | 0,968 | 0,944 |
| PCA, 95% | 10 | 0,975 | 0,981 |

**Reconstrução:** com 1 componente o erro é 8,294; com 2, 5,797; com 3, 4,351; com 5, 2,579; com 8, 1,038; com 13, 0. Em todos os casos coincide com a soma dos autovalores descartados.

---

## 6. Como interpretar (o raciocínio para a atividade)

**Outliers**
1. As 17 linhas sinalizadas pelo IQR são todas **moderadas** (nenhuma extrema). Em dados reais de vinho, isso é típico de variação natural, não de erro de digitação.
2. A Mahalanobis robusta marca bem mais linhas (51) porque estima a covariância usando só a parte "mais comportada" dos dados, o que encolhe a elipse de normalidade; além disso, o corte qui-quadrado supõe dados normais, e os dados reais não são. **Use-a como ranking**: investigue as maiores distâncias (121, 69, 95...) em vez de remover todas as 51.
3. **Decisão neste caso:** remover 9,6% das linhas por IQR seria perder dados reais sem evidência de erro. O mais defensável é **manter** (ou, no máximo, limitar com `clip`) e documentar o motivo. Compare com o quadro de decisão da seção 4.3 do `.md` da Aula 3.

**PCA**
1. PC1 sozinho guarda 36% da variância e PC1+PC2 guardam 55%. Para 95%, são 10 componentes: **os dados não são muito compressíveis**. Os 13 atributos têm correlações moderadas, não fortíssimas.
2. Kaiser sugere 3 e a regra dos 95% sugere 10. Os critérios divergem; a escolha é uma decisão sua e depende do objetivo (visualizar → 2 ou 3; alimentar um modelo → valide por desempenho).
3. PC1 é um eixo "perfil fenólico" (flavonoides, fenóis totais e OD280 de um lado; fenóis não flavonoides e ácido málico do outro). PC2 mistura intensidade de cor, álcool e prolina. Dar nome ao componente é interpretação sua, não resultado da PCA.
4. No gráfico PC1 × PC2, as três classes aparecem bem separadas **sem a PCA ter visto o rótulo**. É o poder do método não supervisionado.
5. Outliers: três linhas erradas bastaram para derrubar o PC1 de 36,2% para 32,2% e girar o eixo. Após remover as linhas erradas, a PCA volta ao resultado original.
6. Supervisionado: **a PCA não melhorou a acurácia** (0,984 sem PCA contra 0,975 com 95%). Ela serve para comprimir, reduzir multicolinearidade e visualizar, mas não garante ganho de desempenho.

---

## 7. Usar com o seu próprio arquivo (CSV)

Troque a célula 1 por:
```python
df_bruto = pd.read_csv("meu_arquivo.csv")        # ajuste separador/decimal se precisar: sep=";", decimal=","
y = df_bruto["coluna_alvo"]                       # opcional: só se existir um rótulo
df = df_bruto.drop(columns=["coluna_alvo", "id"], errors="ignore").select_dtypes("number")
p = df.shape[1]
print(df.shape); print(df.isna().sum())
```
E ajuste as partes que citam `wine`: a célula 8 usa `wine.target_names` (troque por nomes das suas classes ou apague a coloração) e a célula 10 só faz sentido se você tiver um rótulo.

**Checklist antes de rodar PCA no seu dado:**

| Verifique | Por quê | O que fazer |
|---|---|---|
| Valores ausentes | A PCA não aceita `NaN` (erro `Input contains NaN`) | `dropna()` ou imputar (média/mediana) |
| Colunas de ID | Número de identificação não é medida | Remover |
| Variáveis categóricas | PCA exige numéricas contínuas | Não aplicar PCA nelas (ver análise de correspondência, Aula 2) |
| Escalas diferentes | Variáveis de maior escala dominam | Padronizar (`StandardScaler`), como no script |
| Outliers | Distorcem médias, variâncias e eixos | Avaliar com IQR/Mahalanobis **antes** |
| Rótulo | Não faz parte da PCA | Separar em `y` |

---

## 8. Sobre o dataset Boston do capítulo

O capítulo usa `boston_df`, que não é carregado no texto. A função `load_boston` foi **removida do scikit-learn na versão 1.2**, em parte por uma preocupação ética com uma de suas variáveis (a coluna `B`, construída a partir da proporção de moradores negros). Por isso este how-to usa o Wine.

Se quiser reproduzir o capítulo mesmo assim, existe a opção de baixar a base pelo OpenML (precisa de internet; **não testei aqui**, pois meu ambiente não acessa a internet):
```python
from sklearn.datasets import fetch_openml
boston = fetch_openml(name="boston", version=1, as_frame=True)
boston_df = boston.data.apply(pd.to_numeric, errors="coerce")
```
Uma alternativa sem esse problema, também por download (também não testada aqui): `fetch_california_housing(as_frame=True).data`.

---

## 9. Quando usar cada método de outliers (para o `.md` e a prova)

| Método | Quando usar | Exemplo teórico | Exemplo real |
|---|---|---|---|
| **Box-plot / IQR (1,5×)** | Variável **isolada**; sem supor distribuição normal; triagem rápida | Idade = 450 numa coluna de idades | Valor de venda muito acima do normal numa coluna de faturamento |
| **IQR com 3× (extremos)** | Quando quer só os casos gritantes, evitando falsos alarmes | Salário 10 vezes a mediana | Leitura de sensor travada num valor absurdo |
| **Mahalanobis clássica** | Várias variáveis juntas, dados aproximadamente normais, poucos outliers | Altura 1,60 m e peso 120 kg: cada valor é plausível, a combinação não | Cliente com renda baixa e gasto altíssimo em cartão |
| **Mahalanobis robusta (MinCovDet)** | Mesma situação, mas há muitos outliers contaminando a média e a covariância | Base de transações com fraudes misturadas | Detecção de comportamento anômalo em acessos a sistema |
| **Remover** | Erro comprovado (digitação, sensor, corrupção) | Idade negativa | Linha duplicada por falha de integração |
| **Limitar (`clip`)** | Valor real mas extremo, que distorce o modelo; não quer perder a linha | Renda de bilionário numa base de classe média | Preço de imóvel de luxo numa base de moradia popular |
| **Manter e investigar** | Outlier é o objeto de estudo | Fraude, falha, intrusão | Transação suspeita num antifraude |

---

## 10. Problemas comuns

| Sintoma | Causa provável | Solução |
|---|---|---|
| `ModuleNotFoundError: No module named 'sklearn'` | Instalou fora do ambiente virtual | Ative o `.venv` (deve aparecer `(.venv)`), selecione o interpretador (3.5) e rode `pip install -r requirements.txt` |
| `.venv\Scripts\Activate.ps1 cannot be loaded` | PowerShell bloqueia scripts | Use `activate.bat` no cmd (3.3) |
| `Run Cell` não aparece | Extensão Python/Jupyter ausente ou arquivo sem `# %%` | Instale as extensões (seção 2) e use o arquivo original |
| Pede "ipykernel" | Falta o kernel Jupyter | Aceite a instalação ou `pip install ipykernel` |
| Gráfico não abre / script "trava" | Janela do gráfico aberta esperando | Feche a janela do gráfico; ou veja o PNG em `saidas/` |
| `ValueError: Input contains NaN` | Valores ausentes no seu CSV | Trate os ausentes (seção 7) |
| `FileNotFoundError` no CSV | Caminho errado | Coloque o CSV na pasta do projeto ou use o caminho completo |
| Números diferentes dos da seção 5 | Versão diferente de biblioteca | Pequenas diferenças são normais; se forem grandes, confira se usou o Wine |

---

## 11. Exercícios para fixar

1. **Troque o fator:** na célula 3, use `fator=3` na lista principal. O que muda na quantidade de outliers? Qual é a vantagem de cada fator?
2. **PCA sem padronizar:** na célula 6, troque `Xp` por `df.to_numpy()` e compare a variância de PC1. Qual variável domina? (Dica: veja a escala de `proline`.)
3. **PCA sem os outliers do IQR:** rode a PCA em `df_sem_qualquer` (célula 5) e compare com a original. Os 17 outliers faziam diferença?
4. **Escolha de componentes:** na célula 10, teste `PCA(n_components=3)` e `PCA(n_components=5)`. A acurácia sobe ou desce?
5. **Dataset próprio:** aplique o roteiro ao CSV de um projeto seu seguindo o checklist da seção 7.
6. **Explique em 3 linhas** por que, na célula 10, a PCA entra dentro do `Pipeline` e não antes do `train_test_split`.

---

## 12. Arquivos deste pacote

| Arquivo | Para quê |
|---|---|
| `aula03_outliers_pca.py` | Script completo, dividido em células `# %%` |
| `pca_exemplo_imoveis.py` | Exemplo curto e fictício (10 imóveis) para entender a PCA em linguagem prática; roda em segundos e usa as mesmas bibliotecas |
| `requirements.txt` | Bibliotecas a instalar |
| `saidas_exemplo/` | Gráficos que o script gera (para você conferir) e a figura de intuição da PCA |
| `HOWTO_AULA_03_OUTLIERS_PCA_VSCODE.md` | Este guia |
