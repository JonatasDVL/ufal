# https://br.spoj.com/problems/ELEICOES/

# N representando o número de votos.
# Nas próximas N linhas, haverá um inteiro Xi, que representa o i-ésimo voto

# 1 ≤ n ≤ 100000
# 1 < x ≤ 1000000000

n = max(1, min(int(input()), 100000))

candidatos = {}

for i in range(n):
    x = max(2, min(int(input()), 1000000000))
    cond = False
    for j in len(candidatos):
        if x == candidatos[j]:
            cond = True
    if cond == False:
        candidatos[x]:1
    else:
        candidatos[x]:1
