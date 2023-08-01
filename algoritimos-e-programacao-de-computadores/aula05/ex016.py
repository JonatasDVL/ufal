""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 16:
    Buscar um elemento em uma lista de inteiros.

 """ 

numeros = [0,1,2,3,4,5,6,7,8,9,10]
numero = int(input("Digite um número inteiro para ver se tem na lista: "))
condicao = False

for i in numeros:
    if (numero == i):
        condicao = True
        break
    else:
        condicao = False
if (condicao == True):
    print(f"O número {numero} tem na lista!")
else:
    print(f"O número {numero} não tem na lista!")
    
