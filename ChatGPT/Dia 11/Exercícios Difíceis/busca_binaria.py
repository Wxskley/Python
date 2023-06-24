# Algoritmo de Busca Binária
# Este algoritmo realiza uma busca eficiente em uma lista ordenada.


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


# Exemplo de uso:
numeros = [1, 3, 5, 7, 9, 11, 13]
indice = busca_binaria(numeros, 9)
print(indice)
