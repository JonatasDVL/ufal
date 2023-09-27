# 2. Faça um programa que recebe do usuário duas notas de vários alunos e escreve um arquivo csv contendo as duas notas e a média do aluno.
import pandas as pd
import os

caminho = os.path.abspath(__file__)
caminho = caminho.replace("script.py", "arquivo.csv")

dados = {
    "Nome": [],
    "Nota1": [],
    "Nota2": [],
    "Média": []
}

resposta = "s"
i = 1

while resposta == "s":
    dados["Nome"].append(input(f"Digite o nome do {i}º aluno: "))
    dados["Nota1"].append(float(input(f"Digite a primeira nota do {i}º aluno: ")))
    dados["Nota2"].append(float(input(f"Digite a segunda nota do {i}º aluno: ")))
    dados["Média"].append((dados["Nota1"][i-1]+dados["Nota2"][i-1])/2)

    i += 1
    resposta = input("Digite (s) se desejas continuar a adicionar dados: ").lower()

dadosNotas = pd.DataFrame(dados) 
dadosNotas.to_csv(caminho ,index=False)

print(dadosNotas)