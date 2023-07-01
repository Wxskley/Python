from random import randint

numeros = []  # Lista para armazenar os números sorteados


def sorteia():
    for _ in range(5):
        numeros.append(randint(1, 10))


def somaPar():
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma


# Chamada da função sorteia()
sorteia()

# Exibição da lista de números sorteados
print("Números sorteados:", numeros)

# Chamada da função somaPar()
resultado = somaPar()

# Exibição da soma dos números pares
print("Soma dos números pares:", resultado)
