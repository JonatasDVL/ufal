# 1. Implemente e teste os algoritmos de ordenação QuickSort e MergeSort para ordenar um vetor de
# registros que representa uma tabela de campeonato de futebol. O registro é Time, com os campos nome
# e pontuação. A ordenação deve feita pelo campo pontuação.


lista = [
  {"nome":"Flamengo", "pontuacao": 3},
  {"nome":"Botafogo", "pontuacao": 4},
  {"nome":"São Paulo", "pontuacao": 2},
  {"nome":"ASA", "pontuacao": 1},
  {"nome":"Vasco", "pontuacao": 7},
  {"nome":"CSE", "pontuacao": 5}
]
lista2 = lista + [{"nome":"Corithians", "pontuacao": 6}]

def quickSort(lista):
  return lista

def combinacaoMerge(lista1, lista2): 
  j = 0
  i = 0
  lista3 = []
  while j < len(lista2) and i < len(lista1):
      if lista1[i]["pontuacao"] > lista2[j]["pontuacao"]:
          lista3.append(lista2[j])
          j += 1
      else:   
          lista3.append(lista1[i])
          i += 1
  if i < len(lista1):
      lista3 = lista3 + lista1[i:]
  elif j < len(lista2):
      lista3 = lista3 + lista2[j:]
  return lista3

def divisaoMerge(lista):
    if len(lista) == 1:
        return lista
    else:
        return combinacaoMerge(divisaoMerge(lista[0:len(lista)//2]), divisaoMerge(lista[len(lista)//2:]))

def mergeSort(lista):
  lista = divisaoMerge(lista)
  return lista
    
print("------------\nQuickSort: ")
print(quickSort(lista))
print("------------\nMergeSort: ")
print(mergeSort(lista2))