# 3. O jogo da velha é um jogo de passatempo popular que consiste em um tabuleiro 3x3 onde dois oponentes podem escolher uma marcação (O) ou (X). Cada jogador pode fazer uma marcação por vez e o objetivo é completar a sua marcação em uma linha, coluna ou diagonal. O primeiro jogador a atingir o objetivo é o vencedor da partida. Se o tabuleiro for completamente preenchido sem que alguém consiga atingir o objetivo, então o jogo termina empatado. Você deve implementar um programa com uma função que recebe uma matriz que representa o tabuleiro completo e verifica qual dos dois oponentes (O ou X) venceu, ou se houve empate.

# Exemplo 1:
#     O X O
#     X X O
#     O X X
# X vencedor

# Exemplo 2:
#     O X O
#     X X O
#     O O X
# Empate

def verificarVencedor(matriz,m,n):
    # verificando a linha
    for i in range(m):
        contador = 0
        for j in range(n):
            if matriz[i][j] == "X":
                contador += 1
            elif matriz[i][j] == "O":
                contador += 2
            else: 
                break
        if contador == 3:
            return "X é vencedor"
        elif contador == 6:
            return "O é vencedor"

    # verificando a coluna
    for j in range(n):
        contador = 0
        for i in range(m):
            if matriz[i][j] == "X":
                contador += 1
            elif matriz[i][j] == "O":
                contador += 2
            else: 
                break    
        if contador == 3:
            return "X é vencedor"
        elif contador == 6:
            return "O é vencedor"
        else: 
            break

    # verificando a diagonal
    contador = 0
    for i in range(m):
        if matriz[i][i] == "X":
            contador += 1
        elif matriz[i][i] == "O":
            contador += 2
        else: 
            break 
    if contador == 3:
        return "X é vencedor"
    elif contador == 6:
        return "O é vencedor"
    
    # verificando a diagonal
    contador = 0
    j = n
    for i in range(m):
        j -= 1
        if matriz[i][j] == "X":
            contador += 1
        elif matriz[i][j] == "O":
            contador += 2
        else: 
            break
    if contador == 3:
        return "X é vencedor"
    elif contador == 6:
        return "O é vencedor"    

    return "Empate"

tabuleiro = [
    ["O", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "X"]
]
m = len(tabuleiro)
n = len(tabuleiro[0])

print(verificarVencedor(tabuleiro,m,n))


