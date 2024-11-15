import numpy as np


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O Vetor está Vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(
                    i, '-', self.valores[i].vertice.label, ' - ',
                    self.valores[i].custom, ' - ',
                    self.valores[i].vertice.distance, ' - ',
                    self.valores[i].a_star_distance
                )

    # O (n)
    def inserir(self, adjacent):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade Maxima Atiginda')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].a_star_distance > adjacent.a_star_distance:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = adjacent
        self.ultima_posicao += 1


class Vertice:
    def __init__(self, label, distance):
        self.label = label
        self.distance = distance
        self.isVisited = False
        self.adjacents = []

    def add_adjacent(self, adjacent):
        self.adjacents.append(adjacent)

    def show_adjacent(self):
        for adjacent in self.adjacents:
            print(adjacent.vertice.label, adjacent.custom)


class Adjacent:
    def __init__(self, vertice, custom):
        self.vertice = vertice
        self.custom = custom
        self.a_star_distance = vertice.distance + self.custom


class Graph:
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(sibiu, 140))
    arad.add_adjacent(Adjacent(timisoara, 118))

    zerind.add_adjacent(Adjacent(arad, 75))
    zerind.add_adjacent(Adjacent(oradea, 71))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(arad, 140))
    sibiu.add_adjacent(Adjacent(fagaras, 99))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))

    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    lugoj.add_adjacent(Adjacent(timisoara, 111))
    lugoj.add_adjacent(Adjacent(mehadia, 70))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova, 120))

    craiova.add_adjacent(Adjacent(dobreta, 120))
    craiova.add_adjacent(Adjacent(pitesti, 138))
    craiova.add_adjacent(Adjacent(rimnicu, 146))

    rimnicu.add_adjacent(Adjacent(craiova, 146))
    rimnicu.add_adjacent(Adjacent(sibiu, 80))
    rimnicu.add_adjacent(Adjacent(pitesti, 97))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucharest, 211))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(craiova, 138))
    pitesti.add_adjacent(Adjacent(bucharest, 101))

    bucharest.add_adjacent(Adjacent(fagaras, 211))
    bucharest.add_adjacent(Adjacent(pitesti, 101))
    bucharest.add_adjacent(Adjacent(giurgiu, 90))


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-' * 5)
        print('Atual {}'.format(atual.label))
        atual.isVisited = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacents))
            for adjacent in atual.adjacents:
                if not adjacent.vertice.isVisited:
                    adjacent.vertice.isVisited = True
                    vetor_ordenado.inserir(adjacent)
            vetor_ordenado.imprimir()

            if vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0].vertice)


busca_aestrela = AEstrela(Graph.bucharest)
busca_aestrela.buscar(Graph.arad)
