from fila import Fila
from atendente import Atendente

fila = Fila()
caixa1 = Atendente("Cleide", "01")
caixa2 = Atendente("Joshon", "02")
caixa3 = Atendente("Paulo", "03")


print("Bem-vindo ao sistema dos Correios!")
aberto = True
i = 1
while aberto or not(fila.vazia()) or caixa1.ocupado() or caixa2.ocupado() or caixa3.ocupado():
  print("------------------------------------------")
  if caixa1.ocupado(): 
    print("1. Chamar o proximo para caixa 01;")
  if caixa2.ocupado():
    print("2. Chamar o proximo para caixa 02;")
  if caixa3.ocupado():
    print("3. Chamar o proximo para caixa 03;")
  if aberto == True:
    print("4. Adicionar um cliente;")
    print("5. Fechar as portas do Correio;")
  opcao = float(input("Digite o número de uma das opções acima: "))
  print("------------------------------------------")

  if opcao == 1 and caixa1.ocupado():
    numero, nome = caixa1.desocupar()
    print(f"Cliente {nome} de Nº {numero} saiu!")
    if not(fila.vazia()):
      numero, nome = fila.remover()
      caixa1.chamar({"nome": nome, "numero": numero})
  elif opcao == 2 and caixa2.ocupado():
    numero, nome = caixa2.desocupar()
    print(f"Cliente {nome} de Nº {numero} saiu!")
    if not(fila.vazia()):
      numero, nome = fila.remover()
      caixa2.chamar({"nome": nome, "numero": numero})
  elif opcao == 3 and caixa3.ocupado():
    numero, nome = caixa3.desocupar()
    print(f"Cliente {nome} de Nº {numero} saiu!")
    if not(fila.vazia()):
      numero, nome = fila.remover()
      caixa3.chamar({"nome": nome, "numero": numero})
  elif opcao == 4 and aberto == True:
    nome = input(f"Digite o nome do cliente de Nº {i}: ")
    if len(nome) >= 2:
      fila.inserir(i, nome)
    else:
      fila.inserir(i)
    i += 1 
  elif opcao == 5 and aberto == True:
    print("As portas do Correio foram fechadas!")
    aberto = False
  else:
    print("Valor Inválido")
  
  if opcao == 4:
    if not(caixa1.ocupado()):
      numero, nome = fila.remover()
      caixa1.chamar({"nome": nome, "numero": numero})
    elif not(caixa2.ocupado()):
      numero, nome = fila.remover()
      caixa2.chamar({"nome": nome, "numero": numero})
    elif not(caixa3.ocupado()):
      numero, nome = fila.remover()
      caixa3.chamar({"nome": nome, "numero": numero})

  caixa1.imprimir()
  caixa2.imprimir()
  caixa3.imprimir()
  fila.imprimir()
