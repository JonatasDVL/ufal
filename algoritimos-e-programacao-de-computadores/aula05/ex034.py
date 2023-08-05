""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 34:
    15. Algoritmo que recebe dois conjuntos de inteiros A e B de tamanho n e calcula a distância euclidiana entre esses conjuntos. A distância euclidiana é dada por
    D(A,B) = √(A[1] – B[1])² + (A[2] - B[2])² + … + (A[n] - B[n])²

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