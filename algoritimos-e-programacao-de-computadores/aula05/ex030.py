""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 30:
    11. Algoritmo que recebe uma palavra e um caractere e conta as ocorrências do caractere na palavra

"""

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

i = 0

while(len(palavra) > i and letra != palavra[i]):
    i += 1

if(i < len(palavra)):
    print(f"Na palavra '{palavra}' tem a letra '{letra}'.")
else:
    print(f"Na palavra '{palavra}' não tem a letra '{letra}'.")

