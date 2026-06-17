from pathlib import Path

import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import json



# =========================
# CONFIGURAÇÃO
# =========================

st.set_page_config(
    page_title="FarmTech Solutions",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent

ARQUIVO_DADOS = BASE_DIR / "data" / "dados_agricolas.csv"
ARQUIVO_MODELO = BASE_DIR / "models" / "modelo_produtividade.pkl"

# =========================
# ESTILOS GLOBAIS
# =========================

st.markdown("""
<style>
    /* ---- Reset & Base ---- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #0F172A;
        color: #E2E8F0;
    }

    /* ---- Scrollbar ---- */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #0F172A; }
    ::-webkit-scrollbar-thumb { background: #22C55E; border-radius: 3px; }

    /* ---- Sidebar ---- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0B3D2E 0%, #0a2e22 100%);
        border-right: 1px solid #1a4a37;
    }
    [data-testid="stSidebar"] * { color: #E2E8F0 !important; }
    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #22C55E !important;
    }

    /* ---- Main content padding ---- */
    .block-container {
        padding: 1.5rem 2rem 3rem 2rem;
        max-width: 1400px;
    }

    /* ---- Hide default header ---- */
    #MainMenu, footer, header { visibility: hidden; }

    /* ---- Hero Banner ---- */
    .hero-banner {
        background: linear-gradient(135deg, #0B3D2E 0%, #0d4a37 40%, #0F172A 100%);
        border: 1px solid #1e5c44;
        border-radius: 16px;
        padding: 2.5rem 3rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .hero-banner::before {
        content: "";
        position: absolute;
        top: -60px; right: -60px;
        width: 240px; height: 240px;
        background: radial-gradient(circle, rgba(34,197,94,0.12) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero-banner::after {
        content: "";
        position: absolute;
        bottom: -40px; left: 30%;
        width: 180px; height: 180px;
        background: radial-gradient(circle, rgba(34,197,94,0.07) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero-eyebrow {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #22C55E;
        margin-bottom: 0.6rem;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1.1;
        margin-bottom: 0.4rem;
    }
    .hero-title span { color: #22C55E; }
    .hero-subtitle {
        font-size: 1.05rem;
        font-weight: 500;
        color: #94A3B8;
        margin-bottom: 1rem;
    }
    .hero-desc {
        font-size: 0.88rem;
        color: #64748B;
        max-width: 600px;
        line-height: 1.65;
    }
    .hero-badges {
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
    }
    .hero-badge {
        background: rgba(34,197,94,0.12);
        border: 1px solid rgba(34,197,94,0.3);
        color: #22C55E;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        padding: 0.3rem 0.85rem;
        border-radius: 999px;
    }

    /* ---- Section Headers ---- */
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1.2rem;
        margin-top: 0.5rem;
    }
    .section-icon {
        width: 32px; height: 32px;
        background: rgba(34,197,94,0.15);
        border-radius: 8px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1rem;
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #F1F5F9;
        margin: 0;
    }
    .section-divider {
        border: none;
        border-top: 1px solid #1e293b;
        margin: 0.5rem 0 1.5rem 0;
    }

    /* ---- KPI Cards ---- */
    .kpi-card {
        background: linear-gradient(135deg, #111827 0%, #0f1f2e 100%);
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 1.4rem 1.6rem;
        position: relative;
        overflow: hidden;
        transition: border-color 0.2s;
    }
    .kpi-card:hover { border-color: #22C55E44; }
    .kpi-card-accent {
        position: absolute;
        top: 0; left: 0;
        width: 4px; height: 100%;
        border-radius: 14px 0 0 14px;
    }
    .kpi-icon {
        font-size: 1.5rem;
        margin-bottom: 0.75rem;
        display: block;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1;
        margin-bottom: 0.3rem;
    }
    .kpi-label {
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: #64748B;
    }
    .kpi-delta {
        font-size: 0.72rem;
        color: #22C55E;
        margin-top: 0.4rem;
        font-weight: 500;
    }

    /* ---- Metric Cards (AI) ---- */
    .metric-card {
        background: #111827;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        height: 100%;
    }
    .metric-card-title {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #22C55E;
        margin-bottom: 0.5rem;
    }
    .metric-card-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 0.25rem;
    }
    .metric-card-desc {
        font-size: 0.78rem;
        color: #64748B;
        line-height: 1.5;
    }

    /* ---- Dataset Table ---- */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #1e293b !important;
    }

    /* ---- Sliders ---- */
    [data-testid="stSlider"] > div > div > div {
        background: #22C55E !important;
    }
    .stSlider label { color: #94A3B8 !important; font-size: 0.85rem !important; }

    /* ---- Button ---- */
    .stButton > button {
        background: linear-gradient(135deg, #16a34a, #22C55E) !important;
        color: #0B3D2E !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.65rem 2.5rem !important;
        letter-spacing: 0.03em !important;
        transition: all 0.2s !important;
        box-shadow: 0 4px 14px rgba(34,197,94,0.3) !important;
    }
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(34,197,94,0.45) !important;
        transform: translateY(-1px) !important;
    }

    /* ---- Prediction Result Card ---- */
    .prediction-card {
        background: linear-gradient(135deg, #0B3D2E 0%, #0d4a37 100%);
        border: 1px solid #22C55E44;
        border-radius: 16px;
        padding: 2rem 2.5rem;
        text-align: center;
    }
    .prediction-label {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #22C55E;
        margin-bottom: 0.5rem;
    }
    .prediction-value {
        font-size: 3.5rem;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1;
        margin-bottom: 0.3rem;
    }
    .prediction-unit {
        font-size: 0.85rem;
        color: #94A3B8;
        font-weight: 500;
    }

    /* ---- Recommendation Cards ---- */
    .rec-card {
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.7rem;
        display: flex;
        align-items: flex-start;
        gap: 0.8rem;
        border-left: 4px solid;
    }
    .rec-card.success {
        background: rgba(34,197,94,0.08);
        border-color: #22C55E;
    }
    .rec-card.warning {
        background: rgba(234,179,8,0.08);
        border-color: #EAB308;
    }
    .rec-card.danger {
        background: rgba(239,68,68,0.08);
        border-color: #EF4444;
    }
    .rec-icon { font-size: 1.2rem; flex-shrink: 0; margin-top: 0.05rem; }
    .rec-text {
        font-size: 0.85rem;
        line-height: 1.55;
        color: #CBD5E1;
    }
    .rec-text strong { color: #F1F5F9; font-weight: 600; }

    /* ---- Simulator panel ---- */
    .sim-panel {
        background: #111827;
        border: 1px solid #1e293b;
        border-radius: 16px;
        padding: 1.5rem 1.8rem;
    }

    /* ---- Footer ---- */
    .ft-footer {
        border-top: 1px solid #1e293b;
        margin-top: 3rem;
        padding-top: 1.5rem;
        text-align: center;
        color: #334155;
        font-size: 0.78rem;
    }
    .ft-footer span { color: #22C55E; }
</style>
""", unsafe_allow_html=True)

# =========================
# CARREGAR DADOS
# =========================

try:
    df = pd.read_csv(ARQUIVO_DADOS)
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.stop()

try:
    modelo = joblib.load(ARQUIVO_MODELO)
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")
    st.stop()

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0 1.5rem 0;">
        <div style="font-size:2.8rem; margin-bottom:0.5rem;">🌱</div>
        <div style="font-size:1.1rem; font-weight:800; color:#22C55E;">FarmTech Solutions</div>
        <div style="font-size:0.72rem; color:#64748B; letter-spacing:0.1em; text-transform:uppercase; margin-top:0.2rem;">
            Plataforma Cognitiva Agrícola
        </div>
    </div>
    <hr style="border:none; border-top:1px solid #1e5c44; margin:0 0 1.5rem 0;">
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Objetivo")
    st.markdown("""
    <div style="font-size:0.83rem; color:#94A3B8; line-height:1.6;">
    Apoiar gestores agrícolas e executivos do agronegócio na tomada de decisão
    com base em dados históricos e modelos preditivos de Machine Learning.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🤖 Modelo de IA")
    st.markdown("""
    <div style="font-size:0.83rem; color:#94A3B8; line-height:1.7;">
    <b style="color:#22C55E;">Algoritmo:</b> Regressão Supervisionada<br>
    <b style="color:#22C55E;">Framework:</b> Scikit-learn<br>
    <b style="color:#22C55E;">Tarefa:</b> Predição de Produtividade<br>
    <b style="color:#22C55E;">Status:</b> <span style="color:#22C55E;">● Online</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🛠️ Tecnologias")
    techs = ["Python 3.x", "Streamlit", "Scikit-learn", "Pandas", "Plotly", "Joblib"]
    for t in techs:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem;">
            <div style="width:6px; height:6px; background:#22C55E; border-radius:50%;"></div>
            <span style="font-size:0.82rem; color:#94A3B8;">{t}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📊 Dataset")
    st.markdown(f"""
    <div style="font-size:0.83rem; color:#94A3B8; line-height:1.7;">
    <b style="color:#22C55E;">Registros:</b> {len(df):,}<br>
    <b style="color:#22C55E;">Variáveis:</b> {len(df.columns)}<br>
    <b style="color:#22C55E;">Features:</b> 5 inputs<br>
    <b style="color:#22C55E;">Target:</b> produtividade
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.72rem; color:#334155; text-align:center; padding-top:0.5rem;">
        v1.0 · FarmTech Solutions<br>Machine Learning no Agronegócio
    </div>
    """, unsafe_allow_html=True)

# =========================
# 1. HERO BANNER
# =========================

st.markdown("""
<div class="hero-banner">
    <div class="hero-eyebrow">🌾 Agricultura Cognitiva · IA & Machine Learning</div>
    <div class="hero-title">FarmTech <span>Solutions</span></div>
    <div class="hero-subtitle">Assistente Agrícola Inteligente</div>
    <div class="hero-desc">
        Plataforma de Agricultura Cognitiva utilizando Inteligência Artificial e Machine Learning
        para apoio à tomada de decisão agrícola e da análise de solo à previsão de produtividade.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# 2. KPI CARDS
# =========================

st.markdown("""
<div class="section-header">
    <span class="section-title">Indicadores Principais</span>
</div>
<hr class="section-divider">
""", unsafe_allow_html=True)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-card-accent" style="background:#22C55E;"></div>
        <span class="kpi-icon">📋</span>
        <div class="kpi-value">{len(df):,}</div>
        <div class="kpi-label">Total de Registros</div>
        <div class="kpi-delta">↑ Dataset completo</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-card-accent" style="background:#3B82F6;"></div>
        <span class="kpi-icon">💧</span>
        <div class="kpi-value">{df['umidade'].mean():.1f}<span style="font-size:1.2rem; color:#64748B;">%</span></div>
        <div class="kpi-label">Umidade Média</div>
        <div class="kpi-delta">↗ Solo monitorado</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-card-accent" style="background:#F59E0B;"></div>
        <span class="kpi-icon">🌾</span>
        <div class="kpi-value">{df['produtividade'].mean():.1f}</div>
        <div class="kpi-label">Produtividade Média</div>
        <div class="kpi-delta">↑ Referência atual</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    temp_col = "temperatura" if "temperatura" in df.columns else df.select_dtypes("number").columns[2]
    temp_val = df[temp_col].mean() if temp_col in df.columns else 0
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-card-accent" style="background:#EF4444;"></div>
        <span class="kpi-icon">🌡️</span>
        <div class="kpi-value">{temp_val:.1f}<span style="font-size:1.2rem; color:#64748B;">°C</span></div>
        <div class="kpi-label">Temperatura Média</div>
        <div class="kpi-delta">— Estável</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# 3. MÉTRICAS DO MODELO
# =========================

ARQUIVO_METRICAS = BASE_DIR / "models" / "metricas.json"

try:
    with open(ARQUIVO_METRICAS, "r", encoding="utf-8") as f:
        metricas = json.load(f)
except:
    metricas = {}

st.markdown("""
<div class="section-header">
    <span class="section-title">Desempenho do Modelo de IA</span>
</div>
<hr class="section-divider">
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

metrics_data = [
    (
        m1,
        "MAE",
        f"{metricas.get('MAE', 0):.2f}",
        "Erro Médio Absoluto",
        "Média dos erros absolutos entre valores previstos e reais. Quanto menor, melhor."
    ),

    (
        m2,
        "MSE",
        f"{metricas.get('MSE', 0):.2f}",
        "Erro Médio Quadrático",
        "Penaliza erros maiores ao elevar ao quadrado. Sensível a outliers."
    ),

    (
        m3,
        "RMSE",
        f"{metricas.get('RMSE', 0):.2f}",
        "Raiz do Erro Quadrático",
        "Versão interpretável do MSE, na mesma escala do target."
    ),

    (
        m4,
        "R²",
        f"{metricas.get('R2', 0):.4f}",
        "Coeficiente de Determinação",
        "Proporção da variância explicada. Ideal próximo de 1."
    )
]

for col, title, val, full, desc in metrics_data:
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-card-title">{title}</div>
            <div class="metric-card-value">{val}</div>
            <div style="font-size:0.8rem; color:#94A3B8; font-weight:600; margin-bottom:0.35rem;">{full}</div>
            <div class="metric-card-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# 4. GRÁFICOS ANALÍTICOS
# =========================

st.markdown("""
<div class="section-header">
    <span class="section-title">Análise Exploratória</span>
</div>
<hr class="section-divider">
""", unsafe_allow_html=True)

# Linha 1: Correlação + Scatter
col_hm, col_sc = st.columns([1.1, 0.9])

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(15,23,42,0.6)",
    font=dict(family="Inter", color="#94A3B8", size=11),
    margin=dict(l=10, r=10, t=40, b=10),
)

with col_hm:
    corr = df.corr(numeric_only=True)
    fig_hm = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns.tolist(),
        y=corr.index.tolist(),
        colorscale=[
            [0.0, "#0B3D2E"],
            [0.5, "#16653a"],
            [1.0, "#22C55E"],
        ],
        text=[[f"{v:.2f}" for v in row] for row in corr.values],
        texttemplate="%{text}",
        textfont=dict(size=10, color="#FFFFFF"),
        showscale=True,
        colorbar=dict(
            thickness=12,
            tickfont=dict(color="#94A3B8", size=10),
            outlinecolor="rgba(0,0,0,0)",
        ),
        zmin=-1, zmax=1,
    ))
    fig_hm.update_layout(
        **PLOTLY_LAYOUT,
        title=dict(text="Correlação entre Variáveis", font=dict(color="#F1F5F9", size=13, weight=700), x=0),
        height=360,
        xaxis=dict(tickfont=dict(color="#94A3B8"), gridcolor="rgba(0,0,0,0)"),
        yaxis=dict(tickfont=dict(color="#94A3B8"), gridcolor="rgba(0,0,0,0)"),
    )
    st.plotly_chart(fig_hm, use_container_width=True)

