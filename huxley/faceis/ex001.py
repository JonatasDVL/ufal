## 1000 Números do Tio Willy
n = 0

while(n != -1):
    k = 0
    n = 0
    x = 0
    lista = []

    while(n != -1 and x != 1001):
        n = int(input())
        if(n != -1):
            n1 = n
            lista.append(n)
        x += 1

    for i in range(0, x-1):
        if(lista[i] == n1):
            k += 1
    if(k != 0):
        print(f"{n1} appeared {k} times")


"""
k = 0
n = 0
x = 0
lista = []

while(n != -1):
    n = int(input())
    if(n != -1):
        n1 = n
        lista.append(n)
    x += 1

for i in range(0, x-1):
    if(lista[i] == n1):
        k += 1
    if((i / 1000) == 1 or i == (x-2)):
        print(f"{n1} appeared {k} times")
"""