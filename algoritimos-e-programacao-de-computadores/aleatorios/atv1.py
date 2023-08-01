numeros = []
x = int(input("Digite quantos números você deseja adicionar no conjunto: "))

for i in range (0, x):
    numeros.append(float(input("Digite um número para adicionar ao conjunto: ")))

n = int(input("Digite o valor de n: "))
soma = 0
i=0

while(soma < n+1 and i < len(numeros)):   
    soma += numeros[i]
    i += 1

if(soma > n):
    print("A soma do conjunto é maior que n.")
else:
    print("A soma do conjunto não é maior que n.")