""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 29:
    10. Algoritmo que recebe uma palavra e imprime o reverso dessa palavra
   
"""

palavra = input("Digite uma palavra: ")

reverso = []

i = len(palavra) - 1

while(i != -1):
    reverso.append(palavra[i])
    i -= 1

separador = ''
palavra = separador.join(reverso)
print(palavra)