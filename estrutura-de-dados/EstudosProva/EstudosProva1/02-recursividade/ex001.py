#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 01: Fatorial: Escreva uma função recursiva para calcular o fatorial de um número.

def calcularFatorial (n, fator=1):
    if(n > 1):
        return calcularFatorial (n-1, fator*n)
    return fator

n = int(input("Digite um n fatorial: "))
print(calcularFatorial(n))
