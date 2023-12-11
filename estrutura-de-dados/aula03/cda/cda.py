agenda_telefonica = [
    ["Ana", {"telefone": "98134-1567", "email":"ana@gmail.com"}],
    ["Beto", {"telefone": "98234-1567", "email":"beto@gmail.com"}],
    ["Bob", {"telefone": "98334-1567", "email":"bob@gmail.com"}],
    ["João", {"telefone": "98434-1567", "email":"joão@gmail.com"}],
    ["Maria", {"telefone": "98534-1567", "email":"maria@gmail.com"}],
    ["Pedro", {"telefone": "98634-1567", "email":"pedro@gmail.com"}]
    ]

def buscadorNumero(lista, n):
    pontoMedio = len(lista)//2
    if (len(lista) == 0):  
        return False
    elif(lista[pontoMedio][1]["email"] == n):
        return True
    elif(lista[pontoMedio][1]["email"] > n):
        return buscadorNumero(lista[:pontoMedio], n)
    elif(lista[pontoMedio][1]["email"] < n):
        return buscadorNumero(lista[pontoMedio+1:], n)

print(buscadorNumero(agenda_telefonica, "maria@gmail.com"))