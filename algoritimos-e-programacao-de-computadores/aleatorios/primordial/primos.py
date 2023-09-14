def soma_digitos(numero):
    soma = 0
    numero_str = str(numero)
    for digito in numero_str:
        soma += int(digito)
    if soma < 10:
        return soma
    else:
        return soma_digitos(soma)
    
# def crivo_eratostenes(limite):
#     numeros_primos = [True] * (limite + 1)
#     numeros_primos[0] = numeros_primos[1] = False
    
#     for numero in range(2, int(limite**0.5) + 1):
#         if numeros_primos[numero]:
#             for multiplo in range(numero**2, limite + 1, numero):
#                 numeros_primos[multiplo] = False    
#     primos = [numero for numero, primo in enumerate(numeros_primos) if primo]
    
#     return primos

# limite = 900000000  # Defina o limite para encontrar os números primos até 50
# primos_encontrados = crivo_eratostenes(limite)
# print(primos_encontrados)

print("Número | Espaçamento | Soma dos algarismo")

i2 = 2
espacamento = 0
for i in range(100):
    cont = 0
    for j in range(1,i+1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        if i != 2:
            espacamento = i-i2
        print(f"{i:6d} | {espacamento:11d} | {soma_digitos(i):14d}")
        i2 = i

    

    # Exemplo 14 até 18 = 4 + 5 = 9, logo é padrão de todos os números, 14 até 18 -> 4(18-14) + 5(1+4) = 9(1+8)