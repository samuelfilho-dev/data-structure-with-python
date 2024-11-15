nota1 = 7
nota2 = 7
nota3 = 7

media = (nota1 + nota2 + nota3) / 3

if 0 < media < 4:
    print('Reprovado ☠️')
elif 4 < media < 6:
    print('Pegou Exame')

    nota_exame = float(input('Digite a nota do exame: '))

    if nota_exame > 6:
        print('Aprovado')
    elif nota_exame < 6:
        print('Reprovado')

elif 6 < media < 10:
    print('Aprovado')
