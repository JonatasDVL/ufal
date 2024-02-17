#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 06: Inversão de string: Implemente uma função recursiva para inverter uma string.

def inversãoString(palavra, tamanho):
    if tamanho == 1:
        # print(f"{palavra[len(palavra)-tamanho]} = {palavra[1:] + palavra[len(palavra)-tamanho]}")
        return palavra[len(palavra)-tamanho]
    # print(f"{palavra[1:]} + {palavra[len(palavra)-tamanho]} = {palavra[1:] + palavra[len(palavra)-tamanho]}")
    return inversãoString(palavra[1:], tamanho-1) + palavra[len(palavra)-tamanho]

palavra = "jonatas" # gnirts
print(inversãoString(palavra, len(palavra)))