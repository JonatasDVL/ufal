# https://br.spoj.com/problems/ELEICOES/

# N representando o número de votos.
# Nas próximas N linhas, haverá um inteiro Xi, que representa o i-ésimo voto

# 1 ≤ n ≤ 100000
# 1 < x ≤ 1000000000

n = int(input())
n = max(1, min(n, 100000))

candidatos = []

for i in range(n):
    x = int(input())
    x = max(1, min(x, 1000000000))
    cond = False
    j = 0 
    for j in range(len(candidatos)):
        if x == candidatos[j]['codigo']:
            cond = True
            break  
    if cond == False:
        candidatos.append({'codigo': x, 'votos': 1})
    else:
        candidatos[j]['votos'] += 1

vencedor = candidatos[0]

for i in range(len(candidatos)):
    if candidatos[i]['votos'] > vencedor['votos']:
        vencedor = candidatos[i]

print()
print(vencedor['codigo'])