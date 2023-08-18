""" Algoritimos e Programação de Computadores
 Aula 06: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 08:
    8. Faça um programa que recebe duas palavras A e B e verifica se B é uma substring de A.
        Ex:
            A       | B     | resposta
            acabou  | cabo  | SIM
            abobora | bora  | SIM
            calor   | calo  | SIM
            avisar  | vida  | NÃO
""" 

def verificandoSubstring(palavraA, palavraB):
    if(len(palavraA) < len(palavraB)):
        temp = palavraA
        palavraA = palavraB
        palavraB = temp
    contador = 0
    for i in range(len(palavraA)):
        if(contador != len(palavraB)):
            if(palavraA[i] == palavraB[contador]): #b != r
                contador += 1
            else:
                contador = 0 #b == b
                if(palavraA[i] == palavraB[contador]):
                    contador += 1
        else:
            break
    if(contador == len(palavraB)):
        substring = f"{palavraB} é uma substring de {palavraA}."
    else:
        substring = f"{palavraB} não é uma substring de {palavraA}."
    return substring


palavraA = input("Digite uma palavra: ")
palavraB = input("Digite outra palavra: ")

print(verificandoSubstring(palavraA, palavraB))