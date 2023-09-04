m = 4
n = 4

matriz = [0]*m

for i in range(m):
    matriz[i] = [0]*n

print (matriz,"\n")

# for i in range(m):
#     for j in range(n):
#         matriz[i][j] = i+j
#         print (f"{matriz[i][j]}",end=" ")
#     print ()

# for i in range(m):
#     for j in range(n):
#         matriz[i][j] = i*j
#         print (f"{matriz[i][j]}",end=" ")
#     print ()


for i in range(m):
    matriz[i][i] = 1

for i in range(m):
    for j in range(n):
        if i == j:
            matriz[i][j] += 1
        print (f"{matriz[i][j]}",end=" ")
    print ()
