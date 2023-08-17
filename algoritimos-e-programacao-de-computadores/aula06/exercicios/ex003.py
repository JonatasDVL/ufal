""" Algoritimos e Programação de Computadores
 Aula 06: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 03:
    Escreva um programa que possui uma função que recebe uma lista e diz qual a soma máxima entre dois elementos da lista
"""

def calculandoSomaMaxima(lista):
    maior_numero = lista[0]
    segundo_maior_numero = 0
    for numero in lista:
        if(maior_numero <= numero):
            segundo_maior_numero = maior_numero
            maior_numero = numero
    soma_maxima = segundo_maior_numero + maior_numero
    return soma_maxima


lista = [2,2]

print(calculandoSomaMaxima(lista))