"""
palavra = input("Digite uma palavra: ").upper()
letra = input("Digite uma letra: ").upper()
i = 0

while(i < len(palavra) and palavra[i] != letra):
    i += 1
if(len(palavra) == i):
    print("Não tem essa letra na palavra!")
else:
    print("Tem essa letra na palavra!")

"""

palavra = input("Digite uma palavra: ").upper()
letra = input("Digite uma letra: ").upper()
i = 0

while(i < len(palavra) and palavra[i] != letra):
    i += 1
if(palavra[i] == letra):
    print("Tem essa letra na palavra!")
else:
    print("Não tem essa letra na palavra!")
