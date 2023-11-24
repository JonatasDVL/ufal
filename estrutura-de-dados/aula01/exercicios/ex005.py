#  Estrutura de Dados
#  Aula 01: Introdução 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 05:
#  5. Copiar uma lista de inteiros, retirando elementos repetidos
#  Função de Custo de Tempo deste Algoritmos:

entradaConjunto = [2,-5,-9,-4,7,7,8,7,-4,-1, 2,-5]

for i in range(len(entradaConjunto)):
    cont = 0
    for j in range(i+1, len(entradaConjunto)):
        j -= cont
        if entradaConjunto[i] == entradaConjunto[j]:
            del entradaConjunto[j]
            cont += 1
            
print(entradaConjunto)            

