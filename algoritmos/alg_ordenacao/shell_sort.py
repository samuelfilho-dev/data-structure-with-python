import numpy as np


# Depende Do intervalo Escolhido
# Pior Caso: O (n ** 2)
# Melhor Caso: O (n * log n)
def shell_sort(alist):
    n = len(alist) // 2

    while n > 0:
        for i in range(n, len(alist)):
            temp = alist[i]
            j = i
            while j >= n and alist[j - n] > temp:
                alist[j] = alist[j - n]
                j -= n
            alist[j] = temp
        n //= 2

    return alist

print(shell_sort(np.array([15, 34, 8, 3])))
print(shell_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
print(shell_sort(np.array([8,5,1,4,2,3])))
