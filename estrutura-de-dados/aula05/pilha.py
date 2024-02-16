tam = 10
pilha = [None] * tam
fim = 0

def inserir(valor, fim):
  if fim < tam:
    pilha[fim] = valor
    fim += 1
    return fim
  print("Erro Pilha Cheia")
  return fim

def deleteEEdita(fim, valor=None):
  if fim > 0 and valor == None:
    pilha[fim] = valor
    fim -= 1
    return fim
  else:
    fim -= 1
    pilha[fim] = valor
    return fim
  print("Erro Pilha Vazia")
  return fim


fim = inserir(5, fim)
print(pilha)

fim = inserir(1, fim)
print(pilha)

fim = inserir(7, fim)
print(pilha)

fim = deleteEEdita(fim, 3)
print(pilha)

fim = deleteEEdita(fim)
print(pilha)