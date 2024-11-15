import numpy as np


# FIFO (First In - First Out)
class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numeros_elementos = 0
        self.valores = np.empty(capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numeros_elementos == 0

    def __fila_cheia(self):
        return self.numeros_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia(): return print('A Fila está Cheia')

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numeros_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia(): return print('A Fila Já esta Vazia')

        temp = self.valores[self.inicio]
        self.inicio += 1

        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numeros_elementos -= 1
        return temp

    def primeiro_elemento(self):
        if self.__fila_vazia(): return -1
        return self.valores[self.inicio]


fila = FilaCircular(5)
print(fila.primeiro_elemento())

fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
# fila.enfileirar(6)

fila.desenfileirar()
fila.desenfileirar()

fila.enfileirar(6)
fila.enfileirar(7)

print(fila.primeiro_elemento())
