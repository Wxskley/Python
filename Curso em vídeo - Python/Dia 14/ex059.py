# Função para exibir o menu
def exibir_menu():
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")


# Função para realizar a soma
def somar(num1, num2):
    return num1 + num2


# Função para realizar a multiplicação
def multiplicar(num1, num2):
    return num1 * num2


# Função para obter o maior número
def obter_maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Programa principal
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

opcao = 0
while opcao != 5:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        resultado = somar(numero1, numero2)
        print("A soma dos números é:", resultado)
    elif opcao == 2:
        resultado = multiplicar(numero1, numero2)
        print("A multiplicação dos números é:", resultado)
    elif opcao == 3:
        maior = obter_maior(numero1, numero2)
        print("O maior número é:", maior)
    elif opcao == 4:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    elif opcao == 5:
        print("Programa encerrado.")
    else:
        print("Opção inválida. Digite novamente.")
