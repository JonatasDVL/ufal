# 03) Implemente um algoritmo que armazena vários valores em uma lista, em
# seguida, crie uma função que retorna os elementos sem repetição.
# Ex.:
# Entrada: [1, 1, 2, 3, 4, 4, 5, 6, 6]
# Saída: [1, 2, 3, 4, 5, 6]

class Celula:
  def __init__(self, valor):
    self.valor = valor
    self.anterior = None
    self.proximo = None

class Lista:
  def __init__(self):
    self.tam = 0
    self.inicio = None
    self.fim = None

  def append(self, valor):
    c = Celula(valor)
    if self.tam == 0:
      self.inicio = c
    else:
      aux = self.fim
      if self.tam == 1:
        self.inicio.proximo = c
      else:
        self.fim.proximo = c 
      c.anterior = aux
    self.fim = c
    self.tam +=1

  def insert(self, valor, posicao):
    if posicao >= self.tam:
      self.append(valor)
    else:
      c = Celula(valor)
      aux = self.inicio
      if posicao == 0:
        c.proximo = aux
        aux.anterior = c
        self.inicio = c
      else:
        count = 0
        while count < posicao-1:
          aux = aux.proximo
          count += 1
        proximo = aux.proximo
        aux.proximo = c
        c.proximo = proximo
        c.anterior = aux
      self.tam += 1

  def pop(self, posicao):
    if self.tam > 0:
      if posicao < self.tam and posicao >= 0:
        if posicao == 0:
          valor = self.inicio.valor
          if self.tam == 1:
              self.inicio = None 
              self.fim = None
          else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        elif posicao == self.tam-1:
          valor = self.fim.valor
          self.fim = self.fim.anterior
          self.fim.proximo = None
        else:
          count = 0
          if abs(posicao - self.tam-1) > posicao:
            aux = self.inicio
            while count < posicao:
              aux = aux.proximo
              count += 1
          else:
            aux = self.fim
            while count < abs(posicao - self.tam-1):
              aux = aux.anterior
              count += 1
          anterior = aux.anterior
          proximo = aux.proximo
          valor = aux.valor 
          del aux
          proximo.anterior = anterior
          anterior.proximo = proximo
        self.tam -=1
        return valor
      else:
        print("Posição Inválida")
    else:
      print("Lista Vazia")

  def remove(self, valor):
    if self.tam > 0:
      if self.tam == 1:
        if self.inicio.valor == valor:
          self.inicio = None 
          self.fim = None
          self.tam -= 1
        else:
          print("O valor não foi encontrado na lista")
      else:
        aux = self.inicio
        if aux.valor == valor:
          self.inicio = aux.proximo
          self.inicio.anterior = None  
        else:
          while aux != None and aux.valor != valor:
            aux = aux.proximo
          if aux != None:
            if self.fim == aux:
              self.fim = aux.anterior
              self.fim.proximo = None
            else:
              anterior = aux.anterior
              proximo = aux.proximo
              anterior.proximo = proximo
              proximo.anterior = anterior
          else:
            print("O valor não foi encontrado na lista")
        del aux
        self.tam -= 1
    else:
      print("Lista Vazia")

  def removeRepetition(self):
    if self.tam > 0:
      aux = self.inicio
      while aux != None and aux.proximo != None:
        aux2 = aux.proximo
        while aux2 != None:
          proximo = aux2.proximo
          if aux.valor == aux2.valor:
            aux.proximo = aux2.proximo
            del aux2
            self.tam -= 1
          aux2 = proximo
        aux = aux.proximo
    
    else:
      print("Lista Vazia")

  def imprimir(self):
    if self.tam > 0:
      aux = self.inicio
      while aux:
        print(aux.valor, end=" ")
        aux = aux.proximo
      print("")
    else:
      print("Lista Vazia")


entrada = [1, 1, 2, 3, 4, 4, 5, 6, 6]
lista = Lista()

for valor in entrada:
  lista.append(valor)


lista.imprimir()

lista.removeRepetition()

lista.imprimir()
