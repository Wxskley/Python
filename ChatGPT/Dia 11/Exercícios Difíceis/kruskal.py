# Algoritmo de Kruskal para Árvore Geradora Mínima
# Este algoritmo constrói uma árvore geradora mínima em um grafo ponderado.


def encontrar(pai, i):
    if pai[i] == i:
        return i
    return encontrar(pai, pai[i])


def unir(pai, rank, vertice1, vertice2):
    raiz1 = encontrar(pai, vertice1)
    raiz2 = encontrar(pai, vertice2)

    if rank[raiz1] < rank[raiz2]:
        pai[raiz1] = raiz2
    elif rank[raiz1] > rank[raiz2]:
        pai[raiz2] = raiz1
    else:
        pai[raiz2] = raiz1
        rank[raiz1] += 1


def kruskal(grafo):
    arvore_minima = []
    vertices = sorted(grafo.keys(), key=lambda x: grafo[x][2])
    pai = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    for vertice in vertices:
        v1, v2, peso = grafo[vertice]
        raiz1 = encontrar(pai, v1)
        raiz2 = encontrar(pai, v2)

        if raiz1 != raiz2:
            arvore_minima.append(vertice)
            unir(pai, rank, raiz1, raiz2)

    return arvore_minima


# Exemplo de uso:
grafo = {"A": ["B", "C", 2], "B": ["A", "C", 1], "C": ["A", "B", 3]}

arvore_minima = kruskal(grafo)
print(arvore_minima)
