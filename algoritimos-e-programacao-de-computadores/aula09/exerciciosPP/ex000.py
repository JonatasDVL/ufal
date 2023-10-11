# Exercício Pré-Prova 004

# Abrindo um Arquivo
    # Para abrir um arquivo em Python, você pode usar a função open(). Ela aceita dois argumentos principais: o nome do arquivo e o modo de operação (leitura, escrita, etc.). Alguns modos comuns são:

    # 'r': Leitura (padrão). Abre o arquivo para leitura.
    # 'w': Escrita. Abre o arquivo para escrita (cria um novo arquivo ou sobrescreve o conteúdo existente).
    # 'a': Anexar. Abre o arquivo para escrita, mas adiciona dados no final, não sobrescreve.
    # 'b': Modo binário. Use com 'rb' ou 'wb' para ler ou escrever em modo binário.
    # 'x': Criação exclusiva. Cria o arquivo, mas falha se o arquivo já existir.
    # Exemplo de abertura de um arquivo para leitura:

    # with open('exemplo.txt', 'r') as arquivo:
    #     conteudo = arquivo.read()

# Leitura de Arquivos
    # Depois de abrir um arquivo para leitura, você pode ler seu conteúdo usando vários métodos, como read(), readline(), ou readlines():

    # with open('exemplo.txt', 'r') as arquivo:
    #     conteudo = arquivo.read()  # Lê o conteúdo completo do arquivo.

    # with open('exemplo.txt', 'r') as arquivo:
    #     linha = arquivo.readline()  # Lê uma linha por vez.

    # with open('exemplo.txt', 'r') as arquivo:
    #     linhas = arquivo.readlines()  # Lê todas as linhas e as armazena em uma lista.
    
# Escrita em Arquivos
    # Para escrever em um arquivo, você deve abrir o arquivo no modo de escrita 'w' ou modo de anexar 'a'. Você pode usar o método write() para adicionar conteúdo ao arquivo:

    # with open('novo_arquivo.txt', 'w') as arquivo:
    #     arquivo.write('Este é um novo arquivo.\n')
    #     arquivo.write('Segunda linha.\n')
    
# Fechando Arquivos
    # É importante fechar um arquivo após a leitura ou escrita usando o comando with. Isso garante que os recursos do sistema operacional sejam liberados e que as alterações sejam gravadas no arquivo. O uso de with garante que o arquivo seja fechado automaticamente após seu bloco de código:

    # with open('arquivo.txt', 'r') as arquivo:
    #     conteudo = arquivo.read()

    # O arquivo está automaticamente fechado aqui.
    
# Manipulação de Arquivos Binários
    # Você pode trabalhar com arquivos binários, como imagens, usando os modos 'rb' e 'wb':

    # with open('imagem.png', 'rb') as arquivo_binario:
    #     dados_binarios = arquivo_binario.read()

    # with open('copia_imagem.png', 'wb') as copia_binaria:
    #     copia_binaria.write(dados_binarios)
    
