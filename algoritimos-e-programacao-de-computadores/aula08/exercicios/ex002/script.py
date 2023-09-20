# 2. Escreva um programa que lê um arquivo contendo endereços IPs, da seguinte forma:
#     200.135.80.9
#     192.168.1.1
#     8.35.67.74
#     257.32.4.5
# O programa deve mostrar os IPs indicando os que são válidos e inválidos (um endereço ip válido não pode ter uma de suas partes maior que 255).

enderecos = []

arquivo = open(r"ex002\arquivo.txt", "r")
for linha in arquivo.readlines():
    linha = linha.replace("\n","")
    enderecos.append(linha)
arquivo.close()

print(enderecos)

for endereco in enderecos:
    partes = endereco.split(".")
    cond = 0
    if len(partes) == 4:
        for parte in partes:
            parte = int(parte)
            if parte > 255 or parte < 0:
                print(f"O endereço ip, {endereco}, não é válido")
                break
            else: 
                cond += 1
        if cond == 4:
            print(f"O endereço ip, {endereco}, é válido")
    else: 
        print(f"O endereço ip, {endereco}, não é válido")
    