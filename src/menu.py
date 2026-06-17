import os

from data_generator import data_generator
from treinar_modelo import treinar_modelo
from database import criar_banco


while True:

    print("\n" + "=" * 50)
    print("🌱 FARMTECH SOLUTIONS")
    print("Assistente Agrícola Inteligente")
    print("=" * 50)

    print("\n1 - Criar Banco de Dados")
    print("2 - Gerar Dados Agrícolas")
    print("3 - Treinar Modelo de IA")
    print("4 - Abrir Dashboard")
    print("5 - Executar Projeto Completo")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        criar_banco()

        print("\n Banco criado com sucesso!")

    elif opcao == "2":

        data_generator()

        print("\n Dados agrícolas gerados com sucesso!")

    elif opcao == "3":

        treinar_modelo()

        print("\n Modelo treinado com sucesso!")

    elif opcao == "4":

        print("\n Abrindo Dashboard...")

        os.system("streamlit run app.py")

    elif opcao == "5":

        print("\n Executando pipeline completo...\n")

        criar_banco()

        data_generator()

        treinar_modelo()

        print("\n Abrindo Dashboard...")

        os.system("streamlit run app.py")

    elif opcao == "6":

        print("\n Encerrando sistema...")

        break

    else:

        print("\n Opção inválida!")
