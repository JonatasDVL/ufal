from fila import Fila
from atendente import Atendente

fila = Fila()

print("Bem-vindo ao sistema de atendimento dos Correios")
print("------------------------------------------")
quantidadeDeCaixa = int(input("Digite a quantidade de Atendente: "))
if quantidadeDeCaixa > 9:
  print("O máximo de caixas ativo é de 9")
  quantidadeDeCaixa = 9

caixas = []
for i in range(1, quantidadeDeCaixa+1):
  nomeAtendente = input(f"Digite o nome do atendente Nº 0{i}: ")
  caixas.append(Atendente(nomeAtendente, f"{i}"))

print("Caixas Ativos:")
for i in range(quantidadeDeCaixa):
  print(f"Caixa Nº 0{i+1}: {caixas[i].nome}")

aberto = True
i = 1

while aberto or not(fila.vazia()) or caixas[0].ocupado() or caixas[1].ocupado() or caixas[2].ocupado():
  print("------------------------------------------")
  if caixas[0].ocupado(): 
    print("1. Chamar o proximo para caixa 01;")
  if caixas[1].ocupado():
    print("2. Chamar o proximo para caixa 02;")
  if caixas[2].ocupado():
    print("3. Chamar o proximo para caixa 03;")
  if aberto == True:
    print("4. Adicionar um cliente;")
    print("5. Fechar as portas do Correio;")
  opcao = float(input("Digite o número de uma das opções acima: "))
  print("------------------------------------------")

  if opcao == 1 and caixas[0].ocupado():
    numero, nome = caixas[0].desocupar()
    print(f"Cliente {nome} de Nº {numero} saiu!")
    if not(fila.vazia()):
      numero, nome = fila.remover()
      caixas[0].chamar({"nome": nome, "numero": numero})
  elif opcao == 2 and caixas[1].ocupado():
    numero, nome = caixas[1].desocupar()
    print(f"Cliente {nome} de Nº {numero} saiu!")
    if not(fila.vazia()):
      numero, nome = fila.remover()
      caixas[1].chamar({"nome": nome, "numero": numero})
  elif opcao == 3 and caixas[2].ocupado():
    numero, nome = caixas[2].desocupar()
    print(f"Cliente {nome} de Nº {numero} saiu!")
    if not(fila.vazia()):
      numero, nome = fila.remover()
      caixas[2].chamar({"nome": nome, "numero": numero})
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
    if not(caixas[0].ocupado()):
      numero, nome = fila.remover()
      caixas[0].chamar({"nome": nome, "numero": numero})
    elif not(caixas[1].ocupado()):
      numero, nome = fila.remover()
      caixas[1].chamar({"nome": nome, "numero": numero})
    elif not(caixas[2].ocupado()):
      numero, nome = fila.remover()
      caixas[2].chamar({"nome": nome, "numero": numero})

  caixas[0].imprimir()
  caixas[1].imprimir()
  caixas[2].imprimir()
  fila.imprimir()
