class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        atual = self.primeiro

        while atual is not None:
            atual.mostrar_no()
            atual = atual.proximo

    def __lista_vazia(self):
        if self.primeiro is None:
            print('A Lista está Vazia')
            return None

    def excluir_inicio(self):
        self.__lista_vazia()

        temp = self.primeiro

        self.primeiro = self.primeiro.proximo
        return temp

    def pesquisar(self, valor):
        self.__lista_vazia()

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo is None:
                return None
            else:
                atual = atual.proximo

        return atual

    def excluir_posicao(self, valor):
        self.__lista_vazia()

        atual = self.primeiro
        anterior = self.primeiro

        while atual.valor != valor:
            if atual.proximo is None:
                return None
            else:
                anterior = atual
                atual = atual.proximo

            if atual == self.primeiro:
                self.primeiro = self.primeiro.proximo
            else:
                anterior.proximo = atual.proximo

            return atual


lista = ListaEncadeada()

lista.inserir_inicio(1)
lista.inserir_inicio(2)
lista.inserir_inicio(3)
lista.inserir_inicio(4)
lista.inserir_inicio(4)

lista.excluir_inicio()
lista.excluir_inicio()

lista.excluir_posicao(3)
lista.excluir_posicao(0)
lista.excluir_posicao(2)

pesquisa = lista.pesquisar(4)

if pesquisa is not None:
    print(pesquisa.valor)
else:
    print('Não Encontrado')

lista.mostrar()
print(lista.primeiro)
print(lista.primeiro.proximo.proximo.proximo)

