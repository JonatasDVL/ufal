"""
2. Uma empresa quer vericar se um empregado está qualicado para a aposentadoria ou não. Para
estar em condições de se aposentar, pelo menos um dos dos segintes critérios deve ser satisfeito:
• Ter no mínimo 65 anos
• Ter trabalhado no mínimo 30 anos 
• Ter no mínimo 60 anos e ter trabalhado no mínimo 25
Com base nessas informações, faça uma algoritmo que receba a idade de um empregado e o número
de anos de trabalho. O algoritmo deve imprimir se o empregado pode ser aposentado ou não.

"""

idade = int(input("Digite qual é a idade do empregado: "))
tempoTrabalho = int(input("Digite quantos anos o empregado já trabalhou durante a vida: "))

if(idade > 0 and tempoTrabalho >= 0 and tempoTrabalho < idade):
    if(idade >= 65) or (tempoTrabalho >= 30) or (idade >= 60 and tempoTrabalho >= 25):
        print("O empregado já pode se aposentar!!")
    else:
        print("O empregado não poderá se aposentar por enquanto!!")
else:
    print("Você digitou algum valor INVÁLIDO, tente novamente!!")