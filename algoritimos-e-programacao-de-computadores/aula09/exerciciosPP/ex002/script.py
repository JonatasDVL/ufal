# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
    # alexandre       456123789
    # anderson        1245698456
    # antonio         123456456
    # carlos          91257581
    # cesar           987458
    # rosemary        789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
    # ACME Inc.               Uso do espaço em disco pelos usuários
    # ------------------------------------------------------------------------
    # Nr.  Usuário        Espaço utilizado     % do uso

    # 1    alexandre       434,99 MB             16,85%
    # 2    anderson       1187,99 MB             46,02%
    # 3    antonio         117,73 MB              4,56%
    # 4    carlos           87,03 MB              3,37%
    # 5    cesar             0,94 MB              0,04%
    # 6    rosemary        752,88 MB             29,16%

    # Espaço total ocupado: 2581,57 MB
    # Espaço médio ocupado: 430,26 MB

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

import os
caminho = os.path.abspath(__file__)
caminho = caminho.replace("script.py", "usuarios.txt")
caminho2 = caminho.replace("usuarios.txt", "relatorio.txt")

arquivo = open(f"{caminho}", "r")
dados_usuario = []
i=0
espaco_total=0
for linha in arquivo.readlines():
    dados_usuario.append(linha.split())
    espaco_total += float(dados_usuario[i][1])/1048580
    i+=1
arquivo.close()

arquivo = open(f"{caminho2}", "w")
arquivo.write("ACME Inc.               Uso do espaco em disco pelos usuarios\n")
arquivo.write("-" * 70)
arquivo.write("\n{:<4} {:<15} {:<20} {:<10}".format("Nr.", "Usuario", "Espaco utilizado", "% do uso\n\n"))
for pos, linha in enumerate(dados_usuario):
    usuario = linha[0]
    espaco = round(float(linha[1])/1048580, 2)
    percentual = round(espaco / espaco_total * 100, 2)
    percentual = str(percentual)+"%"
    espaco = str(espaco)+"MB"
    arquivo.write(f"{pos+1:<4} {usuario:<15} {espaco:<20}{percentual:<10}\n")
espaco_medio = espaco_total / len(dados_usuario)
arquivo.write("\nEspaco total ocupado: {:.2f} MB".format(espaco_total))
arquivo.write("\nEspaco medio ocupado: {:.2f} MB".format(espaco_medio))

arquivo.close()