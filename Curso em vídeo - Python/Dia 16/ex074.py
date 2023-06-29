import random

# Gera cinco números aleatórios e os coloca em uma tupla
numeros = tuple(random.randint(1, 100) for _ in range(5))

# Exibe a listagem dos números gerados
print("Números gerados:", numeros)

# Encontra o menor valor na tupla
menor_valor = min(numeros)

# Encontra o maior valor na tupla
maior_valor = max(numeros)

# Exibe o menor e o maior valor
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
