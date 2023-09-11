# 1. Uma tarefa muito comum em sistemas web é a realização do login dos usuários autorizados a acessar o sistema. De modo a realizar a autenticação, o sistema guarda os dados de nome, email e senha de todos os usuários cadastrados. Quando um novo usuário precisa realizar o login, este usuário envia, via formulário, o email e senha cadastrados. O sistema então verifica se esse usuário está realmente cadastrado e verifica se a senha cadastrada é igual a senha enviada pelo usuário. Implemente um programa que possua a lista de usuários (nome, email e senha) e que possua uma função de autenticação que recebe email e senha e informa se o login foi realizado ou não.

# Ex:
# Usuário   Email           Senha
# Ana       ana@gmail.com   ana123
# Bob       bob@hotmail.com 123bob
# Claudio   claudio@bol.com clau!*

# {bob@hotmail.com, 123bob}: Autenticado
# {claudio@bol.com, 123claudio}: Não autenticado

def autenticadorLogin(dadosUsuario, senha, email):
    for lista in dadosUsuario.values():
        if email == lista[0] and senha == lista[1]:
            return print(f"{email}{senha}: Autenticado")
    return print(f"{email}{senha}: Não autenticado")

dadosUsuario = {
    "Maria": ["maria@gmail.com", "maria123"],
    "Ana": ["ana@gmail.com", "ana123"],
    "Bob": ["bob@hotmail.com", "123bob"],
    "Claudio": ["claudio@bol.com", "clau!*"]
}

email = "bob@hotmail.com"
senha = "123bob"

autenticadorLogin(dadosUsuario, senha, email)