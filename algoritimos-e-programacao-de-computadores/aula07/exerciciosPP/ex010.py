# Exercício Pré-Prova 010
# 10. Crie uma matriz 2x2 com valores booleanos (True/False) e verifique se todos os valores são True.

def verificadorValoresMatriz(matriz):    
    for i in range(m):
        for j in range(n):
            if matriz[i][j] == False:
                return False
    return True

matriz = [
    [True, True],
    [True, True]
]

# matriz = [
#     [True, False],
#     [False, True]
# ]

m = len(matriz)
n = len(matriz[0])

print(verificadorValoresMatriz(matriz))