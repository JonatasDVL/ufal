# CSV para Dicionário:
# Crie um programa que lê um arquivo CSV (valores separados por vírgula) e o converte em um dicionário onde a primeira linha do arquivo contém os nomes das chaves e as linhas subsequentes contêm os valores.

import os
caminho = os.path.abspath(__file__).replace("script.py", "arquivo.csv")
import pandas as pd

if os.path.isfile(caminho):
    # O arquivo existe.
    data = {}
    df = pd.read_csv(caminho)
    for chave in df.keys():
        lista = []
        for valor in df[f"{chave}"]:
            lista.append(valor)
        data[f"{chave}"] = lista
    print(data)
else:
    # O arquivo não existe.
    data = {
        "nome":["Jônatas","Jônatas","Thallys","Francisco"],
        "idade":[19,19,18,18],
    }
    df = pd.DataFrame(data)
    df.to_csv(caminho, index=False)

