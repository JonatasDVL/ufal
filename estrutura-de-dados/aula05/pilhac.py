class Pilha:
  dados = None
  fim = 0
  tam = None

  def __init__ (self, tam):
    self.dados = [None]*tam 

  def inserir(self, valor):
    if self.fim < self.tam:
      self.dados[self.fim] = valor
      self.fim += 1
    else:
      "Erro, Pilha Cheia"

  def remover(self):
    if self.fim > 0:
      self.fim -= 1
      self.dados[self.fim] = None
    else:
      "Erro, Pilha Vazia"

pilha = Pilha(10)

print(pilha.dados)

pilha.inserir(10)
print(pilha.dados)

