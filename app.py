from pathlib import Path

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CONFIGURAÇÃO
# =========================

st.set_page_config(
    page_title="FarmTech Solutions",
    page_icon="🌱",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

ARQUIVO_DADOS = BASE_DIR / "data" / "dados_agricolas.csv"
ARQUIVO_MODELO = BASE_DIR / "models" / "modelo_produtividade.pkl"

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
# TÍTULO
# =========================

st.title("🌱 FarmTech Solutions")
st.subheader("Assistente Agrícola Inteligente")

st.markdown("---")

# =========================
# MÉTRICAS GERAIS
# =========================

st.header(" Visão Geral dos Dados")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Registros",
    len(df)
)

col2.metric(
    "Umidade Média",
    f"{df['umidade'].mean():.1f}%"
)

col3.metric(
    "Produtividade Média",
    f"{df['produtividade'].mean():.1f}"
)

st.dataframe(df.head())

# =========================
# ESTATÍSTICAS
# =========================

st.header(" Estatísticas Descritivas")

st.dataframe(df.describe())

# =========================
# CORRELAÇÃO
# =========================

st.header(" Correlação entre Variáveis")

corr = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(10, 6))

sns.heatmap(
    corr,
    annot=True,
    cmap="YlGnBu",
    ax=ax
)

st.pyplot(fig)

# =========================
# GRÁFICO PRODUTIVIDADE
# =========================

st.header(" Distribuição da Produtividade")

st.line_chart(df["produtividade"])

# =========================
# MÉTRICAS DO MODELO
# =========================

st.header(" Desempenho do Modelo")

st.info("""
As métricas abaixo devem ser obtidas durante o treinamento
e apresentadas na demonstração do projeto.

• MAE (Erro Médio Absoluto)

• MSE (Erro Médio Quadrático)

• RMSE (Raiz do Erro Médio Quadrático)

• R² (Coeficiente de Determinação)
""")

# =========================
# PREVISÃO
# =========================

st.header(" Previsão de Produtividade")

col1, col2 = st.columns(2)

with col1:

    umidade = st.slider(
        "Umidade (%)",
        20,
        60,
        40
    )

    ph = st.slider(
        "pH",
        5.5,
        7.5,
        6.5
    )

    temperatura = st.slider(
        "Temperatura (°C)",
        20,
        35,
        28
    )

with col2:

    irrigacao = st.slider(
        "Irrigação",
        5,
        20,
        10
    )

    fertilizante = st.slider(
        "Fertilizante",
        2,
        10,
        5
    )

if st.button("Realizar Previsão"):

    entrada = [[
        umidade,
        ph,
        temperatura,
        irrigacao,
        fertilizante
    ]]

    previsao = modelo.predict(entrada)

    st.success(
        f" Produtividade Prevista: {previsao[0]:.2f}"
    )

    st.header(" Recomendações Agrícolas")

    recomendacoes = False

    if umidade < 35:
        st.warning(
            "Aumentar a irrigação para melhorar a umidade do solo."
        )
        recomendacoes = True

    if ph < 6:
        st.warning(
            "Aplicar correção de solo para elevar o pH."
        )
        recomendacoes = True

    elif ph > 7:
        st.warning(
            "Verificar nutrientes devido ao pH elevado."
        )
        recomendacoes = True

    if fertilizante < 4:
        st.warning(
            "Aumentar a fertilização da cultura."
        )
        recomendacoes = True

    if temperatura > 32:
        st.warning(
            "Monitorar o estresse térmico da plantação."
        )
        recomendacoes = True

    if not recomendacoes:
        st.success(
            " As condições atuais são favoráveis para a cultura."
        )

# =========================
# RODAPÉ
# =========================

st.markdown("---")

st.caption(
    "Projeto FarmTech Solutions | Machine Learning aplicado ao Agronegócio"
)