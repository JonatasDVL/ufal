# Uma palavra ou frase é um palíndromo quando pode ser lida de trás pra frente mantendo o mesmo sentido. Exemplos de palavras são “ovo”, “radar”, “reviver”. Exemplos de frases são “A base do teto desaba”, “A dama admirou o rim da amada”.
# Faça um programa que recebe uma palavra ou frase e responda se ela é um palíndromo ou não.

class Celula:
    valor = None
    proximo = None

    def __init__(self,valor):
        self.valor = valor

class Pilha:
    topo = None

    def __init__(self):
        self.topo = None

    def inserir(self,valor):
        c = Celula(valor)
        c.proximo = self.topo
        self.topo = c

    def remover(self):
        if self.topo != None:
            self.topo = self.topo.proximo
        
    def imprimir(self):
        aux = self.topo
        while aux != None:
            print(aux.valor)
            aux = aux.proximo
        print('---')

palavra = "A dama admirou o rim da amada" #coloque apenas strings sem acentos, pois estava com preguiça de fazer para pegar com acentos kkkkkkkk
# copiando a palavra na pilha1
pilha1 = Pilha()
for i in range(len(palavra)):
  pilha1.inserir(palavra[i])
# pilha1.imprimir()

# copiando a palavra ao contrario na pilha2
pilha2 = Pilha()
aux = pilha1.topo
for i in range(len(palavra)):
  pilha2.inserir(aux.valor)
  aux = aux.proximo
# pilha2.imprimir()

x = 0
aux1 = pilha1.topo
aux2 = pilha2.topo
while x != -1 and x!=len(palavra.replace(' ', '')):
    i = 0
    j = 0
    while i == 0:
        if aux1.valor != ' ':
            i+=1
            valor1 = aux1.valor
        aux1 = aux1.proximo    
    while j == 0:
        if aux2.valor != ' ':
            j+=1
            valor2 = aux2.valor
        aux2 = aux2.proximo
    if valor1.lower() == valor2.lower():
        x+=1
        print(f"ok: {valor1} {valor2} {x}")
    else:
        print(f"Não ok: {valor1} {valor2} {x}")
        x=-1

if x == -1:
    print("Essa entrada não é um palidromo")
else:
    print("Essa entrada é um palidromo")
