import timeit


# 11 Passos para execução do problema
# O (n)
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma


# 3 Passos para execução do problema
# 0 (3) - Constante
def soma2(n):
    return (n * (n + 1)) / 2


print(timeit.timeit("soma1(10)", globals=locals()))
print(timeit.timeit("soma2(10)", globals=locals()))
