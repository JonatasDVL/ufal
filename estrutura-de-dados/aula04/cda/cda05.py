# Quick Sort

def compara(lista):
  i = 0
  j = len(lista)-1
  pivo = len(lista)//2
  while j > i: 
    if lista[j] > lista[pivo]:
      j -= 1
    elif lista[i] < lista[pivo]:
      i += 1
    else:
      lista[i], lista[j] = lista[j], lista[i] 
      if pivo == i:
        pivo = j
      elif pivo == j:
        pivo = i
      i += 1
      j -= 1

  if len(lista) == 2:
    lista1, lista2 = lista[:1], lista[1:]
  else:
    if lista[i] < lista[pivo]:
      lista[pivo], lista[i] = lista[i], lista[pivo]
      pivo = i+1
    elif lista[j] > lista[pivo]:
      pivo = j
      lista[pivo], lista[j] = lista[j], lista[pivo]

    lista1, lista2 = lista[:pivo], lista[pivo:]

  print(lista1,lista2)
  return lista1, lista2

def quickSort(lista):
  lista2 = divisaoQuick(lista)
  lista = []
  for i in lista2:
    lista.append(i)
  return lista

def divisaoQuick(lista):
  if len(lista) == 1:
    return lista    
  else:
    lista1, lista2 = compara(lista)
    return quickSort(lista1), quickSort(lista2) 
  
listaUm = [3,5,8,4,2,1,9,0]
listaDois = [3,5,8,1,2,1,9,0]
listaTres = [9,8,7,6,5,4,3,2,1,0]
listaQuatro = [0,1,2,3,4,5,6,7,8,9]

print(quickSort(listaUm))
print("---")
print(quickSort(listaDois))
print("---")
print(quickSort(listaTres))
print("---")
print(quickSort(listaQuatro))
print("---")
