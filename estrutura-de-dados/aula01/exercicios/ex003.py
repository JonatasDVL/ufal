#  Estrutura de Dados
#  Aula 01: Introdução 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 03:
#  3. Calcular o fatorial de um número
#  Função de Custo de Tempo deste Algoritmos:

def calcularFatorial(fator, fatorial=1):
    if fator != 1:
        fatorial *= fator
        fator -=1
        return calcularFatorial(fator, fatorial)
    else:
        return fatorial

numero = 5

print(calcularFatorial(numero)) 

# def fatorial(n):
#     if n==1 or n==0:
#          return 1
#     else:
#         return fatorial(n-1)*n
       
# print(fatorial(numero))