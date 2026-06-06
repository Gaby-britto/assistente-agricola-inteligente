from pathlib import Path
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def treinar_modelo():

    BASE_DIR = Path(__file__).resolve().parent.parent

    ARQUIVO_DADOS = BASE_DIR / "data" / "dados_agricolas.csv"
    MODELO_PATH = BASE_DIR / "models" / "modelo_produtividade.pkl"

    MODELO_PATH.parent.mkdir(parents=True, exist_ok=True)

    # =========================
    # CARREGAR DADOS
    # =========================

    df = pd.read_csv(ARQUIVO_DADOS)

    # =========================
    # VARIÁVEIS DE ENTRADA
    # =========================

    X = df[
        [
            "umidade",
            "pH",
            "temperatura",
            "irrigacao",
            "fertilizante"
        ]
    ]

    # =========================
    # VARIÁVEL ALVO
    # =========================

    y = df["produtividade"]

    # =========================
    # TREINO E TESTE
    # =========================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # =========================
    # TREINAMENTO
    # =========================

    modelo = LinearRegression()

    modelo.fit(X_train, y_train)

    # =========================
    # PREVISÕES
    # =========================

    y_pred = modelo.predict(X_test)

    # =========================
    # MÉTRICAS
    # =========================

    mae = mean_absolute_error(y_test, y_pred)

    mse = mean_squared_error(y_test, y_pred)

    rmse = mse ** 0.5

    r2 = r2_score(y_test, y_pred)

    # =========================
    # RESULTADOS
    # =========================

    print("\n===== RESULTADOS =====")
    print(f"MAE:  {mae:.2f}")
    print(f"MSE:  {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²:   {r2:.4f}")

    # =========================
    # SALVAR MODELO
    # =========================

    joblib.dump(modelo, MODELO_PATH)

    print(f"\nModelo salvo em: {MODELO_PATH}")