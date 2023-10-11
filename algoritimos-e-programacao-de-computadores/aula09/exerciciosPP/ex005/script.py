# Leitura e Escrita Reversa:
# Leia o conteúdo de um arquivo de texto e escreva-o de volta no mesmo arquivo, mas na ordem reversa, de modo que a última linha seja a primeira e assim por diante.

import os
caminho = os.path.abspath(__file__).replace("script.py", "arquivo.txt")

if os.path.isfile(caminho):
    # O arquivo existe.
    linhas = []
    with open(caminho,"r") as arquivo:
        for linha in arquivo.readlines():
            linhas.append(linha.replace("\n","")+"\n")
    with open(caminho,"w") as arquivo:
        for i in range(1,len(linhas)+1):
            arquivo.write(linhas[-i])        
else:
    # O arquivo não existe.
    with open(caminho,"w") as arquivo:
        arquivo.write("oi\nJonatas\noi\nThallys")