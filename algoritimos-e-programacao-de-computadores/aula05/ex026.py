""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 26:
    7. Faça um programa que recebe um conjunto de inteiros e verifica se existe algum número negativo no conjunto
   
"""

print("Este programa irá recebe um conjunto de inteiros e verificará se existe algum número negativo no conjunto.")

numeros = []
contador = 0
x = int(input("Quantos números você quer adicionar ao conjunto: "))

for i in range(x):
    numeros.append(int(input(f"Digite o {i+1} número para adicionar ao conjunto: ")))  

i = 0
while(len(numeros) > i and numeros[i] >= 0):  
    i += 1

print(i)
if(len(numeros) > i):
    print(f"Sim, o conjunto tem números negativos.")
else:
    print(f"Não, o conjunto não tem números negativos.")