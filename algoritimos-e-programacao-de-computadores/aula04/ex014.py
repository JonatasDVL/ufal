""" Algoritimos e Programação de Computadores
 Aula 04: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 14:
    Escreva  um algoritmo que lê dois inteiros A e B e os escreve com a mensagem: “São múltiplos” ou “Não são múltiplos”.

 """ 

print("Este programa irá calcular se os dois números inseridos são múltiplos ou não.")
a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

if(a % b or b % a):
    print("Os dois números são múltiplos.")
else:
    print("Os dois números não são múltiplos.")