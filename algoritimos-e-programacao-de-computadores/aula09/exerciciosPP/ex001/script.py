# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
    # O arquivo de entrada possui o seguinte formato:
    # 200.135.80.9
    # 192.168.1.1
    # 8.35.67.74
    # 257.32.4.5
    # 85.345.1.2
    # 1.2.3.4
    # 9.8.234.5
    # 192.168.0.256
# O arquivo de saída possui o seguinte formato:
    # [Endereços válidos:]
    # 200.135.80.9
    # 192.168.1.1
    # 8.35.67.74
    # 1.2.3.4

    # [Endereços inválidos:]
    # 257.32.4.5
    # 85.345.1.2
    # 9.8.234.5
    # 192.168.0.256

import os
caminho = os.path.abspath(__file__)
caminho = caminho.replace("script.py", "arquivo.txt")
caminho2 = caminho.replace("arquivo.txt", "arquivo2.txt")

arquivo = open(f"{caminho}", "r")
lista1 = []
lista2 = []
for linha in arquivo.readlines():
    linha2 = linha.replace("\n", "").replace(".", " ").split()
    if int(linha2[0]) <= 255 and int(linha2[1]) <= 255 and int(linha2[2]) <= 255 and int(linha2[3]) <= 255 and len(linha2) == 4:
        lista1.append(linha)
    else:
        lista2.append(linha)
arquivo.close()

arquivo = open(f"{caminho2}", "w")
arquivo.write("[Endereços válidos:]\n")
for linha in lista1: 
    arquivo.write(f"{linha}")
arquivo.write("\n[Endereços inválidos:]\n")
for linha in lista2: 
    arquivo.write(f"{linha}")
arquivo.close()
