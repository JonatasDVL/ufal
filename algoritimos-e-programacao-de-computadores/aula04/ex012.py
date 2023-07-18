""" Algoritimos e Programação de Computadores
 Aula 04: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 12:
    Uma das tarefas de um caixa eletrônico é decidir qual a combinação de cédulas deve fornecer ao usuário quando este solicita um saque, de modo a minimizar o número de cédulas fornecidas. Sabendo que um caixa eletrônico possui notas de 100, 50, 10, 5 e 1, faça um programa que recebe um valor a ser sacado e decida qual a combinação de cédulas irá fornecer. 

 """ 

print("Este programa irá decidir qual a combinação de cédulas deve fornecer ao usuário.")
valor = int(input("Digite o valor que queira sacar: "))

nota100 = None
nota50 = None
nota10 = None
nota5 = None
nota1 = None

if(valor >= 0):
    nota100 = valor // 100
    nota50 = (valor-nota100*100) // 50
    nota10 = (valor-nota100*100-nota50*50) // 10
    nota5 = (valor-nota100*100-nota50*50-nota10*10) // 5
    nota1 = (valor-nota100*100-nota50*50-nota10*10-nota5*5) // 1
    print(f"Notas de 100: {nota100}\nNotas de 50: {nota50}\nNotas de 10: {nota10}\nNotas de 5: {nota5}\nNotas de 1: {nota1}")
else:
    print("Você digitou um valor INVÁLIDO!!")


