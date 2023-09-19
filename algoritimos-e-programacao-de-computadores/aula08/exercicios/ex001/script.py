# 1. Escreva um programa que lê um arquivo contendo a identidade e o nome de várias pessoas, no seguinte formato:
#     5384423 Manoel
#     4345566 Alberto
#     3235574 Mariana
# o programa deve gerar um dicionário no qual as chaves são as identidades e os valores os nomes. Ao final o programa deve exibir o dicionário

dados = []

arquivo = open(r"C:\Users\jonat\OneDrive\Documentos\GitHub\ufal\algoritimos-e-programacao-de-computadores\aula08\exercicios\ex001\arquivo.txt", "r")
for linha in arquivo.readlines():
    linha = linha.replace("\n","")
    dados.append(linha)
arquivo.close()

print(dados)

dicionario = {}
for atributos in dados:
    atributo = atributos.split(" ")
    dicionarioTemp = {atributo[0]:atributo[1]}
    dicionario |= dicionarioTemp

print(dicionario)