numeros = []  # Cria uma lista vazia para armazenar os números
pares = []  # Cria uma lista vazia para armazenar os números pares
impares = []  # Cria uma lista vazia para armazenar os números ímpares

while True:
    numero = int(
        input("Digite um número (digite 0 para parar): ")
    )  # Solicita ao usuário um número inteiro
    if numero == 0:  # Verifica se o número digitado é igual a 0
        break  # Encerra o loop se o número for igual a 0
    numeros.append(numero)  # Adiciona o número na lista

    if numero % 2 == 0:  # Verifica se o número é par
        pares.append(numero)  # Adiciona o número par na lista de pares
    else:
        impares.append(numero)  # Adiciona o número ímpar na lista de ímpares

print("Números digitados:", numeros)  # Exibe a lista com todos os números digitados
print("Números pares:", pares)  # Exibe a lista com os números pares
print("Números ímpares:", impares)  # Exibe a lista com os números ímpares
