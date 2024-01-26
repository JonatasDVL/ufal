# 2. Você está realizando um experimento para comparar o algoritmo insertion sort e selection sort. O
# critério de avaliação desse experimento é o número de comparações realizadas pelo algoritmo. Implemente
# os dois algoritmos recebendo uma mesma lista de entrada e imprima na tela o número de comparações
# realizadas por cada algoritmo.

def selection_sort(lista):
    count=0
    for i in range(len(lista)-1):
        min = i
        for j in range(i+1, len(lista)):
            count += 1
            if lista[min] > lista[j]:
                min = j
        lista[min], lista[i] = lista[i], lista[min]
    return lista, count

def insertion_sort(lista):
    count=0
    for i in range(1, len(lista)):
        j = i
        if lista[j-1] < lista[j]: # esse contador não é necessário no codigo normal, porém é necessário para contar  
            count += 1            # com exatidão a quantidade de comparação feito pelo insertion sort.
        while j > 0 and lista[j-1] > lista[j]:
            count += 1
            lista[j-1], lista[j] = lista[j], lista[j-1]
            j -= 1
    return lista, count

lista = [0,1,2,3,4,5,6,7,8,9]
lista2 = [0,1,2,3,4,5,6,7,8,9]
lista1, count1 = selection_sort(lista)
lista2, count2 = insertion_sort(lista2)

print(f"Lista Ordenada pelo Selecion Sort: {lista1}, Comparações feitas: {count1}")
print(f"Lista Ordenada pelo Insertion Sort: {lista2}, Comparações feitas: {count2}")
