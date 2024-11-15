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

    def lista_vazia(self):
        return self.primeiro is None

    def inserir_final(self, valor):
        novo = No(valor)

        if self.lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.lista_vazia(): return print('A Lista está Vazia')

        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo

        return temp


class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDulpla()

    def lista_vazia(self):
        return self.lista.lista_vazia()

    def enfileirar(self, valor):
        self.lista.inserir_final(valor)

    def desenfileirar(self):
        return self.lista.excluir_inicio()

    def ver_inicio(self):
        if self.lista.primeiro is None: return -1
        return self.lista.primeiro.valor


fila = FilaListaEncadeada()
fila.enfileirar(20)
fila.enfileirar(40)
fila.enfileirar(60)
fila.enfileirar(80)
print(fila.ver_inicio())