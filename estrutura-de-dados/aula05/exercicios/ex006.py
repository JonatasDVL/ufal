# 6. Implemente uma pilha para armazenar números e escreva uma função para ordenar os valores da pilha em ordem crescente. Você pode utilizar uma pilha auxiliar para resolver o problema, mas não pode utilizar outro tipo de estrutura de dados.

class Celula:
  valor = None
  proximo = None

  def __init__(self,valor):
    self.valor = valor

class Pilha:
  topo = None

  def __init__(self,):
    self.topo = None

  def inserir(self,valor):
    c = Celula(valor)
    c.proximo = self.topo
    self.topo = c
  
  def remover(self):
    if self.topo != None:
      self.topo = self.topo.proximo 
    else:
      print("Não foi possivel remover, pilha vazia!")
  
  def imprimir(self):
    aux = self.topo
    while aux != None:
      print(aux.valor,end=" ")
      aux = aux.proximo

pilha1 = Pilha()

entrada = [9,8,7,6,5,2,1,2]
# entrada = [4,3,2,1]
# entrada = [1,2,3,4]
# entrada = [4,1,3,2]

for i in entrada:
  pilha1.inserir(i)

pilhaAux1 = Pilha()
pilhaAux2 = Pilha()

print("............")
print("começo")
print("Pilha1:")
print(pilha1.imprimir())
print("Pilha2:")
print(pilhaAux1.imprimir()) 
print("Pilha3:")
print(pilhaAux2.imprimir())

cond = False
cond2 = 0
while cond == False:
  verificar = []
  topoAux = pilha1.topo 
  while topoAux != None and pilhaAux1.topo == None and pilhaAux2.topo == None:
    verificar.append(topoAux.valor)
    topoAux = topoAux.proximo
  if pilhaAux1.topo == None and pilhaAux2.topo == None:
    for i in range(1, len(verificar)):
      if verificar[i] > verificar[i-1]:
        cond = False
        break
      else:
        cond = True
  if cond == False:
    if pilha1.topo != None and cond2 != 1:
      if pilhaAux1.topo == None or pilhaAux1.topo.valor >= pilha1.topo.valor:
        pilhaAux1.inserir(pilha1.topo.valor)
        pilha1.remover()
      elif pilhaAux2.topo == None or pilhaAux2.topo.valor >= pilha1.topo.valor:
        pilhaAux2.inserir(pilha1.topo.valor)
        pilha1.remover()
      elif pilha1.topo.valor > pilhaAux1.topo.valor and pilha1.topo.valor < pilhaAux2.topo.valor:
        pilhaAux2.inserir(pilha1.topo.valor)
        pilha1.remover()
      elif pilha1.topo.valor < pilhaAux1.topo.valor and pilha1.topo.valor > pilhaAux2.topo.valor:
        pilhaAux1.inserir(pilha1.topo.valor)
        pilha1.remover()
      elif pilhaAux2.topo.valor >= pilhaAux1.topo.valor:
        pilhaAux2.inserir(pilha1.topo.valor)
        pilha1.remover()
      else:
        pilhaAux1.inserir(pilha1.topo.valor)
        pilha1.remover()
    else:
      cond2 = 1
      if pilhaAux1.topo != None and pilhaAux2.topo != None:
        if pilhaAux2.topo.valor >= pilhaAux1.topo.valor and (pilha1.topo == None or pilha1.topo.valor <= pilhaAux1.topo.valor):
          pilha1.inserir(pilhaAux1.topo.valor)
          pilhaAux1.remover()
        elif pilhaAux2.topo.valor < pilhaAux1.topo.valor and (pilha1.topo == None or pilha1.topo.valor <= pilhaAux2.topo.valor):
          pilha1.inserir(pilhaAux2.topo.valor)
          pilhaAux2.remover()
        else:      
          cond2 = 3
      elif pilhaAux1.topo != None and pilha1.topo.valor <= pilhaAux1.topo.valor:
        pilha1.inserir(pilhaAux1.topo.valor)
        pilhaAux1.remover()
      elif pilhaAux2.topo != None and pilha1.topo.valor <= pilhaAux2.topo.valor:
        pilha1.inserir(pilhaAux2.topo.valor)
        pilhaAux2.remover()
      else:
        cond2 = 3

  print("............")
  print("Pilha1:")
  print(pilha1.imprimir())
  print("Pilha2:")
  print(pilhaAux1.imprimir()) 
  print("Pilha3:")
  print(pilhaAux2.imprimir())

print("............")
print("Final")
print("Pilha1:")
print(pilha1.imprimir())
print("Pilha2:")
print(pilhaAux1.imprimir()) 
print("Pilha3:")
print(pilhaAux2.imprimir())