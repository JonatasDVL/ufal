#  Estrutura de Dados
#  Aula 01: Introdução 
#  Professor:Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 07:
#       7. Algoritmo que tenta quebrar uma senha de quatro dígitos numéricos
#  Função de Custo de Tempo deste Algoritmos:

senha = "0004"

for tentativa in range(10000):
    tentativa = str(tentativa)
    tentativa = "0" * (4-len(tentativa)) + tentativa
    if senha == tentativa:
        print(f"A senha é {tentativa}")
        break