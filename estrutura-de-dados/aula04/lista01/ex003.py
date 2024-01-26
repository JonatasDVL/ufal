# 03) Implemente um algoritmo de ordenação seguindo a lógica do Selection Sort, sua
# implementação deve retornar, além da lista ordenada, uma variável contadora que
# acompanha o número de comparações feitas durante o processo de ordenação.

def selectionSort(lista):
    count = 0
    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            count +=1
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista, count

lista = [9,8,7,6,5,4,3,2,1,0]
print(selectionSort(lista))