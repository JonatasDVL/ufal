def calculandoSalario(horas_trabalhadas, valor_hora):
    if(horas_trabalhadas > 40):
        return ((horas_trabalhadas - 40) * valor_hora * 1.5) + 40 * valor_hora 
    else:
        return horas_trabalhadas * valor_hora

lista_horas_trabalhadas = [45, 40, 30, 75, 80, 60]
lista_valor_hora = [6.75, 8, 10, 7.5, 8, 15.50]

for i, horas_trabalhadas in enumerate(lista_horas_trabalhadas):
    salario = calculandoSalario(horas_trabalhadas, lista_valor_hora[i])
    print(f"Salário: {salario}\nHoras Trabalhadas: {horas_trabalhadas}\nValor por Hora Normal: {lista_valor_hora[i]}\n...")