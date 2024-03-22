class Celula:
  valor = None
  proximo = None
  anterior = None

  def __init__(self, valor):
    self.valor = valor

class Lista:
  inicio = None
  fim = None
  tam = 0

  def append(self, valor):
    c = Celula(valor)
    if self.inicio == None:
      self.inicio = c
    else:
      c.anterior = self.fim
      self.fim.proximo = c
    self.tam += 1
    self.fim = c

  def inserirPos(self, valor, pos):
    if pos <= self.tam and pos >= 0:
      if self.tam == 0 or pos == self.tam:
        self.append(valor)
      else:
        c = Celula(valor)
        if pos == 0:
          c.proximo = self.inicio
          self.inicio = c 
        else:
          count = 0 
          aux = self.inicio
          while count < pos-1:
            aux = aux.proximo
            count += 1
          c.proximo = aux.proximo
          aux.proximo = c
        self.tam += 1 
    else:
      print("Posição inválida")    

  def pop(self):
    if self.fim != None:
      valor = self.fim.valor
      self.fim = self.fim.anterior
      self.tam -= 1
      return valor
    else:
      print("Lista vazia")

  def removerPos(self, pos):
    if pos < self.tam and pos >= 0:
      if pos == self.tam-1:
        return self.pop()
      elif pos == 0:
        itemParaRemover = self.inicio
        self.inicio = self.inicio.proximo
      else:
        count = 0 
        aux = self.inicio
        while count < pos-1:
          aux = aux.proximo
          count += 1
        itemParaRemover = aux.proximo 
        aux.proximo = itemParaRemover.proximo 
      self.tam -= 1
      valor = itemParaRemover.valor
      del itemParaRemover
      return valor
    else:
      print("Posição Inválida")

  def removerItem(self, valor):
    if self.tam != 0:
      cond = False
      if self.inicio.valor == valor:
        itemParaRemover = self.inicio
        self.inicio = self.inicio.proximo
        cond = True
      else:
        aux = self.inicio
        while aux.proximo != None and aux.proximo.valor != valor:
          aux = aux.proximo
        if aux.proximo != None:
          itemParaRemover = aux.proximo
          aux.proximo = itemParaRemover.proximo  
          cond = True
      if cond:
        self.tam -=1
        del itemParaRemover
        return valor
    else:
      print("Não Existe esse item na lista")
      return
    
  def imprimir(self):
    aux = self.inicio
    lista = []
    if self.tam > 0:
      for i in range(self.tam):
        lista.append(aux.valor)
        aux = aux.proximo    
    print(lista)


lista = Lista()
lista.append(6)
lista.append(7)
lista.append(9)
lista.append(4)
lista.imprimir()

lista.removerItem(9)
lista.removerItem(6)
lista.removerItem(7)
lista.removerItem(4)
lista.removerItem(4)
lista.imprimir()