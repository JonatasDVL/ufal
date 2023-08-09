"""
    3. Uma organização não-governamental está realizando um estudo com uma determinada comunidade. Uma das características analisadas desta comunidade foi o índice de massa corporal (IMC), com
    o objetivo de identificar as pessoas que estão abaixo do peso ideal. O IMC é calculado dividindo o peso
    (em kg) pela altura (em metros) ao quadrado (eq. 1). Você foi então contratado para criar um programa
    que automatiza o processamento destes dados. O programa recebe como entrada uma lista com o peso
    e uma lista com a altura de um conjunto de entrevistados. O programa deve calcular o IMC de cada
    pessoa da lista e classificar a situação de cada pessoa de acordo com a tabela.
    IMC =
    peso
    altura2
    (1)
    IMC Situação
    Abaixo de 18,49 Abaixo do peso
    Entre 18,5 e 24,99 Peso normal
    Entre 25 e 29,99 Acima do peso
    Acima de 30 Obesidade

"""

pesos = []
alturas = []
imcs = []
situacoes = []
peso = 1
altura = 1

quantidade = int(input("Digite quantidade de pessoas examinadas: "))

for i in range (quantidade):
    peso = float(input(f"Digite o peso da {i+1}° pessoa: "))
    while(peso <= 0):
        print("Você digitou um valor inválido!")
        peso = float(input(f"Digite o peso da {i+1}° pessoa: "))
    pesos.append(peso)

    altura = float(input(f"Digite a altura da {i+1}° pessoa: "))
    while(peso <= 0):
        print("Você digitou um valor inválido!")
        altura = float(input(f"Digite a altura da {i+1}° pessoa: "))
    alturas.append(altura)
    
    imcs.append(pesos[i]/(alturas[i]**2))
    if(imcs[i] <= 18.49):
        situacoes.append("abaixo do peso.")
    elif(imcs[i] <= 24.99):
        situacoes.append("no peso normal.")
    elif(imcs[i] <= 29.99):
        situacoes.append("acima do peso.")
    else:
        situacoes.append("com obesidade.")

for i in range(quantidade):
    print(f"O imc da {i+1} pessoa é {imcs[i]:.2f}, ou seja, essa pessoa está ",situacoes[i])