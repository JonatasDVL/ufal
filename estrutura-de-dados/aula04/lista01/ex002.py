# 02) Implemente uma função que recebe uma lista de números e retorna o menor
# número presente na lista.

def menorNumeroLista(lista):
    menor = lista[0] 
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

lista = [2,8,9,5,1,3,0,4,-5,8,10,-7]
print(menorNumeroLista(lista))