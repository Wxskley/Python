# Algoritmo de Ordenação por Inserção
# Este algoritmo ordena uma lista de números em ordem crescente.


def ordenacao_insercao(lista):
    # Itera sobre a lista a partir do segundo elemento
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        # Move os elementos maiores que a chave para a direita
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        # Insere a chave na posição correta
        lista[j + 1] = chave

    return lista


# Exemplo de uso:
numeros = [5, 2, 8, 3, 1]
numeros_ordenados = ordenacao_insercao(numeros)
print(numeros_ordenados)
