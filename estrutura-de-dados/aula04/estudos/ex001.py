# Implementação do Insertion Sort e Selection Sort:
# Implemente a função insertion_sort/selection_sort que recebe uma lista de números e ordena a lista usando o algoritmo de Insertion Sort e Selection Sort.

def selection_sort(lista):
    for i in range(len(lista)-1):
        min = i
        for j in range(i, len(lista)):
            if lista[j] < lista[min]:
                min = j
        lista[min], lista[i] = lista[i], lista[min]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j] < lista[j-1]:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            j -= 1
    return lista

lista = [9,0,1,5,4,7,2,6,4,3]
print(selection_sort(lista))
print(insertion_sort(lista))

