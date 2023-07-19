"""
4. Um hotel cobra R$ 150.00 por diária e mais uma taxa de serviços que é cobrada como descrito
abaixo. Construa um programa que recebe a quantidade de dias que um hóspede irá usar e imprime o
valor a ser cobrado.
• R$ 7.50 por diária, se o número de diárias for maior que 5
• R$ 9.00 por diária, se o número de diárias for igual a 5
• R$ 10.50 por diária, se o número de diárias for menor que 5.

"""

dias = int(input("Digite quantos dias o hospede ficou no hotel: "))
diarias = 150
taxaServicos = None
valorTotal = None

if(dias > 0):
    if(dias > 5):
        taxaServicos = 7.5
    elif(dias == 5):
        taxaServicos = 9
    else:
        taxaServicos = 10.5
    valorTotal = dias * taxaServicos + dias * diarias
    print(f"O valor total da hospedagem a ser cobrada é de R${valorTotal:.2f}")        
else:
    print("Você digitou algum valor INVÁLIDO, tente novamente!!")