# 04) Implemente um algoritmo que recebe uma palavra e uma sub-palavra e verifica
# se a sub-palavra existe na palavra. Use uma lista encadeada para resolver esse
# problema
# Ex.:
# Entradas:
# palavra = ‘especial’
# subpalavra = ‘cia’
# Saída: True


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
  
  def imprimir(self):
    if self.tam > 0:
      aux = self.inicio
      while aux:
        print(aux.valor, end=" ")
        aux = aux.proximo
      print("")
    else:
      print("Lista Vazia")

  def subPalavra(self, subpalavra):
    retorno = False
    if self.tam >= len(subpalavra):
      aux = self.inicio
      while aux != None and not(retorno):
        aux2 = aux
        for letra in subpalavra:
          if aux2 != None and letra == aux2.valor:
            aux2 = aux2.proximo
            retorno = True
          else:
            retorno = False
            break
        aux = aux.proximo
    
    return retorno

lista = Lista()

palavra = "especial"

for letra in palavra:
  lista.append(letra)

lista.imprimir()

palavra = "epecial"

print(lista.subPalavra(palavra))