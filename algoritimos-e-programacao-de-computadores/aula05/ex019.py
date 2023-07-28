""" Algoritimos e Programação de Computadores
 Aula 05: Estruturas de Decisão 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 19:
   Calcular o desconto de imposto de renda de uma lista de funcionários

 """

nomes = []
salarios = []
valoresImposto = []

x = int(input("Quantos funcionários você deseja adicionar na lista: "))

for i in range (0, x):
   nomes.append(input(f"Qual o nome do {i+1}º funcionário: "))
   salarios.append(float(input(f"Qual o salário do {i+1}º funcionário: ")))
   if(salarios[i] < 0):
      nomes.pop(i)
      salarios.pop(i)
      i -= 1
      print("Você digitou um valor inválido, digite novamente!!")
   elif(salarios[i] < 1903.99):
      valoresImposto.append(0)
   elif(salarios[i] <= 2826.65):      
      valoresImposto.append((salarios[i]*0.075)-142.8)
   elif(salarios[i] <= 3751.05):
      valoresImposto.append((salarios[i]*0.15)-354.8)
   elif(salarios[i] <= 4664.68):
      valoresImposto.append((salarios[i]*0.225)-636.13)
   else:
      valoresImposto.append((salarios[i]*0.275)-869.36)

for i in range (0, x):
   print(f"O desconto do imposto de renda do salário de {nomes[i]} é de R$ {valoresImposto[i]:.2f}.")