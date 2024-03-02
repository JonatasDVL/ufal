class Celular():
  valor = None
  proximo = None
  def __init__(self, valor):
    self.valor = valor

class Fila():
  inicio = None
  fim = None

  def inserir(self, valor):
    c = Celular(valor)
    if self.inicio == None: # and self.fim == None
      self.inicio = c
    else:
      self.fim.proximo = c 
    self.fim = c
  
  def remover(self):
    if self.inicio != None:
      valor = self.inicio.valor
      aux = self.inicio
      self.inicio = self.inicio.proximo
      del aux
      return valor
    else:
      print("Fila Vazia")
      return None

  def imprimir(self):
    aux = self.inicio
    if aux != None:
      while aux != None:
        print(f"{aux.valor}", end=' ')
        aux = aux.proximo
      print()
      return True
    else:
      print("Nada")
      return False


fila = Fila()
fila.inserir(2)
fila.inserir(3)
fila.imprimir()
fila.remover()
fila.imprimir()
fila.remover()
fila.remover()
fila.imprimir()
fila.remover()
fila.inserir(7)
fila.imprimir()
fila.remover()
fila.imprimir()