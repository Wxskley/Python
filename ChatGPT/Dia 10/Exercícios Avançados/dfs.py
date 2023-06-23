# Vamos explorar um grafo usando a busca em profundidade (DFS)

# Primeiro, vamos criar um grafo usando um dicionário
graph = {
    "A": {"B", "C"},
    "B": {"A", "D", "E"},
    "C": {"A", "F"},
    "D": {"B"},
    "E": {"B", "F"},
    "F": {"C", "E"},
}


# Vamos implementar o algoritmo DFS
def dfs(graph, start, visited=None):
    # Vamos usar um conjunto para armazenar os vértices visitados
    if visited is None:
        visited = set()

    # Vamos imprimir o vértice atual e marcá-lo como visitado
    print(start)
    visited.add(start)

    # Vamos visitar todos os vizinhos não visitados recursivamente
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)


# Vamos começar a busca a partir do vértice 'A'
dfs(graph, "A")
