import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "dados_agricolas.db"


def criar_banco():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        umidade REAL NOT NULL,
        pH REAL NOT NULL,
        temperatura REAL NOT NULL,
        irrigacao REAL NOT NULL,
        fertilizante REAL NOT NULL,
        produtividade REAL NOT NULL,
        data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("Banco criado com sucesso.")


def inserir_dados(
    umidade,
    ph,
    temperatura,
    irrigacao,
    fertilizante,
    produtividade
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sensores(
        umidade,
        pH,
        temperatura,
        irrigacao,
        fertilizante,
        produtividade
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        umidade,
        ph,
        temperatura,
        irrigacao,
        fertilizante,
        produtividade
    ))

    conn.commit()
    conn.close()


def listar_dados():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM sensores
    ORDER BY id DESC
    LIMIT 10
    """)

    registros = cursor.fetchall()

    conn.close()

    return registros


if __name__ == "__main__":

    criar_banco()

    print("Últimos registros:")

    for registro in listar_dados():
        print(registro)