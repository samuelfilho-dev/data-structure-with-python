import numpy as np


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O Vetor está Vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

    # O (n)
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade Maxima Atiginda')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    # O (n)
    def pesquisar_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1

    # O (log n) - Quebrar a instancia de dados
    def pesquisar_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = (limite_inferior + limite_superior) // 2
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif limite_inferior > limite_superior:
                return -1
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1

    def excluir(self, valor):
        posicao = self.pesquisar_binaria(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1


vetor = VetorOrdenado(10)

vetor.inserir(6)
vetor.inserir(4)
vetor.inserir(3)
vetor.inserir(5)
vetor.inserir(1)
vetor.inserir(8)

vetor.imprimir()

print(vetor.pesquisar_linear(5))
print(vetor.pesquisar_linear(8))
print(vetor.pesquisar_linear(2))

vetor.excluir(5)
vetor.excluir(1)
vetor.excluir(8)
vetor.excluir(9)
vetor.imprimir()


print(vetor.pesquisar_binaria(6))
print(vetor.pesquisar_binaria(1))
print(vetor.pesquisar_binaria(8))
print(vetor.pesquisar_binaria(20))