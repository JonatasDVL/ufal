def converter_para_base10(numero, base_origem):
    # Dicionário que mapeia caracteres alfabéticos (A-Z) para valores numéricos (10-35)
    alfabeto = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
                "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
                "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}  # 10 números (0-9) e 26 letras (A-Z)
    resultado = 0

    # Loop através dos caracteres no número, da direita para a esquerda
    for pos, caractere in enumerate(numero, 1):
        if caractere.isalpha():
            caractere = alfabeto[f"{caractere}"]  # Se o caractere é alfabético, substitua pelo valor numérico correspondente
        resultado += int(caractere) * (base_origem ** (len(numero) - pos))  # Adicione o valor do caractere ponderado pela posição

    return resultado

# Função para converter um número em base 10 para outra base
def converter_da_base10(numero, base_destino):
    restos = []
    alfabeto = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
                "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
                "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}
    numero = int(numero)  # Converta o número de entrada para um número inteiro
    while numero >= base_destino:
        resto = numero % base_destino
        # Se o resto for maior que 9, substitua-o pelo caractere correspondente no alfabeto
        if resto > 9:
            a = list(alfabeto.keys())
            resto = a[resto - 10]
        restos.append(resto)
        numero = numero // base_destino  # Atualize o número dividindo pela nova base

    restos.append(numero)  # Adicione o último dígito
    resultado = ""

    # Monte o resultado concatenando os dígitos da lista de restos na ordem correta
    for i in range(1, len(restos) + 1):
        resultado += f"{restos[-i]}"
    return resultado

# Função para converter um número entre bases diferentes
def converter_base(base_origem,base_destino, numero):
    if base_origem != 10:
        numero = converter_para_base10(numero, base_origem)  # Se a base de origem não for 10, converta para base 10
    if base_destino != 10:
        resultado = converter_da_base10(numero, base_destino)  # Se a base de destino não for 10, converta de base 10
        return resultado
    return numero

print(converter_base(2,10,"1101"))
print(converter_base(3,10,"101"))
print(converter_base(4,10,"32"))
print(converter_base(5,10,"24"))
print(converter_base(6,10,"20"))
print(converter_base(7,10,"16"))
print(converter_base(8,10,"12"))
print(converter_base(9,10,"11"))
print(converter_base(10,10,"42"))
print(converter_base(11,10,"3A"))
print(converter_base(12,10,"32"))
print(converter_base(13,10,"2B"))
print(converter_base(14,10,"28"))
print(converter_base(15,10,"25"))
print(converter_base(16,10,"22"))
print(converter_base(17,10,"1H"))
print(converter_base(18,10,"1G"))
print(converter_base(19,10,"1F"))
print(converter_base(20,10,"1E"))
print(converter_base(21,10,"1D"))
print(converter_base(22,10,"1C"))
print(converter_base(23,10,"1B"))
print(converter_base(24,10,"1A"))
print(converter_base(25,10,"19"))
print(converter_base(26,10,"18"))
print(converter_base(27,10,"17"))
print(converter_base(28,10,"16"))
print(converter_base(29,10,"15"))
print(converter_base(30,10,"14"))
print(converter_base(31,10,"13"))
print(converter_base(32,10,"12"))
print(converter_base(33,10,"11"))
print(converter_base(34,10,"10"))
print(converter_base(35,10,"Z"))
print(converter_base(36,10,"Y"))
