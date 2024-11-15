import numpy as np


def part(arr, begin, end):
    pivot = arr[end]
    i = begin - 1

    for j in range(begin, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


# Pior Caso: O (n ** 2)
# Melhor Caso: O (n * log n)
def quick_sort(arr, begin, final):
    if begin < final:
        position = part(arr, begin, final)
        # Esquerda
        quick_sort(arr, begin, position - 1)

        # Direita
        quick_sort(arr, position + 1, final)
    return arr


vector = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(quick_sort(vector, 0, len(vector) - 1))
