# Concatenação de Arquivos:
# Crie dois arquivos de texto e, em seguida, escreva um programa que os concatene em um terceiro arquivo.

import os
caminho = os.path.abspath(__file__).replace("script.py", "arquivo.txt")
caminho2 = caminho.replace("arquivo.txt", "arquivo2.txt")
caminho3 = caminho.replace("arquivo.txt", "arquivo3.txt")


if os.path.isfile(caminho) and os.path.isfile(caminho2):
    # O arquivo existe.
    linhas = []
    with open(caminho,"r") as arquivo:
        for linha in arquivo.readlines():
            linhas.append(linha)
        linhas.append("\n")
    with open(caminho2,"r") as arquivo:
        for linha in arquivo.readlines():
            linhas.append(linha)
    with open(caminho3,"w") as arquivo:
        for linha in linhas:
            arquivo.write(linha)
else:
    # O arquivo não existe.
    with open(caminho,"w") as arquivo:
        arquivo.write("oi\nJonatas")
    with open(caminho2,"w") as arquivo:
        arquivo.write("oi\nThallys")