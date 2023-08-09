"""
    1. Você está implementando o controlador de uma máquina que filtra produtos com defeito em uma
    esteira de produção. A máquina está sendo utilizada para filtrar creme dental. Um item correto tem peso
    de 90g. Para a indústria, qualquer variação acima de 2 gramas para mais ou para menos, é considerada
    uma avaria no produto, e este não pode seguir para venda. Faça um programa em Python que recebe
    uma lista de pesos para os produtos que passam na esteira e decida quais destes produtos devem ser
    descartados da esteira.

    Exemplo:
    item 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    peso 90 90 91 90 93 90 89 90 87 90 85 91 90 90 86

"""

pesos = []
descartados = []

quantidade = int(input("Digite quantos produtos serão verificados: "))

for i in range (quantidade):
    peso = float(input(f"Digite o peso do {i+1}° produto: "))
    while(peso <= 0):
        print("Você digitou um valor inválido!")
        peso = float(input(f"Digite o peso do {i+1}° produto: "))
    pesos.append(peso)
    if(pesos[i] < 88 or pesos[i] > 92):
        descartados.append(i)

print(descartados)