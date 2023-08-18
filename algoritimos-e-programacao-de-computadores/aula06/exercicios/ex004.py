""" Algoritimos e Programação de Computadores
 Aula 06: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 04:
    4. Faça um algoritmo que copie o conteúdo de uma lista para outra, eliminando valores repetidos. Implemente funções para isso
"""

def copiandoListaSemRepeticao(lista):
    lista2 = []
    for conteudo in lista:
        condicao = False
        for i in range(len(lista2)):
            if(conteudo == lista2[i]):
                condicao = True
                i == len(lista2)
        if(condicao == False):
            lista2.append(conteudo)
    return lista2
            
lista = [0,1,2,3,4,5,56,7,8,4,545,2132,"5",4,84,321,3,8,51,534,887,0]
print(lista)
print(copiandoListaSemRepeticao(lista))