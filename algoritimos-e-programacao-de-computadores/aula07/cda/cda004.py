# def inicializarMatriz(m,n, valor):

matrizA = [[2,3],[0,1]]
matrizB = [[1,-1],[0,2]]

m = 2
n = 2

matrizAB = [0]*m
for i in range(m):
    matrizAB[i] = [0]*n

for i in range(n):
    for j in range(m):
        matrizAB[i][j] = matrizA[i][j] + matrizB[i][j]

for i in range(m):
    for j in range(n):
        print (f"{matrizAB[i][j]}",end=" ")
    print ()