#!/usr/bin/env python3
"""
Gerador do site da Graduação em IA (FMU).

Lê os .md / .ipynb das pastas Semestre_N do repositório e gera as páginas HTML
na pasta site/ (onde este script está).

Uso (na raiz do repositório ou dentro de site/):
    pip install markdown-it-py mdit-py-plugins pygments
    python site/build_site.py

Para incluir uma nova disciplina ou aula, edite apenas o bloco CONFIG abaixo
e rode o script de novo. As páginas são regeneradas por completo.
"""

import html
import json
import re
from pathlib import Path
from urllib.parse import quote

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.util import ClassNotFound

SITE = Path(__file__).resolve().parent
RAIZ = SITE.parent
REPO_GITHUB = "https://github.com/Dani-Emiliano/FMU_Graduacao_IA"

# =====================================================================
# CONFIG — fonte única de semestres, disciplinas, aulas e materiais
# Caminhos relativos à raiz do repositório.
# status: "concluida" | "andamento" | "futura"
# =====================================================================
D1 = "Semestre_1/1-AQUISICAO E PREPARACAO DE DADOS (262GGR6046A)"
D2 = "Semestre_1/2 - AprendizadoSupervisionado"
D3 = "Semestre_1/3 - Aprendizado não supervisionado"

CONFIG = {
    "semestres": [
        {
            "n": 1,
            "status": "andamento",
            "titulo": "Fundamentos de dados e aprendizado de máquina",
            "descricao": (
                "O semestre cobre o ciclo inicial de dados para IA: obter e integrar dados de "
                "fontes diversas, prepará-los e explorá-los, e aplicar os primeiros modelos de "
                "aprendizado supervisionado e não supervisionado."
            ),
            "capacidades_tecnicas": [
                "Obter e integrar dados de fontes heterogêneas (dados abertos e conectados, ETL e Data Warehouse)",
                "Preparar dados: limpeza, normalização e padronização, valores ausentes e outliers",
                "Conduzir análise exploratória (AED) e análise multivariada com visualização adequada",
                "Reduzir dimensionalidade com PCA e agrupar dados sem rótulo com k-means",
                "Construir e avaliar um classificador de texto supervisionado (Naïve Bayes) em Python",
            ],
            "capacidades_aplicacao": [
                "Conectar a análise de dados à gestão de desempenho (BPM, BSC e Six Sigma)",
                "Avaliar o papel do self-service analytics e da governança no uso dos dados",
                "Base para os próximos semestres: todo modelo de IA depende de dados bem tratados",
            ],
        },
        {"n": 2, "status": "futura", "titulo": "", "descricao": ""},
        {"n": 3, "status": "futura", "titulo": "", "descricao": ""},
        {"n": 4, "status": "futura", "titulo": "", "descricao": ""},
        {"n": 5, "status": "futura", "titulo": "", "descricao": ""},
    ],
    "disciplinas": [
        # ---------------------------------------------------------- D1
        {
            "id": "s1-d1",
            "semestre": 1,
            "ordem": 1,
            "nome": "Aquisição e Preparação de Dados",
            "codigo": "262GGR6046A",
            "status": "concluida",
            "nota": "9,6",
            "icone": "dados",
            "pasta": D1,
            "descricao": (
                "Como os dados são obtidos, integrados e preparados para análise: dados abertos e "
                "conectados na web, processos ETL para Data Warehouse, normalização com Pandas, "
                "NumPy e scikit-learn e análise exploratória de dados."
            ),
            "conceitos": ["Dados abertos e dados conectados", "ETL, staging e Data Warehouse",
                          "Normalização (Min-Max, Z-Score, Robust Scaler)", "Análise exploratória (AED)"],
            "compilado": {"arquivo": f"{D1}/DISCIPLINA_AQUISICAO_PREPARACAO_DADOS.ipynb",
                          "titulo": "Compilação da disciplina"},
            # aulas dentro do compilado: link por título da seção
            "aulas": [
                {"n": 1, "tema": "Visão holística dos dados na internet", "secao": "AULA 1: VISÃO HOLÍSTICA DOS DADOS NA INTERNET",
                 "objetivos": ["Explicar o que são dados abertos e suas características", "Diferenciar dados conectados de dados abertos",
                               "Analisar o uso de dados conectados no desenvolvimento de sistemas"]},
                {"n": 2, "tema": "ETL: Extract, Transform and Load", "secao": "AULA 2: ETL — EXTRACT, TRANSFORM AND LOAD",
                 "objetivos": ["Conhecer o conceito de ETL", "Identificar as funções de extração, transformação e carga",
                               "Reconhecer objetivos e vantagens do ETL em Data Warehouse"]},
                {"n": 3, "tema": "Normalização de dados com Pandas, NumPy e scikit-learn", "secao": "AULA 3: NORMALIZAÇÃO DE DADOS COM PANDAS, NUMPY E SCIKIT-LEARN",
                 "objetivos": ["Identificar a necessidade de normalização", "Reconhecer o método de normalização adequado",
                               "Implementar rotinas com Pandas e NumPy"]},
                {"n": 4, "tema": "Análise exploratória de dados (AED)", "secao": "AULA 4: ANÁLISE EXPLORATÓRIA DE DADOS (AED)",
                 "objetivos": ["Definir o processo de análise exploratória", "Descrever as etapas de uma AED",
                               "Reconhecer objetivos e importância da AED"]},
            ],
            "labs": [],
            "atividades": [],
            "pdfs": [
                (f"{D1}/aquisicao e preparação de dados-cap1.pdf", "Cap. 1 · Aquisição e preparação de dados"),
                (f"{D1}/ETL-cap2.pdf", "Cap. 2 · ETL"),
                (f"{D1}/Preparação e analise exploratorio - cap 3.pdf", "Cap. 3 · Preparação e análise exploratória"),
                (f"{D1}/Análise exploratória de dados - cap 4.pdf", "Cap. 4 · Análise exploratória de dados"),
            ],
            "imagens": [],
        },
        # ---------------------------------------------------------- D2
        {
            "id": "s1-d2",
            "semestre": 1,
            "ordem": 2,
            "nome": "Aprendizado de Máquina Supervisionado",
            "codigo": "262GGR4728A",
            "status": "concluida",
            "nota": "8,8",
            "icone": "alvo",
            "pasta": D2,
            "descricao": (
                "Introdução ao aprendizado de máquina e suas aplicações, passando pela gestão de "
                "desempenho de negócios (BPM) até a classificação de textos com PLN, com a "
                "implementação completa de um classificador Naïve Bayes em Python."
            ),
            "conceitos": ["Tipos de aprendizado e principais algoritmos", "BPM, BSC e Six Sigma",
                          "Pipeline de classificação de textos (PLN)", "Naïve Bayes e métricas de avaliação"],
            "compilado": {"arquivo": f"{D2}/Disciplina/DISCIPLINA_APRENDIZADO_MAQUINA_SUPERVISIONADO.md",
                          "titulo": "Compilação da disciplina"},
            "aulas": [
                {"n": 1, "tema": "Aprendizado de máquina (Machine Learning)", "arquivo": f"{D2}/Aulas/AULA_01_RESUMO_APRENDIZADO_DE_MAQUINA.md",
                 "objetivos": ["Definir aprendizado de máquina", "Descrever algoritmos de aprendizado de máquina", "Listar aplicações"]},
                {"n": 2, "tema": "Business Performance Management (BPM)", "arquivo": f"{D2}/Aulas/AULA_02_RESUMO_BPM.md",
                 "objetivos": ["Explicar estratégia, plano e monitoramento", "Aplicar medidas de desempenho", "Analisar metodologias de BPM"]},
                {"n": 3, "tema": "Classificação de textos: introdução ao aprendizado supervisionado", "arquivo": f"{D2}/Aulas/AULA_03_RESUMO_CLASSIFICACAO_DE_TEXTOS.md",
                 "objetivos": ["Definir a área de machine learning", "Descrever aplicações de ML na classificação de textos",
                               "Identificar os elementos de uma solução de classificação de textos"]},
                {"n": 4, "tema": "Classificação de textos com Python", "arquivo": f"{D2}/Aulas/AULA_04_RESUMO_CLASSIFICACAO_TEXTO_PYTHON.md",
                 "objetivos": ["Descrever a manipulação de dados para classificadores de texto", "Analisar o classificador Naïve Bayes",
                               "Aplicar o Naïve Bayes em um estudo prático"]},
            ],
            "labs": [
                {"slug": "aula-04-pratico", "titulo": "Aula 4 · Código prático (classificação de texto)",
                 "arquivo": f"{D2}/Aulas/AULA_04_CLASSIFICACAO_TEXTO_PYTHON_PRATICO.md", "extras": []},
                {"slug": "aula-04-lab-vscode", "titulo": "Aula 4 · Laboratório guiado no VS Code",
                 "arquivo": f"{D2}/Aulas/AULA_04_LABORATORIO_VSCODE.md", "extras": []},
            ],
            "atividades": [
                {"slug": "atividade-03", "titulo": "Atividade 3", "arquivo": f"{D2}/Atividades/Aprendizadosupervisionado_atividade3.md"},
            ],
            "pdfs": [
                (f"{D2}/Livros_Capitulos/AULA_01_Aprendizado_de_Maquina_(Big_Data_e_IoT_-_Izabelly_Soares_de_Morais).pdf", "Aula 1 · Aprendizado de Máquina (I. S. de Morais)"),
                (f"{D2}/Livros_Capitulos/AULA_02_BPM_(Inteligencia_de_Negocios_-_Aline_Zanin).pdf", "Aula 2 · BPM (A. Zanin)"),
                (f"{D2}/Livros_Capitulos/AULA_03_Classificacao_de_Textos_Intro_(PLN_-_Michel_B_F_da_Silva).pdf", "Aula 3 · Classificação de textos (M. B. F. da Silva)"),
                (f"{D2}/Livros_Capitulos/AULA_04_Classificacao_de_Textos_Python_(PLN_-_Juliano_Vieira_Martins).pdf", "Aula 4 · Classificação de textos em Python (J. V. Martins)"),
            ],
            "imagens": [],
        },
        # ---------------------------------------------------------- D3
        {
            "id": "s1-d3",
            "semestre": 1,
            "ordem": 3,
            "nome": "Aprendizado de Máquina Não Supervisionado",
            "codigo": "262GGR6044A",
            "status": "concluida",
            "nota": "9,4",
            "icone": "clusters",
            "pasta": D3,
            "descricao": (
                "Da qualidade dos dados à descoberta de padrões sem rótulo: fundamentos de IA, ML e "
                "Deep Learning, análise multivariada e agrupamento com k-means, redução de "
                "dimensionalidade com PCA, tratamento de outliers e self-service analytics."
            ),
            "conceitos": ["Qualidade e limpeza de dados", "Análise multivariada e k-means",
                          "PCA e outliers (IQR, box-plot, Mahalanobis)", "AED e self-service analytics"],
            "compilado": {"arquivo": f"{D3}/DISCIPLINA_APRENDIZADO_MAQUINA_NAO_SUPERVISIONADO.md",
                          "titulo": "Compilação da disciplina"},
            "aulas": [
                {"n": 1, "tema": "Qualidade de dados, IA, Machine Learning e Deep Learning", "arquivo": f"{D3}/1_Resumos_das_aulas/AULA_01_RESUMO_LIMPEZA_DADOS_ML_DL.md",
                 "objetivos": ["Comparar mitos e verdades sobre IA", "Relacionar engenharia do conhecimento e sistemas inteligentes",
                               "Reconhecer tecnologias e ferramentas para aplicações inteligentes"]},
                {"n": 2, "tema": "Análise multivariada e agrupamento (k-means)", "arquivo": f"{D3}/1_Resumos_das_aulas/AULA_02_RESUMO_ANALISE_MULTIVARIADA_KMEANS.md",
                 "objetivos": ["Conceituar a análise multivariada", "Descrever as formas de condução",
                               "Identificar o tipo de visualização e suas variáveis"]},
                {"n": 3, "tema": "PCA e tratamento de outliers", "arquivo": f"{D3}/1_Resumos_das_aulas/AULA_03_RESUMO_PCA_OUTLIERS.md",
                 "objetivos": ["Conceituar a PCA, sua metodologia e aplicações em ML",
                               "Identificar outliers por IQR e box-plot e decidir sobre a remoção"]},
                {"n": 4, "tema": "AED (revisão) e self-service analytics", "arquivo": f"{D3}/1_Resumos_das_aulas/AULA_04_RESUMO_AED_SELF_SERVICE.md",
                 "objetivos": ["Definir a AED, suas etapas e importância",
                               "Reconhecer o papel do autoatendimento e apontar estratégias"]},
            ],
            "labs": [
                {"slug": "aula-03-lab-vscode", "titulo": "Aula 3 · Laboratório outliers e PCA no VS Code",
                 "arquivo": f"{D3}/2_Laboratorios/aula03_vscode/HOWTO_AULA_03_OUTLIERS_PCA_VSCODE.md",
                 "extras": [f"{D3}/2_Laboratorios/aula03_vscode/aula03_outliers_pca.py",
                            f"{D3}/2_Laboratorios/aula03_vscode/pca_exemplo_imoveis.py",
                            f"{D3}/2_Laboratorios/aula03_vscode/requirements.txt"],
                 "imagens": [
                     (f"{D3}/2_Laboratorios/aula03_vscode/saidas_exemplo/00_intuicao_pca_2d.png", "Intuição da PCA em 2D"),
                     (f"{D3}/2_Laboratorios/aula03_vscode/saidas_exemplo/01_boxplots.png", "Box-plots"),
                     (f"{D3}/2_Laboratorios/aula03_vscode/saidas_exemplo/02_scree_variancia.png", "Scree plot · variância"),
                     (f"{D3}/2_Laboratorios/aula03_vscode/saidas_exemplo/03_pc1_pc2_biplot.png", "Biplot PC1 × PC2"),
                 ]},
            ],
            "atividades": [],
            "pdfs": [
                (f"{D3}/3_Capitulos_de_livro/AULA_01_Engenharia_do_conhecimento_e_IA.pdf", "Aula 1 · Engenharia do conhecimento e IA"),
                (f"{D3}/3_Capitulos_de_livro/AULA_02_Unidade_2_Analise_multivariada_e_kmeans.pdf", "Aula 2 · Análise multivariada e k-means"),
                (f"{D3}/3_Capitulos_de_livro/AULA_03_Unidade_3_PCA_e_outliers.pdf", "Aula 3 · PCA e outliers"),
                (f"{D3}/3_Capitulos_de_livro/AULA_03_Capitulo_Tratando_outliers_Pandas_Numpy.pdf", "Aula 3 · Tratando outliers com Pandas e NumPy"),
                (f"{D3}/3_Capitulos_de_livro/AULA_04_Unidade_4_AED_e_self_service.pdf", "Aula 4 · AED e self-service"),
            ],
            "imagens": [
                (f"{D3}/4_Anexos/AULA_01_Infografico_Deep_Learning_e_RNA.png", "Aula 1 · Deep Learning e RNA"),
                (f"{D3}/4_Anexos/AULA_01_Infografico_Dificuldades_da_limpeza_de_dados.png", "Aula 1 · Dificuldades da limpeza de dados"),
                (f"{D3}/4_Anexos/AULA_03_Infografico_PCA_x_Analise_Fatorial.png", "Aula 3 · PCA × Análise Fatorial"),
            ],
        },
    ],
}

