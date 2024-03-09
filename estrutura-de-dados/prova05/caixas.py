class Caixa():
  nome = None
  aberto = True
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
    elif not(self.aberto):
      print("Esse caixa já está fechado")
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

  def fechar(self):
    if self.aberto:
      self.aberto = False
    else:
      print(f"Esse caixa já está fechado!")

  def abrir(self):
    if self.aberto == False:
      self.aberto = True
    else:
      print(f"Esse caixa já está aberto!")
  
  def imprimir(self):
    if not(self.aberto) and self.ocupado():
      print(f"Caixa {self.numeroCaixa}: -{self.nome}- 'Fechado Temporariamente'")
      numero = self.cliente["numero"]
      nome = self.cliente["nome"]
      print(f"Cliente: Nº {numero}, {nome}")
    else:
      print(f"Caixa {self.numeroCaixa}: -{self.nome}-")
      if self.ocupado():
        numero = self.cliente["numero"]
        nome = self.cliente["nome"]
        print(f"Cliente: Nº {numero}, {nome}")
      elif not(self.aberto):
        print("Fechado")
      else:
        print("Livre")
      
class Caixas():
  caixas = []
  quantidadeDeCaixa = 0

  def __init__(self, quantidadeDeCaixa, modoTeste=False):
    self. quantidadeDeCaixa = quantidadeDeCaixa
    if modoTeste == False:
      for i in range(1, quantidadeDeCaixa+1):
        nomeAtendente = input(f"Digite o nome do atendente Nº 0{i}: ")
        self.caixas.append(Caixa(nomeAtendente, f"0{i}"))
    else:
      self.caixas.append(Caixa("Rodolfo", "01"))
      self.caixas.append(Caixa("Patrick", "02"))
      self.caixas.append(Caixa("Raquel", "03"))

  def contarAbertos(self):
    count = 0
    for caixa in self.caixas:
      if caixa.aberto:
        count += 1
    return count
  
  def contarOcupados(self):
    count = 0
    for caixa in self.caixas:
      if caixa.ocupado():
        count += 1
    return count

  def imprimir(self):
    for caixa in self.caixas:
      caixa.imprimir()

  def imprimirAtendentes(self, opcao=0):
    if opcao == 1: 
      for caixa in self.caixas:
        if not(caixa.aberto):
          print(f"Caixa Nº 0{caixa.numeroCaixa}: {caixa.nome}")
    elif opcao == 2: 
      for caixa in self.caixas:
        if caixa.aberto:
          print(f"Caixa Nº 0{caixa.numeroCaixa}: {caixa.nome}")
    elif opcao == 0:
      for caixa in self.caixas:
        print(f"Caixa Nº {caixa.numeroCaixa}: {caixa.nome}")
