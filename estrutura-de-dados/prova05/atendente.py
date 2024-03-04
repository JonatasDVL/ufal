class Atendente():
  nome = None
  numeroCaixa = None
  cliente = None

  def __init__(self, nome, numeroCaixa):
    self.nome = nome
    self.numeroCaixa = numeroCaixa
  
  def ocupado(self):
    return self.cliente != None

  def chamar(self, cliente):
    if self.ocupado:
      print("Esse caixa já está ocupado!")
    else:
      self.cliente = cliente

  def desocupar(self):
    if self.ocupado:
      self.cliente = None
    else:
      print("Esse caixa já está desocupado!")

  def imprimir(self):
    print(f"Caixa: Nº {self.numeroCaixa} -{self.nome}-")
    if self.ocupado:
      print(f"Cliente: Nº {self.cliente["nome"]} -{self.cliente["nome"]}-")
    else:
      print("Livre")