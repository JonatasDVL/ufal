""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 35:
    16. Implemente um algoritmo para a Cifra de César
    Texto:  a ligeira raposa marrom saltou sobre o cachorro cansado
    chave = 5
    Cifra: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR

"""

normal = [" ","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "X", "Z"]
criptografada = [" ", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "X", "Z", "A", "B", "C"]

texto = input("Digite um texto para criptografar: ").upper()
textoCriptografado = []

for i in range(0, len(texto)):
    x = 1
    for j in range(0, len(normal)):
        if(texto[i] == normal[j]):
            textoCriptografado.append(criptografada[j])
        elif(texto[i] not in criptografada) and j == 26:
            textoCriptografado.append(texto[i])

separador = ''
textoCriptografadoA = separador.join(textoCriptografado)

print(textoCriptografadoA)

