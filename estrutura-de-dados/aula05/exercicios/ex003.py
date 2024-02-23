# 3 . Uma expressão aritmética com parênteses, colchetes e chaves é dita bem formada se estes símbolos são fechados na ordem inversa que são abertos.
# ● Ex: expressão bem formada
# – 3-[15+2*(4-3)*[2+(5-1)]]/4
# ● Ex: expressão mal formada
# – 5-[4+(0-3]
# Faça um algoritmo para resolver o problema usando pilhas

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

entrada = "–3-[15+2*(4-3)*[2+(5-1)]]/4"
pilha = Pilha()

for caractere in entrada:
  if caractere == "(" or caractere == "{" or caractere == "[" or caractere == "]" or caractere == "}" or caractere == ")":
    pilha.inserir(caractere)




