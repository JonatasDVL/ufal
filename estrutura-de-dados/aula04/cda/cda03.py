# Ordenando a lista por meio de InsertionSort

lista = [2,3,6,10,8,7,5,1]

for i in range(1, len(lista)):
    j = i
    while j > 0 and lista[j] < lista[j-1]:
        # print(lista, lista[j], lista[j-1])
        lista[j], lista[j-1] = lista[j-1], lista[j]
        j -= 1

print(lista)