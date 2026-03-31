    # Cria o laco de repeticao
while True:
    try:
        # Solicita os dois numeros
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        # Apresenta as operacoes disponiveis

        print("Escolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisao")

        # Solicita a operacao de 1 a 4

        op = int(input("Digite a operacao desejada: "))

        # Faz os caulos com if ou elif

        if op == 1:
            resultado = n1 + n2
            print("O resultado da soma é:", resultado)

        elif op == 2:
            resultado = n1 - n2
            print("O resultado da Subtração é:", resultado)

        if op == 3:
            resultado = n1 * n2
            print("O resultado da Multiplicação é:", resultado)

        elif op == 4:
            resultado = n1 / n2
            print("O resultado da Divisao é:", resultado)



        # Pergunta se quer continuar calculando ou encerrar a calculadora

        print("Deseja fazer outro calculo? ")
        print("1 - Sim")
        print("2 - Nao")
        continuar = int(input("Digite a opcao desejada: "))
        if continuar == 2:
            print("Encerrando a calculadora... Até logo!")
            break

    except ValueError:
        print("\n⚠️ Opção inválida! Por favor, digite apenas números.")
        continue # Isso faz o programa voltar para o começo do laço em vez de fechar