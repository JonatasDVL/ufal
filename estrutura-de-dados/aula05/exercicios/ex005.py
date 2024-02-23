# 5. Implemente uma função que simula a navegação de páginas em um navegador web onde o usuário possa retornar a páginas anteriores mantendo a ordem inversa de visita.
# Utilize uma pilha encadeada para resolver o problema.

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

  def imprimir(self):
    aux = self.topo
    while aux != None:
      print(aux.valor)
      aux = aux.proximo
    print('---')

anteriores = Pilha()
sucessores = Pilha()

resposta = "a"
while resposta != "para":
  resposta = input()
  if resposta != "para":
    if resposta != "alt-" and resposta != "alt+":
      anteriores.inserir(resposta)
      sucessores = Pilha()
    elif resposta == "alt+":
      if sucessores.topo != None:
        anteriores.inserir(sucessores.topo.valor)
      else:
        print("A atual página foi a primeira acessada")
      sucessores.remover()
    else:
      if anteriores.topo != None:
        sucessores.inserir(anteriores.topo.valor)
      else:
        print("A atual página foi a ultima nova pagina acessada")
      anteriores.remover()

print("Sucessores:")
sucessores.imprimir()
print("Anteriores:")  
anteriores.imprimir()



