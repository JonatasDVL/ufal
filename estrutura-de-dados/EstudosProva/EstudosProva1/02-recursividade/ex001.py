#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 01: Fatorial: Escreva uma função recursiva para calcular o fatorial de um número.

# def calcularFatorial (n, fator=1):
#     if(n > 1):
#         return calcularFatorial (n-1, fator*n)
#     return fator

#  Forma mais tradicional
def calcularFatorial (n):
    if(n == 1 or n == 0):
        return 1
    elif(n < 0):
        return "Não existe fatorial de número negativo"
    return n * calcularFatorial (n-1)



n = int(input("Digite um n fatorial: "))
print(calcularFatorial(n))
