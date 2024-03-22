class Lista:
  tamanho = 0
  itens = None
  fim = 0

  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.itens = [None] * tamanho

  def inserirPos(self, item, pos="sem"):
    if pos == "sem":
      pos = self.fim
    if self.fim < self.tamanho and abs(pos) <= self.fim:
      self.itens[pos] = item
      if pos == self.fim:
        self.fim += 1
    else:
      print("Error de Posição")

  # def append(self, item):
  #   self.itens.inserirPos(self.fim, item)

  def inserirDesloque(self, item, pos):
    if self.fim < self.tamanho and abs(pos) <= self.fim:
      aux = self.fim
      while aux != pos:
        self.itens[aux] = self.itens[aux-1]
        aux -= 1
      self.itens[pos] = item
      self.fim += 1
    else:
      print("erro posição")

  def remover(self, pos="sem"):
    if pos == "sem":
      pos = self.fim-1
    if pos < self.tamanho and abs(pos) <= self.fim and self.itens[pos] != None:
      valor = self.itens[pos]
      self.itens[pos] = None
      if pos != self.fim-1 and self.itens[pos+1] != None:
        self.itens.inserirDesloque(self.itens[pos+1], pos)
      self.fim -= 1
      return valor
    
    else:
      print("Erro de alguma coisa")

  # def pop(self, item):
  #   self.itens.remover(self.fim, item)

lista = Lista(3)

lista.inserirPos(2,0)
lista.inserirPos(3)
lista.inserirDesloque(4,1)
print(lista.itens)
lista.remover()
lista.remover(0)
print(lista.itens)