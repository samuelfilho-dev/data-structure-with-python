# Ler 5 notas e informar a média
notas = []

for i in range(5):
    notas.append(float(input('Digite a nota: ')))

media = sum(notas) / len(notas)
print('Média: {:.2f}'.format(media))