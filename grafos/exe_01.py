import numpy as np

from algortimo_de_dijkstra import Dijkstra

vertices2 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
vertices2_inv = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

arestas2 = np.zeros([len(vertices2), len(vertices2)], dtype=int)
arestas2[vertices2['A'], [vertices2['B']]] = 2
arestas2[vertices2['A'], [vertices2['C']]] = 1
arestas2[vertices2['B'], [vertices2['D']]] = 1
arestas2[vertices2['C'], [vertices2['D']]] = 3
arestas2[vertices2['C'], [vertices2['E']]] = 4
arestas2[vertices2['D'], [vertices2['F']]] = 2
arestas2[vertices2['E'], [vertices2['F']]] = 2

dijkstra = Dijkstra(vertices2_inv, arestas2, vertices2['A'])
dijkstra.dijkstra()
