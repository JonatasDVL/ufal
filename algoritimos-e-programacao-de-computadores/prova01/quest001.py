"""
1. A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar
mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%.
Escreva um algoritmo que leia o número de horas trabalhadas em uma semana, o salário por hora e
escreva o salário total do funcionário na semana, que deverá ser acrescido das horas extras, caso tenham
sido trabalhadas

"""

horas = int(input("Digite quantas horas você trabalhou essa semana: "))
salarioHora = float(input("Digite qual é o valor do seu salário por hora: "))
salarioTotal = None
horasExtras = None

if(0 <= horas <= 40 and salarioHora > 0):
    salarioTotal = horas * salarioHora
    print(f"Seu salário total dessa semana será de R${salarioTotal:.2f}")
elif(horas > 40 and salarioHora > 0):
    horasExtras = horas - 40
    salarioTotal = salarioHora * horas + salarioHora * horasExtras * 0.5
    print(f"Seu salário total dessa semana será de R${salarioTotal:.2f}")
else:
    print("Você digitou algum valor INVÁLIDO, tente novamente!!")