num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))

maiorDivisor = 1
if(num1 < num2):
    j = num1
else:
    j = num2

if(num1 == num2):
    for i in range (1, j+1):
        if(num1 % i == 0 and num2 % i == 0 and maiorDivisor < i):
            maiorDivisor = i
else:
    maiorDivisor = num1
    
print(maiorDivisor)