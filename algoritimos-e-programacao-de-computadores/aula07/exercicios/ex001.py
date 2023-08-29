""" Algoritimos e Programação de Computadores
 Aula 07: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 01:
     1. Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.
"""

def lerQuantidadeVogais(frase):
    vogais = "AEIOU"
    vogaisAcentuadas = "ÂÃÁÀÉÊÍÎÓÔÕÚÛ"
    vogaisAcentuadasSemAcento = "AAAAEEIIOOOUU"
    frase = frase.upper()
    quantidadeVogais = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    for i in range(len(frase)):
        condicao = False
        for j in vogais:
            if frase[i] == j: 
                quantidadeVogais[j] += 1
                condicao = True
                break
        if condicao == False:
            x = 0
            for j in vogaisAcentuadasSemAcento:
                if frase[i] == vogaisAcentuadas[x]: 
                    quantidadeVogais[j] += 1
                    break
                x += 1
    return quantidadeVogais 

frase = input("Digite uma frase: ") 
print(lerQuantidadeVogais(frase))