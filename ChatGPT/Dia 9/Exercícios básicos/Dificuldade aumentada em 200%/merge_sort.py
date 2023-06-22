def merge_sort(arr):
    # Função que implementa o algoritmo de ordenação Merge Sort
    # Recebe uma lista não ordenada como entrada e retorna a lista ordenada

    if len(arr) <= 1:
        # Caso base: se a lista tem tamanho 0 ou 1, ela já está ordenada
        return arr

    mid = len(arr) // 2
    # Divide a lista em duas partes, aproximadamente do mesmo tamanho
    left = merge_sort(arr[:mid])
    # Chama recursivamente o merge_sort na primeira metade da lista
    right = merge_sort(arr[mid:])
    # Chama recursivamente o merge_sort na segunda metade da lista

    return merge(left, right)
    # Retorna a chamada da função merge com as duas metades ordenadas


def merge(left, right):
    # Função auxiliar que mescla duas listas ordenadas em uma única lista ordenada
    # Recebe as listas left e right, que são as metades ordenadas da lista original

    merged = []
    # Lista vazia para armazenar os elementos mesclados
    i = j = 0
    # Variáveis para percorrer as listas left e right

    while i < len(left) and j < len(right):
        # Loop para comparar os elementos das duas listas e adicioná-los em ordem à lista merged
        if left[i] <= right[j]:
            # Se o elemento da lista left for menor ou igual ao elemento da lista right
            merged.append(left[i])
            # Adiciona o elemento da lista left à lista merged
            i += 1
            # Incrementa o índice i para avançar na lista left
        else:
            # Se o elemento da lista right for menor que o elemento da lista left
            merged.append(right[j])
            # Adiciona o elemento da lista right à lista merged
            j += 1
            # Incrementa o índice j para avançar na lista right

    while i < len(left):
        # Adiciona os elementos restantes da lista left à lista merged, se houver
        merged.append(left[i])
        i += 1

    while j < len(right):
        # Adiciona os elementos restantes da lista right à lista merged, se houver
        merged.append(right[j])
        j += 1

    return merged
    # Retorna a lista merged, que contém todos os elementos ordenados


# Exemplo de uso
lista = [4, 2, 9, 1, 7, 5, 3, 8, 6]
# Lista de números desordenados
lista_ordenada = merge_sort(lista)
# Chama a função merge_sort passando a lista como argumento e armazena o resultado na variável lista_ordenada
print(lista_ordenada)
# Imprime a lista ordenada na saída
