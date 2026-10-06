# %% [markdown]
# # Aula 3 — Outliers (IQR, box-plot, Mahalanobis) e PCA
# Aprendizado de Máquina Não Supervisionado (262GGR6044A)
#
# Como usar no VS Code: execute célula por célula (Shift+Enter em cada bloco "# %%")
# ou rode o arquivo inteiro (botão ▶ "Run Python File").
# Os gráficos também são salvos na pasta "saidas/".

# %% 0. Configuração e imports
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import chi2
from sklearn.covariance import MinCovDet
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

SAIDA = Path("saidas")
SAIDA.mkdir(exist_ok=True)
RANDOM_STATE = 42
pd.set_option("display.width", 150)
pd.set_option("display.max_columns", 30)
sns.set_theme(style="whitegrid")

# %% 1. Carregar os dados (Wine: 178 vinhos, 13 variáveis numéricas, 3 classes)
# Troque esta célula para usar o seu próprio CSV: df = pd.read_csv("meu_arquivo.csv")
wine = load_wine(as_frame=True)
df = wine.data.copy()          # somente variáveis numéricas (sem rótulo)
y = wine.target                # rótulo (só usado para colorir gráficos e na etapa supervisionada)
p = df.shape[1]

print("Formato:", df.shape)
print(df.head())
print("\nValores ausentes por coluna:\n", df.isna().sum()[df.isna().sum() > 0])
print(df.describe().T[["mean", "std", "min", "max"]].round(2))

# %% 2. Visualizar: box-plot de cada variável (escalas diferentes → um gráfico por coluna)
fig, eixos = plt.subplots(3, 5, figsize=(16, 8))
for ax, col in zip(eixos.ravel(), df.columns):
    sns.boxplot(x=df[col], ax=ax, color="#4C72B0")
    ax.set_title(col, fontsize=10)
    ax.set_xlabel("")
for ax in eixos.ravel()[p:]:
    ax.axis("off")
fig.suptitle("Box-plots: pontos isolados fora dos bigodes são outliers (regra 1,5 × IQR)")
fig.tight_layout()
fig.savefig(SAIDA / "01_boxplots.png", dpi=130)
plt.show()

# %% 3. Identificar outliers com o método do intervalo interquartil (IQR)
def limites_iqr(dados: pd.DataFrame, fator: float = 1.5):
    """Devolve (limite_inferior, limite_superior) por coluna: Q1 - f*IQR e Q3 + f*IQR."""
    q1, q3 = dados.quantile(0.25), dados.quantile(0.75)
    iqr = q3 - q1
    return q1 - fator * iqr, q3 + fator * iqr


def identificar_outliers(serie: pd.Series, fator: float = 1.5) -> pd.Series:
    """Versão univariada (equivalente à função do capítulo): valores e índices fora dos limites."""
    q1, q3 = np.percentile(serie, [25, 75])
    iqr = q3 - q1
    return serie[(serie < q1 - fator * iqr) | (serie > q3 + fator * iqr)]


inf, sup = limites_iqr(df)                      # cercas internas (1,5 × IQR)
mascara = (df < inf) | (df > sup)               # True = outlier moderado ou extremo
resumo = pd.DataFrame({
    "limite_inf": inf, "limite_sup": sup,
    "n_outliers": mascara.sum(), "pct": (mascara.mean() * 100).round(1),
})
print(resumo.round(2))

linhas_com_outlier = mascara.any(axis=1)
print(f"\nLinhas com pelo menos um outlier: {linhas_com_outlier.sum()} de {len(df)} "
      f"({linhas_com_outlier.mean():.1%})")

# cercas externas (3 × IQR): outliers extremos
inf3, sup3 = limites_iqr(df, fator=3)
mascara_ext = (df < inf3) | (df > sup3)
print("\nOutliers EXTREMOS (3 × IQR) por coluna:")
print(mascara_ext.sum()[mascara_ext.sum() > 0])

