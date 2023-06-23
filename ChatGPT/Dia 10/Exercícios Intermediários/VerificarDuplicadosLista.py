# Este algoritmo verifica se uma lista contém elementos duplicados.


def has_duplicates(nums):
    return len(nums) != len(
        set(nums)
    )  # Comparamos o tamanho da lista original com o tamanho de um conjunto dos seus elementos (conjunto não permite duplicados)


print(
    has_duplicates([1, 2, 3, 4, 5])
)  # Exemplo de uso: Verifica se a lista [1, 2, 3, 4, 5] contém elementos duplicados
