# Análise de Log:
# Crie um programa que lê um arquivo de log de servidor e identifica quantas vezes um determinado IP acessou o servidor.

import os
caminho = os.path.abspath(__file__).replace("script.py", "arquivo.txt")

if os.path.isfile(caminho):
    ip = input("Digite o ip: ")
    while ip == "":
        ip = input("Digite o ip: ") 
    # O arquivo existe.
    with open(caminho,"r") as arquivo:
        i = arquivo.read().split(f"{ip}")
    print(f"O IP acessou {len(i)-1} o servidor.")
else:
    # O arquivo não existe.
    with open(caminho,"w") as arquivo:
        arquivo.write("oi\nJonatas")