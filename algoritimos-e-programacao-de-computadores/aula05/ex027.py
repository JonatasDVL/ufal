""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 27:
    8. Faça um programa que recebe um conjunto de inteiros e um valor n e verifica se existe algum número com valor maior que n no conjunto 
   
"""

print("Este programa irá recebe um conjunto de inteiros e um valor n e verificará se existe algum número com valor maior que n no conjunto.")

numeros = []
contador = 0
x = int(input("Quantos números você quer adicionar ao conjunto: "))

while(x <= 0):
    x = int(input("Quantos números você quer adicionar ao conjunto: "))

for i in range(x):
    numeros.append(int(input(f"Digite o {i+1} número para adicionar ao conjunto: ")))  

i = 0
n = float(input("Qual o valor de n: "))

while(len(numeros) > i and numeros[i] <= n):  
    i += 1

if(len(numeros) > i):
    print(f"Sim, no conjunto tem pelo menos um número maior que n.")
else:
    print(f"Não, no conjunto não tem pelo menos um número maior que n.")