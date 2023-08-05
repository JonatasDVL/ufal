""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 31:
    12. Algoritmo que recebe uma palavra e conta quantas vogais há na palavra

"""

palavra = input("Digite uma palavra: ")

i = 0
contador = 0

while(len(palavra) > i):
    if("a" == palavra[i] or "e" == palavra[i] or "i" == palavra[i] or "o" == palavra[i] or "u" == palavra[i]):
        contador +=1
    i += 1

if(contador > 0):
    print(f"Na palavra '{palavra}' tem {contador} vogais.")
else:
    print(f"Na palavra '{palavra}' não tem {contador} vogais.")

