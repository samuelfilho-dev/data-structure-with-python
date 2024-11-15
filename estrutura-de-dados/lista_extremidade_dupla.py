class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)


class ListaEncadeadaExtremidadeDulpla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro is None

    def inserir_inicio(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def inserir_final(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia(): return print('A Lista está Vazia')

        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo

        return temp

    def mostrar(self):
        if self.__lista_vazia(): return print('A Lista está Vazia')

        atual = self.primeiro
        while atual is not None:
            atual.mostrar_no()
            atual = atual.proximo


lista = ListaEncadeadaExtremidadeDulpla()
lista.inserir_inicio(1)
lista.inserir_inicio(2)
lista.inserir_inicio(3)
lista.inserir_inicio(4)
lista.inserir_inicio(5)

lista.inserir_final(1)
lista.inserir_final(2)
lista.inserir_final(3)
lista.inserir_final(4)
lista.inserir_final(5)

lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()

lista.mostrar()
# print(lista.primeiro, lista.ultimo)
