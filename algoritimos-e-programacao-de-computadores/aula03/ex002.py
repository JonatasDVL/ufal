""" Algoritimos e Programação de Computadores
 Aula 03: Introdução a Python 
 Professor:Rodolfo Carneiro Cavalcante
 Aluno: Jônatas Duarte Vital Leite

 Exercício 02:
 Programa para converter temperatura de Farenheit para Celcius
   - entrada: temperatura em Celsius

 """ 

print("Este programa irá converter a temperatura de Farenheit para Celcius.")
temperaturaFarenheit = float(input("Digite a temperatura em Farenheit que deseja converter: "))
temperaturaCelcius = (temperaturaFarenheit - 32)/ 1.8 
print(f"{temperaturaFarenheit:.2f}°F equivale a {temperaturaCelcius:.2f}°C")