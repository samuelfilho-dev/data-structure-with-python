from vetor_ordenado import VetorOrdenado

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


class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-' * 5)
        print(f'Atual {atual.label}')
        atual.isVisited = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacents))
            for adjacent in atual.adjacents:
                if not adjacent.vertice.isVisited:
                    adjacent.vertice.is_visited = True
                    vetor_ordenado.inserir(adjacent.vertice)
            vetor_ordenado.imprimir()

            if vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0])

busca_gulosa = Gulosa(Graph.bucharest)
busca_gulosa.buscar(Graph.arad)