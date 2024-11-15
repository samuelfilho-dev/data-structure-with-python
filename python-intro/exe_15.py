class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def __str__(self):
        return f'Aluno {self.nome} - Nota 1: {self.nota1} - Nota 2: {self.nota2}'

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def resultado(self):
        if ((self.nota1 + self.nota2) / 2) > 6:
            return 'Aprovado'
        else:
            return 'Reprovado'


aluno_1 = Aluno('Samuel', 8, 9)
print(aluno_1)
print(aluno_1.media())
print(aluno_1.resultado())

aluno_2 = Aluno('Janina', 5, 6)
print(aluno_2)
print(aluno_2.media())
print(aluno_2.resultado())
