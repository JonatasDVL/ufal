""" Algoritimos e Programação de Computadores
 Aula 06: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 02:
    Escreva um programa que possui uma função que recebe uma lista e um valor e verifica se existe o valor na lista
"""

def verificadorValor(lista, valor):
    for elemento in lista:
        if(str(elemento) == valor):
            resultado = "Sim, existe esse valor na lista."
            return resultado
        else:
            resultado = "Não, não existe esse valor na lista."
    return resultado

lista = [1,2,3,4,5,6,7,8,9,10]
valor = input("Digite um valor: ")
print(verificadorValor(lista, valor))