STATUS_TXT = {"concluida": "Concluída", "andamento": "Em andamento", "futura": "Futuro"}

# =====================================================================
# Utilitários
# =====================================================================
e = html.escape


def slug_github(texto: str) -> str:
    """Mesmo padrão de âncoras do GitHub (mantém acentos), para os índices dos .md funcionarem."""
    s = texto.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def url_repo(caminho: str) -> str:
    """URL relativa (a partir de site/) para um arquivo do repositório."""
    return "../" + "/".join(quote(p) for p in caminho.split("/"))


def nome_pagina_disc(d):   return f"{d['id']}.html"
def nome_pagina_doc(d, s): return f"{d['id']}-{s}.html"
def nome_pagina_sem(n):    return f"semestre-{n}.html"


def disciplinas_do_semestre(n):
    return sorted([d for d in CONFIG["disciplinas"] if d["semestre"] == n], key=lambda d: d["ordem"])


# ---------- Markdown → HTML ----------
_fmt = HtmlFormatter(nowrap=False, cssclass="highlight")


def _realce(codigo, lang, _attrs):
    try:
        lexer = get_lexer_by_name(lang) if lang else guess_lexer(codigo)
    except ClassNotFound:
        lexer = get_lexer_by_name("text")
    return highlight(codigo, lexer, _fmt)


