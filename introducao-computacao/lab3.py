# Roteiro de Laboratório – Mudança de Bases Numéricas
    # Objetivo: Dado um número, sua base de origem e a informação da base de destino, o sistema deve receber realizar a conversão de base e apresentar o valor equivalente do número na base de destino.
    
    # Comportamento desejado:
        # ◦ O sistema deve ler inicialmente uma base (de origem), um número nessa base e uma outra base (de destino).
        # ◦ Em seguida, deve executar uma função converter_base(numero, base_origem, base_destino).
        # ◦ Finalmente, deve apresentar uma mensagem informando que o número “numero”, escrito na base “base_origem” é equivalente ao número “resultado” na base “base_destino”.
    
    # Observações Adicionais:
        # ◦ OBS.1: Pode implementar com interface textual mesmo. A implementação com interface gráfica será valorizada como pontuação extra.
        # ◦ OBS.2: A conversão de números inteiros já vale 90% da atividade. Para garantir os 100%, deve incluir a conversão de números reais.
        # ◦ OBS.3: Além da tela do computador em si, o rosto do apresentador também deve aparecer no vídeo de apresentação.
        # ◦ OBS.4: Quem preferir, ao invés de gravar o vídeo, pode agendar com o professor um horário para apresentar pessoalmente.
    
    #  DICA:
        # ◦ Uma dica seria implementar três funções:
            # ▪ 1- Uma para converter de qualquer base para a base 10
                # converter_para_base10(numero, base_origem)
            # ▪ 2- Uma para converter da base 10 para qualquer base
                # converter_da_base10(numero, base_destino)
            # ▪ 3- Uma para utilizar as outras duas, convertendo de qualquer base para qualquer base
                # converter_base(numero, base_origem, base_destino)
        # ◦ Podemos limitar as bases possíveis de 2 a 36. O limite até a base 36 é para assumir que nos limitaremos aos números e letras do alfabeto, ok?

def converter_para_base10(numero, base_origem):
    alfabeto = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
                "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
                "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}
    resultado = 0

    for pos, caractere in enumerate(numero, 1):
        if caractere.isalpha():
            caractere = alfabeto[f"{caractere}"]
        resultado += int(caractere) * (base_origem ** (len(numero) - pos))

    return resultado

def converter_da_base10(numero, base_destino):
    restos = []
    alfabeto = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
                "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
                "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}
    numero = int(numero)
    while numero >= base_destino:
        resto = numero % base_destino
        if resto > 9:
            a = list(alfabeto.keys())
            resto = a[resto - 10]
        restos.append(resto)
        numero = numero // base_destino

    restos.append(numero)
    resultado = ""

    for i in range(1, len(restos) + 1):
        resultado += f"{restos[-i]}"
    return resultado

def converter_base(numero, base_origem, base_destino):
    if base_origem != 10:
        numero = converter_para_base10(numero, base_origem)
    if base_destino != 10:
        resultado = converter_da_base10(numero, base_destino)
        return resultado
    return numero

def principal():
    flutuantes_maiores_base = "1"
    numero = input("Digite um número: ").upper()
    base_origem = int(input("Digite o número da base de origem: "))
    base_destino = int(input("Digite o número da base de destino: "))
    numero = numero.replace(",", ".")
    flutuante = 0
    if "." in numero:
        numero, flutuante = numero.split(".")
        flutuantes_maiores_base = list(filter(lambda x: x >= base_origem, list(map(int, flutuante.split())))
    numeros_maiores_base = list(filter(lambda x: x >= base_origem, list(map(int, numero.split())))
    if (len(numeros_maiores_base) > 1 or len(flutuantes_maiores_base) > 1 or base_destino <= 1 or base_origem <= 1):
        print("Não é foi possivel, tente novamente!")
        principal()
    else:
        resultado2 = 0
        if flutuante != 0:
                resultado2 = converter_base(flutuante, base_origem, base_destino)
        if '-' in numero:
            numero = numero.replace("-", "") 
            resultado = converter_base(numero, base_origem, base_destino)
            resultado = f"-{resultado}.{resultado2}"
            numero = f"-{numero}.{flutuante}"
        else:
            resultado = converter_base(numero, base_origem, base_destino)
            resultado = f"{resultado}.{resultado2}"

        print(f"O número {numero}.{flutuante}, escrito na base {base_origem}, é equivalente ao número {resultado} na base {base_destino}")

principal()
