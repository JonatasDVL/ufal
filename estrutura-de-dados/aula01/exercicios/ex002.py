#  Estrutura de Dados
#  Aula 01: Introdução 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 02:
#  2. Identificar os valores de um conjunto que estão abaixo da média do conjunto
#  Função de Custo de Tempo deste Algoritmos:

entradaConjunto = [2,-5,-9,7,-4,-1]
soma = 0

for numero in entradaConjunto:
    soma += numero     

media = soma/len(entradaConjunto)

for numero in entradaConjunto:
    if numero < media:
        print(f"O número {numero} está abaixo da média.")