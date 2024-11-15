import time


# 0(n)
def lista1():
    lista = []
    for i in range(1_000):
        lista += [i]
    return lista


def lista2():
    return range(1_000)


antes = time.time()
print(lista1())
print(len(lista1()))
depois = time.time()

print(f'Execução da Lista 1: {depois - antes}')

antes_lista_2 = time.time_ns()
print(lista2())
print(len(lista2()))
depois_lista_2 = time.time_ns()

print(f'Execução da Lista 2: {depois_lista_2 - antes_lista_2} ns')
