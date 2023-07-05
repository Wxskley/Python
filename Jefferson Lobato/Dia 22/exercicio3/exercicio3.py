import matematico

continuar = ""
while True:
    continuar = input("Deseja calcular? s/n ")
    if continuar.lower() == "n":
        break
    else:
        operacao = int(
            input(
                "Qual operação deseja fazer?\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n"
            )
        )
        if operacao == 1:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            print(matematico.soma(a, b))
        elif operacao == 2:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            print(matematico.subtracao(a, b))
        elif operacao == 3:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            print(matematico.divisao(a, b))
        elif operacao == 4:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            print(matematico.multiplicacao(a, b))
        else:
            print("Digite uma opção válida.")
