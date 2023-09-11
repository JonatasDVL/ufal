# Exercício Pré-Prova 002
# 2. Dada uma lista de números, crie uma nova lista que contenha apenas os números ímpares.

lista = []
novaLista = []
numero = None


while(numero == None or resposta == "s"):
    numero = int(input("Digite um número inteiro: "))
    resposta = input("Desejas continuar a adicionar numeros(s/n)? ").lower()
    while(resposta != "s" and resposta != "n"):
        resposta = input("Desejas continuar a adicionar numeros(s/n)? ").lower()
    lista.append(numero)

# print(lista)

for i in lista:
    if i % 2 == 1:
        novaLista.append(i)

print(novaLista)