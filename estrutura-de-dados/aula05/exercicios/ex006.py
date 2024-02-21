# 6. Implemente uma pilha para armazenar números e escreva uma função para ordenar os valores da pilha em ordem crescente. Você pode utilizar uma pilha auxiliar para resolver o problema, mas não pode utilizar outro tipo de estrutura de dados.

class Celula:
  valor = None
  proximo = None

  def __init__(self,valor):
      self.valor = valor

class Pilha:
  topo = None

  def __init__(self):
    self.topo = None

  def inserir(self,valor):
    c = Celula(valor)
    c.proximo = self.topo
    self.topo = c

  def remover(self):
    if self.topo != None:
      self.topo = self.topo.proximo

  def ultimoValor(self):
    if self.topo != None:
      return self.topo.valor

  def imprimir(self):
    aux = self.topo
    while aux != None:
      print(aux.valor)
      aux = aux.proximo
    print('---')

pilha = Pilha()
for i in range(10,0,-1):
  pilha.inserir(i)
pilha.imprimir()

pilhaAux1 = Pilha()
pilhaAux2 = Pilha()


pilhaAux1.inserir(pilha.ultimoValor())
print(pilhaAux1.topo)

pilhaAux1.imprimir()
