#  Estrutura de Dados
#  Aula 02: Recursividade 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 03: Implemente uma função recursiva que, dada uma lista de inteiros ordenada, busque por um valor
import random

def buscadorNumero(lista, n, tamanho):
    tamanho = tamanho-1
    if (tamanho == -1):
        return False
    elif (lista[tamanho] == n):
        return True
    else:    
        return buscadorNumero(lista, n, tamanho)


lista = [-10,-9,-8,-7,-5,-4,-3,-1,0,1,2,4,5,6,7,8,10]
n = random.randint(-20, 20)
# n = int(input("n: "))

print(f"O número escolhido foi {n}\n{buscadorNumero(lista, n, len(lista))}")
