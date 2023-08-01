""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Repetição 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 18:
    Calcular IMC de uma lista de pessoas.

 """ 

nomes = ["Jônatas","Thallys","Francisco","Anderson","Rayane","Laiane"]
alturas = [1.67, 1.82, 1.70, 1.78, 1.68, 1.60]
pesos = [52, 79, 61, 76, 60, 56]
imcs = []

for i in range(len(nomes)):
   imc = pesos[i]/alturas[i]**2
   imcs.append(imc)
   print(f"{imcs[i]:.2f} é o valor do imc de {nomes[i]}")
