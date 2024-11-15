lista = []

try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    div = lista[0] / lista[1]
except ValueError:
    print('Valor Incorreto')
except ZeroDivisionError:
    print('Valor Divido Por Zero')
except IndexError:
    print(f'Array tem apenas {len(lista)} Valores')
except KeyboardInterrupt:
    print('Usuario Interronpeu a execução')
else:
    print('O Valor da Divisao {:.2f}'.format(div))