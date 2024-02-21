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

pilha = Pilha()
pilha.inserir(10)
pilha.inserir(-1)
pilha.inserir(0)
pilha.imprimir()
pilha.remover()
pilha.imprimir()
pilha.remover()
pilha.imprimir()
pilha.remover()
pilha.imprimir()
pilha.remover()
pilha.imprimir()
pilha.inserir(0)
pilha.imprimir()