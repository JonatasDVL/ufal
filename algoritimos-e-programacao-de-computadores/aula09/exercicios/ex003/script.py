# 3. Faça um programa que recebe dados de vários contatos (nome, telefone, email) e escreve os dados em um arquivo csv. O programa tem uma função que lê o arquivo e faz busca pelo nome do contato.

import pandas as pd
import os

# pegando do arquivo caminho
caminho = os.path.abspath(__file__)
caminho = caminho.replace("script.py", "arquivo.csv")

def escreverDadosArquivos(dados, caminho):
    df = pd.DataFrame(dados)
    df.to_csv(caminho, index=False)
    return

def lerDadosArquivos(caminho):
    dados = pd.read_csv(caminho)
    return dados

def buscarDadosArquivos(caminho, nome):
    dados = lerDadosArquivos(caminho)
    resultado = ""
    for i in range(len(dados["Nome"])):
        if dados["Nome"][i] == nome:
            for chave in dados.keys():
                resultado += f"{dados[chave][i]} "
            return resultado
    resultado = "Não existe contato com esse nome."
    return resultado


dados = {
    "Nome": [],
    "Telefone": [],
    "E-mail": [] 
    }
resposta = "s"
i = 1

while resposta == "s":
    dados["Nome"].append(input(f"Digite o nome do {i}º contato: "))
    dados["Telefone"].append(input(f"Digite o telefone do {i}º contato: "))
    dados["E-mail"].append(input(f"Digite o e-mail do {i}º contato: "))

    i += 1
    resposta = input("Digite (s) se desejas continuar a adicionar dados: ").lower()

escreverDadosArquivos(dados, caminho)

nome = input("Qual o nome do Contato que desejas procurar: ")
print(buscarDadosArquivos(caminho, nome))