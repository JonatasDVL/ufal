def quickSort(lista): 
  tamanhoDaLista = len(lista)
  if tamanhoDaLista <= 1:
    return lista
  else:
    pivo = tamanhoDaLista//2
    i = 0
    j = tamanhoDaLista-1
    while i < j:
      if lista[i] <= lista[pivo] and i != pivo:
        i += 1
      elif lista[j] >= lista[pivo] and j != pivo:
        j -= 1
      else:
        lista[i], lista[j] = lista[j], lista[i]
        if pivo == j:
          pivo = i
          i -=1
        elif pivo == i:
          pivo = j
          j +=1
        i +=1
        j -=1
    return quickSort(lista[:pivo]) + quickSort(lista[pivo:])

lista1 = [9,8,7,6,5,4,3,2,1]
print(quickSort(lista1))
lista2 = [1,2,3,4,5,6,7,8,9]
print(quickSort(lista2))
lista3 = [2,1,4,3,6,5,8,7,9]
print(quickSort(lista3))
lista4 = [9,2,1,4,3,6,5,8,7]
print(quickSort(lista4))
lista5 = [3,5,8,4,2,1,9,0]
print(quickSort(lista5))
lista6 = [3,5,8,1,2,1,9,0]
print(quickSort(lista6))
lista7 = [9,8,7,6,5,4,3,2,1,0]
print(quickSort(lista7))
lista8 = [0,1,2,3,4,5,6,7,8,9]
print(quickSort(lista8))

# lista = [9,8,7,6,5,4,3,2,1]
# print(lista[:5], lista[5], lista[5+1:])