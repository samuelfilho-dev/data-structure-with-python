import numpy as np


# Pior Caso: O (n * log n)
# Melhor Caso: O (n * log n)
def merge_sort(array):
    if len(array) > 1:
        div = len(array) // 2
        left = array[:div].copy()
        right = array[div:].copy()

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


print(merge_sort(np.array([15, 34, 8, 3])))
print(merge_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
print(merge_sort(np.array([38, 27, 43, 3, 9, 82, 10])))
