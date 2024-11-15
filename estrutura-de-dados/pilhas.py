import numpy as np


# LIFO (Last In - First Out)
class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A Pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('Pilha está Vazia')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1


pilha = Pilha(5)

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(6)

pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
print(pilha.ver_topo())
