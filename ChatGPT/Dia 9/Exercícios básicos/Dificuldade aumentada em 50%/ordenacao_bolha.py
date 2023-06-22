# Função de ordenação pelo método da bolha
def ordenacao_bolha(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Lista de números desordenada
lista = [9, 5, 7, 1, 3, 2, 8, 6, 4]

# Ordena a lista pelo método da bolha
ordenacao_bolha(lista)

# Exibe a lista ordenada
print("Lista ordenada:", lista)