def _md():
    md = (MarkdownIt("commonmark", {"html": True, "breaks": True, "linkify": False, "typographer": False, "highlight": _realce})
          .enable("table").enable("strikethrough"))
    md.use(anchors_plugin, min_level=1, max_level=4, slug_func=slug_github, permalink=False)
    return md


MAPA_MD = {}  # caminho do .md no repositório -> página gerada (preenchido em montar_mapa)


def ajustar_links(html_str: str, origem: str) -> str:
    """Reescreve href/src relativos do .md para funcionarem a partir de site/."""
    base = Path(origem).parent

    def troca(m):
        attr, alvo = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#|data:)", alvo):
            return m.group(0)
        caminho, _, ancora = alvo.partition("#")
        from urllib.parse import unquote
        resolvido = (RAIZ / base / unquote(caminho)).resolve()
        try:
            rel = resolvido.relative_to(RAIZ).as_posix()
        except ValueError:
            return m.group(0)
        if rel in MAPA_MD:
            novo = MAPA_MD[rel] + (f"#{ancora}" if ancora else "")
        else:
            novo = url_repo(rel) + (f"#{ancora}" if ancora else "")
        return f'{attr}="{novo}"'

    return re.sub(r'(href|src)="([^"]+)"', troca, html_str)


def seccionar(corpo: str) -> str:
    """Quebra o texto em blocos: cada h1 vira uma abertura de capítulo e cada h2 um bloco próprio."""
    partes = re.split(r'(?=<h[12][ >])', corpo)
    limpa = lambda t: re.sub(r'^\s*(<hr\s*/?>\s*)+|(\s*<hr\s*/?>)+\s*$', '', t)
    saida, aberto = [], False
    for p in partes:
        if not p.strip():
            continue
        if p.startswith('<h1'):
            if aberto:
                saida.append('</section>'); aberto = False
            fim = p.index('</h1>') + 5
            saida.append(f'<div class="capitulo">{p[:fim]}</div>')
            resto = limpa(p[fim:])
            if resto.strip():
                saida.append(f'<div class="abertura">{resto}</div>')
        elif p.startswith('<h2'):
            if aberto:
                saida.append('</section>')
            saida.append(f'<section class="bloco">{limpa(p)}'); aberto = True
        else:
            saida.append(limpa(p))
    if aberto:
        saida.append('</section>')
    return "\n".join(saida)


