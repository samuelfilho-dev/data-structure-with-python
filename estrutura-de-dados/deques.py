import numpy as np


class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numeros_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade - 1) or (
                self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    # O (1)
    def inserir_inicio(self, valor):
        if self.__deque_cheio(): return print('O Deque está cheio')

        # Se Estiver Vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Inicio na primeira posição
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor

    def inserir_final(self, valor):
        if self.__deque_cheio(): return print('O Deque está cheio')

        # Se estiver Vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Final na Ultima Posição
        elif self.final == self.capacidade - 1:
            self.final = 0
        else:
            self.final += 1

        self.valores[self.final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio(): return print('Deque está vazio')

        # Possui somente um elemento
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        else:
            # Voltar para posicão inicial
            if self.inicio == self.capacidade - 1:
                self.inicio = 0
            else:
                # Incrementar o inicio para remover o atual
                self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio(): return print('Deque está vazio')

        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        elif self.inicio == 0:
            self.final = self.capacidade - 1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio(): return print('Deque está vazio')
        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0: return print('Deque está vazio')
        return self.valores[self.final]


deque = Deque(5)

deque.inserir_final(5)
deque.inserir_final(10)
deque.inserir_inicio(3)
deque.inserir_inicio(2)
deque.inserir_final(11)

deque.excluir_inicio()
deque.excluir_final()

print(deque.get_inicio())
print(deque.get_final())
print(deque.valores)
