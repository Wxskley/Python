# Este algoritmo ordena uma lista de números em ordem crescente.
# Usamos o algoritmo chamado Bubble Sort.


def bubble_sort(nums):
    n = len(nums)

    # Percorremos a lista várias vezes
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Comparamos dois números adjacentes e os trocamos se estiverem na ordem errada
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


nums = [4, 2, 7, 1, 9]
bubble_sort(nums)
print(nums)  # Exemplo de uso: Ordena a lista [4, 2, 7, 1, 9]
