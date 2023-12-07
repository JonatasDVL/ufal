#  Estrutura de Dados
#  Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 02: Implemente uma função recursiva que, dados dois números inteiros x e n, calcule o valor de x^n

import random

def elevacao(x, n):
    if (n == 0):
        if (x == 0):
            return "Inderterminação Matemática"
        return 1
    elif (n > 1):
        return x * elevacao(x, n-1)
    elif (n < -1):
        n = -n
        x * elevacao(x, n-1)
        return 1 / elevacao(x, n-1)

    return x


# x = int(input("x: "))
# n = int(input("n: "))

x = random.randint(-10, 10)
n = random.randint(-10, 10)

print(f"{x} x {n} = {elevacao(x, n)}")


#ainda tem um problema