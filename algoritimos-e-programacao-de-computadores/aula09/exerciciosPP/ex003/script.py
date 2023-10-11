# Contagem de Linhas:
# Escreva um programa que lê um arquivo de texto e conta quantas linhas ele possui.

import os
caminho = os.path.abspath(__file__).replace("script.py", "arquivo.txt")

if os.path.isfile(caminho):
    # O arquivo existe.
    i=0
    with open(caminho,"r") as arquivo:
        for linhas in arquivo.readlines():
            i+=1
    print(f"O arquivo possui {i} linhas.")
else:
    # O arquivo não existe.
    with open(caminho,"w") as arquivo:
        arquivo.write("oi\nJonatas")
