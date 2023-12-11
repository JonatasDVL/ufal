#  Estrutura de Dados
#  Aula 02: Recursividade 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 03: Implemente uma função recursiva que, dada uma lista de inteiros ordenada, busque por um valor

import random

## Forma menos eficiente
# def buscadorNumero(lista, n, tamanho):
#     if (tamanho == -1):
#         return False
#     elif (lista[tamanho] == n):
#         return True
#     else:    
#         return buscadorNumero(lista, n, tamanho-1)

# # Forma mais eficiente
# def buscadorNumero(lista, n, tamanho, times=2):
#     valor = len(lista)//(2**times)
#     if valor < 1:
#         valor = 1
#     if (times == 2):
#         tamanho = tamanho//2
#     if(times >= pontoMedio+2 or tamanho < 0 or tamanho > len(lista)-1):
#         return False
#     elif (lista[tamanho] == n):
#         return True
#     elif (lista[tamanho] > n):
#         return buscadorNumero(lista, n, tamanho-valor, times+1)
#     elif (lista[tamanho] < n):
#         return buscadorNumero(lista, n, tamanho+valor, times+1)

# Forma Plus de eficiência

def buscadorNumero(lista, n):
    pontoMedio = len(lista)//2
    if (len(lista) == 0):  
        return False
    elif(lista[pontoMedio] == n):
        return True
    elif(lista[pontoMedio] > n):
        return buscadorNumero(lista[:pontoMedio], n)
    elif(lista[pontoMedio] < n):
        return buscadorNumero(lista[pontoMedio+1:], n)

lista = [1,2,3,5,6,7,9,10]
n = random.randint(-5, 15)
# n = int(input("n: "))

print(f"O número escolhido foi {n}")
print(f"{buscadorNumero(lista, n)}")
