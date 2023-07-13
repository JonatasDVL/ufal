""" Algoritimos e Programação de Computadores
 Aula 04: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 09:
 Faça um programa que receba três números e ordene eles em ordem crescente.
 
 """ 

print("Este programa irá receber três números e ordene eles em ordem crescente.")
numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite mais um número:"))
numero3 = float(input("Digite mais um número:"))


if numero1 <= numero2 <= numero3:
    print(f"Os números em ordem crescente: {numero1}, {numero2}, {numero3}")
elif numero1 <= numero2 >= numero3 and numero1 <= numero3:
    print(f"Os números em ordem crescente: {numero1}, {numero3}, {numero2}")
elif numero1 >= numero2 <= numero3 and numero1 <= numero3:
    print(f"Os números em ordem crescente: {numero2}, {numero1}, {numero3}")
elif numero1 >= numero2 <= numero3 and numero1 >= numero3:
    print(f"Os números em ordem crescente: {numero2}, {numero3}, {numero1}")
elif numero1 <= numero2 >= numero3 and numero1 >= numero3:
    print(f"Os números em ordem crescente: {numero3}, {numero1}, {numero2}")
elif numero1 >= numero2 >= numero3:
    print(f"Os números em ordem crescente: {numero3}, {numero2}, {numero1}")
else:
    print("ERRO!!")