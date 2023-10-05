# https://br.spoj.com/problems/ELEICOES/

# N representando o número de votos.
# Nas próximas N linhas, haverá um inteiro Xi, que representa o i-ésimo voto

# 1 ≤ n ≤ 100000
# 1 < x ≤ 1000000000

n = int(input())

if 1 <= n <= 100000:
    candidatos = []
    vencedor = None

    for i in range(n):
        x = int(input())
        if 1 < x <= 1000000000:
            cond = False
            j = 0 
            for j in range(len(candidatos)):
                if x == candidatos[j]['codigo']:
                    cond = True
                    break  
            if not cond:
                candidatos.append({'codigo': x, 'votos': 1})
                if vencedor is None:
                    vencedor = candidatos[0]
            else:
                candidatos[j]['votos'] += 1
                if vencedor is None or candidatos[j]['votos'] > vencedor['votos']:
                    vencedor = candidatos[j]

    print(vencedor['codigo'])

