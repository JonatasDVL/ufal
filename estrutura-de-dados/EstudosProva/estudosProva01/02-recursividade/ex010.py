#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 10: Caminho em um labirinto: Crie uma função recursiva para encontrar um caminho válido de entrada para saída em um labirinto representado por uma matriz.

def encontrar_caminho_labirinto(labirinto, linha, coluna, caminho):
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    # Verifica se a posição está dentro dos limites do labirinto
    if linha < 0 or linha >= linhas or coluna < 0 or coluna >= colunas or labirinto[linha][coluna] != 1:
        return False
    
    # Marca o caminho na posição atual
    caminho[linha][coluna] = 1

    # Se alcançou a saída, retorna True
    if linha == linhas - 1 and coluna == colunas - 1:
        return True

    # Tentativas de movimento: direita, baixo, esquerda, cima
    if (
        encontrar_caminho_labirinto(labirinto, linha, coluna + 1, caminho) or  # Direita
        encontrar_caminho_labirinto(labirinto, linha + 1, coluna, caminho) or  # Baixo
        encontrar_caminho_labirinto(labirinto, linha, coluna - 1, caminho) or  # Esquerda
        encontrar_caminho_labirinto(labirinto, linha - 1, coluna, caminho)  # Cima
    ):
        return True

    # Se nenhum movimento leva à saída, marca a posição como não parte do caminho
    caminho[linha][coluna] = 0
    return False

# Exemplo de uso:
labirinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1]
]

# Matriz para registrar o caminho
caminho = [[0 for _ in range(len(labirinto[0]))] for _ in range(len(labirinto))]

if encontrar_caminho_labirinto(labirinto, 0, 0, caminho):
    print("Caminho encontrado:")
    for row in caminho:
        print(row)
else:
    print("Não há caminho possível.")
