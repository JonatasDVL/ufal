""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor: Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 21:
    2. Faça um programa que conta o número de valores negativos em um conjunto  
 
"""

print("Este programa irá contar o número de valores negativos em um conjunto.")

numeros = []
negativos = []
contador = 0
x = int(input("Quantos números você quer adicionar ao conjunto: "))

for i in range(x):
    numeros.append(int(input(f"Digite o {i+1} número para adicionar ao conjunto: ")))
    if(numeros[i] < 0):
        contador += 1  
        negativos.append(numeros[i])

print(negativos)
print(f"{contador} é a quantidade de números negativos do conjunto criado.")