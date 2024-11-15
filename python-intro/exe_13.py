alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('arquivos/notas-alunos.txt', 'w') as file:
    for aluno, nota in alunos.items():  # (key,value): ordem da função .items()
        file.write(f'{aluno},{nota} \n')

with open('arquivos/notas-alunos.txt', 'r') as file:
    for line in file:
        print(line)