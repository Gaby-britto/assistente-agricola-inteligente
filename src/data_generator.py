from pathlib import Path
import csv
import random

def data_generator():

    BASE_DIR = Path(__file__).resolve().parent.parent
    ARQUIVO = BASE_DIR / "data" / "dados_agricolas.csv"

    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)

    with open(ARQUIVO, mode="w", newline="") as file:

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
            ph = round(random.uniform(5.5, 7.5), 2)
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

            writer.writerow([
                umidade,
                ph,
                temperatura,
                irrigacao,
                fertilizante,
                round(produtividade, 2)
            ])

    print(f"Dados gerados com sucesso em: {ARQUIVO}")