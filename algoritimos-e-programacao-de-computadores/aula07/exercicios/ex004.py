# 1. Implemente uma função que recebe uma matriz e verifica se ela é simétrica

def criarMatriz(m,n,valor=0):
    matriz = [valor]*m
    for i in range(m):
        matriz[i] = [valor]*n
    return matriz    

def verMatriz(m,n, matriz):
    for i in range(m):
        for j in range(n):
            print (f"{matriz[i][j]}",end=" ")
        print ()    

matriz = criarMatriz(2,2)
verMatriz(2,2,matriz)