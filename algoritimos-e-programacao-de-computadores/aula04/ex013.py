""" Algoritimos e Programação de Computadores
 Aula 04: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 13:
    Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.
 
 """ 

print("Este programa irá calcular o salário final do vendedor.")
quantidadeCarros = int(input("Digite a quantidade de carros vendidos: "))
valorTotal = float(input("Digite o valor total de suas vendas: "))
salario = float(input("Digite o seu salário: "))
comissaoCarros = float(input("Digite a o valor que recebe por cada carro vendido: "))
salarioFinal = None

salarioFinal = salario + (valorTotal * 0.05) + (quantidadeCarros * comissaoCarros)

if(quantidadeCarros >= 0 and salario > 0 and valorTotal >= 0 and comissaoCarros >= 0):
    print(f"O salário final do vendedor será R${salarioFinal:.2f}.")
else:
    print("Você digitou algum valor INVÁLIDO!!")