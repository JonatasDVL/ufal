# 2. Problema dos palíndromos. Um palíndromo é uma palavra ou frase que mantém o mesmo sentido
# quando lida de trás para frente. Palíndromos estão muito presentes na literatura e na publicidade, porque
# são palavras fáceis de memorizar. Exemplos de palavras palíndromas são arara, asa, osso, radar, reger,
# ralar, reviver, somávamos etc. Exemplos de nomes de pessoas que são palíndromos: Ada, Ana, Bob,
# Natan, Renner, Mussum, entre outros. Escreva um programa que recebe como entrada uma string que
# representa uma palavra e imprima na tela “sim” se a palavra é um palíndromo e “não” caso contrário.
# Você deve utilizar uma das estruturas de dados pilha para implementar esse programa.

# Exemplos de entradas e saídas:
# Expressão                 Saída
# osso                      sim
# radar sim
# a base do teto desaba     sim
# a cara rajada da jararaca sim
# ame o poema               sim
# rodolfo                   não
# algoritmo                 não


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
        print("\n__________")
        while aux != None:
            print(aux.valor, end=" ")
            aux = aux.proximo

def verificadorPalidromo(expressao):
    pilha1 = Pilha()
    pilha2 = Pilha()
    expressao = expressao.replace(" ","").lower()

    substituicoes = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'ã': 'a', 'õ': 'o', 'ñ': 'n', 'ç': 'c', '-': '', 
        '.': '', ',': '', ':': '', ';': ''
    }
    for substituido, sucessor in substituicoes.items():
        expressao = expressao.replace(substituido, sucessor)

    for caractere in expressao:
        pilha1.inserir(caractere)

    aux = pilha1.topo
    while aux != None:
        pilha2.inserir(aux.valor)
        aux = aux.proximo

    aux = pilha1.topo
    aux2 = pilha2.topo
    cond = "sim"
    while aux != None and aux2 != None and cond == "sim":
        if aux.valor != aux2.valor:
            cond = "não"
        else:
            cond = "sim"
        aux = aux.proximo
        aux2 = aux2.proximo
    
    return cond

expressoes = ["arara", "ana", "bob", "natan", "renner", "mussum", "ama", "esse", "socorram me subi no onibus em marrocos", "anotaram a data da maratona", "a torre da derrota", "a sacada da casa", "após a sopa", "a mala nada na lama", "a Rita", "Ame o poema", "A base do teto desaba", "A cara rajada da jararaca", "Socorram-me, subi no ônibus em Marrocos", "O lobo ama o bolo", "A grama é amarga", "Ame o poema", "Anotaram a data da maratona", "Rodolfo", "Algoritmo", "Carneiro", "TAFRJ", "Jônatas","Duarte","Vital","Leite","ovo","ava","A miss é pessima"]

print(f"{'Expressão':<40} Saída")
for expressao in expressoes:
    print(f"{expressao:<40} {verificadorPalidromo(expressao)}")
