# Importamos a biblioteca deque do módulo collections
from collections import deque

# Criamos um grafo representado por um dicionário
graph = {
    "A": {"B", "C"},  # O vértice A tem conexões com os vértices B e C
    "B": {"A", "D", "E"},  # O vértice B tem conexões com os vértices A, D e E
    "C": {"A", "F"},  # O vértice C tem conexões com os vértices A e F
    "D": {"B"},  # O vértice D tem conexão com o vértice B
    "E": {"B", "F"},  # O vértice E tem conexões com os vértices B e F
    "F": {"C", "E"},  # O vértice F tem conexões com os vértices C e E
}


# Criamos uma função chamada bfs (busca em largura) para explorar o grafo
def bfs(graph, start):
    # Criamos um conjunto para armazenar os vértices visitados
    visited = set()
    # Criamos uma fila (deque) para armazenar os vértices a serem visitados
    queue = deque([start])

    # Enquanto a fila não estiver vazia
    while queue:
        # Retiramos o primeiro vértice da fila
        vertex = queue.popleft()

        # Se o vértice ainda não foi visitado
        if vertex not in visited:
            # Imprimimos o vértice para mostrar que estamos visitando ele
            print(vertex)
            # Adicionamos o vértice ao conjunto de vértices visitados
            visited.add(vertex)
            # Adicionamos todos os vizinhos não visitados do vértice à fila
            queue.extend(graph[vertex] - visited)


# Chamamos a função bfs passando o grafo e o vértice inicial "A"
bfs(graph, "A")
