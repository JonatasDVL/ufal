""" Algoritimos e Programação de Computadores
 Aula 06: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 07:
    7. Faça um programa que tenha duas funções, uma para calcular a média e outra para calcular a variância de um conjunto de números.
"""

def calcularMedia(conjunto_numeros):
    soma = 0
    for numeros in conjunto_numeros:
        soma += numeros
    media = soma / len(conjunto_numeros)
    return media

def calcularVariancia(conjunto_numeros, media):
    soma_diferenciada = 0
    for numeros in conjunto_numeros:
        soma_diferenciada += (numeros - media)**2
    variancia = soma_diferenciada / len(conjunto_numeros)
    return variancia

conjunto_numeros = [0,1,2,3,4,5,6,7,8,9,10]

media = calcularMedia(conjunto_numeros)
print(media)
print(calcularVariancia(conjunto_numeros, media))