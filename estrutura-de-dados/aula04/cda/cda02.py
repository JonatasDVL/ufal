agenda = [
    {"nome":"Jônatas Duarte","telefone":"82 99426-1785"},
    {"nome":"Thallys Asafe","telefone":"82 99426-1785"},
    {"nome":"Francisco Colatino","telefone":"82 99426-1785"},
    {"nome":"Anderson Silva","telefone":"82 99426-1785"},
    {"nome":"Rayane Quézia","telefone":"82 99426-1785"}
]

# Ordenando a lista por meio de SelectionSort
def selectionSort(agenda):
    for i in range(len(agenda)-1):
        menor = i
        for j in range(i+1,len(agenda)):
            if agenda[menor]["nome"][0] > agenda[j]["nome"][0]:
                menor = j    
        agenda[i], agenda[menor] = agenda[menor], agenda[i]
    return agenda

selectionSort(agenda)

for i in agenda:
    print(i)