# 4. Uma função muito utilizada de um editor de texto é a função de desfazer as ultimas ações de edição, voltando o texto ao estado anterior.
# Implemente a função de desfazer em de um editor de texto, onde a estrutura armazena cada estado atual do texto. Considere uma alteração como uma inserção de uma nova palavra no texto.


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
    self.tam +=1
    c = Celula(valor)
    c.proximo = self.topo
    self.topo = c

  def remover(self):
    if self.topo != None:
      self.tam -=1
      self.topo = self.topo.proximo

  def imprimir(self):
    aux = self.topo
    while aux != None:
      print(aux.valor)
      aux = aux.proximo
    print('---')

dados = Pilha()
dado = input("Digite o texto: ")
while dado != "para":
  if dado == "ctrl-z" and dados.tam !=0:
    dados.remover()
    dados.imprimir()
  else:
    dados.inserir(dado)
    dados.imprimir()
  dado = input("Digite o texto: ")

dados.imprimir()
