""" Algoritimos e Programação de Computadores
 Aula 06: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 06:
    6. Um a palavra A é dita uma permutação de uma palavra B se os caracteres de A formam uma permutação dos caracteres de B
        Ex: amor é uma permutação de roma
        Ex: metro é uma permutação de morte
    Faça uma função permutação que recebe duas palavras e verifica se uma é permutação da outra
"""

def verificandoPermutacao(palavraA, palavraB):
    if(len(palavraA) == len(palavraB)):
        condicao = 0
        for i in range(len(palavraA)):
            for j in range(len(palavraB)):
                if(palavraA[i] == palavraB[j]):
                    condicao += 1
                    j == len(palavraB)
        if(condicao >= len(palavraA)):
            permutacao = f"{palavraA} é uma permutação de {palavraB}"
            return permutacao
        else:
            permutacao = f"{palavraA} não é uma permutação de {palavraB}"
            return permutacao
    else:
        permutacao = f"{palavraA} não é uma permutação de {palavraB}"
        return permutacao

palavraA = "amor"
palavraB = "roma"

print(verificandoPermutacao(palavraA, palavraB))