# 2. Um problema enfrentado por uma empresa que gerencia um porto é o empilhamento de containers. Uma pilha de containers pode ter até 5 containers empilhados. Quando um novo container precisa ser empilhado, deve-se empilhá-lo na menor pilha no momento. Cada container possui um código associado. No porto é possível fazer apenas 4 pilhas de containers, mais uma pilha que pode ser utilizada temporariamente (swap). Essa pilha adicional deve ser mantida vazia e utilizada apenas caso um container que não está no topo da pilha precise ser retirado. 
# Faça um algoritmo que recebe uma lista de containers e imprima o resultado das pilhas ao final da operação.

class Celula:
  valor = None
  proximo = None

  def __init__(self,valor):
      self.valor = valor

class Pilha:
  topo = None
  tam = 0

  def __init__(self):
    self.topo = None

  def inserir(self,valor):
    if self.tam <= 4:
      self.tam +=1
      c = Celula(valor)
      c.proximo = self.topo
      self.topo = c
    else:
      print(f"Não foi possivel adicionar o container[{valor}], pois a pilha está cheia")

  def remover(self):
    if self.topo != None:
      self.topo = self.topo.proximo

  def tamanhoDaPilha(self):
    aux = self.topo
    i = 0
    while aux != None:
      aux = aux.proximo
      i+=1
    return i
  
  def imprimir(self):
    aux = self.topo
    while aux != None:
      print(aux.valor)
      aux = aux.proximo
    print('---')



entrada = ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13","c14","c15","c16","c17","c18","c19","c20","c21"]

pilha1 = Pilha()
pilha2 = Pilha()
pilha3 = Pilha()
pilha4 = Pilha()
# swap = Pilha()

for container in entrada:
  if pilha1.tamanhoDaPilha() <= pilha2.tamanhoDaPilha() and pilha1.tamanhoDaPilha() <= pilha3.tamanhoDaPilha() and pilha1.tamanhoDaPilha() <= pilha4.tamanhoDaPilha():
    pilha1.inserir(container)
  elif pilha2.tamanhoDaPilha() <= pilha3.tamanhoDaPilha() and pilha2.tamanhoDaPilha() <= pilha4.tamanhoDaPilha():
    pilha2.inserir(container)
  elif pilha3.tamanhoDaPilha() <= pilha4.tamanhoDaPilha():
    pilha3.inserir(container)
  else:
    pilha4.inserir(container)

pilha1.imprimir()
pilha2.imprimir()
pilha3.imprimir()
pilha4.imprimir()