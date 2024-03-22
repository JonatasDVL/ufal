# 01) Implemente uma função que recebe duas listas implementadas com arrays e
# entrelaça seus elementos.
# Ex.:
# Entradas:
# lista1 = [1, 3, 5, 7]
# lista2 = [2, 4, 6, 8]
# Saída: [1, 2, 3, 4, 5, 6, 7, 8]

class Celula:
  proximo = None
  valor = None

  def __init__(self, valor):
    self.valor = valor

class Lista:
  tam = 0
  inicio = None
  fim = None

  def imprimir(self):
    if self.tam != 0:
      aux = self.inicio
      while aux != None:
        print(aux.valor, end=" ")
        aux = aux.proximo
      print()
    else:
      print("Lista Vazia")

  def append(self, valor):
    c = Celula(valor)
    if self.tam == 0:
      self.inicio = c
    else:
      self.fim.proximo = c 
    self.fim = c    
    self.tam += 1

  def insert(self, valor, posicao):
    if posicao < 0:
        posicao = self.tam+posicao
    if posicao >= self.tam:
      self.append(valor)
    else:
      c = Celula(valor)
      count = 0
      aux = self.inicio
      if posicao > 0:
        while count != posicao-1:
          aux = aux.proximo
          count += 1
        proximo = aux.proximo
        aux.proximo = c
      elif posicao == 0:
        proximo = aux
        self.inicio = c
      else:
        print("Lista com o index fora do alcance")
        return  
      c.proximo = proximo
      self.tam += 1

  def pop(self, posicao):
    if self.tam > 0:
      if posicao < 0:
        posicao = self.tam+posicao
      elif posicao >= self.tam:
        posicao = self.tam -1
      if posicao > 0: 
        count = 0
        aux = self.inicio
        while count < posicao-1:
          aux = aux.proximo
          count += 1
        deletar = aux.proximo  
        aux.proximo = aux.proximo.proximo
      elif posicao == 0:
        deletar = self.inicio
        self.inicio = self.inicio.proximo
      else:
        print("Index fora do alcance da lista")
        return None
      valor = deletar.valor
      del deletar
      self.tam -= 1
      return valor
    else:
      print("Lista Vazia")

  def remove(self, valor):
    if self.tam > 0:
      aux = self.inicio
      if aux.valor == valor:
        self.inicio = aux.proximo
        deletar = aux
      else:
        while aux.proximo != None and aux.proximo.valor != valor:
          aux = aux.proximo
        if aux.proximo == None:
          print("Não foi encontrado esse Item na Lista")
          return None
        deletar = aux.proximo
        aux.proximo = deletar.proximo
      del deletar
      return valor
    else:
      print("Lista Vazia")

  def entrelacar(self, lista):
    if self.tam > 0 and lista.tam > 0:
      count = 0
      tamanho = self.tam
      aux1 = self.inicio
      aux2 = lista.inicio
      while aux2 != None:
        valor = aux2.valor
        c = Celula(valor)
        if count != tamanho:
          count +=1
          proximo = aux1.proximo
          aux1.proximo = c
          c.proximo = proximo
          if count != tamanho:
            aux1 = aux1.proximo.proximo
          else:
            aux1 = aux1.proximo
        else:
          aux1.proximo = c
          aux1 = aux1.proximo
        aux2 = aux2.proximo
        self.tam +=1

lista1 = Lista()
lista2 = Lista()

lista1.append(7)
lista1.append(8)
lista1.append(9)

lista2.append(1)
lista2.append(3)
lista2.append(1)
lista2.append(3)
lista2.append(1)
lista2.append(3)


lista1.imprimir()
lista2.imprimir()

lista1.entrelacar(lista2)
lista1.imprimir()

#   if count != tamanho:
#     aux1 = aux1.proximo.proximo
#   else:
#     aux1 = aux1.proximo
# else:
#   self.fim.proximo = c
#   self.fim = c