import numpy as np


# O (n ** 2)
# n ** 2 / 2 Comparações

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array


print(bubble_sort(np.array([15, 34, 8, 3])))
print(bubble_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
