class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def lista_vazia(self):
        if self.primeiro is None:
            print('A Lista está Vazia')
            return None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def excluir_inicio(self):
        self.lista_vazia()

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp


class PilhaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeada()

    def empilhar(self, valor):
        self.lista.inserir_inicio(valor)

    def desempilhar(self):
        return self.lista.excluir_inicio()

    def pilha_vazia(self):
        return self.lista.lista_vazia()

    def mostrar_topo(self):
        if self.lista.primeiro is None: return -1
        return self.lista.primeiro.valor


pilha = PilhaListaEncadeada()
pilha.empilhar(20)
pilha.empilhar(40)

print(pilha.mostrar_topo())
