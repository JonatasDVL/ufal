# 3. O método de ordenação por seleção funciona colocando o menor elemento do vetor na primeira
# posição, o segundo menor na segunda posição e assim por diante. Altere o algoritmo para que, a cada
# passo, ele coloque o maior elemento na última posição, o segundo maior na penúltima posição, e assim
# por diante.

def selectionSortInvertido(lista):
  print(lista)
  j = len(lista)
  while j != 1:
    j-=1
    i = j 
    posicao = i
    while i != 0:
      i-=1
      if lista[i] > lista[posicao]:
        posicao = i
    lista[j], lista[posicao] = lista[posicao], lista[j]
    print(lista, lista[posicao], lista[j])
  return lista



lista = [9,8,7,6,5,4,3,2,3,1]
selectionSortInvertido(lista)

