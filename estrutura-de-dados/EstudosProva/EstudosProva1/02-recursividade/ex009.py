#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 09: Soma de dígitos: Escreva uma função recursiva para calcular a soma dos dígitos de um número inteiro.

def soma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + soma_digitos(n // 10)

# Exemplo de uso:
numero = 12345
resultado = soma_digitos(numero)
print(f"A soma dos dígitos de {numero} é {resultado}.")