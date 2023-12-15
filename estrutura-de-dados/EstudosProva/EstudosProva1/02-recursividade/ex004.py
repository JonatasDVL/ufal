#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 04: Contagem regressiva: Crie uma função recursiva que imprima uma contagem regressiva a partir de um número dado até zero.

# def calcularContagemRegressiva(n):
#     if(n > 0):
#         print(n)
#         return calcularContagemRegressiva(n-1)
#     return n

# Forma mais tradicional
def calcularContagemRegressiva(n):
    if(n == 0):
        return 0
    print(n)
    if(n < 0):
        return calcularContagemRegressiva(n+1)
    return calcularContagemRegressiva(n-1)

n = int(input("Digite o valor de n: "))
print(calcularContagemRegressiva(n))