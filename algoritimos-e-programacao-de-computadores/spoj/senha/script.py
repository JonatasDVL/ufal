# https://br.spoj.com/problems/SENHA/

n = int(input())
z = 0
respostas = []

while n != 0:
    dicionarios = []
    senhaLetras = []

    for i in range(n):
        entrada = input().upper().replace(" ","")    
        dicionarios.append({"A": entrada[0:2],"B": entrada[2:4],"C": entrada[4:6],"D": entrada[6:8],"E": entrada[8:10]})    
        senhaLetras.append(entrada[10:16])
     
    resposta = ""
    for j in range(6):
        a = dicionarios[0][senhaLetras[0][j]][0] # é o senha letra
        b = dicionarios[0][senhaLetras[0][j]][1]    
        for i in range(1, n):
            a2 = dicionarios[i][senhaLetras[i][j]][0]
            b2 = dicionarios[i][senhaLetras[i][j]][1]
            if a != None:
                if (a == a2 and b != b2) or (b == a2 and a != b2):
                    chave = a2
                    a = None
                elif (a == b2 and b != a2) or (b == b2 and a != a2):
                    chave = b2
                    a = None
            elif chave == a2:
                chave = a2
            elif chave == b2:
                chave = b2
        resposta += f"{chave} "
    z += 1

    respostas.append(f"Teste {z}\n{resposta}\n")
    
    n = int(input())

for i in range(0,z):
    print(respostas[i])