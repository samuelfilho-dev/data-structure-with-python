import numpy as np

# 0 (N ** 2)
def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        min_id = i
        for j in range(i + 1, n):
            if vetor[min_id] > vetor[j]:
                min_id = j
        temp = vetor[i]
        vetor[i] = vetor[min_id]
        vetor[min_id] = temp

    return vetor


print(selection_sort(np.array([15, 34, 8, 3])))
print(selection_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
