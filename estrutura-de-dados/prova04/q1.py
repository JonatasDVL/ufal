# 1. Em um trabalho escolar, um professor de matemática pediu para que os alunos escrevessem
# expressões aritméticas de forma a exercitar tal conteúdo. Em sala de aula foi dito que uma expressão
# aritmética bem formada obedece as seguintes exigências:
# • todo parênteses, colchetes ou chaves que for aberto deve ser fechado;
# • nenhum parênteses, colchetes ou chaves pode ser fechado sem antes ter sido aberto;
# • deve haver correspondência na ordem de abertura e fechamento de parênteses, colchetes ou chaves.
# Escreva um programa que recebe como entrada uma expressão aritmética e imprime “sim” se a expressão estiver
# correta e “não” caso contrário. Você pode assumir que os operadores e operandos estão escritos corretamente,
# pois o objetivo é verificar a abertura e fechamento de colchetes, parênteses e chaves. Implemente a estrutura
# de dados pilha da forma mais adequada para resolver o problema.
# Exemplos de entradas e saídas:
# Expressão Saída
# (1 + 2) + (3 + 4)     sim
# {[(1 + 2) + (3 + 4)]} sim
# [()()]                sim
# {[()()]}              sim
# ((                    não
# [()()[                não
# {[()))]}              não

class Celula():
  def __init__(self, valor, proximo=None):
    self.valor = valor
    self.proximo = proximo

class Pilha():
  topo = None

  def inserir(self, valor):
    proximo = self.topo
    c = Celula(valor, proximo)
    self.topo = c

  def remover(self):
    if self.topo != None:
      self.topo = self.topo.proximo

  def imprimir(self):
    aux = self.topo
    print("__________")
    while aux != None:
      print(aux.valor, end=" ")
      aux = aux.proximo

def verificaExpressaoBemFormulada(expressao):
  pilha = Pilha()
  for caractere in expressao:
    if caractere == "{" or caractere == "[" or caractere == "(":
      pilha.inserir(caractere)
    elif (caractere == "}" or caractere == "]" or caractere == ")") and pilha.topo != None:
      if (caractere == "}" and pilha.topo.valor == "{") or (caractere == "]" and pilha.topo.valor == "[") or (caractere == ")" and pilha.topo.valor == "("):
        pilha.remover()
      else:
        return "não"  
    elif caractere != "{" and caractere != "[" and caractere != "(" and caractere != "}" and caractere != "]" and caractere != ")":
      pass
    else:
      return "não"
  if pilha.topo == None:
    return "sim"
  else:
    return "não"

print(f"{'Expressão':<25} Saída")
expressao = "(1 + 2) + (3 + 4)"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "{[(1 + 2) + (3 + 4)]}"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "[()()]"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "{[()()]}"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "(("
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "[()()["
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "{[()))]}"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = ")("
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "{)(}"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "{)()(}"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "{(})"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "{()})"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = "{[(()])}"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")
expressao = ")"
print(f"{expressao:<25} {verificaExpressaoBemFormulada(expressao)}")


