arquivo = open(r"C:\Users\jonat\OneDrive\Documentos\GitHub\ufal\algoritimos-e-programacao-de-computadores\aula08\cda\cda01\dados.txt")
lista = []
for linha in arquivo.readlines():
    linha = linha.replace("\n","")
    lista.append(linha)
arquivo.close()

usuarios = []

for elemento in lista:
    atributo = elemento.split(", ")
    usuario = {"nome":atributo[0], "email":atributo[1], "senha":atributo[2]}
    usuarios.append(usuario)
print(usuarios)