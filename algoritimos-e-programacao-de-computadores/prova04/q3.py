# Você foi contratado para dar manutenção em um sistema de uma empresa. Ao observar os dados, você percebeu que o sistema armazena dados sensíveis do usuário de forma não protegida, inclusive a senha de acesso. Você então decidiu aplicar mecanismos de segurança da informação, como criptografia para a senha do usuário. Escreva um programa que lê um arquivo csv com dados do usuário, encripta a senha do usuário e escreve um novo arquivo csv com os mesmos dados, mas com a nova senha criptografada. Para criptografar a senha, você irá utilizar a seguinte função:
    # import hashlib
    # def encriptar( t e x t o ):
        # hash_obj = hashlib.sha256( )
        # hash_obj.update (texto.encode('utf−8'))
        # hash_hex = hash_obj.hexigest()
        # return hash_hex
    # Exemplo de arquivo:
    # id,usuario,telefone,email,senha
    # 1,ana,982569878,ana@gmail.com,12345
    # 2,bob,998784523,bob@gmail.com,112205
    # 3,pedro,996584578,pedro@gmail.com,ab23pedro
    # 4,marta,985478569,marta@hotmail.com,mtr123

import hashlib
import os

caminho = os.path.abspath(__file__).replace("q3.py", "q3.csv")
caminho2 = caminho.replace("q3.csv", "q3-novo.csv")

def encriptar(texto):
    hash_obj = hashlib.sha256()
    hash_obj.update(texto.encode('utf-8'))
    hash_hex = hash_obj.hexdigest()
    return hash_hex

dataFrame = {}

with open(caminho, "r") as arquivo:
    i=0
    for linha in arquivo.readlines():
        if i == 0:
            lista = linha.replace("\n","").split(",")
            for chave in lista:
                dataFrame[f"{chave}"] = []
            i+=1
        else:
            lista2 = linha.replace("\n","").split(",")
            j =0
            for chave in lista:
                if chave == "senha":
                    encritado = encriptar(lista2[j])
                    dataFrame[f"{chave}"].append(encritado)
                else:
                    dataFrame[f"{chave}"].append(lista2[j])
                j += 1

with open(caminho2, "w") as arquivo:
    k=0
    for chave in dataFrame.keys():
        if k == j-1:
            k=0
            arquivo.write(f"{chave}\n")
        elif k != j-1:
            k+=1
            arquivo.write(f"{chave},")
    for i in range(j-1):
        for chave in dataFrame.keys():
            if k == j-1:
                k=0
                arquivo.write(f"{dataFrame[chave][i]}\n")
            elif k != j-1:
                k+=1
                arquivo.write(f"{dataFrame[chave][i]},") 

