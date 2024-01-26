# Inserção Decrescente:
# Modifique a função selection_sort/insertion_sort para aceitar um parâmetro adicional chamado reverse (padrão False). Se reverse for True, a função deve ordenar a lista em ordem decrescente.

def selection_sort(lista, reverse=False):
    for i in range(len(lista)-1):
        index = i
        for j in range(i, len(lista)):
            if reverse == False and lista[j] < lista[index]:
                index = j
            elif reverse == True and lista[j] > lista[index]:
                index = j
        lista[i], lista[index] = lista[index], lista[i]
    return lista

def insertion_sort(lista, reverse=False):
    for i in range(len(lista)-1):
        j = i
        while j > 0 and reverse == False and lista[j] < lista[j-1]:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            j -= 1
        while j > 0 and reverse == True and lista[j] > lista[j-1]:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            j -= 1
    return lista

lista = [9,0,1,5,4,7,2,6,4,3]
print(selection_sort(lista, False))
print(insertion_sort(lista, False))