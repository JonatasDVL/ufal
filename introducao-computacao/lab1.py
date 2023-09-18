# Roteiro de Laboratório – Obter status do aluno, a partir de suas notas
# Objetivo: O sistema deve receber as notas de um aluno e calcular o seu conceito, dentre
# as quatro possibilidades: a seguir:
    # ◦ AP: Aprovado por Média
    # ◦ RP: Reprovado por Média
    # ◦ AF: Aprovado na Final
    # ◦ RF: Reprovado na Final
# Comportamento desejado:
    # ◦ O sistema deve ler inicialmente duas notas: AB1 e AB2. Caso alguma dessas notas seja abaixo da média (7.0), o sistema deve ler uma terceira nota: REAVALIACAO.
    
    # ◦ A partir daí, deve-se calcular uma média aritmética das duas maiores notas, dentre AB1, AB2 e REAVALIAÇÃO. Isto é, a reavaliação tem o potencial de substituir a menor nota entre AB1 e AB2.

    # ◦ Se a média calculada for >= 7.0, o aluno obtém o status AP. Caso contrário, se a média calculada for <5.0, o aluno obtém o status RP. Caso a média calculada seja >=5.0 e < 7.0, o sistema deve ler mais uma nota, denominada FINAL.
    
    # ◦ Deve-se calcular uma nova média considerando a média aritmética anterior e a nota
    
    # FINAL. A nova média deve ser ponderada, atribuindo peso 6 (seis) para a média
    # aritmética anterior e peso 4 (quatro) para a nota FINAL:
        # ▪ (6 x media + 4 x FINAL) / 10
    # ◦ O aluno que tiver chegado à prova final e alcançar média ponderada final >= 5.5
    # obtém o status AF. Caso contrário, obtém o status RF.
# Diretrizes Adicionais:
    # ◦ Para estilumar o raciocínio modular, crie pelo menos uma função adicional no seu
    # programa (além da função “inicio”)

def inicio(status):
    nota1 = float(input("Qual foi a primeira nota do aluno: "))
    nota2 = float(input("Qual foi a segunda nota do aluno: "))

    if nota1 < 7 or nota2 < 7:
        reavaliacao = float(input("Digite a nota da reavalização: "))
        if nota1 > nota2 and nota2 < reavaliacao:
            nota2 = reavaliacao
        elif nota1 < nota2 and nota1 < reavaliacao:
            nota1 = reavaliacao
        
    media = calcularMedia(nota1, nota2)

    if media >= 5 and media < 7:
        final = float(input("Qual foi a nota final do aluno: "))
        media = (6 * media + 4 * final) / 10
        status = "."
    status = calcularStatus(media, status)
    return status

def calcularMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def calcularStatus(media, status=None):
    if media >= 5.5 and status == ".":
        status = "AF: Aprovado na Final"
    elif media < 5.5 and status == ".":
        status = "RF: Reprovado na Final"
    elif media >= 7:
        status = "AP: Aprovado por Média"
    elif media < 5:
        status = "RP: Reprovado por Média"
    return status

status = None

status = inicio(status)
print(status)