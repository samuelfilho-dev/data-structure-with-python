lista = []

for i in range(5):
    num = int(input('Digite um valor: '))
    lista.append(num)

soma = 0
for i in lista:
    soma += i

print('A Soma da Lista: {}'.format(soma))