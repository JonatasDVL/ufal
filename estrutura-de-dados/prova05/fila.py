class Pessoa():
  numero_de_chegada = None
  nome = None
  proximo = None
  def __init__(self, numero_de_chegada, nome):
    self.numero_de_chegada = numero_de_chegada
    self.nome = nome

class Fila():
  inicio = None
  fim = None

  def vazia(self):
    return self.inicio == None
  
  def inserir(self, numero_de_chegada, nome="NI"): #Não informado = NI
    p = Pessoa(numero_de_chegada, nome)
    if self.vazia():
      self.inicio = p
    else:
      self.fim.proximo = p 
    self.fim = p
  
  def remover(self):
    if not(self.vazia()):
      numero = self.inicio.numero_de_chegada
      nome = self.inicio.nome
      aux = self.inicio
      self.inicio = self.inicio.proximo
      del aux
      return numero, nome
    else:
      return None


  def imprimir(self):
    if not(self.vazia()):
      aux = self.inicio
      while aux != None:
        print(f"Nº {aux.numero_de_chegada}: {aux.nome}") 
        aux = aux.proximo
      return True
    else:
      print("Fila Vazia")
      return False