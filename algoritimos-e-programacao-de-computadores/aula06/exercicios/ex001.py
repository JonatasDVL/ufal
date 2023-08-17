""" Algoritimos e Programação de Computadores
 Aula 06: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 01:
    Escreva um programa que possui uma função “maior”, que recebe uma lista e devolve o maior elemento na lista
"""

def maior(lista_numeros):
    maior_numero = lista_numeros[0]
    for numero in (lista_numeros):
        if(numero > maior_numero):
            maior_numero = numero
    return maior_numero


lista_numeros = [10,0,1,2,3,4,5,9,7,8,6]

print(maior(lista_numeros))
