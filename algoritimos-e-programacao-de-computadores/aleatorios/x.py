palavraA = input("Digite uma palavra: ")
palavraB = input("Digite outra palavra: ")

if(len(palavraA) < len(palavraB)):
    temp = palavraA
    palavraA = palavraB
    palavraB = temp
contador = 0
for i in range(len(palavraA)):
    print(contador, len(palavraB), palavraA[i], palavraB[contador]) 
    if(contador != len(palavraB)):
        if(palavraA[i] == palavraB[contador]):
            contador += 1
        else:
            contador = 0
            if(palavraA[i] == palavraB[contador]):
                contador += 1
    else:
        break
if(contador == len(palavraB)):
    substring = f"{palavraB} é uma substring de {palavraA}."
else:
    substring = f"{palavraB} não é uma substring de {palavraA}."

print(substring)