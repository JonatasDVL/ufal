""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 15:
    Calcular a média de uma lista de inteiros.

 """ 

""" outra forma
numeros = [0,1,2,3,4,5,6,7,8,9,10]
soma = 0

for i in numeros:
    soma += i

media = soma / (len(numeros)) 
print(media)

"""

numeros = []
soma = 0
quantidade = int(input("Digite a quantidade de números que você deseja digitar: "))

for i in range (quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    soma += numeros[i]

media = soma / (len(numeros)) 
print(media)
