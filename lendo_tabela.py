# Importação da biblioteca para manipulação de dados em tabelas
import pandas as pd  


#tirando os limites do display para mostrar a tabela toda
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)



#Lê o arquivo excel 'teste.csv', usando codificação latin-1 e separador ';',
# e carrega os dados como uma tabela (DataFrame) na variável df
# CSV do Excel usa ';' como separador, por isso especificamos o sep
df = pd.read_csv("teste.csv",
    encoding="latin-1",
    sep=";"
)

# Exibe a tabela
print(df)


