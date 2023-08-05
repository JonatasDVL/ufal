""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 32:
    13. Algoritmo que recebe um conjunto de inteiros e dois números e verifica se estes dois numeros ocorrem em sequência no conjunto
    Ex: lista = [1, 3, 5, 8, 6, 7, 4], n1 = 5 e n2 = 8

"""

numeros = []

x = int(input("Quantos números você quer adicionar ao conjunto: "))

while(x <= 0):
    x = int(input("Quantos números você quer adicionar ao conjunto: "))

for i in range(x):
    numeros.append(int(input(f"Digite o {i+1} número para adicionar ao conjunto: ")))  

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))

contador = 0
i = 0

while(len(numeros) > i and contador < 1):
    if(i > 0):
        if((numero1 == numeros[i-1] and numero2 == numeros[i]) or (numero1 == numeros[i] and numero2 == numeros[i-1])):
            contador = 1
    i += 1

if(contador == 1):
    print("Os dois números digitados ocorrem em sequência no conjunto.")
else:
    print("Os dois números digitados não ocorrem em sequência no conjunto.")
