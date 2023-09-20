# 4. Faça um programa que leia a temperatura média de cada mês do ano em um arquivo e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . ).

def calculaMes(numero):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return meses[numero - 1]

arquivo = open(r"ex004\arquivo.txt", "r")
temperaturas = []
for linha in arquivo.readlines():
    linha = linha.replace("\n", "")
    temperaturas.append(linha)
arquivo.close()

media = 0
i = 0
print("Temperaturas por mês:")
for temperatura in temperaturas:
    media += float(temperatura)

media = media / len(temperaturas)
print(f"Média anual das temperaturas: {media:.2f}°C")    
for temperatura in temperaturas:
    i += 1
    mes = calculaMes(i)
    if float(temperatura) > media:
        print(f"{mes}: {temperatura}°C")
    if i == 12:
        i = 0
