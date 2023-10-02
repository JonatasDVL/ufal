# https://br.spoj.com/problems/SENHA/

n = int(input())

while n != 0:
    dicionarios = []
    senhaLetras = []

    for i in range(n):
        senhaNumero = ""
        senhaLetra = ""
        entrada = input().upper().split(" ")
        for n in range(0, 10):
            senhaNumero += f"{entrada[n]}"    
        dicionarios.append({"A": senhaNumero[0:2],"B": senhaNumero[2:4],"C": senhaNumero[4:6],"D": senhaNumero[6:8],"E": senhaNumero[8:10]})
        for l in range(10, 16):
            senhaLetra += f"{entrada[l]}"    
        senhaLetras.append(senhaLetra)
    
    resposta = ""
    for j in range(6):
        a = dicionarios[0][j][0] # é o senha letra
        b = dicionarios[0][j][1]    
        for i in range(1, n):
            print(dicionarios[i][j][0])
            a2 = dicionarios[i][j][0]
            print(dicionarios[i][j][1])
            b2 = dicionarios[i][j][1]
            if a != None:
                if a == a2:
                    a = None
                    chave = a2
                elif a == b2:
                    a = None
                    chave = b2
                elif b == a2:
                    a = None
                    chave = a2
                elif b == b2:
                    a = None
                    chave = b2
            elif chave == a2:
                chave = a2
            elif chave == b2:
                chave = b2
            else:
                print("Não foi possivel")
                break
        resposta += f"{chave} " 
    respostas = (f"Teste {a+1}\n{resposta}\n")
    
    n = int(input())

print(respostas)