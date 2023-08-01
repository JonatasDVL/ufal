""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 22:
   3. Faça um programa que recebe um conjunto de inteiros e imprime os valores que estão abaixo da média do conjunto

"""

print("Este programa irá receber um conjunto de inteiros e imprimir os valores que estão abaixo da média do conjunto.")
x = int(input("Digite a quantidade de números que deseja adicionar no conjunto: "))
conjunto = []
abaixo = []
soma = 0

for i in range(x):
  numero = int(input("Digite o número para adicionar ao conjunto: "))
  conjunto.append(numero)
  soma += numero

media = soma/x

for i in range(x):
  if(conjunto[i] < media):
    abaixo.append(conjunto[i])

print("Todos os valores que estão a abaixo da média: ")
print(abaixo)