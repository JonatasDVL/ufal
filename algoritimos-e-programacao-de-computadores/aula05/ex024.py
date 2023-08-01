""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 24:
   5. Faça um programa que recebe um conjunto de inteiros e calcula a amplitude do conjunto.

"""

print("Este programa irá receber um conjunto de inteiros e calculará a amplitude do conjunto.")

conjunto = []

r = "S"
i = 0

while(r != "NAO" and r != "N" and r != "NÃO"):
  numero = int(input("Digite o número para adicionar ao conjunto: "))
  conjunto.append(numero)
  r = input("Você deseja continuar[N/S]? ").upper()
  if(i == 1):
    if(conjunto[i] > conjunto[i-1]):
      maior = conjunto[i]
      menor = conjunto[i-1]
    else:
      maior = conjunto[i-1]
      menor = conjunto[i]
  elif(i > 1):
    if(conjunto[i] > maior):
      maior = conjunto[i]
    elif(conjunto[i] < menor):
      menor = conjunto[i]
  i += 1

amplitude = maior - menor

print(f"O maior número do conjunto é {maior} e o menor é {menor}, logo a amplitude é {amplitude}.")