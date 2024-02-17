def combinaListasOrdenando(lista1, lista2):
  i = 0 # index da lista1
  j = 0 # index da lista2
  lista3 = []
  tamanhoDaLista1 = len(lista1)
  tamanhoDaLista2 = len(lista2)
  while i < tamanhoDaLista1 and j < tamanhoDaLista2:
    if lista1[i] <= lista2[j]:
      lista3.append(lista1[i])
      i += 1
    else:
      lista3.append(lista2[j])
      j += 1
  lista3 = lista3 + lista1[i:]
  lista3 = lista3 + lista2[j:]
  return lista3

def dividiListaAoMeio(lista):
  tamanhoDaLista = len(lista)
  metadeDaLista = tamanhoDaLista//2
  if tamanhoDaLista == 1:
    return lista
  else:
    return combinaListasOrdenando(dividiListaAoMeio(lista[0:metadeDaLista]), dividiListaAoMeio(lista[metadeDaLista:]))

def mergeSort(lista):
  return dividiListaAoMeio(lista)

lista1 = [9,8,7,6,5,4,3,2,1]
print(mergeSort(lista1))
lista2 = [1,2,3,4,5,6,7,8,9]
print(mergeSort(lista2))
lista3 = [2,1,4,3,6,5,8,7,9]
print(mergeSort(lista3))
lista4 = [9,2,1,4,3,6,5,8,7]
print(mergeSort(lista4))