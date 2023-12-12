#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 05: Potência: Escreva uma função recursiva para calcular a potência de um número.

def calcularPotencia(base, expoente):
    if(base == 0 or base == 1):
        return base
    elif(expoente > 1):
        return base * calcularPotencia(base, expoente-1)
    elif(expoente < 1):
        return 1 / (base*calcularPotencia(base, -expoente-1)) 
    elif(expoente == 0):
        return 1
    return base

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor da expoente: "))
print(calcularPotencia(base, expoente))