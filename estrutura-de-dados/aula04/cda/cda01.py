
lista = [2,3,6,10,8,7,5,1]

# Ordenando a lista por meio de SelectionSort
def selectionSort(lista):
    for i in range(len(lista)-1):
        menor = i
        for j in range(i+1,len(lista)):
            if lista[menor] > lista[j]:
                menor = j    
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

selectionSort(lista)

print(lista)