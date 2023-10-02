# https://br.spoj.com/problems/ESTAGIO/

#  entrada uma lista de nomes e de médias finais dos alunos de uma turma, e determina o aluno com a maior média na turma

MAX_ALUNOS = 1000  # Define o número máximo de alunos

def main():
    turma = 1  # Inicializa o número da turma
    
    while True:  # Loop principal para processar múltiplas turmas
        n = int(input())  # Lê o número de alunos na turma
        
        if n == 0:
            break  # Se o número de alunos for zero, encerra o programa
        
        alunos = []  # Inicializa uma lista para armazenar os dados dos alunos
        
        for _ in range(n):
            # Lê o código e a média de cada aluno e os armazena em um dicionário
            codigo, media = map(int, input().split())
            alunos.append({'codigo': codigo, 'media': media})
        
        indice_melhor = 0  # Inicializa o índice do aluno com a maior média
        
        for i in range(1, n):
            # Compara as médias dos alunos para encontrar o aluno com a maior média
            if alunos[i]['media'] > alunos[indice_melhor]['media']:
                indice_melhor = i        


        # Imprime os resultados para a turma atual
        print(f'Turma {turma}')
        for i in range(0, n):
            if alunos[indice_melhor]['media'] == alunos[i]['media']:
                print(alunos[i]['codigo'], end=" ")  # Imprime o código do aluno com a maior média
        print()
        
        turma += 1  # Incrementa o número da turma para a próxima iteração

if __name__ == "__main__":
    main()  # Chama a função principal se o script for executado como um programa
