alunos_notas = {}

for i in range(3):
    nome_aluno = input('Nome Do Aluno: ')
    nota_aluno = float(input('Nota do Aluno: '))
    alunos_notas[nome_aluno] = nota_aluno

soma = 0
for i in alunos_notas.values():
    soma += i

media = soma / len(alunos_notas.keys())
print('A Média da Notas: {:.2f}'.format(media))