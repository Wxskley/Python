# Este algoritmo verifica se uma lista está ordenada de forma crescente.


def is_sorted(nums):
    return all(
        nums[i] <= nums[i + 1] for i in range(len(nums) - 1)
    )  # Comparamos cada número com o próximo


print(
    is_sorted([1, 2, 3, 4, 5])
)  # Exemplo de uso: Verifica se a lista [1, 2, 3, 4, 5] está ordenada
