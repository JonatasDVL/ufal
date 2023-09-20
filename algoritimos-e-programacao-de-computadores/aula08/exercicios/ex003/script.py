# 3. Faça um programa que leia um número qualquer de notas em um arquivo. Após a leitura dos dados, faça o seguinte:
#     Mostre a quantidade de notas que foram lidas.
#     Exiba todas as notas na ordem em que foram informadas.
#     Calcule e mostre a soma das notas.
#     Calcule e mostre a média das notas.
#     Calcule e mostre a quantidade de notas acima da média calculada.

def exibirNotas(listasNotas):
    print("| AB1   | AB2   | SOMA  | MÉDIA |\n+-------+-------+-------+-------+")
    contador = 0
    quantidade = 0
    for notas in listasNotas:
        notas = notas.split(" ")
        for nota in notas:
            print(f"| {nota:<5} ", end="")
            quantidade += 1
        print("|")
        quantidade -= 2
        if float(nota) >= 7:
            contador += 1
    print(f"Quantidade de notas lidas: {quantidade}")
    print(f"Quantidade de notas acima da média: {contador}\n") 
    return 

def adicionarDadosArquivo():
    arquivo = open(r"ex003\arquivo.txt", "a")
    resposta = "s"
    while resposta == "s":
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        soma = nota1 + nota2
        media = soma/2
        arquivo.write(f"{nota1} {nota2} {soma} {media}\n")
        resposta = input("Digite (s) se desejas continuar: ") 
    arquivo.close()
    notas = lerArquivos()
    return notas

def removerAdicionarDadosArquivo():
    arquivo = open(r"ex003\arquivo.txt", "w")
    arquivo.write("")
    arquivo.close()
    notas = adicionarDadosArquivo()
    return notas

def lerArquivos():
    arquivo = open(r"ex003\arquivo.txt", "r")    
    notas = []
    for linha in arquivo.readlines():
        linha = linha.replace("\n","")
        notas.append(linha)
    return notas

def inicio():
    notas = lerArquivos()
    resposta = "s"    
    while resposta == "s":
        opcao = input("Opções do Sistema de Notas:\n1.Adicionar notas no sistema; \n2.Exibir as notas do sistema; \n3.Remover os dados anteriores e adicionar novas notas no sistema; \n4.Fechar e salvar o sistema; \nDigite o número da opção que desejas: ")
        if opcao == "1":
            print("Você escolheu a opcao número 1.\n")
            notas = adicionarDadosArquivo()
        elif opcao == "2":
            print("Você escolheu a opcao número 2.\n")
            exibirNotas(notas)
        elif opcao == "3":
            print("Você escolheu a opcao número 3.\n")
            notas = removerAdicionarDadosArquivo()
        elif opcao == "4":
            resposta = "n"
            print("Você fechou o programa.")
        else:
            print("Você não digitou um valor válido.")

inicio()