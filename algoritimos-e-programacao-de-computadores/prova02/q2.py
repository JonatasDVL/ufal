"""
    2. Você está implementando um sistema de taxi por aplicativo. Quando um usuário solicita um taxi,
    o aplicativo carrega a localização deste usuário e precisa encontrar o taxi mais próximo para realizar a
    chamada. Para calcular a distância, o aplicativo utiliza a distância euclidiana, como descrito abaixo. Faça
    um programa que recebe como entradas a localização atual de um usuário (x,y) e as lista de localizações
    dos taxis disponíveis taxisx = [x1,x2,...,xn], taxisy = [y1,y2,...,yn], e imprima na tela o taxi mais próximo.
    d((xi
    , yi),(xj , yj ) = p
    (xi − xj )
    2 + (yi − yj )
    2
    Exemplo:
    x = 10, y = 8
    taxisx = [21, 40, 35, 17, −42, 82, 60, −1, −15, 25, 29, 0]
    taxisy = [25, 30, −1, 45, −20, 60, 0, 26, −10, 52, 36, −1]
    saída: 11

"""

taxisX = []
taxisY = []
usuario = []
distancia = []

usuario.append(int(input(f"Qual a localização do usuário na posição x: ")))
usuario.append(int(input(f"Qual a localização do usuário na posição y: ")))

quantidade = int(input("Digite quantos taxis estão disponíveis: "))

for i in range (quantidade):
    taxisX.append(int(input(f"Qual a localização do {i+1}° taxi na posição x: ")))
    taxisY.append(int(input(f"Qual a localização do {i+1}° taxi na posição y: ")))
    """taxisX = [21, 40, 35, 17, -42, 82, 60, -1, -15, 25, 0, 29]
    taxisY = [25, 30, -1, 45, -20, 60, 0, 26, -10, 52, -1, 36]"""
    distancia.append( ( (taxisX[i] - usuario[0])**2 + (taxisY[i] - usuario[1])**2 )**0.5 ) 
    if(taxisX[i] == usuario[0] and taxisY[i] == usuario[1]):
        saida = i
        break
    elif(i == 0):
        saida = i
        distanciaTemporaria = distancia[i]
    elif(distancia[i] < distanciaTemporaria):
        saida = i
        distanciaTemporaria = distancia[i]

print(saida)


""" não deu tempo de aprimorar
    taxisX = []
    taxisY = []
    usuario = []
    distancia = []

    usuario.append(int(input(f"Qual a localização do usuário na posição x: ")))
    usuario.append(int(input(f"Qual a localização do usuário na posição y: ")))

    quantidade = int(input("Digite quantos taxis estão disponíveis: "))

    i = 0
    taxisX.append(int(input(f"Qual a localização do {i+1}° taxi na posição x: ")))
    taxisY.append(int(input(f"Qual a localização do {i+1}° taxi na posição y: ")))
    distancia.append( ( (taxisX[i] - usuario[0])**2 + (taxisY[i] - usuario[1])**2 )**0.5 )
    saida = i
    distanciaTemporaria = distancia[i]

    while(i != quantidade and (taxisX[i] != usuario[0] and taxisY[i] != usuario[1])):
        i += 1
        taxisX.append(int(input(f"Qual a localização do {i+1}° taxi na posição x: ")))
        taxisY.append(int(input(f"Qual a localização do {i+1}° taxi na posição y: ")))
        distancia.append( ( (taxisX[i] - usuario[0])**2 + (taxisY[i] - usuario[1])**2 )**0.5 ) 
        if(distancia[i] < distanciaTemporaria):
            saida = i
            distanciaTemporaria = distancia[i]
    print(saida)
"""