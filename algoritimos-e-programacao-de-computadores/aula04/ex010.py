""" Algoritimos e Programação de Computadores
 Aula 04: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 10:
 Uma empresa de vendas tem vários corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 a comissão será de 9.5%. Em qualquer outro caso, a comissão será de 7%. Escreva um programa que recebe o nome e o valor vendido por um corretor e indique qual será sua comissão.
 
 """ 

print("Este programa irá receber o nome e o valor vendido por um corretor e indicará qual será sua comissão.")
nome = input("Digite seu nome:")
valor = float(input("Digite o valor da sua venda:"))
juros = None

if valor > 50000:
    juros = 0.12
elif 30000 <= valor <= 50000:
    juros = 0.095
elif 0 < valor < 30000:
    juros = 0.05
else:
    juros = 0

if juros == 0:
    print("O valor da venda está equivocado reinicie o programa!!")
else:
    comissao = valor * juros
    print(f"Olá, corretor {nome}! O valor da sua venda foi de R${valor}, logo o juros será de {juros} e sua comissao será de R${comissao:.2f}!")