with col_sc:
    num_cols = df.select_dtypes("number").columns.tolist()
    x_col = "umidade" if "umidade" in num_cols else num_cols[0]
    y_col = "produtividade" if "produtividade" in num_cols else num_cols[-1]
    color_col = "temperatura" if "temperatura" in num_cols else (num_cols[2] if len(num_cols) > 2 else num_cols[0])

    fig_sc = px.scatter(
        df, x=x_col, y=y_col,
        color=color_col if color_col in df.columns else None,
        color_continuous_scale=["#0B3D2E", "#22C55E", "#F59E0B"],
        opacity=0.75,
        size_max=8,
    )
    fig_sc.update_traces(marker=dict(size=6, line=dict(width=0)))
    fig_sc.update_layout(
        **PLOTLY_LAYOUT,
        title=dict(text=f"{x_col.capitalize()} × Produtividade", font=dict(color="#F1F5F9", size=13, weight=700), x=0),
        height=360,
        xaxis=dict(title=dict(text=x_col.capitalize(), font=dict(color="#64748B")), gridcolor="#1e293b", zerolinecolor="#1e293b"),
        yaxis=dict(title=dict(text="Produtividade", font=dict(color="#64748B")), gridcolor="#1e293b", zerolinecolor="#1e293b"),
        coloraxis_colorbar=dict(thickness=12, tickfont=dict(color="#94A3B8", size=10), outlinecolor="rgba(0,0,0,0)"),
    )
    st.plotly_chart(fig_sc, use_container_width=True)

