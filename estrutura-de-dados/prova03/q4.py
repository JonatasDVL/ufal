# 4. Modifique o programa do quicksort de modo que, se um sub-vetor for pequeno, a ordenação por
# seleção seja usada.

def quickSort(lista): 
  tamanhoDaLista = len(lista)
  if tamanhoDaLista < 1:
    return lista
  elif tamanhoDaLista <= 4:
    return selectionSort(lista)
  else:
    pivo = lista[tamanhoDaLista - 1]
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

def selectionSort(lista):
  j = 0
  while j != len(lista)-1:
    i = j 
    posicao = i
    while i != len(lista)-1:
      i+=1
      if lista[i] < lista[posicao]:
        posicao = i
    lista[j], lista[posicao] = lista[posicao], lista[j]
    j+=1
  return lista

lista1 = [9,8,7,6,5,4,3,2,1]
print(quickSort(lista1))