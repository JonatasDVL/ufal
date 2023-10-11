# Faça um programa capaz de identificar a letra mais frequente em um texto em um arquivo. A saída deverá ser a letra mais frequente seguida por pela porcentagem de suas ocorrências no texto. Deve-se desconsiderar diferenças de maiúsculas e minúsculas. Qualquer outro caractere que não seja uma letra de A a Z deverá ser desconsiderado no cálculo da porcentagem e da contagem, inclusive o caractere vazio (espaço em branco) deve ser desconsiderado. A saída deve ser dada em letras minúsculas. Segue um arquivo de exemplo.

import os
caminho = os.path.abspath(__file__).replace("q2.py", "q2.txt")

alfabeto = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, 
    "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, 
    }

total_de_letras = 0

with open(caminho, "r") as arquivo:
    conteudo = arquivo.read().lower()

for letra in conteudo:
    if letra in "abcdefghijklmnopqrstuvwxyz":
        alfabeto[letra] += 1
        total_de_letras +=1

maior_letra = "a"
for chave in alfabeto.keys():
    if alfabeto[maior_letra] < alfabeto[chave]:
        maior_letra = chave

porcetagem_da_maior_letra = round(alfabeto[maior_letra]/total_de_letras*100, 2)

print(f"A letra mais frequente foi a letra '{maior_letra}' com {porcetagem_da_maior_letra}%")