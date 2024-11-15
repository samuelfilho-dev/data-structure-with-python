import numpy as np


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O Vetor está Vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i].label, ' - ', self.valores[i].distance)

    # O (n)
    def inserir(self, vertice):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade Maxima Atiginda')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distance > vertice.distance:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = vertice
        self.ultima_posicao += 1
