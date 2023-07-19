"""
3. Escreva um programa Python que recebe como dados de entrada o nome, a altura e o sexo (M ou
F) de uma pessoa, e calcula e o peso ideal dessa pessoa, utilizando as seguintes fórmulas:
• sexo masculino: peso ideal = (72.7 * altura) - 58
• sexo feminino: peso ideal = (62.1 * altura) - 44.7
"""

nome = input("Digite seu nome: ")
altura = float(input("Digite a sua altura em METROS: "))
sexo = input("Digite M ou F para identificar o seu sexo: ")
pesoIdeal = None

if(altura > 0 and (sexo == 'M' or sexo == 'F')):
    if(sexo == 'M'):
        pesoIdeal = (72.7 * altura) - 58
    else:
        pesoIdeal = (62.1 * altura) - 44.7
    print(f"Olá, {nome}! O seu peso ideal é {pesoIdeal:.2f}Kg")
else:
    print("Você digitou algum valor INVÁLIDO, tente novamente!!")