# Tratamento de Exceções
    # Ao lidar com arquivos, é importante tratar exceções, como FileNotFoundError e PermissionError, que podem ocorrer se o arquivo não existir ou não tiver permissões adequadas.

    # try:
    #     with open('arquivo.txt', 'r') as arquivo:
    #         conteudo = arquivo.read()
    # except FileNotFoundError:
    #     print('O arquivo não foi encontrado.')
    # except PermissionError:
    #     print('Sem permissão para acessar o arquivo.')
    # Estes são os conceitos essenciais para trabalhar com arquivos em Python. Certifique-se de fechar os arquivos corretamente após o uso e de tratar exceções para lidar com situações inesperadas durante a manipulação de arquivos.


    # Pandas é uma das bibliotecas mais populares em Python para análise de dados e manipulação de dados em formato tabular. Ela fornece estruturas de dados eficientes e ferramentas para trabalhar com dados, especialmente em tarefas de análise de dados e preparação de dados. Abaixo, vou cobrir os principais conceitos e funcionalidades do Pandas:

    # Estruturas de Dados Principais do Pandas
    # O Pandas possui duas estruturas de dados principais:

    # DataFrame: É uma estrutura de dados bidimensional semelhante a uma planilha ou tabela de banco de dados. Ele é usado para armazenar e manipular dados em formato tabular, onde você tem colunas com rótulos e linhas com índices. Cada coluna pode conter diferentes tipos de dados.

    # Series: É uma estrutura de dados unidimensional semelhante a uma matriz ou lista, mas com rótulos em cada elemento. As séries são usadas para armazenar uma única coluna ou uma única variável em um DataFrame.

    # Principais Funcionalidades
    # Aqui estão algumas das principais funcionalidades do Pandas:

    # Leitura e Escrita de Dados: O Pandas pode ler dados de uma variedade de formatos, como CSV, Excel, SQL, JSON, HTML e muito mais. Ele também permite escrever dados em muitos desses formatos.

    # import pandas as pd

    # # Leitura de um arquivo CSV
    # df = pd.read_csv('dados.csv')

    # # Escrita em um arquivo CSV
    # df.to_csv('novo_dados.csv', index=False)
    
    # Indexação e Seleção de Dados: Você pode selecionar dados com base em rótulos de colunas e índices de linhas usando operações de indexação, como .loc[] e .iloc[].

    # # Selecionando uma coluna
    # coluna = df['nome_da_coluna']

    # # Selecionando linhas com base em condições
    # selecao = df[df['idade'] > 25]
    
    # Manipulação de Dados: O Pandas permite fazer operações como filtragem, ordenação, agrupamento e agregação de dados.

    # # Filtrando dados
    # filtro = df[df['idade'] > 30]

    # # Ordenando dados
    # df_ordenado = df.sort_values(by='idade')

    # # Agrupando e agregando dados
    # grupo = df.groupby('cidade')['idade'].mean()
    # Manipulação de Missing Data: O Pandas oferece ferramentas para lidar com valores ausentes (NaN) de forma eficiente.

    # # Preenchendo valores ausentes
    # df.fillna(valor)

    # # Removendo linhas com valores ausentes
    # df.dropna()
    # Visualização de Dados: Você pode criar visualizações simples usando o Pandas, embora a biblioteca mais comumente usada para visualização seja o Matplotlib.

    # import matplotlib.pyplot as plt

    # df['idade'].hist()
    # plt.title('Histograma de Idade')
    # plt.xlabel('Idade')
    # plt.ylabel('Frequência')
    # plt.show()
    # Operações de Merge e Join: O Pandas permite combinar DataFrames com base em chaves comuns.

    # df1.merge(df2, on='chave_comum')
    # Leitura de Dados na Web: O Pandas pode ler dados diretamente de páginas da web ou APIs.

    # url = 'https://exemplo.com/dados.csv'
    # df = pd.read_csv(url)
    # O Pandas é uma ferramenta poderosa para trabalhar com dados em Python e é amplamente usado em ciência de dados, análise de dados e engenharia de dados. É altamente recomendável aprender a utilizá-lo se você estiver envolvido em projetos que envolvem manipulação de dados em Python.

# my codes

    # codigo do caminho:

        # import os
        # caminho = os.path.abspath(__file__)
        # caminho = caminho.replace("script.py", "arquivo.csv")

    # outro
        # arquivo = open(r"ex005\arquivo.txt", "w")
        #   for nome, telefone in agendaTelefonica.items():
        #       arquivo.write(f"{nome}|{telefone}\n") 
        #   arquivo.close()

    # arquivo = open(f"{caminho}", "r")
    # lista = []
    # for linha in arquivo.readlines():
    #     linha = linha.replace("\n", "")
    #     lista.append(linha)
    # arquivo.close()



# import pandas as pd
# df = pd.read_csv('vendas.csv')
# print(df) # mostra a tabela inteira
# print(df.head(10)) # mostra as x primeiras
# print(df.tail(3)) # mostra as x ultimas
# print(df.columns) # mostra as colunas
# print(df.keys()) # mostras as colunas
# print(df.email) # se vc colocar o nome da coluna ele ira mostrar todos os valores pertencentes aquela coluna, exemplo é email
# print(df['name']) # pode achar assim tbm
# print(df.sort_values(by='created_at')) # imprimi os dados organizados
# print(df[df.email == 'jaida.schaden@example.com']) # imprimir as linhas que apresentam esse email
# print(df[df.quantity > 3]) # apresenta quem teve quantity maior q 3

# alunos = ['ana', 'carlos', 'gilberto', 'marta']
# trabalhos = [9,8,7,6]
# provas = [9,8,7,6]
# seminarios = [9,8,7,6]
# artigos = [9,8,7,6]

# pdf = pd.DataFrame({'aluno': alunos,'trabalho': trabalhos, 'prova': provas, 'seminário': seminarios, 'artigo': artigos})
# print(pdf)
# pdf.to_csv('alunos.csv',index=False)