def renderizar(caminho: str):
    """Retorna (html, sumario[(nivel, texto, id)]) para .md ou .ipynb."""
    arq = RAIZ / caminho
    if arq.suffix == ".ipynb":
        nb = json.loads(arq.read_text(encoding="utf-8"))
        partes = []
        for c in nb["cells"]:
            src = "".join(c["source"])
            if c["cell_type"] == "markdown":
                partes.append(src)
            elif c["cell_type"] == "code":
                partes.append(f"```python\n{src}\n```")
        texto = "\n\n".join(partes)
    else:
        texto = arq.read_text(encoding="utf-8")

    md = _md()
    tokens = md.parse(texto)
    sumario = []
    for i, t in enumerate(tokens):
        if t.type == "heading_open" and t.tag in ("h1", "h2", "h3"):
            inline = tokens[i + 1]
            txt = re.sub(r"[*_`]", "", inline.content)
            sumario.append((int(t.tag[1]), txt, t.attrs.get("id", "")))
    corpo = md.renderer.render(tokens, md.options, {})
    return seccionar(ajustar_links(corpo, caminho)), sumario


# =====================================================================
# Layout
# =====================================================================
ICONES = {
    "indice": '<svg class="ico" viewBox="0 0 24 24"><rect x="4" y="3" width="16" height="18" rx="3"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
    "pasta": '<svg class="ico" viewBox="0 0 24 24"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>',
    "livro": '<svg class="ico" viewBox="0 0 24 24"><path d="M4 19V5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zm0 0a2 2 0 0 0 2 2h13"/></svg>',
    "codigo": '<svg class="ico" viewBox="0 0 24 24"><path d="M9 8l-4 4 4 4M15 8l4 4-4 4"/></svg>',
    "pdf": '<svg class="ico" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>',
    "seta": '<svg class="ico" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg>',
    "voltar": '<svg class="ico" viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></svg>',
    "lua": '<svg class="ico lua" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    "sol": '<svg class="ico sol" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
}

# Ícones ilustrativos por disciplina (use a chave "icone" no CONFIG)
ICONES_DISC = {
    "dados": '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="7" ry="2.6"/><path d="M5 5v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6V5"/><path d="M5 11v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6v-6"/></svg>',
    "alvo": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.4"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/></svg>',
    "clusters": '<svg viewBox="0 0 24 24"><circle cx="7" cy="8" r="4.5" stroke-dasharray="2 2"/><circle cx="16.5" cy="15.5" r="5" stroke-dasharray="2 2"/><circle cx="6" cy="7" r="1"/><circle cx="8.5" cy="9.2" r="1"/><circle cx="15" cy="14.5" r="1"/><circle cx="18" cy="16.5" r="1"/><circle cx="16" cy="18" r="1"/></svg>',
    "padrao": '<svg viewBox="0 0 24 24"><path d="M4 19V5M4 19h16"/><path d="M7 15l4-4 3 3 5-6"/></svg>',
}


