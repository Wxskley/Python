# Este algoritmo verifica se uma lista é um subconjunto de outra lista.


def is_subset(subset, superset):
    return set(subset).issubset(
        set(superset)
    )  # Convertemos as listas em conjuntos e verificamos se o conjunto do subconjunto está contido no conjunto do superconjunto


print(
    is_subset([1, 2], [1, 2, 3, 4, 5])
)  # Exemplo de uso: Verifica se a lista [1, 2] é um subconjunto da lista [1, 2, 3, 4, 5]
