# Exercício Pré-Prova 006
# 6. Crie um dicionário com nomes de alunos e suas respectivas notas. Calcule a média das notas.

notasAlunos = {
    "Alice": [9.5, 8.0],
    "Bob": [8.0, 8.5],
    "Carol": [9.8, 9.0],
    "David": [7.2, 6.5],
    "Eva": [8.5, 7.7]
}

for nome, notas in notasAlunos.items():
    media = 0.0
    for i in range(len(notas)):
        media += notas[i]
    media = media/len(notas)
    print(f"A nota de {nome} é: {media}")