def ico_disc(d, grande=False):
    svg = ICONES_DISC.get(d.get("icone", "padrao"), ICONES_DISC["padrao"])
    return f'<span class="disc-ico{" g" if grande else ""}" aria-hidden="true">{svg}</span>'


def anel_nota(nota, grande=False):
    if not nota:
        return ""
    try:
        v = float(nota.replace(",", ".")) * 10
    except ValueError:
        return ""
    rot = '<small>nota final</small>' if grande else ""
    return f'<span class="anel{" g" if grande else ""}" style="--v:{v:.0f}" title="Nota final {e(nota)}"><span>{e(nota)}{rot}</span></span>'


def rede_neural_svg():
    """Ilustração animada de uma rede neural (camadas → conexões com pulsos)."""
    camadas = [(70, 3), (160, 5), (250, 5), (340, 2)]
    nos = []
    for x, n in camadas:
        passo = 64
        y0 = 200 - passo * (n - 1) / 2
        nos.append([(x, y0 + i * passo) for i in range(n)])
    lig, pulsos = [], []
    k = 0
    for a, b in zip(nos, nos[1:]):
        for (x1, y1) in a:
            for (x2, y2) in b:
                lig.append(f'<line class="lig" x1="{x1}" y1="{y1:.0f}" x2="{x2}" y2="{y2:.0f}"/>')
                if k % 3 == 0:
                    pulsos.append(f'<line class="pulso" x1="{x1}" y1="{y1:.0f}" x2="{x2}" y2="{y2:.0f}" '
                                  f'style="animation-delay:-{(k * 0.37) % 3.4:.2f}s"/>')
                k += 1
    circ = []
    j = 0
    for camada in nos:
        for (x, y) in camada:
            d = f"animation-delay:-{(j * 0.41) % 2.8:.2f}s"
            circ.append(f'<circle class="halo" cx="{x}" cy="{y:.0f}" r="14" style="{d}"/>'
                        f'<circle class="no" cx="{x}" cy="{y:.0f}" r="11"/>'
                        f'<circle class="no-c" cx="{x}" cy="{y:.0f}" r="5" style="{d}"/>')
            j += 1
    return f"""<svg class="rede" viewBox="0 0 410 400" role="img" aria-label="Ilustração de uma rede neural">
  <defs><linearGradient id="gradPulso" x1="0" x2="1"><stop offset="0" stop-color="#ffb75e" stop-opacity="0"/><stop offset="1" stop-color="#ff7a45"/></linearGradient></defs>
  <circle class="orbita" cx="205" cy="200" r="190"/>
  <circle class="orbita" cx="205" cy="200" r="150" style="animation-direction:reverse"/>
  {''.join(lig)}{''.join(pulsos)}{''.join(circ)}
</svg>"""


def cabecalho(ativo=""):
    def item(href, txt, chave):
        cur = ' aria-current="page"' if chave == ativo else ""
        return f'<a href="{href}"{cur}>{txt}</a>'
    return f"""
<header class="topo">
  <div class="container">
    <a class="marca" href="index.html"><span class="logo">IA</span><span><strong>Graduação em IA</strong><small>FMU · Base de conhecimento</small></span></a>
    <nav class="nav" aria-label="Navegação principal">
      {item("index.html", "Home", "home")}
      {item("index.html#semestres", "Semestres", "semestres")}
      <a class="btn-indice" href="index.html#indice" title="Índice de disciplinas por semestre">{ICONES["indice"]}<span>Índice</span></a>
    </nav>
  </div>
</header>"""


def rodape(extra=""):
    return f"""
<footer class="rodape">
  <div class="container">
    <span>Graduação em Inteligência Artificial · FMU</span>
    <span>{extra}</span>
  </div>
</footer>"""


