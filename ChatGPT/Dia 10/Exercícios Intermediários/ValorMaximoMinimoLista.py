# Este algoritmo encontra o valor máximo e mínimo em uma lista de números.


def find_max_min(nums):
    max_num = float("-inf")  # Definimos o máximo inicial como menos infinito
    min_num = float("inf")  # Definimos o mínimo inicial como mais infinito

    # Percorremos a lista e atualizamos o máximo e mínimo se necessário
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num


nums = [4, 2, 7, 1, 9]
max_num, min_num = find_max_min(nums)
print(
    max_num, min_num
)  # Exemplo de uso: Encontra o valor máximo e mínimo na lista [4, 2, 7, 1, 9]
