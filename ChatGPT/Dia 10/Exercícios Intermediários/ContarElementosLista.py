# Este algoritmo conta o número de ocorrências de cada elemento em uma lista.


def count_elements(nums):
    counts = {}  # Criamos um dicionário vazio para armazenar as contagens

    # Percorremos a lista e atualizamos as contagens no dicionário
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return counts


print(
    count_elements([1, 2, 1, 3, 2, 4, 1])
)  # Exemplo de uso: Conta o número de ocorrências de cada elemento na lista [1, 2, 1, 3, 2, 4, 1]
