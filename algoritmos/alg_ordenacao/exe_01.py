import time
import random
import sys
from alg_ordenacao.bubble_sort import bubble_sort
from alg_ordenacao.merge_sort import merge_sort
from alg_ordenacao.quick_sort import quick_sort

sys.setrecursionlimit(10_000)

lista = []
for _ in range(5_000):
    lista.append(
        round(random.random(), 4)
    )


# Bubble Sort
start = time.time()
bubble_sort(lista)
end = time.time()
print(f'Tempo Do Bubble Sort: {end - start}')


# Merge Sort
start = time.time()
merge_sort(lista)
end = time.time()
print(f'Tempo Do Merge Sort: {end - start}')


# Quick Sort
start = time.time()
quick_sort(lista, 0, len(lista) - 1)
end = time.time()
print(f'Tempo Do Quick Sort: {end - start}')