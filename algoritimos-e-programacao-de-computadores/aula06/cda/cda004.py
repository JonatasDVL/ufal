def calculandoImposto(salario):
    if(salario > 1500):
        return round(salario * 0.27,2)
    else:
        return "Isento"

lista_salarios_funcionarios = [1500.00, 1750.50, 945.75, 1799.90, 2750.00, 450.45]
lista_nomes_funcionarios = ["Jônatas", "Thallys", "Sara", "Rayane", "Francisco", "Anderson"]

for salario in lista_salarios_funcionarios:
    imposto = calculandoImposto(salario)
    print(f"Salário: {salario}\nImposto: {imposto}\n...")