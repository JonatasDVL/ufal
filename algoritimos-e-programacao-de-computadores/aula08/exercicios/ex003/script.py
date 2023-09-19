# 3. Faça um programa que leia um número qualquer de notas em um arquivo. Após a leitura dos dados, faça o seguinte:
#     Mostre a quantidade de notas que foram lidas.
#     Exiba todas as notas na ordem em que foram informadas.
#     Calcule e mostre a soma das notas.
#     Calcule e mostre a média das notas.
#     Calcule e mostre a quantidade de notas acima da média calculada.

# def mostrarQuantidadeNotas(notas):
#      quantidade = len(notas)
#      return quantidade

# def exibirNotas(notas):
#     print(notas)
#     return 

# def calcularSoma(nota1, nota2):    
#     soma = nota1 + nota2
#     return soma

# def calcularMedia(nota1, nota2, somas=None):
#     if somas == None:
#         somas = calcularSoma(nota1, nota2)
#     media = somas/2
#     return media

# def calcularMostrarQuantidadeAcimaMedia():

#     return 

# def adicionarDadosArquivo():
#     arquivo = open(r"ex003\arquivo.txt", "a")
#     resposta = "s"
#     while resposta == "s":
#         nota1 = float(input("Digite a primeira nota: "))
#         nota2 = float(input("Digite a segunda nota: "))
#         soma = 
#         arquivo.append(nota)
#     arquivo.close()


def removerAdicionarDadosArquivo():
    arquivo = open(r"ex003\arquivo.txt", "w")
    arquivo.write()
    arquivo.close()


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
        opcao = input("Opções do Sistema de Notas:\n1.Adicionar notas no sistema; \n2.Exibir as notas do sistema; \n3.Remover os dados anteriores e adicionar novas notas no sistema; \n4.Fechar o sistema; \nDigite o número da opção que desejas: ")
        if opcao == "1":
            print("Você escolheu a opcao número 1.")
            
        elif opcao == "2":
            print("Você escolheu a opcao número 2.")

        elif opcao == "3":
            print("Você escolheu a opcao número 3.")
            notas = removerAdicionarDadosArquivo(notas)
        elif opcao == "4":
            resposta = "n"
            print("Você fechou o programa.")
        else:
            print("Você não digitou um valor válido.")

inicio()