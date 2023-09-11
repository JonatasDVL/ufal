# 2. Você está trabalhando em um programa de codificação de caracteres. Atualmente você está trabalhando com o código UTF8, que relaciona letras e códigos como descrito na tabela abaixo. Implemente um programa que recebe uma lista de códigos UTF8 e decodifique para a linguagem natural.

# a 61 g 67 l 6c q 71 v 76
# b 62 h 68 m 6d r 72 w 77
# c 63 i 69 n 6e s 73 x 78
# d 64 j 6a o 6f t 74 y 79
# e 65 k 6b p 70 u 75 z 7a
# f 66 espaço 20

# Ex: entrada = ["65","75","20","61","6d","6f","20","70","72","6f","67","72","61","6d","61","72"]
# saída = "eu amo programar"

def decodificadorUTF8(dicionario, entrada):
    saida = ""
    for i in range(len(entrada)):
        for caractere, codigo in dicionario.items():
            if codigo == entrada[i]:
                saida += caractere
    return saida

dicionario = {
    "a": "61", "g": "67", "l": "6c", "q": "71", "v": "76",
    "b": "62", "h": "68", "m": "6d", "r": "72", "w": "77",   
    "c": "63", "i": "69", "n": "6e", "s": "73", "x": "78",
    "d": "64", "j": "6a", "o": "6f", "t": "74", "y": "79",
    "e": "65", "k": "6b", "p": "70", "u": "75", "z": "7a",
    "f": "66", " ": "20"
}


entrada = ["65","75","20","61","6d","6f","20","70","72","6f","67","72","61","6d","61","72"]

print(decodificadorUTF8(dicionario, entrada))
