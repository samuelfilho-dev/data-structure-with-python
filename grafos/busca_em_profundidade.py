from distutils.command.build import build

from grafo import Graph, graph
from pilha import Pilha


class BuscaProfundidade():
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.isVisited = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(inicio)

    def buscar(self):
        topo = self.pilha.ver_topo()
        print(f'Topo: {topo.label}')

        for adjacent in topo.adjacents:
            print(f'Topo é {topo.label}. {adjacent.vertice.label} já foi visitada? {adjacent.vertice.isVisited}')
            if not adjacent.vertice.isVisited:
                adjacent.vertice.isVisited = True
                self.pilha.empilhar(adjacent.vertice)
                print(f'Empilhou {adjacent.vertice.label}')
                self.buscar()

        print(f'Desempilhou: {self.pilha.desempilhar().label} \n')


buscar = BuscaProfundidade(graph.arad)
buscar.buscar()
