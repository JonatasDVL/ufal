from fila import Fila
from caixas import Caixas

fila = Fila()
modoTeste = True

print("------------------------------------------")
print("Bem-vindo ao sistema de atendimento dos Correios")
print("------------------------------------------")

quantidadeDeCaixa = None

if not(modoTeste):
  while quantidadeDeCaixa == None:
    try: 
      quantidadeDeCaixa = int(input("Digite a quantidade de atendente: "))
      if quantidadeDeCaixa > 9:
        print("O máximo de caixas ativo é de 9")
        quantidadeDeCaixa = 9
    except ValueError:
      print("Você digitou um valor inválido, tente novamente!")
      quantidadeDeCaixa = None
  print("------------------------------------------")
else:
  quantidadeDeCaixa = 3

caixasObjeto = Caixas(quantidadeDeCaixa, modoTeste)

print("Caixas Ativos:")
caixasObjeto.imprimirAtendentes()

caixas = caixasObjeto.caixas

aberto = True
i = 1

while aberto or not(fila.vazia()) or caixasObjeto.contarOcupados() != 0:
  print("------------------------------------------")
  j  = 0
  if caixasObjeto.contarOcupados() != 0: 
    j += 1
    print(f"{j}. Finalizar atendimento e provavelmente chamar o próximo da fila para o caixa;")
  if caixasObjeto.contarAbertos() != quantidadeDeCaixa:
    j += 1
    print(f"{j}. Abrir caixa;")
  if caixasObjeto.contarAbertos() != 0:
    j += 1
    print(f"{j}. Fechar caixa;")
  if aberto == True:
    j += 1
    print(f"{j}. Adicionar um cliente;")
    j += 1
    print(f"{j}. Fechar as portas do Correio;")
  try:
    opcao = float(input("Digite o número de uma das opções acima: "))
  except ValueError:
    opcao = 1000
  print("------------------------------------------")

  if ((opcao == j-2 or opcao == j-3 or opcao == j-4) and aberto == True) or aberto == False: 
    if caixasObjeto.contarOcupados() != 0 and (opcao == j-4 and caixasObjeto.contarAbertos() != 0 and caixasObjeto.contarAbertos() != quantidadeDeCaixa or opcao == j-3 and (caixasObjeto.contarAbertos() == 0 or caixasObjeto.contarAbertos() == quantidadeDeCaixa) or aberto == False and opcao == j-2 and caixasObjeto.contarAbertos() != 0 and caixasObjeto.contarAbertos() != quantidadeDeCaixa or opcao == j-1 and (caixasObjeto.contarAbertos() == 0 or caixasObjeto.contarAbertos() == quantidadeDeCaixa)):
      print("Caixas disponiveis finalizar o atendimento e provavelmente para chamar o próximo:")
      for caixa in caixas:
        if caixa.ocupado():
          caixa.imprimir()          
      j = "chamar"
    elif caixasObjeto.contarAbertos() != quantidadeDeCaixa and (opcao == j-3 or opcao == j-2 and caixasObjeto.contarAbertos() == 0 or aberto == False and (opcao == j-1 or opcao == j and caixasObjeto.contarAbertos() == 0)): 
      print(f"Caixas disponiveis para abrir caixa")
      caixasObjeto.imprimirAtendentes(1)
      j = "abrir"
    else:
      print(f"Caixas disponiveis para fechar caixa")
      caixasObjeto.imprimirAtendentes(2)
      j = "fechar"
    try:
      opcao = int(input("Digite o número um dos caixas acima: "))
    except ValueError:
      opcao = 1000
    print("------------------------------------------")

    # ajeitar
      #     for caixa in caixas:
      # if not(caixas.ocupado()):
    
    try:
      caixas[opcao-1].ocupado()
      cond = True
    except ValueError:
      cond = False

    if j == "chamar" and cond and caixas[opcao-1].ocupado():  
      numero, nome = caixas[opcao-1].desocupar()
      print(f"Cliente {nome} de Nº {numero} saiu!")
      if not(fila.vazia()):
        numero, nome = fila.remover()
        caixas[opcao-1].chamar({"nome": nome, "numero": numero})
    elif j == "abrir" and cond and not(caixas[opcao-1].aberto):
      caixas[opcao-1].abrir()
      if fila.vazia():
        print(f"O caixa de Nº {opcao} abriu!")
      else:
        numero, nome = fila.remover()
        caixas[opcao-1].chamar({"nome": nome, "numero": numero})
        print(f"Cliente {nome} de Nº {numero} saiu e o caixa de Nº {opcao} fechou!")
    elif j == "fechar" and cond and caixas[opcao-1].aberto:
      if caixas[opcao-1].ocupado():
        numero, nome = caixas[opcao-1].desocupar()
        print(f"Cliente {nome} de Nº {numero} saiu e o caixa de Nº {opcao} fechou!")
      else:
        print(f"O caixa de Nº {opcao} fechou!")
      caixas[opcao-1].fechar()
    else:
      print("Valor Inválido")

# ajeitado
  elif opcao == j-1 and aberto == True:
    nome = input(f"Digite o nome do cliente de Nº {i}: ")
    if len(nome) >= 2:
      fila.inserir(i, nome)
    else:
      fila.inserir(i)
    i += 1 
    for caixa in caixas:
      if not(caixa.ocupado()) and caixa.aberto:
        numero, nome = fila.remover()
        caixa.chamar({"nome": nome, "numero": numero})
        break
  elif opcao == j and aberto == True:
    print("As portas do Correio foram fechadas!")
    aberto = False
  else:
    print("Valor Inválido")

  caixasObjeto.imprimir()
  fila.imprimir()
