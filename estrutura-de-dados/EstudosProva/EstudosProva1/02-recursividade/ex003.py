#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 03: Soma de elementos de uma lista: Escreva uma função recursiva para calcular a soma de todos os elementos de uma lista.

def calcularSomaElementos(lista, tamanho, soma=0):
    if(tamanho != -1 and len(lista) != 0):
        return calcularSomaElementos(lista, tamanho-1, soma+lista[tamanho])
    return soma

lista = [2,1,2,3,4,5,6,7,8,9,10,1]
print(calcularSomaElementos(lista, len(lista)-1))