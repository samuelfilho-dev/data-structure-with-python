try:
    n = int(input('Digite um Número Inteiro: '))
except:
    print('Valor Invalido!')
else:
    print('Valor Digitado é {}'.format(n))

while True:
    try:
        n = int(input('Digite um Número Inteiro: '))
    except:
        print('Valor Invalido!')
    else:
        print('Valor Digitado é {}'.format(n))
        break

while True:
    try:
        p = int(input('Digite um Número Inteiro: '))
    except ValueError:
        print('Valor Invalido')
    except KeyboardInterrupt:
        print('Usuario Interrompeu a execução')
    else:
        print('Valor Digitado é {}'.format(p))
        break
