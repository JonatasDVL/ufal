# https://br.spoj.com/problems/QUERM/   

def verificaGanhadores(entradas, a):
    for i in range(len(entradas)):
        if (i+1) == int(entradas[i]):
            ganhador = i+1 
    print(f"Teste {a+1}")
    print(ganhador)
    print()
    return

valores = []
n = int(input())

while 0 < n <= 10000:
    entradas = input().split()
    valores.append(entradas)
    n = int(input())


for i in range(len(valores)):
    verificaGanhadores(valores[i], i)