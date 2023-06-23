# Vamos começar com uma lista de números desorganizados
array = [4, 2, 7, 1, 9, 3]


# Agora vamos usar o algoritmo Merge Sort para organizar essa lista
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Agora vamos juntar as listas ordenadas em uma única lista
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Adicionamos os elementos restantes, se houver algum
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Vamos imprimir a lista ordenada
sorted_array = merge_sort(array)
print(sorted_array)
