#  Estrutura de Dados
#  Estudos da Aula 03: Algoritmos de Busca
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 01: Busca linear: Escreva uma função que realize uma busca linear em uma lista por um elemento específico.

def busca_linear(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Retorna o índice onde o elemento foi encontrado
    return -1  # Retorna -1 se o elemento não estiver na lista

# Exemplo de uso:
lista_exemplo = [4, 2, 7, 1, 9, 5]
elemento_procurado = 7
indice = busca_linear(lista_exemplo, elemento_procurado)

if indice != -1:
    print(f"O elemento {elemento_procurado} foi encontrado no índice {indice}.")
else:
    print(f"O elemento {elemento_procurado} não está na lista.")