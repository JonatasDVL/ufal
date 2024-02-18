# 2. Mostre as etapas de funcionamento do QuickSort e Mergesort (apresentando inclusive as chamadas
# recursivas) para ordenar a sequência de números:
# 6 2 9 12 5 1 3

def combinaListasOrdenando(lista1, lista2):
  i = 0 
  j = 0 
  lista3 = []
  tamanhoDaLista1 = len(lista1)
  tamanhoDaLista2 = len(lista2)
  while i < tamanhoDaLista1 and j < tamanhoDaLista2:
    if lista1[i] <= lista2[j]:
      print(f"{lista1[i]} <= {lista2[j]}")
      lista3.append(lista1[i])
      i += 1
    else:
      print(f"{lista1[i]} > {lista2[j]}")
      lista3.append(lista2[j])
      j += 1
  lista3 = lista3 + lista1[i:]
  lista3 = lista3 + lista2[j:]
  print(f"Combinando as Listas em Ordem: {lista1} + {lista2} = {lista3}")
  return lista3

def dividiListaAoMeio(lista):
  tamanhoDaLista = len(lista)
  metadeDaLista = tamanhoDaLista//2
  if tamanhoDaLista == 1:
    return lista
  else:
    print(f"Dividindo {lista}: {lista[0:metadeDaLista]}, {lista[metadeDaLista:]}")
    return combinaListasOrdenando(dividiListaAoMeio(lista[0:metadeDaLista]), dividiListaAoMeio(lista[metadeDaLista:]))

def mergeSort(lista):
  return dividiListaAoMeio(lista)

def quickSort(lista):
  tamanhoDaLista = len(lista)
  if tamanhoDaLista <= 1:
    if tamanhoDaLista == 1:
      print(f"Retornando Lista: {lista}")
    return lista
  else:
    pivo = lista[tamanhoDaLista//2]
    lista1 = []
    lista2 = []
    lista3 = []
    for i in lista:
      if i < pivo:
        print(f"{i} < {pivo}")
        lista1.append(i)
      elif i == pivo:
        print(f"{i} == {pivo}")
        lista2.append(i)
      else:
        print(f"{i} > {pivo}")
        lista3.append(i)
    print(f"Divindindo Lista em Três em Ordem do Pivô({pivo}): {lista1} {lista2} {lista3}")
    print(f"Retornando Lista: {lista2}")

    return quickSort(lista1) + lista2 + quickSort(lista3)
  
lista1 = [9,8,7,6,5,4,3,2,1]
lista2 = [9,8,7,6,5,4,3,2,1]

print("------------\nProcesso de QuickSort: ")
lista1=quickSort(lista1)
print("Resultado do QuickSort:\n",lista1)
print("------------\nProcesso de MergeSort: ")
lista2 = mergeSort(lista2)
print("Resultado do MergeSort:\n",lista2)



# outro quickSort que fiz:

# def quickSort(lista): 
#   tamanhoDaLista = len(lista)
#   if tamanhoDaLista <= 1:
#     return lista
#   else:
#     pivo = tamanhoDaLista//2
#     i = 0
#     j = tamanhoDaLista-1
#     while i < j:
#       if lista[i] <= lista[pivo] and i != pivo:
#         i += 1
#       elif lista[j] >= lista[pivo] and j != pivo:
#         j -= 1
#       else:
#         lista[i], lista[j] = lista[j], lista[i]
#         if pivo == j:
#           pivo = i
#           i -=1
#         elif pivo == i:
#           pivo = j
#           j +=1
#         i +=1
#         j -=1
#     return quickSort(lista[:pivo]) + quickSort(lista[pivo:])

# lista1 = [9,8,7,6,5,4,3,2,1]

# print("------------\nProcesso de QuickSort: ")
# lista1=quickSort(lista1)
# print(lista1)