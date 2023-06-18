# Solicita ao usuário que digite o valor inicial do intervalo
inicio = int(input("Digite o valor inicial do intervalo: "))

# Solicita ao usuário que digite o valor final do intervalo
fim = int(input("Digite o valor final do intervalo: "))

# Percorre todos os números dentro do intervalo informado, incluindo o valor de início e fim
for numero in range(inicio, fim + 1):
    # Inicializa a variável eh_primo como True para cada número
    eh_primo = True

    # Loop que verifica a divisibilidade do número por todos os valores entre 2 e o próprio número
    for i in range(2, numero):
        if numero % i == 0:  # Se o número for divisível por algum valor, não é primo
            eh_primo = False
            break

    # Se eh_primo for True, imprime o número como um número primo
    if eh_primo:
        print(numero, "é um número primo")
