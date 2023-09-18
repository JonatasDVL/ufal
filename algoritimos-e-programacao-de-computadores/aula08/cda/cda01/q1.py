arquivo = open(r"C:\Users\jonat\OneDrive\Documentos\GitHub\ufal\algoritimos-e-programacao-de-computadores\aula08\cda\cda01\dados.txt")
texto = arquivo.read()
arquivo.close()
print(texto)

texto = texto.split("\n")
print(texto)

usuarios = []

for elemento in texto:
    atributo = elemento.split(", ")
    usuario = {"nome":atributo[0], "email":atributo[1], "senha":atributo[2]}
    usuarios.append(usuario)

print(usuarios)