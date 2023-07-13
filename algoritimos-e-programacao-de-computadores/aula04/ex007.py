""" Algoritimos e Programação de Computadores
 Aula 04: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 07:
 Faça um programa que leia dois números A e B e imprima o maior deles
 
 """ 

print("Este programa irá dizer qual dos dois números é o maior.")
numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite mais um número:"))

if numero1 > numero2:
    print(f"O primeiro número digitado({numero1}) é o maior!")
elif numero1 < numero2:
    print(f"O segundo número digitado({numero2}) é o maior!") 
elif numero1 == numero2:
    print("Os dois números são iguais!")
else:
    print("Error!!")