# exemplo univariado: quais valores e índices
print("\nOutliers de 'malic_acid':")
print(identificar_outliers(df["malic_acid"]))

# %% 4. Outliers multivariados: distância de Mahalanobis
# MD² de dados normais multivariados segue qui-quadrado com p graus de liberdade.
# Candidato a outlier: MD² > quantil 0,975 de χ²(p).
X = df.to_numpy()
corte = chi2.ppf(0.975, df=p)

# (a) Clássica: média e covariância da amostra (sensíveis aos próprios outliers)
dif = X - X.mean(axis=0)
md2_classica = np.einsum("ij,jk,ik->i", dif, np.linalg.inv(np.cov(X, rowvar=False)), dif)

# (b) Robusta: MinCovDet estima média/covariância ignorando as observações mais estranhas
mcd = MinCovDet(random_state=RANDOM_STATE).fit(X)
md2_robusta = mcd.mahalanobis(X)               # devolve MD² (distância ao quadrado)

out_classica = md2_classica > corte
out_robusta = md2_robusta > corte
print(f"Corte χ²(0,975; gl={p}) para MD²: {corte:.2f}")
print(f"Outliers (Mahalanobis clássica): {out_classica.sum()}")
print(f"Outliers (Mahalanobis robusta) : {out_robusta.sum()}")
print(f"Em comum: {(out_classica & out_robusta).sum()}")

top = (pd.DataFrame({"MD2_classica": md2_classica, "MD2_robusta": md2_robusta}, index=df.index)
       .sort_values("MD2_robusta", ascending=False).head(8))
print("\nMaiores distâncias (robusta):\n", top.round(1))

# Linhas que o IQR (univariado) e a Mahalanobis (multivariada) sinalizam
print("\nIQR e Mahalanobis robusta concordam em:", (linhas_com_outlier.to_numpy() & out_robusta).sum(), "linhas")

# %% 5. Decidir e tratar (marcar primeiro, decidir depois)
df_sem_qualquer = df[~linhas_com_outlier]                      # a) remove linhas com qualquer outlier (1,5 × IQR)
df_sem_extremos = df[~mascara_ext.any(axis=1)]                 # b) remove só linhas com outlier extremo (3 × IQR)
df_limitado = df.clip(lower=inf, upper=sup, axis=1)            # c) limita (clip) os valores às cercas

print(f"Original             : {len(df)} linhas")
print(f"a) sem qualquer outl.: {len(df_sem_qualquer)} linhas ({1 - len(df_sem_qualquer)/len(df):.1%} perdidas)")
print(f"b) sem extremos      : {len(df_sem_extremos)} linhas ({1 - len(df_sem_extremos)/len(df):.1%} perdidas)")
print(f"c) clip              : {len(df_limitado)} linhas (nenhuma perdida; valores ajustados)")
# Regra prática: erro de coleta → corrigir/remover; valor real e relevante → manter e investigar.

# %% 6. PCA passo a passo "na mão" (NumPy) — espelha a metodologia do capítulo
# Passo 1: padronizar (média 0, desvio 1) — a PCA é sensível à escala
Xp = StandardScaler().fit_transform(df)

# Passo 2: matriz de covariância (p × p, simétrica). Com dados padronizados ≈ matriz de correlação
C = np.cov(Xp, rowvar=False)

# Passo 3: autovalores e autovetores (eigh é o indicado para matriz simétrica)
autovalores, autovetores = np.linalg.eigh(C)

# Passo 4: ordenar do maior para o menor autovalor
ordem = np.argsort(autovalores)[::-1]
autovalores, autovetores = autovalores[ordem], autovetores[:, ordem]

# Passo 5: variância explicada = autovalor / soma dos autovalores
var_explicada = autovalores / autovalores.sum()
tabela = pd.DataFrame({
    "autovalor": autovalores,
    "var_explicada_%": var_explicada * 100,
    "acumulada_%": var_explicada.cumsum() * 100,
}, index=[f"PC{i+1}" for i in range(p)])
print(tabela.round(2))

