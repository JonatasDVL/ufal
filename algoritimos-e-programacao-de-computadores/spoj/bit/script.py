# https://br.spoj.com/problems/BIT/

def caixaEletronica(v, a):
    i = v//50
    v %= 50
    j = v//10
    v %= 10
    k = v//5
    v %= 5
    l = v
    print(f"Teste {a+1}")
    print(f"{i} {j} {k} {l}")
    print()
    return

valores = []
v = 1

while 0 < v <= 10000:
    v = int(input())
    valores.append(v)

for i in range(len(valores)-1):
    caixaEletronica(valores[i], i)