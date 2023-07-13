""" Algoritimos e Programação de Computadores
 Aula 03: Introdução a Python 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 03:
 Programa para converter dolar para real
   - entradas: valor e taxa de câmbio

 """ 
print("Este programa irá converter o valor do dolar para real.")
valorDolar = float(input("Digite o valor em dolar que deseja converter: "))
taxaCambio = float(input("Digite o valor da taxa de câmbio: "))
valorReal = (taxaCambio * valorDolar)
print(f"US${valorDolar:.2f} equivale a R${valorReal:.2f}")