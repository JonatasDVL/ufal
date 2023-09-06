# 1. Implemente uma função que recebe uma matriz e verifica se ela é simétrica

# def criarMatriz(m,n,valor=0):
#     matriz = [valor]*m
#     for i in range(m):
#         matriz[i] = [valor]*n
#     return matriz    

def verMatriz(m,n, matriz):
    for i in range(m):
        for j in range(n):
            print (f"{matriz[i][j]}",end=" ")
        print ()    

def verificarSimetria(m,n, matriz):
    if m == n:
        i = 0
        j = 0
        condicao = 0
        while i < m:
            while j < n: # tem como melhorar, pelo menos cortar pela metade 
                if(matriz[i][j] == matriz[j][i]):
                    condicao += 1
                    if(m*n == condicao):
                        return True
                else: 
                    return False
                j +=1
            j = 0
            i += 1
    else:
        return False

matriz = [0,1,2], [1,2,3], [2,3,3]

m = len(matriz)
n = len(matriz[0])

# matriz = criarMatriz(m,n)
verMatriz(m,n,matriz)

print(verificarSimetria(m,n,matriz))