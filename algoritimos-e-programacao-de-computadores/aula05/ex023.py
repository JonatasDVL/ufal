""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 23:
   4. Faça um programa programa que recebe um conjunto de inteiros e conta quantos elementos maiores que n existem no conjunto

"""


print("Este programa irá receber um conjunto de inteiros e contará quantos elementos maiores que n existem no conjunto.")

conjunto = []
maiores = []

n = int(input("Digite o valor de n: "))

r = "S"
i = 0

while(r != "NAO" and r != "N" and r != "NÃO"):
  numero = int(input("Digite o número para adicionar ao conjunto: "))
  conjunto.append(numero)
  r = input("Você deseja continuar[N/S]? ").upper()
  if(conjunto[i] > n):
    maiores.append(conjunto[i])
  i += 1

print("Todos os valores que são maiores que n: ")
print(maiores)