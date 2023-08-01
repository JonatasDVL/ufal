""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 25:
    6. Faça um algoritmo que recebe dois conjuntos de inteiros A e B e calcula a distância euclidiana entre estes dois conjuntos
   
"""

print("Este programa irá receber um conjunto de inteiros e calculará a amplitude do conjunto.")

conjuntoA = []
conjuntoB = []

r = "S"
i = 0

while(r != "NAO" and r != "N" and r != "NÃO"):
  numero = int(input("Digite o número para adicionar ao conjunto: "))
  conjuntoA.append(numero)
  r = input("Você deseja continuar[N/S]? ").upper()

r = "S"

while(r != "NAO" and r != "N" and r != "NÃO"):
  numero = int(input("Digite o número para adicionar ao conjunto: "))
  conjuntoB.append(numero)
  r = input("Você deseja continuar[N/S]? ").upper()
