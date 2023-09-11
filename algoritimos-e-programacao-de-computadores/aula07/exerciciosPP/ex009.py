# Exercício Pré-Prova 009
# Matrizes:
# 9. Crie uma matriz 3x3 (uma lista de listas) com números inteiros e calcule a soma de todos os elementos.

def criarMatriz(m,n,valor=0):
    matriz = [valor]*m
    for i in range(m):
        matriz[i] = [valor]*n
    return matriz    

def somadorMatriz(matriz1,matriz2, m, n):
    matriz = criarMatriz(m, n)
    for i in range(m):
        for j in range(n):
            matriz[i][j] = matriz1[i][j] + matriz2[i][j]
    return matriz

def verMatriz(m,n, matriz):
    for i in range(m):
        for j in range(n):
            print (f"{matriz[i][j]}",end=" ")
        print ("")

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

m = len(matriz1)
n = len(matriz1[0])

matriz3 = somadorMatriz(matriz1,matriz2, m, n)
verMatriz(m, n, matriz1)
print("---------------")
verMatriz(m, n, matriz2)
print("---------------")
verMatriz(m, n, matriz3)