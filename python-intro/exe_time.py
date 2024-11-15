import time as tm

print(tm.time())

antes = tm.time()
lista = []
for i in range(100_000):
    lista.append(i)

depois = tm.time()

intevalo = depois - antes
print(f'Tempo : {intevalo}')

print('Finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Ate a Proxima')