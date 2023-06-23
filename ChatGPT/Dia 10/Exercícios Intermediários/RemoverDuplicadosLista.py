# Este algoritmo remove elementos duplicados de uma lista.


def remove_duplicates(nums):
    return list(
        set(nums)
    )  # Convertendo a lista em conjunto e depois de volta em lista, removemos os elementos duplicados


print(
    remove_duplicates([1, 2, 1, 3, 2, 4, 1])
)  # Exemplo de uso: Remove elementos duplicados da lista [1, 2, 1, 3, 2, 4, 1]
