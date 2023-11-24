#  Estrutura de Dados
#  Aula 01: Introdução 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 04:
#  4. Identificar a soma máxima entre dois elementos de um conjunto
#  Função de Custo de Tempo deste Algoritmos:

entradaConjunto = [2,-5,-9,7,-4,-1]
somaMaxima = []
numeroMaior = None

for numero in entradaConjunto:
    if numeroMaior == None or numeroMaior < numero:
        numeroMaior = numero
        cont = 0
    if numeroMaior == numero:
        cont += 1

numeroMaiorAnt = numeroMaior
numeroMaior = entradaConjunto[0]
for numero in entradaConjunto:
    if numeroMaior < numero and numero != numeroMaiorAnt:
        numeroMaior = numero
        
for numero in entradaConjunto:
    if numero != numeroMaiorAnt:
        somaMaxima.append(numeroMaiorAnt + numero)
    else:
        somaMaxima.append(numeroMaior + numero)

print(f"As somas máxima são {somaMaxima}")

# entradaConjunto = [2,-5,-9,7,-4,-1]
# somaMaxima = []

# for numero in entradaConjunto:
#     somaMaior = None
#     for numero2 in entradaConjunto:
#         soma = numero + numero2     
#         if somaMaior == None or somaMaior < soma:
#             somaMaior = soma
#     somaMaxima.append(somaMaior)

# print(f"As somas máxima são {somaMaxima}")