# 01) Descreva com suas palavras o processo de ordenação realizado nos algoritmos
# Insertion Sort e Selection Sort, em seguida, identifique a ordem de complexidade
# desses algoritmos.

# Selection Sort:
# O Selection Sort é um algoritimo de ordenação que utiliza o processo de selecionar o 
# menor número e colocar no primeiro lugar, depois selecionar o segundo menor número da lista e 
# coloca no segundo lugar e assim por diante. Desta forma, é possivel perceber que a complexidade
# desse algoritmo O(n²)
# Ex: lista=(2,7,1,3,5)
# 2,7,1,3,5 pega o número 2 e compara com todos os números posteriores e percebe que 1 é o menor
# 1,7,2,3,5 "7"2 é o menor
# 1,2,7,3,5 "7"3 é o menor
# 1,2,3,7,5 "7"5 é o menor
# 1,2,3,5,7 pronto

# Insertion Sort:
# O Insertion Sort é um algoritimo de ordenação que utiliza um processo mais sofisticado. Desta forma, é possivel perceber que a complexidade desse algoritmo O(n²)
# Ex: lista=(2,7,1,3,5)
# 2,7,1,3,5 pega o número 7 e compara com todos o número anterior e percebe que o 2 é o menor
# 2,7,1,3,5 "1"7 é o maior, então troca
# 2,1,7,3,5 "1"2 é o maior, então troca
# 1,2,7,3,5 "3"7 é o maior, então troca
# 1,2,3,7,5 "3"2 é o menor, então não troca e segue
# 1,2,3,7,5 "5"7 é o maior, então troca 
# 1,2,3,5,7