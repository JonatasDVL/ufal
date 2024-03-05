class Atendente():
  nome = None
  numeroCaixa = None
  cliente = {"numero": None, "nome": None}

  def __init__(self, nome, numeroCaixa):
    self.nome = nome
    self.numeroCaixa = numeroCaixa
  
  def ocupado(self):
    return self.cliente["numero"] != None

  def chamar(self, cliente):
    if self.ocupado():
      print("Esse caixa já está ocupado!")
    else:
      self.cliente = cliente

  def desocupar(self):
    if self.ocupado():
      numero = self.cliente["numero"]
      nome = self.cliente["nome"]
      self.cliente = {"numero": None, "nome": None}
      return numero, nome
    else:
      print("Esse caixa já está desocupado!")

  def imprimir(self):
    print(f"Caixa {self.numeroCaixa}: -{self.nome}-")
    if self.ocupado():
      numero = self.cliente["numero"]
      nome = self.cliente["nome"]
      print(f"Cliente: Nº {numero}, {nome}")
    else:
      print("Livre")