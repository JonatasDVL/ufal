# 3. Implemente uma função que recebe uma matriz e um inteiro e verifica se o inteiro existe na matriz

def verMatriz(m,n, matriz):
    for i in range(m):
        for j in range(n):
            print (f"{matriz[i][j]}",end=" ")
        print ("")

def verificandoNumeroMatriz(m,n,matriz,valor):
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == valor:
                return True
    return False

matriz = [0,1,2], [1,2,3], [2,3,3]

m = len(matriz)
n = len(matriz[0])

valor = 5

# matriz = criarMatriz(m,n)
verMatriz(m,n,matriz)
print(verificandoNumeroMatriz(m,n,matriz,valor))