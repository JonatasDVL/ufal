# Exercício Pré-Prova 001
# Listas:
# 1. Crie uma lista com os números de 1 a 10 e imprima os números pares.

lista = []

for i in range(1,11):
    lista.append(i)

# print(lista)

for i in range(1,11):
    if i % 2 == 0:
        print(i,end=" ")