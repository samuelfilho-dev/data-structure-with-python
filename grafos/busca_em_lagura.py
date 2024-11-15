from fila import FilaCircular
from grafo import graph


class BuscaLagura:
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.isVisited = True
        self.fila = FilaCircular(20)
        self.fila.enfileirar(self.inicio)

    def buscar(self):
        primeiro = self.fila.primeiro_elemento()
        print('-' * 5)
        print(f'Primeiro da Fila: {primeiro.label}')

        temp = self.fila.desenfileirar()
        print(f'Desemfilerou {temp.label}')

        for adjacent in primeiro.adjacents:
            print(
                f'Primeiro Elemento era {temp.label}. {adjacent.vertice.label} já foi visitado? {adjacent.vertice.isVisited}'
            )
            if not adjacent.vertice.isVisited:
                adjacent.vertice.isVisited = True
                self.fila.enfileirar(adjacent.vertice)
                print(f'Enfilerou: {adjacent.vertice.label}')
        if self.fila.numeros_elementos > 0:
            self.buscar()


busca_lagura = BuscaLagura(graph.arad)
busca_lagura.buscar()
