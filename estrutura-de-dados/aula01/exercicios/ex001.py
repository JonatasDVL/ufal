#  Estrutura de Dados
#  Aula 01: Introdução 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 01:
#  1. Contar o número de elementos negativos em um conjunto
#  Função de Custo de Tempo deste Algoritmos:

entradaConjunto = [2,-5,-
]9,7,-4]
contador = 0

for numero in entradaConjunto:
    if numero < 0:
        contador +=1 

print(f"O número de elementos negativos é {contador} elementos.")