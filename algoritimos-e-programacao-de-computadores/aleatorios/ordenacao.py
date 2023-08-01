"""
Dado um conjunto de n valores inteiros, ordene-os em ordem crescente.

Formato de entrada

Um inteiro n indicando quantos números serão fornecidos, seguidos de n inteiros separados por um final de linha

Formato de saída

A sequência de n números ordenada em ordem crescente, obedecendo ao seguinte formato:
[numero][numero][numero][numero]
Onde depois do último número existe um final de linha.

"""

numeros = []
ordem = []
ordem2 = []
qnt = int(input('Quantos números você deseja inserir? '))
verificador = 0

for i in range(0, qnt):
    numeros.append(int(input(f"Digite o número {i+1}: ")))

'''
while(verificador != qnt):
    for j in range(qnt+1):
        if(i != 0):
            if(numeros[j] < numeros[j+1]):
                verificador += 1
            else:
                verificador = 0
                break
    '''

for n in range(len(numeros) - 1):
    if numeros[n] >= numeros[n+1]:
        ordem.insert(n, numeros[n+1])
        ordem.insert(n+1, numeros[n])
        print(ordem)
    numeros = ordem[:]