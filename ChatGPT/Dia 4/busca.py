def busca(lista, elemento):
    # Função para realizar busca em uma lista e retornar o índice do elemento encontrado

    for i in range(len(lista)):
        # Percorre os índices da lista usando a função range

        if lista[i] == elemento:
            # Verifica se o elemento na posição i é igual ao elemento buscado

            return i
            # Se o elemento for encontrado, retorna o índice

    return -1
    # Caso o elemento não seja encontrado, retorna -1


lista = [10, 20, 30, 40, 50]
# Lista de exemplo para realizar a busca

resultado_busca = busca(lista, 30)
# Chama a função de busca passando a lista e o elemento 30 como argumentos

print(resultado_busca)
# Exibe o resultado da busca (índice do elemento encontrado ou -1 se não encontrado)
