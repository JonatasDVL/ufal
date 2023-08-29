""" Algoritimos e Programação de Computadores
 Aula 07: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 03:
     3. Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:

        incluirNovoNome - essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones. 

        incluirTelefone - essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluílo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. 
        
        excluirTelefone - essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.  
        
        excluirNome - essa função exclui uma pessoa da agenda. 

        consultarTelefone - essa função retorna os telefones de uma pessoa na agenda. 
"""

def incluirNovoNome(agendaTelefonica, nome=""):
    if nome == "":
        nome = input("Digite o nome do novo contato: ") 
    telefones = []
    while not telefones or resposta == "S": 
        numeroTelefone = input(f"Digite o número que deseja adicionar no contato de {nome}: ")
        ##fazer uma função de verificador de numero 
        telefones.append(numeroTelefone)
        resposta = input("Você quer adicionar mais um número(s/n)").upper()
    
    agendaTelefonica[nome] = telefones
    return agendaTelefonica

def incluirTelefone(agendaTelefonica):
    nome = input("Digite o nome do contato: ") 
    resposta2 = "N"
    if len(agendaTelefonica) != 0:
        for chave in agendaTelefonica:
            resposta1 = "S"
            if chave == nome:
                resposta1 = "N"
                break
    else:
        resposta1 = "S"
    if resposta1 == "S":
        resposta2 = input("Você quer adicionar esse novo contato na sua agenda(s/n): ").upper()
    if resposta2 == "S":
        agendaTelefonica = incluirNovoNome(agendaTelefonica, nome)
        return agendaTelefonica
    else:
        telefones = agendaTelefonica[nome]
        resposta = "S"
        while resposta == "S": 
            numeroTelefone = input(f"Digite o número que deseja adicionar no contato de {nome}: ")
            ##fazer uma função de verificador de numero 
            telefones.append(numeroTelefone)
            resposta = input("Você quer adicionar mais um número(s/n): ").upper()
        agendaTelefonica[nome] = telefones
        return agendaTelefonica

def excluirTelefone(agendaTelefonica):
    nome = input("Digite o nome do contato: ") 
    if len(agendaTelefonica) != 0:
        for chave in agendaTelefonica:
            resposta = "N"
            if chave == nome:
                resposta = "S"
                break
    else:
        resposta = "N"
    if resposta == "S":
        while resposta == "S":
            print(f"{nome}: |",end="")
            for elemento in agendaTelefonica[nome]:
                print(f"{elemento}|",end="")
            telefone = input("\nDigite o número de telefone que deseja excluir: ")
            for i in range (len(agendaTelefonica[nome])):
                if(agendaTelefonica[nome][i] == telefone):
                    del agendaTelefonica[nome][i]
                    break
            if len(agendaTelefonica[nome]) == 0:
                del agendaTelefonica[nome] 
                resposta = "N"
            else:
                resposta = input("Você deseja continuar a excluir números telefonicos desse contatos(s/n): ").upper()
    else:   
        print("Esse contanto não existe.")
    return agendaTelefonica

def excluirNome(agendaTelefonica):
    nome = input("Digite o nome do contato que deseja excluir: ") 
    return agendaTelefonica

def consultarTelefone(agendaTelefonica):
    nome = input("Digite o nome do contato que deseja excluir: ") 
    return agendaTelefonica

agendaTelefonica = {}
opcao = "a"

while opcao != "":
    opcao = input(f"\n1.Para incluir um novo contato; \n2.Para incluir um novo telefone a um contato já existente; \n3.Para excluir um número de um contato já existente; \n4.Para excluir um contato;\n5.Para consultar um telefone;\n\nEscolha uma das opções descrita acima: ")
    if opcao == "1":
        agendaTelefonica = incluirNovoNome(agendaTelefonica)
    elif opcao == "2":
        agendaTelefonica = incluirTelefone(agendaTelefonica)
    elif opcao == "3":
        agendaTelefonica = excluirTelefone(agendaTelefonica)    
    elif opcao == "4":
        agendaTelefonica = excluirNome(agendaTelefonica)
    elif opcao == "5":
        agendaTelefonica = consultarTelefone(agendaTelefonica)

print(agendaTelefonica)