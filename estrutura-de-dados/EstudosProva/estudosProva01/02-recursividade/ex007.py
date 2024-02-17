#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 07: Busca binária: Implemente a busca binária de forma recursiva em uma lista ordenada.

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
def busca_binaria(lista, elemento):
    return busca_binaria_recursiva(lista, elemento, 0, len(lista) - 1)

# Exemplo de uso:
lista_ordenada = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
elemento_procurado = 12
indice = busca_binaria(lista_ordenada, elemento_procurado)

if indice != -1:
    print(f"O elemento {elemento_procurado} foi encontrado no índice {indice}.")
else:
    print(f"O elemento {elemento_procurado} não está na lista.")