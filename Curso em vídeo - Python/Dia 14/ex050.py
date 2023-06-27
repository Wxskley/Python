soma = 0  # Variável para armazenar a soma dos números pares

for _ in range(6):  # Loop para ler os seis números
    numero = int(
        input("Digite um número inteiro: ")
    )  # Solicita ao usuário para digitar um número inteiro

    if numero % 2 == 0:  # Verifica se o número é par
        soma += numero  # Adiciona o número à soma apenas se for par

# Imprime a soma dos números pares
print("A soma dos números pares é:", soma)
