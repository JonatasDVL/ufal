def quickSort(lista): 
  tamanhoDaLista = len(lista)
  if tamanhoDaLista <= 1:
    return lista
  else:
    pivo = lista[tamanhoDaLista//2]
    lista1 = []
    lista2 = []
    lista3 = []
    for i in lista:
      if i < pivo:
        lista1.append(i)
      elif i == pivo:
        lista2.append(i)
      else:
        lista3.append(i)
    return quickSort(lista1) + lista2 + quickSort(lista3)

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