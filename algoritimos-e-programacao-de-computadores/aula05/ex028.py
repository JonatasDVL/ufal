""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 28:
    9. Faça um programa que recebe um conjunto de inteiros e um valor n e indica qual o valor mais próximo de n no conjunto
   
"""

print("Este programa irá recebe um conjunto de inteiros ee um valor n e indicará qual o valor mais próximo de n no conjunto.")

numeros = []
contador = 0

x = int(input("Quantos números você quer adicionar ao conjunto: "))

while(x <= 0):
    x = int(input("Quantos números você quer adicionar ao conjunto: "))

for i in range(x):
    numeros.append(int(input(f"Digite o {i+1} número para adicionar ao conjunto: ")))  

i = 0
n = float(input("Qual o valor de n: "))

proximo = numeros[0]

while(len(numeros) > i and proximo != n):  
    if((proximo - n) < 0 and (numeros[i] - n) < 0):
        if((proximo + n) > (numeros[i] + n)):
            proximo = numeros[i]
    elif((proximo - n) < 0):
        if((proximo + n) > (numeros[i] - n)):
            proximo = numeros[i]
    elif((numeros[i] - n) < 0):
        if((proximo - n) > (numeros[i] + n)):
            proximo = numeros[i]
    else:
        if((proximo - n) > (numeros[i] - n)):
            proximo = numeros[i]

    i += 1

if(proximo == 0):
    print(f"O número do conjunto que está mais próximo de n é {proximo}, ou seja, o mesmo valor de n.")    
else:
    print(f"O número do conjunto que está mais próximo de n é {proximo}.")