# Passo 6: projetar os dados nos componentes (scores) = dados padronizados × autovetores
scores_manual = Xp @ autovetores

# Conferência com o scikit-learn (o sinal de cada componente é arbitrário → comparamos o valor absoluto)
pca_full = PCA().fit(Xp)
print("\nAutovalores iguais ao sklearn? ", np.allclose(autovalores, pca_full.explained_variance_))
print("Scores iguais ao sklearn (|valor|)?", np.allclose(np.abs(scores_manual), np.abs(pca_full.transform(Xp))))

# %% 7. PCA com scikit-learn: quantos componentes manter?
acumulada = np.cumsum(pca_full.explained_variance_ratio_)
n95 = int(np.argmax(acumulada >= 0.95) + 1)
autovalores_corr = np.sort(np.linalg.eigvalsh(df.corr().to_numpy()))[::-1]
kaiser = int((autovalores_corr > 1).sum())
print(f"Componentes para ≥ 95% da variância: {n95}")
print(f"Critério de Kaiser (autovalor da matriz de correlação > 1): {kaiser}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4.5))
ax1.plot(range(1, p + 1), autovalores_corr, "o-")
ax1.axhline(1, color="red", ls="--", label="Kaiser (autovalor = 1)")
ax1.set(title="Scree plot (procure o 'cotovelo')", xlabel="Componente", ylabel="Autovalor")
ax1.legend()
ax2.bar(range(1, p + 1), pca_full.explained_variance_ratio_ * 100, alpha=0.6, label="Individual")
ax2.plot(range(1, p + 1), acumulada * 100, "o-", color="darkred", label="Acumulada")
ax2.axhline(95, color="gray", ls="--", label="95%")
ax2.set(title="Variância explicada (%)", xlabel="Componente", ylabel="%")
ax2.legend()
fig.tight_layout()
fig.savefig(SAIDA / "02_scree_variancia.png", dpi=130)
plt.show()

# Cargas (loadings): peso de cada variável original em cada componente
cargas = pd.DataFrame(pca_full.components_.T, index=df.columns,
                      columns=[f"PC{i+1}" for i in range(p)])
print("\nCargas dos 3 primeiros componentes (maiores valores absolutos = variáveis mais importantes):")
print(cargas.iloc[:, :3].round(2).sort_values("PC1", key=np.abs, ascending=False))

# %% 8. Projeção em 2D (PC1 × PC2) e biplot
pca2 = PCA(n_components=2).fit(Xp)
scores2 = pca2.transform(Xp)
nomes_classe = dict(enumerate(wine.target_names))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))
for classe, nome in nomes_classe.items():
    ax1.scatter(*scores2[y == classe].T, label=nome, alpha=0.8)
ax1.set(xlabel=f"PC1 ({pca2.explained_variance_ratio_[0]:.1%})",
        ylabel=f"PC2 ({pca2.explained_variance_ratio_[1]:.1%})",
        title="Scores: cada ponto é um vinho (cor = classe, só para visualizar)")
ax1.legend()

ax2.axhline(0, color="gray", lw=0.5); ax2.axvline(0, color="gray", lw=0.5)
for i, col in enumerate(df.columns):
    vx, vy = pca2.components_[0, i], pca2.components_[1, i]
    ax2.arrow(0, 0, vx, vy, color="tab:red", head_width=0.015, length_includes_head=True)
    ax2.text(vx * 1.08, vy * 1.08, col, fontsize=8, ha="center")
ax2.set(xlabel="PC1", ylabel="PC2", title="Cargas: setas próximas apontam para variáveis correlacionadas")
ax2.set_aspect("equal")
fig.tight_layout()
fig.savefig(SAIDA / "03_pc1_pc2_biplot.png", dpi=130)
plt.show()

