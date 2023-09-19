matriz = []

quantidade = int(input())

def preencher_matriz():
    for i in range(quantidade):
        linha = list(map(int, (input().split())))
        matriz.append(linha)

def valor_linha():
    value = 0
    status = True
    for array in matriz:
        soma = sum(array)
        if (value == 0):
            value = soma
        else:
            if (soma != value):
                status = False
    return status, value
def verificar_coluna():
    value = 0
    status = True
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz)):
            soma += matriz[j][i]
        if (value == 0):
            value = soma
        else:
            if (soma != value):
                status = False
    return status

def verificar_diagonais():
    soma = 0
    status = True
    for i in range(quantidade):
        soma += matriz[i][i]
    soma2 = 0
    for j in range(quantidade-1, 0, -1):
        soma2 += matriz[j][j]
    print(soma)
    print(soma2)
    if (soma == soma2):
        return True
    else:
        return False
# [0][3]
# [1][2]
# [2][1]

if (quantidade >= 2 and quantidade <= 10):
    preencher_matriz()
    statusUm, value = valor_linha()
    statusDois = verificar_coluna()
    statusDiagonal = verificar_diagonais()
    print(statusDiagonal)

    if (statusUm == True and statusDois == True):
        print(value)
    else:
        print(-1)
