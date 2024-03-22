# 02) Implemente o algoritmo Selection Sort em uma lista encadeada.
# Ex.:
# Entrada: [6, 4, 3, 7, 8, 2]
# Saída: [2, 3, 4, 6, 7, 8]

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

  def insert(self, valor, posicao):
    if posicao >= self.tam:
      self.append(valor)
    else:
      c = Celula(valor)
      aux = self.inicio
      if posicao == 0:
        c.proximo = aux
        aux.anterior = c
        self.inicio = c
      else:
        count = 0
        while count < posicao-1:
          aux = aux.proximo
          count += 1
        proximo = aux.proximo
        aux.proximo = c
        c.proximo = proximo
        c.anterior = aux
      self.tam += 1

  def pop(self, posicao):
    if self.tam > 0:
      if posicao < self.tam and posicao >= 0:
        if posicao == 0:
          valor = self.inicio.valor
          if self.tam == 1:
              self.inicio = None 
              self.fim = None
          else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        elif posicao == self.tam-1:
          valor = self.fim.valor
          self.fim = self.fim.anterior
          self.fim.proximo = None
        else:
          count = 0
          if abs(posicao - self.tam-1) > posicao:
            aux = self.inicio
            while count < posicao:
              aux = aux.proximo
              count += 1
          else:
            aux = self.fim
            while count < abs(posicao - self.tam-1):
              aux = aux.anterior
              count += 1
          anterior = aux.anterior
          proximo = aux.proximo
          valor = aux.valor 
          del aux
          proximo.anterior = anterior
          anterior.proximo = proximo
        self.tam -=1
        return valor
      else:
        print("Posição Inválida")
    else:
      print("Lista Vazia")

  def remove(self, valor):
    if self.tam > 0:
      if self.tam == 1:
        if self.inicio.valor == valor:
          self.inicio = None 
          self.fim = None
          self.tam -= 1
        else:
          print("O valor não foi encontrado na lista")
      else:
        aux = self.inicio
        if aux.valor == valor:
          self.inicio = aux.proximo
          self.inicio.anterior = None  
        else:
          while aux != None and aux.valor != valor:
            aux = aux.proximo
          if aux != None:
            if self.fim == aux:
              self.fim = aux.anterior
              self.fim.proximo = None
            else:
              anterior = aux.anterior
              proximo = aux.proximo
              anterior.proximo = proximo
              proximo.anterior = anterior
          else:
            print("O valor não foi encontrado na lista")
        del aux
        self.tam -= 1
    else:
      print("Lista Vazia")
  
  def imprimir(self):
    if self.tam > 0:
      aux = self.inicio
      while aux:
        print(aux.valor, end=" ")
        aux = aux.proximo
      print("")
    else:
      print("Lista Vazia")

  def selectionSort(self):
    if self.tam > 0:
      menor = self.inicio
      while menor.proximo != None:
        primeiro = menor
        aux = menor
        while aux != None:
          if menor.valor > aux.valor:
            menor = aux
          aux = aux.proximo
        if primeiro != menor:
          if primeiro == self.inicio and menor == self.fim:
            self.inicio = menor
            self.fim = primeiro
          elif primeiro == self.inicio:
            self.inicio = menor
          elif menor == self.fim:
            self.fim = primeiro
            
          proximoDoPrimeiro = primeiro.proximo
          anteriorDoPrimeiro = primeiro.anterior
          proximoDoMenor = menor.proximo
          anteriorDoMenor = menor.anterior

          if primeiro.proximo != menor:
            primeiro.proximo = proximoDoMenor
            primeiro.anterior = anteriorDoMenor
            menor.proximo = proximoDoPrimeiro
            menor.anterior = anteriorDoPrimeiro
            
            if primeiro != self.fim:
              proximoDoMenor.anterior = primeiro 
            anteriorDoMenor.proximo = primeiro          
            
            proximoDoPrimeiro.anterior = menor
            if menor != self.inicio:
              anteriorDoPrimeiro.proximo = menor
          else:
            primeiro.proximo = proximoDoMenor
            primeiro.anterior = proximoDoPrimeiro
            menor.proximo = anteriorDoMenor
            menor.anterior = anteriorDoPrimeiro

            if primeiro != self.fim:
              proximoDoMenor.anterior = primeiro 
            
            if menor != self.inicio:
              anteriorDoPrimeiro.proximo = menor
              
        menor = menor.proximo
    else:
      print("Lista Vazia")

entrada = [6, 4, 3, 7, 8, 2]
# entrada = [8, 7 , 2]
# entrada = [2,1]
lista = Lista()
for valor in entrada:
  lista.append(valor)

lista.imprimir()

lista.selectionSort()

lista.imprimir()





# [6, 4, 3, 7, 8, 2]
# None <- 6 <-> 4 <-> 3 <-> 7 <-> 8 <-> 2 -> None
# Inicio -> 6 e Fim -> 2

# [2, 4, 3, 7, 8, 6]
# None <- 2 <-> 4 <-> 3 <-> 7 <-> 8 <-> 6 -> None
# Inicio -> 2 e Fim -> 6

# [2, 3, 4, 7, 8, 6]
# None <- 2 <-> 3 <-> 4 <-> 7 <-> 8 <-> 6 -> None
# Inicio -> 2 e Fim -> 6