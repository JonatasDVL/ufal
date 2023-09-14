pino1 = []
pino2 = []
pino3 = []

n = int(input("Digite a quantidade de disco na torre de Hanoi: "))
for i in range(n):
    pino1.insert(0,i)

pino = pino1 + []


while pino2 != pino and pino3 != pino: 
    if len(pino2) == 0:
        pino2.append(pino1.pop()) 
    elif len(pino3) == 0:
        pino3.append(pino1.pop())
    elif len(pino1) == 0 and pino2[-1] > pino3[-1]:
        pino1.append(pino2.pop())
    elif len(pino1) == 0 and pino2[-1] < pino3[-1]:
        pino1.append(pino3.pop())
    elif pino1[-1] < pino2[-1]:
        pino2.append(pino1.pop())
    elif pino1[-1] < pino3[-1]:
        pino3.append(pino1.pop())
    elif pino2[-1] < pino3[-1]:
        pino3.append(pino2.pop())
    elif pino2[-1] > pino3[-1]:
        pino2.append(pino3.pop())
    elif pino1[-1] > pino3[-1]:
        pino1.append(pino3.pop())
    elif pino2[-1] < pino1[-1]:
        pino1.append(pino2.pop())
    else:
        break

print(pino,pino1,pino2,pino3)