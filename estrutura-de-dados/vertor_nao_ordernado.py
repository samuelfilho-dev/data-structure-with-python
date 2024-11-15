import numpy as np


class VetorNaoOrdernado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O Vetor está Vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

    # O(1)
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade Maxima Atiginda')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O (n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        else:
            return -1

    # O (n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1


vetor = VetorNaoOrdernado(5)

vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(5)
vetor.inserir(8)
vetor.inserir(7)

vetor.imprimir()

print(vetor.pesquisar(8))
print(vetor.pesquisar(2))  # Melhor Caso de Pesquisa
print(vetor.pesquisar(9))  # Pior Caso De Pesquisa

vetor.excluir(5)
vetor.excluir(7)
vetor.excluir(2)

vetor.inserir(5)
vetor.inserir(1)
vetor.imprimir()
