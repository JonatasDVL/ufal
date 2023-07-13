""" Algoritimos e Programação de Computadores
 Aula 04: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 08:
 Faça um programa que leia a idade de uma pessoa e imprima sua categoria:
    - Criança, se menor de 14 anos
    - Adolescente, se entre 14 e 17 anos
    - Adulto, se entre 18 e 59 anos
    - Idoso, se maior que 60 anos

 """ 

print("Este programa irá ler qual a idade de uma pessoa e dizer sua categoria.")
idade = int(input("Digite a sua idade:"))

if idade < 14 and idade > 0:
    print(f"Você tem {idade} anos, logo você é uma Criança!")
elif idade <= 17 and idade > 0:
    print(f"Você tem {idade} anos, logo você é um Adolescente!")
elif idade <= 59 and idade > 0:
    print(f"Você tem {idade} anos, logo você é um adulto!") 
elif idade >= 60 and idade <= 122:
    print(f"Você tem {idade} anos, logo você é um idoso!")
elif idade >= 122:
    print(f"Interessante, você tem {idade} anos, logo você é um idoso, por enquanto, acho bom você entrar no guines book o mais rápido possível!")
else:
    print("Error!!")

