from pathlib import Path
import pandas as pd
import joblib
import json

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

    METRICAS_PATH = BASE_DIR / "models" / "metricas.json"

    MODELO_PATH.parent.mkdir(parents=True, exist_ok=True)

    # =========================
    # CARREGAR DADOS
    # =========================

    df = pd.read_csv(ARQUIVO_DADOS)

    print("\n===================================")
    print(" INFORMAÇÕES DO DATASET")
    print("===================================")

    print(f"Quantidade de registros: {len(df)}")
    print(f"Quantidade de colunas: {len(df.columns)}")

    print("\nColunas:")
    print(df.columns.tolist())

    print("\nPrimeiras linhas:")
    print(df.head())

    print("\nEstatísticas:")
    print(df.describe())

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

    print("\n===================================")
    print(" DIVISÃO DOS DADOS")
    print("===================================")

    print(f"Treinamento: {len(X_train)} registros")
    print(f"Teste: {len(X_test)} registros")

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

    print("\n===================================")
    print(" RESULTADOS DO MODELO")
    print("===================================")

    print(f"MAE:  {mae:.2f}")
    print(f"MSE:  {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²:   {r2:.4f}")

    # =========================
    # IMPORTÂNCIA DAS VARIÁVEIS
    # =========================

    print("\n===================================")
    print(" IMPACTO DAS VARIÁVEIS")
    print("===================================")

    importancia = pd.DataFrame({
        "Variável": X.columns,
        "Coeficiente": modelo.coef_
    })

    importancia = importancia.sort_values(
        by="Coeficiente",
        ascending=False
    )

    print(importancia)

    # =========================
    # EXEMPLO DE PREVISÃO
    # =========================

    print("\n===================================")
    print(" EXEMPLO DE PREVISÃO")
    print("===================================")

    amostra = [[45, 6.5, 28, 10, 5]]

    previsao = modelo.predict(amostra)

    print(f"Produtividade prevista: {previsao[0]:.2f}")

    # =========================
    # SALVAR MÉTRICAS
    # =========================

    metricas = {
        "MAE": float(mae),
        "MSE": float(mse),
        "RMSE": float(rmse),
        "R2": float(r2),
        "registros_dataset": int(len(df)),
        "quantidade_variaveis": int(len(X.columns))
    }

    with open(METRICAS_PATH, "w", encoding="utf-8") as arquivo:
        json.dump(metricas, arquivo, indent=4)

    print(f"\nMétricas salvas em: {METRICAS_PATH}")

    # =========================
    # SALVAR MODELO
    # =========================

    joblib.dump(modelo, MODELO_PATH)

    print(f"\nModelo salvo em: {MODELO_PATH}")

    print("\n===================================")
    print(" TREINAMENTO FINALIZADO")
    print("===================================")

    print(
        "Modelo treinado com sucesso utilizando "
        "Regressão Linear do Scikit-Learn."
    )

    print(
        "O modelo está pronto para ser utilizado "
        "pelo dashboard Streamlit."
    )


if __name__ == "__main__":
    treinar_modelo()

