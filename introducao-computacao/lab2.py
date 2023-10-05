# Roteiro de Laboratório – Cálculos do Fatorial (versões iterativa e recursiva)
    # Objetivo: Dado um número, o sistema deve receber efetuar o cálculo do seu fatorial de duas formas:
        # ◦ Utilizando um algoritmo iterativo: função fatorial_iterativo(numero)
        # ◦ Utilizando um algoritmo recursivo: função fatorial_recursivo(numero)

    # Comportamento desejado:
        # ◦ O sistema deve ler inicialmente um número: numero.
        # ◦ Em seguida, deve executar a função fatorial_iterativo(numero) e apresentar seu retorno.
        # ◦ Finalmente, deve executar a função fatorial_recursivo(numero) e apresentar seu retorno.
        # ◦ Os retornos das duas funções deve ser o mesmo, equivalente a “numero fatorial”.
    
    # Diretrizes Adicionais:
        # ◦ A função “fatorial_iterativo(numero)” deve utilizar estruturas de repetição (enquanto ou para).
        # ◦ A função “fatorial_recursivo(numero)” NÃO deve utilizar estruturas de repetição (enquanto ou para), mas chamadas recursivas para a função.

def fatorial_iterativo(numero):
    fatorial = 1 
    for i in range(2, numero):
        fatorial *= i
    return fatorial

def fatorial_recursivo(numero):
    return fatorial

numero = int(input("Digite um número: "))

print(fatorial_iterativo(numero))
# print(fatorial_recursivo(numero))