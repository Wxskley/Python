# Algoritmo de Busca em Profundidade (DFS)
# Este algoritmo realiza uma busca em profundidade em um grafo.


def busca_profundidade(grafo, vertice_inicial):
    visitados = set()

    def dfs(vertice):
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs(vizinho)

    dfs(vertice_inicial)
    return visitados


# Exemplo de uso:
grafo = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": ["A"]}

vertice_inicial = "A"
vertices_visitados = busca_profundidade(grafo, vertice_inicial)
print(vertices_visitados)
