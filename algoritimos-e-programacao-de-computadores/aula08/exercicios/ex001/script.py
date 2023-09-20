# 1. Escreva um programa que lê um arquivo contendo a identidade e o nome de várias pessoas, no seguinte formato:
#     5384423 Manoel
#     4345566 Alberto
#     3235574 Mariana
# o programa deve gerar um dicionário no qual as chaves são as identidades e os valores os nomes. Ao final o programa deve exibir o dicionário

dados = []
dicionario = {}
arquivo = open(r"ex001\arquivo.txt", "r")
for linha in arquivo.readlines():
    chave, valor = linha.replace("\n","").split(" ")
    dicionario[chave] = valor
arquivo.close()    

print(dicionario)