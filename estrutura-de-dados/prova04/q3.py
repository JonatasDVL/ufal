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

    def imprimir(self):
        aux = self.topo
        print("__________")
        while aux != None:
            print(aux.valor, end=" ")
            aux = aux.proximo


def verificaExpressaoBemFormulada(expressao):
    pilha = Pilha()
    pilha2 = Pilha()

    for caractere in expressao:
        if caractere == "{" or caractere == "}" or caractere == "[" or caractere == "]" or caractere == "(" or caractere == ")":
            pilha.inserir(caractere)

    aux = pilha.topo
    while aux != None:
        pilha2.inserir(aux.valor)
        aux = aux.proximo

    aux = pilha.topo
    aux2 = pilha2.topo
    cond = "sim"
    while aux != None and aux2 != None and cond == "sim":
        if aux.valor == "{" and aux2.valor == "}":
            cond = "sim"
        elif aux.valor == "[" and aux2.valor == "]":
            cond = "sim"
        elif aux.valor == "(" and aux2.valor == ")":
            cond = "sim"
        elif aux2.valor == "{" and aux.valor == "}":
            cond = "sim"
        elif aux2.valor == "[" and aux.valor == "]":
            cond = "sim"
        elif aux2.valor == "(" and aux.valor == ")":
            cond = "sim"
        else:
            cond = "não"
        aux = aux.proximo
        aux2 = aux2.proximo


    return cond


expressao = "(1 + 2) + (3 + 4)"
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = "{[(1 + 2) + (3 + 4)]}"
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = "[()()]"
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = "{[()()]}"
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = "(("
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = "[()()["
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = "{[()))]}"
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = ")("
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = "{)(}"
print(expressao, verificaExpressaoBemFormulada(expressao))
expressao = "{)()(}"
print(expressao, verificaExpressaoBemFormulada(expressao))