# %% 9. Efeito dos outliers na PCA (por que limpar/avaliar ANTES de reduzir)
rng = np.random.default_rng(RANDOM_STATE)
df_sujo = df.copy()
linhas_falsas = []
for _ in range(3):                                   # 3 linhas com erros de digitação em 3 colunas cada
    linha = df.mean().copy()
    cols = rng.choice(df.columns, size=3, replace=False)
    linha[cols] = df[cols].mean() + 8 * df[cols].std()
    linhas_falsas.append(linha)
df_sujo = pd.concat([df, pd.DataFrame(linhas_falsas)], ignore_index=True)

# limpa as linhas com outlier extremo (3 × IQR) e refaz a PCA
i3, s3 = limites_iqr(df_sujo, fator=3)
df_sujo_limpo = df_sujo[~((df_sujo < i3) | (df_sujo > s3)).any(axis=1)]


def pca_resumo(dados: pd.DataFrame, rotulo: str):
    pca = PCA().fit(StandardScaler().fit_transform(dados))
    return pca, {"base": rotulo, "linhas": len(dados),
                 "PC1_%": pca.explained_variance_ratio_[0] * 100,
                 "PC1+PC2_%": pca.explained_variance_ratio_[:2].sum() * 100}


pca_ref, r1 = pca_resumo(df, "original")
pca_sujo, r2 = pca_resumo(df_sujo, "com 3 linhas erradas")
pca_limpo, r3 = pca_resumo(df_sujo_limpo, "erradas removidas (3×IQR)")
for r, pc in ((r1, pca_ref), (r2, pca_sujo), (r3, pca_limpo)):
    r["cos_PC1_vs_original"] = abs(float(pca_ref.components_[0] @ pc.components_[0]))
print(pd.DataFrame([r1, r2, r3]).round(3).to_string(index=False))
print("\n(cos_PC1 = 1 significa mesma direção do PC1 da base original; menor que 1 = o outlier girou o eixo)")

# %% 10. PCA no fluxo supervisionado: sempre dentro de um Pipeline (evita vazamento de dados)
X_tr, X_te, y_tr, y_te = train_test_split(df, y, test_size=0.3, stratify=y, random_state=RANDOM_STATE)
modelos = {
    "Sem PCA (13 variáveis)": Pipeline([("pad", StandardScaler()),
                                        ("clf", LogisticRegression(max_iter=2000))]),
    "PCA com 2 componentes": Pipeline([("pad", StandardScaler()), ("pca", PCA(n_components=2)),
                                       ("clf", LogisticRegression(max_iter=2000))]),
    "PCA mantendo 95%": Pipeline([("pad", StandardScaler()), ("pca", PCA(n_components=0.95)),
                                  ("clf", LogisticRegression(max_iter=2000))]),
}
for nome, modelo in modelos.items():
    cv = cross_val_score(modelo, X_tr, y_tr, cv=5).mean()
    modelo.fit(X_tr, y_tr)
    n_comp = modelo.named_steps["pca"].n_components_ if "pca" in modelo.named_steps else p
    print(f"{nome:<26} componentes={n_comp:>2}  acurácia CV={cv:.3f}  teste={modelo.score(X_te, y_te):.3f}")
# O scaler e a PCA são ajustados SOMENTE no treino de cada dobra; o teste só é transformado.

# %% 11. Erro de reconstrução: quanto de informação se perde ao descartar componentes?
linhas = []
for k in (1, 2, 3, 5, 8, 13):
    pca_k = PCA(n_components=k).fit(Xp)
    Xr = pca_k.inverse_transform(pca_k.transform(Xp))
    erro_total_por_linha = np.mean(np.sum((Xp - Xr) ** 2, axis=1))
    descartado = pca_full.explained_variance_[k:].sum() * (len(Xp) - 1) / len(Xp)
    linhas.append({"componentes": k, "var_mantida_%": pca_k.explained_variance_ratio_.sum() * 100,
                   "erro_reconstrucao": erro_total_por_linha, "soma_autovalores_descartados": descartado})
print(pd.DataFrame(linhas).round(3).to_string(index=False))
print("\nErro de reconstrução = soma dos autovalores descartados (as duas últimas colunas coincidem).")
