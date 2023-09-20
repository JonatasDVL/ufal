# 5. Implemente uma agenda telefônica onde o usuário pode inserir, remover, editar e buscar por telefones de contatos. Cada contato tem um nome e apenas um telefone. Utilize um arquivo para servir como banco de dados da aplicação.

def lerAgendaTelefonica():
    arquivo = open(r"ex005\arquivo.txt", "r")
    agendaTelefonica = {}
    for linha in arquivo.readlines():
        atributosContatos = []
        linha = linha.replace("\n", "")
        atributosContatos = linha.split("|")
        contato = {atributosContatos[0]: atributosContatos[1]}
        agendaTelefonica |= contato
    return agendaTelefonica

def exibirContatos(agendaTelefonica):
    print("Lista de Contatos:")
    print("Nome\t| Telefone")
    print("-" * 20)
    for nome, telefone in agendaTelefonica.items():
        print(f"{nome}\t| {telefone}")

def inserirContatos(): 
    arquivo = open(r"ex005\arquivo.txt", "a")
    resposta = "s"
    while resposta == "s":
        nome = input("Digite o nome da pessoa: ")
        telefone = input("Digite o número de telefone: ")
        arquivo.write(f"{nome}|{telefone}\n")
        resposta = input("Digite (s) se desejas continuar: ") 
    arquivo.close()
    agendaTelefonica = lerAgendaTelefonica()
    return agendaTelefonica

def removerContatos(agendaTelefonica):
    resposta = "s"
    while resposta == "s":
        exibirContatos(agendaTelefonica)
        telefone = input("Digite o telefone do contato que desejas remover: ")
        cond = 0
        for chave, valor in agendaTelefonica.items():
            if valor == telefone:
                agendaTelefonica.pop(chave)
                print("Contato removido com sucesso.")
                cond = 1
                break
        if cond == 0:
            print("Não foi possivel remover esse contato, pois esse número de telefone não existe.")
        resposta = input("Digite (s) se desejas continuar: ") 
    
    arquivo = open(r"ex005\arquivo.txt", "w")
    for nome, telefone in agendaTelefonica.items():
        arquivo.write(f"{nome}|{telefone}\n") 
    arquivo.close()
    return agendaTelefonica

def editarContatos(agendaTelefonica): 
    resposta = "s"
    while resposta == "s":
        exibirContatos(agendaTelefonica)
        telefone = input("Digite o telefone do contato que desejas editar: ")
        opcao = input("Digite (nome) se desejas editar o nome ou digite (telefone) se desejas editar o telefone")
        if opcao == "nome":
            for chave, valor in agendaTelefonica.items():
                if valor == telefone:
                    novaChave = input("Digite o novo nome do contato: ")
                    agendaTelefonica[novaChave] = agendaTelefonica.pop(chave) 
                    print("Contato editado com sucesso.")
                    break
        elif opcao == "telefone":
            for chave, valor in agendaTelefonica.items():
                if valor == telefone:
                    novoValor = input("Digite o novo telefone do contato: ")
                    agendaTelefonica[chave] = novoValor
                    print("Contato editado com sucesso.")
                    break
        else:
            print("Opção inválida, tente novamente!")
        resposta = input("Digite (s) se desejas continuar: ") 
    arquivo = open(r"ex005\arquivo.txt", "w")
    for nome, telefone in agendaTelefonica.items():
        arquivo.write(f"{nome}|{telefone}\n") 
    arquivo.close()
    return agendaTelefonica

def buscarContatos(agendaTelefonica):
    telefone = input("Digite o número de telefone que desejas buscar: ")    
    for chave, valor in agendaTelefonica.items():
        if valor == telefone:
            print(f"O telefone {valor} é do contato {chave}")
            return
    print("Não foi possivel achar esse número de telefone")
    return 
def inicio():
    agendaTelefonica = lerAgendaTelefonica()
    resposta = "s"
    while resposta == "s":
        opcao = input("\nOpções do Sistema de Notas: \n1.Exibir os contatos na agenda telefonica; \n2.Inserir contatos na agenda telefonica;\n3.Remover contatos na agenda telefonica; \n4.Editar contatos na agenda telefonica;\n5.Buscar telefone nos contatos na agenda telefonica; \n6.Fechar e salvar o sistema; \nDigite o número da opção que desejas: ")
        if opcao == "1":
            print("\nVocê escolheu a opcao número 1.\n")
            exibirContatos(agendaTelefonica)
        elif opcao == "2":
            print("\nVocê escolheu a opcao número 2.\n")
            agendaTelefonica = inserirContatos()
        elif opcao == "3":
            print("\nVocê escolheu a opcao número 3.\n")
            agendaTelefonica = removerContatos(agendaTelefonica)
        elif opcao == "4":
            print("\nVocê escolheu a opcao número 4.\n")
            agendaTelefonica = editarContatos(agendaTelefonica)
        elif opcao == "5":
            print("\nVocê escolheu a opcao número 5.\n")
            buscarContatos(agendaTelefonica)
        elif opcao == "6":
            resposta = "n"
            print("\nVocê fechou o programa.")
        else:
            print("Você não digitou um valor válido.")

inicio()