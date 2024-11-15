import numpy as np

matriz = np.array([[1,2,3],[4,5,6]])

print(matriz)
print(matriz.shape) # Qtd de Linhas de Colunas da Matriz
print(matriz[0]) # Linhas da Matriz
print(matriz[0][0]) # Colunas da Matriz

for i in range(matriz.shape[0]): # Pecorrer uma Matiz
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])