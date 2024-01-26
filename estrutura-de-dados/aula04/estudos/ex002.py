# Ordenação de Strings com Insertion Sort e Selection Sort:
# Crie uma função insertion_sort_strings/selection_sort_string que recebe uma lista de strings e ordena a lista usando o algoritmo de Insertion Sort e Selection Sort.

def selection_sort_string(lista):
    for i in range(len(lista)-1):
        menor = i
        for j in range(i, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i] 
    return lista

def insertion_sort_string(lista):
    for i in range(len(lista)-1):
        j = i
        while j > 0 and lista[j] < lista[j-1]:
            lista[j], lista[j-1] = lista[j-1], lista[j] 
    return lista

lista = ["rayane","thallys","jonatas","francisco","anderson"]
print(selection_sort_string(lista))
print(insertion_sort_string(lista))