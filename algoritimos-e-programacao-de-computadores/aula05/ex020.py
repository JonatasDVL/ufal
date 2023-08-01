""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 20:
    1. Faça um programa que recebe um número e calcula o fatorial desse número 

"""

print("Este programa irá recebe um número e calcula o fatorial desse número.")
numero = int(input("Digite o número para calcular o seu fatorial: "))
fator = 1
produto = 1

if(numero == 0):
    print("O fatorial de 0 é 1 ")
elif(numero > 0):
    while(numero != (fator-1)):
        produto = produto * fator
        fator += 1
    print(f"O fatorial de {numero} é {produto}")
else:
    print("Você digitou um número inválido.")
    
