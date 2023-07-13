""" Algoritimos e Programação de Computadores
 Aula 03: Introdução a Python 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 05:
 Programa que calcula o pagamento com atraso de um boleto bancário
    - O valor final a ser pago é dado por
    - Total = valor + multa + (valor*juros*dias)
    - Sabendo que a multa é de 2 e a taxa de juros é de 0,05

 """ 

print("Este programa irá calcular o pagamento com atraso de um boleto bancário.")
valor = float(input("Digite o valor do boleto: "))
dias = int(input("Digite a quantidade de dias que atrasou o pagamento: "))
multa = 2
juros = 0.05
total = (valor*juros*dias) + valor + multa
print(f"O valor total a ser pago é R${total:.2f}")