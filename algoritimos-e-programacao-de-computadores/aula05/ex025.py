""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 25:
    6. Faça um algoritmo que recebe dois conjuntos de inteiros A e B e calcula a distância euclidiana entre estes dois conjuntos
   
"""

conjuntoA = []
conjuntoB = []
euclidiana = 0

n = int(input("Quantos números você quer adicionar aos conjuntos: "))

while(n <= 0):
    n = int(input("Quantos números você quer adicionar ao conjunto: "))

for i in range(n):
    conjuntoA.append(int(input(f"Digite o {i+1} número para adicionar ao conjunto A: ")))  

for i in range(0, n):
    conjuntoB.append(int(input(f"Digite o {i+1} número para adicionar ao conjunto B: ")))  

for i in range(0, n):
    euclidiana += (conjuntoA[i] - conjuntoB[i])**2 

euclidiana = euclidiana ** (1/2)

print(f"O valor da distância euclidiana é {euclidiana:.2f}")