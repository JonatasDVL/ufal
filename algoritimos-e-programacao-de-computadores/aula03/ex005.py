""" Algoritimos e Programação de Computadores
 Aula 03: Introdução a Python 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 05:
 Programa para calcular o volume de um cilindro
   - entradas: raio e altura

 """ 

print("Este programa irá calcular o volume de uma circunferência.")
raio = float(input("Digite o valor em metros do raio da circunferência: "))
altura= float(input("Digite o valor em metros da altura da circunferência: "))
volume = (3.14 * raio**2) * altura
print(f"O volume da circunferência é aproximadamente {volume:.2f}m³")