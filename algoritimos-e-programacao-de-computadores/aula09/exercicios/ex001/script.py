# 1. Faça um programa que lê um arquivo csv contendo dados de temperatura e umidade em vários dias em uma cidade e diga qual foi o dia mais quente o mais frio da cidade.
import pandas as pd
import os

caminho = os.path.abspath(__file__)
caminho = caminho.replace("script.py", "arquivo.csv")

def maiorTemperatura(dadosClima):
    temperaturaMaisQuente = dadosClima["temperatura"][0]
    diasMaisQuente = []
    for i in range(len(dadosClima["temperatura"])):    
        if temperaturaMaisQuente == dadosClima["temperatura"][i]:
            diasMaisQuente.append(dadosClima["dia"][i])
        elif temperaturaMaisQuente < dadosClima["temperatura"][i]:
            diasMaisQuente = []
            temperaturaMaisQuente = dadosClima["temperatura"][i]
            diasMaisQuente.append(dadosClima["dia"][i])
    return diasMaisQuente, temperaturaMaisQuente

def menorTemperatura(dadosClima):
    temperaturaMaisFrio = dadosClima["temperatura"][0]
    diasMaisFrio = []
    for i in range(len(dadosClima["temperatura"])):    
        if temperaturaMaisFrio == dadosClima["temperatura"][i]:
            diasMaisFrio.append(dadosClima["dia"][i])
        elif temperaturaMaisFrio > dadosClima["temperatura"][i]:
            diasMaisFrio = []
            temperaturaMaisFrio = dadosClima["temperatura"][i]
            diasMaisFrio.append(dadosClima["dia"][i])
    return diasMaisFrio, temperaturaMaisFrio

def mostrarMensagem(dias,temperatura, status):
    if len(dias) > 1:    
        print(f"A temperatura dos dias mais {status}s foi {temperatura}C°.")
        print(f"Esse foram os dias mais {status}:")
        for i in dias:
            print(f"{i}",end=" ")
        print()
    else:
        print(f"A temperatura do {dias[0]}, o mais {status}, foi {temperatura}C°.")

    return

dadosClima = pd.read_csv(caminho)
print(dadosClima)

diasMaisQuente, temperaturaMaisQuente = maiorTemperatura(dadosClima)
diasMaisFrio, temperaturaMaisFrio = menorTemperatura(dadosClima)

mostrarMensagem(diasMaisQuente, temperaturaMaisQuente, "quente")
mostrarMensagem(diasMaisFrio, temperaturaMaisFrio, "frio")