# Linha 2: Evolução da produtividade (largura total)
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(
    y=df["produtividade"],
    x=list(range(len(df))),
    mode="lines",
    name="Produtividade",
    line=dict(color="#22C55E", width=1.8),
    fill="tozeroy",
    fillcolor="rgba(34,197,94,0.07)",
))
fig_line.add_trace(go.Scatter(
    y=[df["produtividade"].mean()] * len(df),
    x=list(range(len(df))),
    mode="lines",
    name="Média",
    line=dict(color="#F59E0B", width=1.5, dash="dot"),
))
fig_line.update_layout(
    **PLOTLY_LAYOUT,
    title=dict(text="Evolução da Produtividade ao Longo dos Registros", font=dict(color="#F1F5F9", size=13, weight=700), x=0),
    height=280,
    xaxis=dict(title=dict(text="Registro", font=dict(color="#64748B")), gridcolor="#1e293b", zerolinecolor="#1e293b"),
    yaxis=dict(title=dict(text="Produtividade", font=dict(color="#64748B")), gridcolor="#1e293b", zerolinecolor="#1e293b"),
    legend=dict(font=dict(color="#94A3B8"), bgcolor="rgba(0,0,0,0)", bordercolor="rgba(0,0,0,0)"),
    hovermode="x unified",
)
st.plotly_chart(fig_line, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# 5. DATASET
# =========================

st.markdown("""
<div class="section-header">
    <span class="section-title">Base de Dados</span>
</div>
<hr class="section-divider">
""", unsafe_allow_html=True)

tab_preview, tab_stats = st.tabs([" Amostra dos Dados", " Estatísticas Descritivas"])

with tab_preview:
    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=False,
    )

