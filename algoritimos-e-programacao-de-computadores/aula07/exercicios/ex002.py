""" Algoritimos e Programação de Computadores
 Aula 07: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 02:
     2. Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma função que retorna a média do aluno, dado seu nome.
"""

def calculaMediaNotasAlunos (nota1, nota2):
    media = (nota1 + nota2) /2
    return media

boletinsAlunos = {}
i = 1

while i == 1 or nome != "":
    nome = input(f"Digite nome do {i}° aluno: ")
    if nome != "":
        nota1 = float(input(f"Digite a primeira nota de {nome}: "))
        nota2 = float(input(f"Digite a segunda nota de {nome}: "))
        boletinsAlunos[nome] = [nota1, nota2]
    i += 1

nome = input(f"Digite nome do aluno que deseja ver a nota: ")
while nome != "":
    if nome in boletinsAlunos:
        media = calculaMediaNotasAlunos(boletinsAlunos[nome][0], boletinsAlunos[nome][1])
        print(f"A média de {nome} é de {media}")
    else:
        print("Você digitou um nome inválido. Tente novamente!!")
    nome = input(f"Digite nome do aluno que deseja ver a nota: ")

