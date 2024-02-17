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

def combinacaoMerge(lista1, lista2): 
  j = 0
  i = 0
  lista3 = []
  tamanhoDaLista1 = len(lista1)
  tamanhoDaLista2 = len(lista2)
  while j < tamanhoDaLista2 and i < tamanhoDaLista1:
    if lista1[i]["pontuacao"] > lista2[j]["pontuacao"]:
      lista3.append(lista2[j])
      j += 1
    else:   
      lista3.append(lista1[i])
      i += 1
  lista3 = lista3 + lista1[i:] # add o que resta
  lista3 = lista3 + lista2[j:] # add o que resta
  return lista3

def divisaoMerge(lista):
    tamanhoDaLista = len(lista)
    if tamanhoDaLista == 1:
        return lista
    else:
        return combinacaoMerge(divisaoMerge(lista[0:tamanhoDaLista//2]), divisaoMerge(lista[tamanhoDaLista//2:]))

def mergeSort(lista):
  lista = divisaoMerge(lista)
  return lista

def quickSort(lista):
  tamanhoDaLista = len(lista)
  if tamanhoDaLista <= 1:
    return lista
  else:
    pivo = lista[tamanhoDaLista//2]["pontuacao"]
    lista1 = []
    lista2 = []
    lista3 = []
    for i in lista:
      if i["pontuacao"] < pivo:
        lista1.append(i)
      elif i["pontuacao"] == pivo:
        lista2.append(i)
      else:
        lista3.append(i)
    return quickSort(lista1) + lista2 + quickSort(lista3)
  
print("------------\nQuickSort: ")
for i in quickSort(lista):
  print(i)
print("------------\nMergeSort: ")
for i in mergeSort(lista2):
  print(i)