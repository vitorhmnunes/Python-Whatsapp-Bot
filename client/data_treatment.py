import pandas as pd

#lendo a planilha
clientes_df = pd.read_excel("ARQUIVE PATH")

#criando um dataframe com apenas os dados essenciais 
clientes2_df = clientes_df.loc[:, ['NOME', 'CPF', 'DT DE NASCIMENTO', 'DDD1', 'FONE1']]

#Filtrando os clientes pela idade, <= de 65 anos
clientes2_df["DT DE NASCIMENTO"] = pd.to_datetime(clientes2_df['DT DE NASCIMENTO'])
clientes2_df = clientes2_df.loc[clientes2_df['DT DE NASCIMENTO'] >= '1959-01-01' ]

#Retirando duplicatas
clientes3_df = clientes2_df.drop_duplicates()

#Colocando o valor 0 nas linhas com valores vazios
clientes4_df = clientes3_df.fillna(value = 0)

#reorganizando os índices
clientes4_df = clientes4_df.reset_index()
clientes4_df = clientes4_df.drop('index', axis=1)

#retorna os valores do telefone e nome
#se não houver número de telefone retorna -1 e
#se o número não começar com 9, ou seja, se não for número de celular, retorna -1
def client_info(i):
   
    numero = str(int(clientes4_df.loc[i, "FONE1"]))

    if numero != '0' and numero[0] == '9':
        #pegando apenas o primeiro nome 
        nome_completo = clientes4_df.loc[i, "NOME"]
        nomes = nome_completo.split(" ")
        nome = nomes[0]
        nome = nome.title()

        ddd = str(int(clientes4_df.loc[i,"DDD1"]))
        telefone = '55' + ddd + numero

        return nome, telefone
    else:
        return -1
        
