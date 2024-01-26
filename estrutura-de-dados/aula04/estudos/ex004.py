# 04) Implemente o Insertion Sort / Selection Sort de forma recursiva.

def selection_sort(lista, i=0, j=0, index=1):
    if i == len(lista)-1:
        return lista 
    elif index == len(lista):
        if lista[j] < lista[i]:
            lista[j], lista[i] = lista[i], lista[j]
        return selection_sort(lista, i+1, i+1, i+2)
    elif(lista[j] > lista[index]):
        return selection_sort(lista, i, index, index+1)
    elif(lista[j] < lista[index]):
        return selection_sort(lista, i, j, index+1)

def insertion_sort(lista):
    return lista

lista = [1,8,5,6]
print(selection_sort(lista))
# print(insertion_sort(lista))