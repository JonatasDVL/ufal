import pandas as pd
import os

# # caminho = os.getcwd()

# df = pd.read_csv("vendas.csv") # é igual uma tabela sendo as chaves a linha 0 e as colunas os 

# print(df.head(10)) # mostrar as 10 primeiras linhas

# print(df.tail(10)) # mostrar as 10 ultimas linhas

dataframe = {
    "num": [1,2,3],
    "nome": ["Jônatas","Thallys","Francisco"],
    "matricula": [17852,24157,33584]
}

arquivo = pd.DataFrame(dataframe)
print(arquivo)
arquivo.to_csv("arquivo_alunos.csv",index=False)