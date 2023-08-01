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
i = int(input("Quantos números você quer adicionar ao conjunto: "))
j = 0
while(i != j):
    numeros.append(int(input(f"Digite o {j+1} número para adicionar ao conjunto: ")))
    if(numeros[j] < 0):
        contador += 1  
        negativos.append(numeros[j])
    j += 1

print(negativos)
print(f"{contador} é a quantidade de números negativos do conjunto criado.")