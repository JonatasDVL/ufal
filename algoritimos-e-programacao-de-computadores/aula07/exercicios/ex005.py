# 2. Implemente uma função que recebe uma matriz e um inteiro e faz a multiplicação da matriz pelo inteiro

# def criarMatriz(m,n,valor=0):
#     matriz = [valor]*m
#     for i in range(m):
#         matriz[i] = [valor]*n
#     return matriz    

def verMatriz(m,n, matriz):
    for i in range(m):
        for j in range(n):
            print (f"{matriz[i][j]}",end=" ")
        print ("")

def multiplicandoMatriz(m,n,matriz,valor):
    for i in range(m):
        for j in range(n):
            matriz[i][j] = matriz[i][j]*valor
    return matriz

matriz = [0,1,2], [1,2,3], [2,3,3]

m = len(matriz)
n = len(matriz[0])

valor = 2

# matriz = criarMatriz(m,n)
verMatriz(m,n,matriz)
multiplicandoMatriz(m,n,matriz,valor)
print("--------")
print(verMatriz(m,n,matriz))