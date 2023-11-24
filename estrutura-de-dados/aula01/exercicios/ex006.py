#  Estrutura de Dados
#  Aula 01: Introdução 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 06:
#  6. Algoritmo que recebe duas listas e imprime a intersecção das duas listas
#  Função de Custo de Tempo deste Algoritmos:

lista1 = [0,1,2,3,4,5,6,7,8]
lista2 = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
lista3 = []

for numero1 in lista1:
    for numero2 in lista2:
        if numero1 == numero2:
            lista3.append(numero1)
            break

print(lista3)