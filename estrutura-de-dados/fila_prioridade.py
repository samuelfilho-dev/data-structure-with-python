import numpy as np


class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numeros_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numeros_elementos == 0

    def __fila_cheia(self):
        return self.numeros_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia(): return print('A Fila está cheia')

        if self.numeros_elementos == 0:
            self.valores[self.numeros_elementos] = valor
            self.numeros_elementos += 1
        else:
            x = self.numeros_elementos - 1

            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1

            self.valores[x + 1] = valor
            self.numeros_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia(): return print('A Fila Está Vazia')

        valor = self.valores[self.numeros_elementos - 1]
        self.numeros_elementos -= 1
        return valor

    def primeiro_elemento(self):
        if self.__fila_vazia(): return -1
        return self.valores[self.numeros_elementos - 1]


fila = FilaPrioridade(5)
# print(fila.primeiro_elemento())

fila.enfileirar(30)
fila.enfileirar(50)
fila.enfileirar(10)
fila.enfileirar(40)
fila.enfileirar(20)
# fila.enfileirar(2)

fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()

fila.enfileirar(5)

print(fila.primeiro_elemento())

