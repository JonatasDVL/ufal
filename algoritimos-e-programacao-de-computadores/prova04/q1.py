# 1. Faça um programa que leia um arquivo contendo N sequências de 5 números inteiros e imprima qual o maior elemento em cada sequência.
# Exemplo de arquivo.
    # 50 80 89 69 78
    # -1 5 12 26 86
    # 0 0 1 0 0
    # 78 89 58 -2 4

import os
caminho = os.path.abspath(__file__).replace("q1.py", "q1.txt")

elementos = []
with open(caminho, "r") as arquivo:
    for linha in arquivo.readlines():
        linha = linha.split()
        maior = linha[0]
        for elemento in linha:
            if maior < elemento: 
                maior = elemento
        elementos.append(maior)

print(elementos)