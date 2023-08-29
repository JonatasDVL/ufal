""" Algoritimos e Programação de Computadores
 Aula 07: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 01:
     1. Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.
"""

def lerQuantidadeVogais(frase):
    vogais = "aeiou"
    frase.lower()
    quantidadeVogais = {}
    quantidadeVogais = [("A:", 0), ("B:", 0), ("C:", 0), ("D:", 0), ("E:", 0)]
    for i in range(len(frase)):
        for j in (len(vogais)):
            if frase[i] == vogais[j]: 
                quantidadeVogais[j][1] += + 1
    return quantidadeVogais 

frase = "Ana Subiu o pé de feijão."
print(lerQuantidadeVogais(frase))