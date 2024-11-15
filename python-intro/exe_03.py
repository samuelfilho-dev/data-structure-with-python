age = int(input('Qual é Sua Idade? '))

if 0 < age < 12:
    print('Criança')
elif 13 < age < 17:
    print('Aborrecente')
elif age > 18:
    print('Adulto')
else:
    print('Idade Invalida')
