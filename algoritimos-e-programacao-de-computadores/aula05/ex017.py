""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor: Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 17:
    Verificar se uma lista é subconjunto de outra lista.

 """ 

listaA = [0]
listaB = [0]

condicao1 = 0
condicao2 = 0
x = 0

if(len(listaA) >= len(listaB)):
    for i in listaA:
        for j in listaB:
            if (j == i):
                condicao1 += 1
        x += 1
        if(len(listaB) == x):
            break
    if(condicao1 == len(listaB) == len(listaA)):
        print(f"A lista A é igual da lista B")
    elif(condicao1 == len(listaB)):    
        print(f"A lista B é um subconjunto da lista A")
    else:
        print(f"A lista B não é um subconjunto da lista A")
else:
    for i in listaB:
        for j in listaA:
            if (j == i):
                condicao2 += 1
        x += 1
        if(len(listaA) == x):
            break
    if(condicao2 == len(listaA)):
        print(f"A lista A é um subconjunto da lista B")
    else:
        print(f"A lista A não é um subconjunto da lista B")

    