def pagina(titulo, corpo, ativo="", leitura=False):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(titulo)}</title>
  <script>try{{var t=localStorage.getItem('tema');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
<!-- Página gerada por build_site.py. Edite o CONFIG do script ou os .md de origem. -->
{'<div class="barra-leitura" aria-hidden="true"></div>' if leitura else ''}
{cabecalho(ativo)}
{corpo}
<script src="site.js"></script>
</body>
</html>
"""


def trilha(*itens):
    partes = []
    for href, txt in itens:
        partes.append(f'<a href="{href}">{e(txt)}</a>' if href else f"<span>{e(txt)}</span>")
    return '<nav class="trilha" aria-label="Você está em">' + " <span>›</span> ".join(partes) + "</nav>"


def status_chip(st):
    return f'<span class="status {st}">{STATUS_TXT[st]}</span>'


# =====================================================================
# Páginas
# =====================================================================
def tabela_indice():
    linhas = []
    for s in CONFIG["semestres"]:
        discs = disciplinas_do_semestre(s["n"])
        if not discs:
            linhas.append(f'<tr><td class="sem">S{s["n"]}</td><td class="cod">—</td>'
                          f'<td class="futuro">A definir</td><td>{status_chip("futura")}</td></tr>')
        for d in discs:
            linhas.append(f'<tr><td class="sem">S{s["n"]}</td><td class="cod">{e(d["codigo"])}</td>'
                          f'<td><a href="{nome_pagina_disc(d)}">{e(d["nome"])}</a></td><td>{status_chip(d["status"])}</td></tr>')
    return "\n".join(linhas)


def media_notas():
    vs = []
    for d in CONFIG["disciplinas"]:
        try:
            vs.append(float(d.get("nota", "").replace(",", ".")))
        except ValueError:
            pass
    return f"{sum(vs) / len(vs):.1f}".replace(".", ",") if vs else "—"


def gerar_index():
    discs = CONFIG["disciplinas"]
    n_aulas = sum(len(d["aulas"]) for d in discs)
    n_labs = sum(len(d["labs"]) for d in discs)

    # jornada dos semestres
    etapas = []
    ultimo_ativo = 0
    for s in CONFIG["semestres"]:
        ds = disciplinas_do_semestre(s["n"])
        ativo = bool(ds)
        if ativo:
            ultimo_ativo = s["n"]
        tag = "a" if ativo else "div"
        href = f' href="{nome_pagina_sem(s["n"])}"' if ativo else ""
        sub = f'{len(ds)} disciplina{"s" if len(ds) != 1 else ""}' if ativo else "Em breve"
        etapas.append(f"""
      <{tag} class="etapa {'on' if ativo else 'off'}"{href}>
        <span class="marco">S{s["n"]}</span>
        <span><h3>Semestre {s["n"]}</h3><p>{e(s["titulo"] or sub)}</p>{status_chip(s["status"])}</span>
      </{tag}>""")
    prog = max(4, (ultimo_ativo - 0.5) / len(CONFIG["semestres"]) * 80)

    # cards das disciplinas em andamento/recentes
    cards = "".join(f"""
      <a class="card" href="{nome_pagina_disc(d)}">
        <div class="topo-card">{ico_disc(d)}</div>
        <h3>{e(d["nome"])}</h3>
        <span class="sub">Semestre {d["semestre"]} · {e(d["codigo"])}</span>
        <p>{e(d["descricao"])}</p>
        <div class="rodape-card">{status_chip(d["status"])}<span>Abrir {ICONES["seta"]}</span></div>
      </a>""" for d in discs)

    corpo = f"""
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">FMU · Graduação em Inteligência Artificial</span>
      <h1>Minha base de conhecimento em <em>Inteligência Artificial</em></h1>
      <p class="lead">
        Este material reúne, de forma organizada e acumulativa, os conteúdos da graduação em Inteligência
        Artificial da FMU. É construído aula a aula, a partir dos materiais acadêmicos, das minhas
        anotações e de complementos, para manter acesso contínuo aos aprendizados sempre que forem
        necessários no futuro.
      </p>
      <div class="acoes">
        <a class="btn cheio" href="#semestres">Explorar semestres {ICONES["seta"]}</a>
        <a class="btn contorno" href="#indice">{ICONES["indice"]} Índice de disciplinas</a>
      </div>
    </div>
    <div class="hero-arte">{rede_neural_svg()}</div>
  </div>
  <div class="container">
    <div class="stats">
      <div class="stat"><b>{len(discs)}</b><span>disciplinas documentadas</span></div>
      <div class="stat"><b>{n_aulas}</b><span>aulas resumidas</span></div>
      <div class="stat"><b>{n_labs}</b><span>laboratórios práticos</span></div>
    </div>
  </div>
</section>

<section class="secao" id="semestres">
  <div class="container">
    <div class="secao-titulo"><h2>Jornada do curso</h2><small>5 semestres</small></div>
    <div class="jornada" style="--prog:{prog:.0f}%">{"".join(etapas)}
    </div>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="secao-titulo"><h2>Disciplinas</h2><small>{len(discs)} até agora</small></div>
    <div class="grade">{cards}
    </div>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="secao-titulo"><h2>Como este material é construído</h2></div>
    <div class="grade">
      <div class="card spot"><span class="num">01</span><h3>Material acadêmico</h3><p>Conteúdo da FMU e dos professores: capítulos, slides, videoaulas e atividades.</p></div>
      <div class="card spot"><span class="num">02</span><h3>Minhas observações</h3><p>Interpretações, dúvidas e aplicações profissionais, separadas do conteúdo oficial.</p></div>
      <div class="card spot"><span class="num">03</span><h3>Complementação</h3><p>Explicações e pesquisas externas, sempre identificadas como complementares.</p></div>
      <div class="card spot"><span class="num">04</span><h3>Prática</h3><p>Códigos, laboratórios e notebooks mantidos no repositório do curso.</p></div>
    </div>
  </div>
</section>
{rodape()}

<div class="indice" id="indice" role="dialog" aria-modal="true" aria-labelledby="indice-titulo">
  <div class="indice-caixa">
    <div class="indice-cab"><h2 id="indice-titulo">Índice de disciplinas</h2></div>
    <p class="indice-legenda">Todas as disciplinas do curso, por semestre.</p>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Semestre</th><th>Código</th><th>Disciplina</th><th>Status</th></tr></thead>
        <tbody>
{tabela_indice()}
        </tbody>
      </table>
    </div>
    <div class="indice-rodape"><a class="btn cheio" href="#">Fechar</a></div>
  </div>
</div>"""
    (SITE / "index.html").write_text(pagina("Graduação em IA · FMU", corpo, "home"), encoding="utf-8")


def gerar_semestre(s):
    discs = disciplinas_do_semestre(s["n"])
    if not discs:
        return
    feitas = sum(1 for d in discs if d["status"] == "concluida")
    pct = round(100 * feitas / len(discs))
    cards = "".join(f"""
      <a class="card" href="{nome_pagina_disc(d)}">
        <div class="topo-card">{ico_disc(d)}</div>
        <h3>{e(d["nome"])}</h3>
        <span class="sub">Disciplina {d["ordem"]} · {e(d["codigo"])} · {len(d["aulas"])} aulas</span>
        <p>{e(d["descricao"])}</p>
        <div class="rodape-card">{status_chip(d["status"])}<span>Abrir {ICONES["seta"]}</span></div>
      </a>""" for d in discs)
    li = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)
    corpo = f"""
<section class="hero">
  <div class="container">
    {trilha(("index.html", "Home"), (None, f"Semestre {s['n']}"))}
    <span class="eyebrow">Semestre {s["n"]}</span>
    <h1>{e(s["titulo"])}</h1>
    <p class="lead">{e(s["descricao"])}</p>
    <div class="progresso">
      <div class="trilho"><div class="barra" style="width:{pct}%"></div></div>
      <span>{feitas} de {len(discs)} disciplinas concluídas</span>
    </div>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="secao-titulo"><h2>Disciplinas</h2><small>{len(discs)} no semestre</small></div>
    <div class="grade">{cards}
    </div>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="secao-titulo"><h2>Capacidades desenvolvidas</h2></div>
    <div class="duas-col">
      <div class="painel"><h3>Competências técnicas</h3><ul class="lista">{li(s.get("capacidades_tecnicas", []))}</ul></div>
      <div class="painel"><h3>Aplicações e conexões</h3><ul class="lista">{li(s.get("capacidades_aplicacao", []))}</ul>
        <p class="origem">Síntese elaborada a partir dos objetivos e conteúdos das disciplinas do semestre.</p></div>
    </div>
  </div>
</section>
{rodape(f'<a href="index.html">← Home</a> · ')}"""
    (SITE / nome_pagina_sem(s["n"])).write_text(
        pagina(f"Semestre {s['n']} · Graduação em IA", corpo, "semestres"), encoding="utf-8")


def gerar_doc(d, slug, titulo, arquivo, eyebrow, anterior=None, proximo=None, extras=(), imagens=()):
    corpo_md, sumario = renderizar(arquivo)
    itens_sum = "".join(f'<li class="n{n}"><a href="#{i}">{e(t)}</a></li>' for n, t, i in sumario if i)

    bloco_extras = ""
    if extras:
        blocos = []
        for x in extras:
            p = RAIZ / x
            if not p.exists():
                continue
            lang = "python" if p.suffix == ".py" else "text"
            blocos.append(f'<h3 id="arq-{slug_github(p.stem)}">{e(p.name)}</h3>'
                          + _realce(p.read_text(encoding="utf-8"), lang, None))
        if blocos:
            bloco_extras = '<h2 id="arquivos-do-laboratorio">Arquivos do laboratório</h2>' + "".join(blocos)
            itens_sum += '<li class="n2"><a href="#arquivos-do-laboratorio">Arquivos do laboratório</a></li>'
    if imagens:
        gal = "".join(f'<a href="{url_repo(c)}" target="_blank"><img src="{url_repo(c)}" alt="{e(t)}" loading="lazy"><span>{e(t)}</span></a>'
                      for c, t in imagens)
        bloco_extras += f'<h2 id="saidas-de-exemplo">Saídas de exemplo</h2><div class="galeria">{gal}</div>'
        itens_sum += '<li class="n2"><a href="#saidas-de-exemplo">Saídas de exemplo</a></li>'

    nav = ""
    if anterior or proximo:
        a = f'<a class="btn contorno" href="{anterior[0]}">{ICONES["voltar"]} {e(anterior[1])}</a>' if anterior else "<span></span>"
        p = f'<a class="btn cheio" href="{proximo[0]}">{e(proximo[1])} {ICONES["seta"]}</a>' if proximo else ""
        nav = f'<div class="doc-nav">{a}{p}</div>'

    corpo = f"""
<section class="hero compacto">
  <div class="container">
    {trilha(("index.html", "Home"), (nome_pagina_sem(d["semestre"]), f"Semestre {d['semestre']}"),
            (nome_pagina_disc(d), d["nome"]), (None, titulo))}
    <span class="eyebrow">{e(eyebrow)} · {e(d["nome"])}</span>
    <h1>{e(titulo)}</h1>
    <div class="meta">
      <a class="chip" href="{nome_pagina_disc(d)}">{ICONES["voltar"]} Voltar à disciplina</a>
    </div>
  </div>
</section>
<div class="container leitura">
  <details class="sumario" open>
    <summary>Nesta página</summary>
    <ol>{itens_sum}</ol>
  </details>
  <article class="prosa">
{corpo_md}
{bloco_extras}
{nav}
  </article>
</div>
{rodape(f'<a href="{nome_pagina_disc(d)}">← {e(d["nome"])}</a> · ')}"""
    (SITE / nome_pagina_doc(d, slug)).write_text(
        pagina(f"{titulo} · {d['nome']}", corpo, leitura=True), encoding="utf-8")


def gerar_disciplina(d):
    comp = d["compilado"]
    pag_comp = nome_pagina_doc(d, "compilado")
    aulas_arq = [a for a in d["aulas"] if a.get("arquivo")]

    gerar_doc(d, "compilado", "Compilação da disciplina", comp["arquivo"], "Compilação")
    for idx, a in enumerate(aulas_arq):
        ant = aulas_arq[idx - 1] if idx > 0 else None
        prox = aulas_arq[idx + 1] if idx + 1 < len(aulas_arq) else None
        gerar_doc(d, f'aula-{a["n"]:02d}', f'Aula {a["n"]} · {a["tema"]}', a["arquivo"], f'Aula {a["n"]}',
                  anterior=(nome_pagina_doc(d, f'aula-{ant["n"]:02d}'), f'Aula {ant["n"]}') if ant else None,
                  proximo=(nome_pagina_doc(d, f'aula-{prox["n"]:02d}'), f'Aula {prox["n"]}') if prox else None)
    for lab in d["labs"]:
        gerar_doc(d, lab["slug"], lab["titulo"], lab["arquivo"], "Laboratório",
                  extras=lab.get("extras", []), imagens=lab.get("imagens", []))
    for at in d["atividades"]:
        gerar_doc(d, at["slug"], at["titulo"], at["arquivo"], "Atividade")

    itens = []
    for a in d["aulas"]:
        if a.get("arquivo"):
            href, meta = nome_pagina_doc(d, f'aula-{a["n"]:02d}'), "Resumo completo da aula"
        else:
            href, meta = f'{pag_comp}#{slug_github(a["secao"])}', "Seção da compilação"
        cls = "aula feita" if d["status"] == "concluida" else "aula"
        itens.append(f"""
        <a class="{cls}" href="{href}">
          <span class="check" aria-hidden="true"></span>
          <span class="txt"><span class="n-aula">Aula {a["n"]}</span><strong>{e(a["tema"])}</strong><span class="meta-aula">{meta}</span></span>
          {ICONES["seta"]}
        </a>""")

    praticas = "".join(f'<a class="arquivo" href="{nome_pagina_doc(d, l["slug"])}">{ICONES["codigo"]}{e(l["titulo"])}<small>Lab</small></a>' for l in d["labs"])
    praticas += "".join(f'<a class="arquivo" href="{nome_pagina_doc(d, x["slug"])}">{ICONES["livro"]}{e(x["titulo"])}<small>Atividade</small></a>' for x in d["atividades"])
    pdfs = "".join(f'<a class="arquivo" href="{url_repo(c)}" target="_blank">{ICONES["pdf"]}{e(t)}<small>PDF</small></a>' for c, t in d["pdfs"])
    gal = "".join(f'<a href="{url_repo(c)}" target="_blank"><img src="{url_repo(c)}" alt="{e(t)}" loading="lazy"><span>{e(t)}</span></a>' for c, t in d["imagens"])
    objetivos = "".join(
        f'<div class="painel"><h3>Aula {a["n"]} · {e(a["tema"])}</h3><ul class="lista">'
        + "".join(f"<li>{e(o)}</li>" for o in a.get("objetivos", [])) + "</ul></div>"
        for a in d["aulas"])
    feitas = len(d["aulas"]) if d["status"] == "concluida" else 0

    corpo = f"""
<section class="hero">
  <div class="container hero-grid">
    <div>
      {trilha(("index.html", "Home"), (nome_pagina_sem(d["semestre"]), f"Semestre {d['semestre']}"), (None, d["nome"]))}
      <span class="eyebrow">Semestre {d["semestre"]} · Disciplina {d["ordem"]} · {e(d["codigo"])}</span>
      <h1>{e(d["nome"])}</h1>
      <p class="lead">{e(d["descricao"])}</p>
      <div class="meta">{"".join(f'<span class="chip conceito">{e(c)}</span>' for c in d["conceitos"])}</div>
      <div class="acoes">
        <a class="btn cheio" href="{pag_comp}">{ICONES["livro"]} Ler a compilação completa</a>
      </div>
    </div>
    <div class="hero-disc">{ico_disc(d, grande=True)}</div>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="secao-titulo"><h2>Aulas</h2><small>{feitas} de {len(d["aulas"])} concluídas · {STATUS_TXT[d["status"]]}</small></div>
    <div class="aulas">{"".join(itens)}
    </div>
  </div>
</section>

{f'''<section class="secao"><div class="container"><div class="secao-titulo"><h2>Laboratórios e atividades</h2></div><div class="arquivos">{praticas}</div></div></section>''' if praticas else ""}

<section class="secao">
  <div class="container">
    <div class="secao-titulo"><h2>Objetivos de aprendizagem</h2><small>material acadêmico</small></div>
    <div class="duas-col">{objetivos}</div>
  </div>
</section>

{f'''<section class="secao"><div class="container"><div class="secao-titulo"><h2>Infográficos e anexos</h2></div><div class="galeria">{gal}</div></div></section>''' if gal else ""}

<section class="secao">
  <div class="container">
    <div class="secao-titulo"><h2>Capítulos e livros-base</h2></div>
    <div class="arquivos">{pdfs}</div>
  </div>
</section>
{rodape(f'<a href="{nome_pagina_sem(d["semestre"])}">← Semestre {d["semestre"]}</a> · ')}"""
    (SITE / nome_pagina_disc(d)).write_text(pagina(f"{d['nome']} · Graduação em IA", corpo), encoding="utf-8")


def montar_mapa():
    for d in CONFIG["disciplinas"]:
        MAPA_MD[d["compilado"]["arquivo"]] = nome_pagina_doc(d, "compilado")
        for a in d["aulas"]:
            if a.get("arquivo"):
                MAPA_MD[a["arquivo"]] = nome_pagina_doc(d, f'aula-{a["n"]:02d}')
        for l in d["labs"]:
            MAPA_MD[l["arquivo"]] = nome_pagina_doc(d, l["slug"])
        for x in d["atividades"]:
            MAPA_MD[x["arquivo"]] = nome_pagina_doc(d, x["slug"])
        MAPA_MD[d["pasta"]] = nome_pagina_disc(d)


def main():
    montar_mapa()
    faltando = [p for p in MAPA_MD if not (RAIZ / p).exists()]
    for p in faltando:
        print(f"[aviso] não encontrado: {p}")
    gerar_index()
    for s in CONFIG["semestres"]:
        gerar_semestre(s)
    for d in CONFIG["disciplinas"]:
        gerar_disciplina(d)
    print(f"Site gerado em {SITE}")


if __name__ == "__main__":
    main()
