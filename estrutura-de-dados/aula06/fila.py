class Fila():
  tamanho = 0
  inicio = 0
  fim = 0
  estrutura = None

  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.estrutura = [None]*tamanho

  def inserir(self,valor):
    if not self.estaCheia():
      self.estrutura[self.fim] = valor
      self.fim = (self.fim + 1) % self.tamanho
    else:
      return print(f"Fila Cheia")

  def remover(self):
    if not fila.estaVazia():
      self.estrutura[self.inicio] = None
      self.inicio = (self.inicio + 1) % self.tamanho
    else:
      return print(f"Fila Vazia")

  def estaVazia(self):
    return self.inicio == self.fim

  def estaCheia(self):
    return self.inicio % self.tamanho == (self.fim + 1) % self.tamanho

fila = Fila(10)
print(fila.estrutura)
fila.inserir(1)
fila.inserir(1)
fila.inserir(1)
fila.inserir(1)
fila.inserir(1)
fila.inserir(1)
print(fila.estrutura)
fila.inserir(1)
fila.inserir(1)
fila.inserir(1)
fila.inserir(1)
print(fila.estrutura)
print(fila.estaCheia())
print(fila.estaVazia())
fila.remover()
fila.remover()
fila.remover()
fila.remover()
fila.remover()
fila.remover()
print(fila.estrutura)
fila.inserir(3)
fila.inserir(4)
fila.inserir(3)
fila.inserir(4)
fila.inserir(3)
fila.inserir(4)
fila.inserir(3)
fila.inserir(4)
fila.remover()
print(fila.estrutura)
print(fila.estaCheia())
print(fila.estaVazia())