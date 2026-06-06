from data_generator import data_generator
from treinar_modelo import treinar_modelo

while True:
    print("\n===== FARMTECH SOLUTIONS =====")
    print("1 - Gerar dados agrícolas")
    print("2 - Treinar modelo")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        data_generator()
        print("Dados gerados com sucesso!")

    elif opcao == "2":
        treinar_modelo()
        print("Modelo treinado com sucesso!")

    elif opcao == "3":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")