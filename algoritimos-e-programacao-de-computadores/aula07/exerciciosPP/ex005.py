# Exercício Pré-Prova 005
# Dicionários:
# 5. Crie um dicionário com nomes de países e suas respectivas capitais. Permita que o usuário pesquise uma capital e retorne o nome do país.

lugares = {
    "Japão":  "Tokio",
    "Brasil":  "Brasília",
    "Argentina":  "Buenos Aires",
    "França":  "Paris"
}

capital = "Tokio"

for pais, cidade in lugares.items(): # .keys() e .values()
    if cidade == capital:
        break

print("País:", pais)
print("Capital:", capital)


# def existe(chave):
#     chaves = agenda.keys()
#     for c in chaves:
#         if c == chave:
#             return True
#     return False