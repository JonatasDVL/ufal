# 4. Um quadrado mágico é aquele dividido em linhas e colunas no qual a soma das linhas, das colunas e diagonais é a mesma. Ex:
# 8  3  4
# 1  5  9
# 6  7  2
# Implemente uma função que recebe uma matriz e verifica se é um quadrado mágico

def verMatriz(m,n, matriz):
    for i in range(m):
        for j in range(n):
            print (f"{matriz[i][j]}",end=" ")
        print ()

def verificarQuadradoMagico(m,n,matriz):
    valor1 = 0
    valor2 = 0
    for i in range(m):
        for j in range(n):
            valor1 += matriz[i][j]
        if (valor1 != valor2 and i != 0):
           return False
        valor2 = valor1
        valor1 = 0
    for j in range(n):
        for i in range(m):
            valor1 += matriz[i][j]
        if (valor1 != valor2):
            return False
        valor2 = valor1
        valor1 = 0
    for i in range(m):
        valor1 += matriz[i][i]
    if (valor1 != valor2):
        print(1, valor1,valor2)
        return False
    valor2 = valor1
    valor1 = 0
    j=0
    for i in range(m):
        valor1 += matriz[i][j]
    j += 1
    valor2 = valor1
    if (valor1 != valor2):
        return False


    return True
matriz = [8,3,4], [1,5,9], [6,7,4]

m = len(matriz)
n = len(matriz[0])

# matriz = criarMatriz(m,n)
verMatriz(m,n,matriz)
print(verificarQuadradoMagico(m,n,matriz))