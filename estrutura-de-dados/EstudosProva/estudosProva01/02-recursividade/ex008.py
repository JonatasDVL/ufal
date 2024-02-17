#  Estrutura de Dados
#  Estudos da Aula 02: Recursividade 
#  Professor: Rodolfo Carneiro Cavalcante
#  Aluno: Jônatas Duarte Vital Leite
#  Exercício 08: Torre de Hanoi: Resolva o problema da Torre de Hanoi usando recursão.

# def torre_hanoi(n, origem, destino, auxiliar):
#     if n == 1:
#         print(f"Mova o disco de {origem} para {destino}")
#     else:
#         torre_hanoi(n - 1, origem, auxiliar, destino)
#         print(f"Mova o disco de {origem} para {destino}")
#         torre_hanoi(n - 1, auxiliar, destino, origem)

# # Exemplo de uso:
# num_discos = 3
# torre_hanoi(num_discos, 'A', 'C', 'B')