from flask import Flask, render_template, request

app = Flask(__name__)

# Função para converter um número em base não decimal para base 10
def converter_para_base10(numero, base_origem, alfabeto):
    resultado = 0
    numero = str(numero)
    for pos, caractere in enumerate(numero, 1):
        if caractere.isalpha():
            caractere = alfabeto[f"{caractere}"]
        resultado += int(caractere) * (base_origem ** (len(numero) - pos))
    return resultado

# Função para converter um número em base 10 para outra base
def converter_da_base10(numero, base_destino, alfabeto):
    restos = []
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

# Função para converter um número entre bases diferentes
def converter_base(numero, base_origem, base_destino, alfabeto):
    if base_origem != 10:
        numero = converter_para_base10(numero, base_origem, alfabeto)
    if base_destino != 10:
        resultado = converter_da_base10(numero, base_destino, alfabeto)
        return resultado
    return numero

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def principal():
    alfabeto = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
                "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
                "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}
    if request.method == 'POST':
        numero = str(request.form['numero'].upper())
        base_origem = int(request.form['base_origem'])
        base_destino = int(request.form['base_destino'])
        numero = numero.replace(",", ".")
        verifica = False
        flutuante = 0
        if "." in numero:
            numero, flutuante = numero.split(".")
            for n in flutuante:
                if n.isalpha():
                    n = alfabeto[f"{n}"]
                if int(n) >= base_origem:
                    verifica = True
                    break
        for n in numero.replace("-", ""):
            if n.isalpha():
                n = alfabeto[f"{n}"]
            if int(n) >= base_origem or verifica == True:
                verifica = True
                break
        if (verifica == True or base_destino <= 1 or base_origem <= 1 or base_destino > 36 or base_origem > 36):
            resposta = "Não é possível, tente novamente!"
        else:
            resultado2 = 0
            if flutuante != 0:
                resultado2 = converter_base(flutuante, base_origem, base_destino, alfabeto)
            if '-' in numero:
                resultado = converter_base(numero.replace("-", ""), base_origem, base_destino, alfabeto)
                resultado = f"-{resultado}.{resultado2}"
            else:
                resultado = converter_base(numero, base_origem, base_destino, alfabeto)
                resultado = f"{resultado}.{resultado2}"

            resposta = f"O número {numero}.{flutuante}, escrito na base {base_origem}, é equivalente ao número {resultado} na base {base_destino}"

        return render_template('index.html', resposta=resposta)

    return render_template('index.html', resposta='')

if __name__ == '__main__':
    app.run(debug=True)
