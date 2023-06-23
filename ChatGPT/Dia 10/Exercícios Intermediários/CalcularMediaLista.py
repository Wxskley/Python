# Este algoritmo calcula a média dos números em uma lista.


def calculate_average(nums):
    return sum(nums) / len(nums)  # Somamos todos os números e dividimos pelo total


print(
    calculate_average([1, 2, 3, 4, 5])
)  # Exemplo de uso: Calcula a média dos números na lista [1, 2, 3, 4, 5]
