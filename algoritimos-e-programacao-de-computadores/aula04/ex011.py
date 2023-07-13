""" Algoritimos e Programação de Computadores
 Aula 04: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 11:
 Escreva um algoritmo que recebe três valores para os lados de um triângulo (a,b e c) e decide se a forma geométrica é um triângulo ou não e em caso positivo, classifique em isósceles, escaleno ou equilátero.
    - O valor de cada lado deve ser menor que a soma dos outros dois
    - Isósceles: dois lados iguais e um diferente
    - Escaleno: todos os lados diferentes
    - Equilátero: todos os lados iguais

 """ 

print("Este programa irá receber três valores para os lados de um triângulo e indicará o tipo dele.")

lado1 = float(input("Digite o tamanho em metros do primeiro lado do triângulo: "))
lado2 = float(input("Digite o tamanho em metros do segundo lado do triângulo: "))
lado3 = float(input("Digite o tamanho em metros do terceiro lado do triângulo: "))

if (lado1 + lado2 >= lado3 and lado2 + lado3 >= lado1 and lado1 + lado3 >= lado2 and lado1 > 0 and lado2 > 0 and lado3 > 0):
    if (lado1 == lado2 == lado3):
        print("equilátero")
    elif (lado1 != lado2 != lado3):
        print("Escaleno")
    else:
        print("isosceles")
else:
    print("Você não digitou um triângulo com valores corretos")
