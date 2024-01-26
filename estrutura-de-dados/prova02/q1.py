# 1. A mediana de um conjunto com um número ímpar de elementos é o valor central que se obtém apósordenar o conjunto. 
# A mediana de um conjunto com um número par de elementos é a média aritméticados dois valores centrais que se obtêm após ordenar o conjunto. 
# Por exemplo, para obter a mediana do conjunto de valores 1, 3, 4, 5, 4, 2}, considera-se o conjunto ordenado {1, 2, 3, 4, 4, 5}; os dois valores 
# centrais são 3 e 4, pelo que a mediana é 3.5. Escreva um programa para achar e imprimir a medianade um conjunto de valores inteiros utilizando um
# algoritmo de ordenação. Seu código deve possuir uma função que recebe um vetor de valores não ordenados e imprime na tela tanto o vetor ordenado 
# quanto o valor da mediana para o conjunto.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j-1] > lista[j]:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            j -= 1
    return lista

def mediana(lista):
    lista = insertion_sort(lista)
    if len(lista) % 2 == 0:
        meio = len(lista)//2
        mediana = (lista[meio] + lista[meio-1]) / 2
    else:
        meio = len(lista)//2
        mediana = lista[meio]
    return lista, mediana

lista = [2,2,2,2,3,4,4,4,4]
lista, mediana_lista = mediana(lista)
print(f"Lista Ordenada: {lista}, Mediana: {mediana_lista}")