with tab_stats:
    st.dataframe(
        df.describe().round(3),
        use_container_width=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# 6. SIMULADOR DE IA
# =========================

st.markdown("""
<div class="section-header">
    <span class="section-title">Simulador de Produtividade — IA</span>
</div>
<hr class="section-divider">
""", unsafe_allow_html=True)



col_sliders, col_result = st.columns([1.1, 0.9], gap="large")

with col_sliders:
    st.markdown("<div style='font-size:0.8rem; font-weight:600; color:#64748B; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:1rem;'>Parâmetros de Entrada</div>", unsafe_allow_html=True)

    umidade = st.slider(" Umidade do Solo (%)", 20, 60, 40)
    ph = st.slider(" pH do Solo", 5.5, 7.5, 6.5)
    temperatura = st.slider(" Temperatura (°C)", 20, 35, 28)
    irrigacao = st.slider(" Irrigação (mm)", 5, 20, 10)
    fertilizante = st.slider(" Fertilizante (kg/ha)", 2, 10, 5)

    predict_btn = st.button(" Executar Previsão de IA", use_container_width=True)

with col_result:
    st.markdown("<div style='font-size:0.8rem; font-weight:600; color:#64748B; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:1rem;'>Resultado do Modelo</div>", unsafe_allow_html=True)

    if predict_btn:
        entrada = [[umidade, ph, temperatura, irrigacao, fertilizante]]
        previsao = modelo.predict(entrada)

        st.markdown(f"""
        <div class="prediction-card">
            <div class="prediction-label"> Resultado da IA · Previsão</div>
            <div class="prediction-value">{previsao[0]:.2f}</div>
            <div class="prediction-unit">Produtividade estimada (unid.)</div>
        </div>
        """, unsafe_allow_html=True)

        st.session_state["previsao_realizada"] = True
        st.session_state["ultima_previsao"] = {
            "umidade": umidade, "ph": ph, "temperatura": temperatura,
            "irrigacao": irrigacao, "fertilizante": fertilizante,
            "resultado": previsao[0]
        }
    else:
        st.markdown("""
        <div style="
            background: rgba(34,197,94,0.04);
            border: 1px dashed #1e5c44;
            border-radius: 16px;
            padding: 2.5rem 2rem;
            text-align: center;
            color: #334155;
        ">
            <div style="font-size:0.88rem; color:#475569; line-height:1.6;">
                Ajuste os parâmetros ao lado<br>e clique em <b style="color:#22C55E;">Executar Previsão</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# 7. RECOMENDAÇÕES
# =========================

if st.session_state.get("previsao_realizada") and "ultima_previsao" in st.session_state:
    params = st.session_state["ultima_previsao"]
    umidade = params["umidade"]
    ph = params["ph"]
    temperatura = params["temperatura"]
    irrigacao = params["irrigacao"]
    fertilizante = params["fertilizante"]

    st.markdown("""
    <div class="section-header">
        <div class="section-icon"></div>
        <span class="section-title">Recomendações Agronômicas</span>
    </div>
    <hr class="section-divider">
    """, unsafe_allow_html=True)

    recomendacoes = []

    if umidade < 35:
        recomendacoes.append(("warning", "⚠️", "<strong>Umidade baixa detectada.</strong> Aumentar a irrigação para melhorar a umidade do solo. Considere sistema de gotejamento nas próximas 48h."))

    if ph < 6:
        recomendacoes.append(("danger", "🔴", "<strong>pH abaixo do ideal.</strong> Aplicar calagem para elevar o pH. Solo ácido reduz a disponibilidade de nutrientes essenciais."))
    elif ph > 7:
        recomendacoes.append(("warning", "⚠️", "<strong>pH elevado.</strong> Verificar disponibilidade de micronutrientes. pH alto pode causar deficiência de ferro e manganês."))

    if fertilizante < 4:
        recomendacoes.append(("danger", "🔴", "<strong>Fertilização insuficiente.</strong> Aumentar a aplicação de fertilizantes. Nível atual está abaixo do mínimo recomendado para a cultura."))

    if temperatura > 32:
        recomendacoes.append(("warning", "⚠️", "<strong>Estresse térmico identificado.</strong> Monitorar o desenvolvimento vegetativo. Temperaturas acima de 32°C podem reduzir a produtividade em até 15%."))

    if not recomendacoes:
        recomendacoes.append(("success", "✅", "<strong>Condições ideais.</strong> Todos os parâmetros estão dentro das faixas otimizadas para a cultura. Mantenha o monitoramento periódico."))

    rec_cols = st.columns(min(len(recomendacoes), 2))
    for i, (tipo, icon, texto) in enumerate(recomendacoes):
        with rec_cols[i % len(rec_cols)]:
            st.markdown(f"""
            <div class="rec-card {tipo}">
                <span class="rec-icon">{icon}</span>
                <div class="rec-text">{texto}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

# =========================
# 8. RODAPÉ
# =========================

st.markdown("""
<div class="ft-footer">
    <span>FarmTech Solutions</span> · Machine Learning aplicado ao Agronegócio ·
    Plataforma de Agricultura Cognitiva com IA
</div>
""", unsafe_allow_html=True)