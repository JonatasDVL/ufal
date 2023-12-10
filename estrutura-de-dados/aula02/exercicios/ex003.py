#  Estrutura de Dados
#  Aula 02: Recursividade 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 03: Implemente uma função recursiva que, dada uma lista de inteiros ordenada, busque por um valor
import random

## Forma mesmo eficiente
# def buscadorNumero(lista, n, tamanho):
#     if (tamanho == -1):
#         return False
#     elif (lista[tamanho] == n):
#         return True
#     else:    
#         return buscadorNumero(lista, n, tamanho-1)

# Forma mais eficiente
def buscadorNumero(lista, n, tamanho, times=2):
    valor = len(lista)//(2**times)
    if valor < 1:
        valor = 1
    if (times == 2):
        tamanho = tamanho//2
    if(times >= len(lista)//2+2 or tamanho < 0 or tamanho > len(lista)-1):
        return False
    elif (lista[tamanho] == n):
        return True
    elif (lista[tamanho] > n):
        return buscadorNumero(lista, n, tamanho-valor, times+1)
    elif (lista[tamanho] < n):
        return buscadorNumero(lista, n, tamanho+valor, times+1)

lista = [0,1,2,4,5,6,7,8,10]
n = random.randint(-5, 15)
# n = int(input("n: "))

print(f"O número escolhido foi {n}")
print(f"{buscadorNumero(lista, n, len(lista)-1)}")
