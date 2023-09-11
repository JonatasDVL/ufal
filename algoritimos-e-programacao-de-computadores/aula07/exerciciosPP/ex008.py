# Exercício Pré-Prova 008
# 8. Crie um conjunto com nomes de cores e permita que o usuário adicione uma nova cor ao conjunto.

cores = {"vermelho", "azul", "verde", "amarelo", "roxo", "laranja"}
cor = None

while(cor == None or resposta == "s"):
    cor = input("Digite um nome de uma cor: ")
    resposta = input("Desejas continuar a adicionar cores(s/n)? ").lower()
    while(resposta != "s" and resposta != "n"):
        resposta = input("Desejas continuar a adicionar cores(s/n)? ").lower()
    cores.add(cor)

print(cores)