#  Estrutura de Dados
#  Estudos da Aula 03: Algoritmos de Busca
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 02: Busca binária: Implemente a busca binária em uma lista ordenada.

def busca_binaria_recursiva(lista, elemento, esquerda, direita):
    if direita >= esquerda:
        meio = esquerda + (direita - esquerda) // 2
        elemento_meio = lista[meio]

        if elemento_meio == elemento:
            return meio  # Retorna o índice onde o elemento foi encontrado
        elif elemento < elemento_meio:
            return busca_binaria_recursiva(lista, elemento, esquerda, meio - 1)
        else:
            return busca_binaria_recursiva(lista, elemento, meio + 1, direita)
    else:
        return -1  # Retorna -1 se o elemento não estiver na lista

# Função de apoio para iniciar a busca binária recursiva
def busca_binaria_inicial(lista, elemento):
    return busca_binaria_recursiva(lista, elemento, 0, len(lista) - 1)

# Exemplo de uso:
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17]
elemento_procurado = 11
indice = busca_binaria_inicial(lista_ordenada, elemento_procurado)

if indice != -1:
    print(f"O elemento {elemento_procurado} foi encontrado no índice {indice}.")
else:
    print(f"O elemento {elemento_procurado} não está na lista.")