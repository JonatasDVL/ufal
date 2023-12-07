#  Estrutura de Dados
#  Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 01: Implemente uma função recursiva que, dados dois números inteiros x e n, calcule o valor de x.n
import random

def multiplicacao(x, n):
    if(n == 0 or x == 0):
        return 0
    elif (n != 0):
        if(n < 0):
            x = -x
            n = -n
        return x + multiplicacao(x, n-1)
    return x

# x = int(input("x: "))
# n = int(input("n: "))

x = random.randint(-10, 10)
n = random.randint(-10, 10)

print(x,"x",n,"=",multiplicacao(x, n))

