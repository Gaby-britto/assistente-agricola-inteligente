from pathlib import Path
import csv
import random
import pandas as pd

from database import criar_banco, inserir_dados


def data_generator():

    BASE_DIR = Path(__file__).resolve().parent.parent

    ARQUIVO = BASE_DIR / "data" / "dados_agricolas.csv"

    ARQUIVO.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # cria o banco caso não exista
    criar_banco()

    with open(
        ARQUIVO,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "umidade",
            "pH",
            "temperatura",
            "irrigacao",
            "fertilizante",
            "produtividade"
        ])

        for _ in range(1000):

            umidade = random.randint(20, 60)

            ph = round(
                random.uniform(5.5, 7.5),
                2
            )

            temperatura = random.randint(20, 35)

            irrigacao = random.randint(5, 20)

            fertilizante = random.randint(2, 10)

            ruido = random.uniform(-5, 5)

            produtividade = (
                umidade * 0.5
                + irrigacao * 2
                + fertilizante * 1.5
                - abs(ph - 6.5) * 5
                - abs(temperatura - 28) * 1.2
                + ruido
            )

            produtividade = round(
                produtividade,
                2
            )

            # salva CSV
            writer.writerow([
                umidade,
                ph,
                temperatura,
                irrigacao,
                fertilizante,
                produtividade
            ])

            # salva SQLite
            inserir_dados(
                umidade,
                ph,
                temperatura,
                irrigacao,
                fertilizante,
                produtividade
            )

    df = pd.read_csv(ARQUIVO)

    print("\n===== DADOS GERADOS =====")

    print(f"Total de registros: {len(df)}")

    print("\nPrimeiras linhas:")

    print(df.head())

    print("\nCSV salvo com sucesso.")

    print("Dados inseridos no SQLite com sucesso.")

