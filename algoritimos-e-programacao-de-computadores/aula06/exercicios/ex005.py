""" Algoritimos e Programação de Computadores
 Aula 06: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 05:
    5. Um professor teve uma ideia de como avaliar seus alunos em uma atividade que vale entre 0 e 10 de modo a incentivar a competição entre os alunos. Quem tirar a maior nota terá 10. Quem tirar a menor nota, terá 0. As outras notas serão algo entre 0 e 10 da seguinte forma:
        Nota = ((nota-min)/(max – min))*10
    Faça um programa para calcular as notas dos alunos segundo essa regra, utilizando funções

"""
def calculandoNotas(notas):
    notasCalculadas = []
    max = notas[0]
    min = notas[0]
    for nota in notas:
        if(nota >= max):
            max = nota
        elif(nota <= min):
            min = nota
    for nota in notas:
        notasCalculadas.append(round(((nota - min)/(max - min))*10,2))
    return notasCalculadas, max, min


notas = [2,3,3,3,4,5,5,5,5,6,6,6,7,7,7.5,7.5,8,8,8.5,8]
print(notas)
print(calculandoNotas(notas))