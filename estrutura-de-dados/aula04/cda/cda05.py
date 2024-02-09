# Quick Sort

def compara(lista):
  i = 0
  j = len(lista)-1
  pivo = len(lista)//2
  valorPivo = lista[pivo]
  while j!=i and j > i:
    if lista[j] > lista[pivo]:
      j -= 1
    elif lista[i] < lista[pivo]:
      i += 1
    else:
      lista[i], lista[j] = lista[j], lista[i] 
      i += 1
      j -= 1
  lista1, lista2 = lista[:i], lista[i:]
  # if valorPivo != lista[pivo]:
  #   lista1, lista2 = lista[:i], lista[i:]
  #   print("oi")
  # else:
  #   lista1, lista2 = lista[:(len(lista)//2)], lista[(len(lista)//2):]
  print(lista1,lista2)
  return lista1, lista2

def quickSort(lista):
  lista1, lista2 = compara(lista)
  return lista

# def quickSort(lista):
#   if len(lista) == 4:
#     print(lista)    
#   else:
#     lista1, lista2 = compara(lista)
#     return quickSort(lista1), quickSort(lista2) 
#   return lista

lista = [3,5,8,4,2,1,9,0]
# lista = [9,8,7,6,5,4,3,2,1,0]
print(quickSort(lista))
