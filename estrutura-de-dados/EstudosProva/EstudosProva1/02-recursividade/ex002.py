#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 02: Fibonacci: Crie uma função recursiva para encontrar o N-ésimo termo da sequência de Fibonacci.

def calcularFibonacci(n, valor=0):
    if n == 1:
        return calcularFibonacci(n-1, 1)
    elif n > 1:
        return calcularFibonacci(n-2, valor) + calcularFibonacci(n-1, valor)
    return valor

n = int(input("Digite o valor de n: "))
print(calcularFibonacci(n))