numeros = []  # Cria uma lista vazia para armazenar os números

# Loop para ler os números digitados pelo usuário
while True:
    numero = int(
        input("Digite um número (digite 0 para parar): ")
    )  # Solicita ao usuário um número inteiro
    if numero == 0:  # Verifica se o número digitado é igual a 0
        break  # Encerra o loop se o número for igual a 0
    numeros.append(numero)  # Adiciona o número na lista

print(
    f"Foram digitados {len(numeros)} números."
)  # Exibe a quantidade de números digitados
numeros.sort(reverse=True)  # Ordena a lista em ordem decrescente
print(
    f"Números digitados em ordem decrescente: {numeros}"
)  # Exibe os números em ordem decrescente

if 5 in numeros:  # Verifica se o número 5 está presente na lista
    print(
        "O valor 5 foi digitado e está na lista."
    )  # Exibe mensagem informando que o número 5 está na lista
else:
    print(
        "O valor 5 não foi digitado ou não está na lista."
    )  # Exibe mensagem informando que o número 5 não está na lista
