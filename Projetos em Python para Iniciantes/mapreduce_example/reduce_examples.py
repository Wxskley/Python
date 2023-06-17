from functools import reduce

# Lista de números
numbers = [1, 2, 3, 4, 5]


# Função de redução para somar dois valores
def reducer(acc, val):
    return acc + val


# Utiliza a função reduce para aplicar a função reducer aos elementos da lista numbers
# O valor inicial é 10, que será utilizado como o valor inicial do acumulador (acc)
# A função reducer será aplicada a cada elemento da lista, somando o elemento atual ao acumulador
# O resultado final será retornado
print(reduce(reducer, numbers, 10))
