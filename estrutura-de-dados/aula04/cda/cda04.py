# Merge Sort

# def combinacao(lista1, lista2):
#     j = 0
#     i = 0
#     lista3 = []
#     while j < len(lista2) and i < len(lista1):
#         if lista1[i] > lista2[j]:
#             lista3.append(lista2[j])
#             j += 1
#         else:   
#             lista3.append(lista1[i])
#             i += 1
#     if i < len(lista1):
#         lista3 = lista3 + lista1[i:]
#     elif j < len(lista2):
#         lista3 = lista3 + lista2[j:]
#     return lista3

# def divisao(lista):
#     if len(lista) == 1:
#         return lista
#     else:
#         return combinacao(divisao(lista[0:len(lista)//2]), divisao(lista[len(lista)//2:]))
# lista = [9,8,7,6,5,4,3,2,1]

# print(divisao(lista))


