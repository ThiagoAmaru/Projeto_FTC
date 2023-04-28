import pandas as pd

# importa os dados
df = pd.read_csv("dataset/zomato.csv")

# criando cópia para preservaar o dataset original
df1 = df.copy()

#1. Quantos restaurantes únicos estão registrados?

# Identifica os valores unicos, o tamanho sem os valores repetido, [0] pega apenas as linhas, [1] seria 
df1['Restaurant ID'].unique().shape[0]

#2. Quantos países únicos estão registrados?

# Identifica os valores unicos, o tamanho sem os valores repetido, [0] pega apenas as linhas, [1] seria colunas
df1['Country Code'].unique().shape[0]

# 3. Quantas cidades únicas estão registradas?

# Identifica os valores unicos, o tamanho sem os valores repetido, [0] pega apenas as linhas, [1] seria colunas
df1['City'].unique().shape[0]

# 4. Qual o total de avaliações feitas?

#soma os valores da coluna
df1['Votes'].sum()

# 5. Qual o total de tipos de culinária registrados?

# Identifica os valores unicos, o tamanho sem os valores repetido, [0] pega apenas as linhas, [1] seria colunas
df1['Cuisines'].unique().shape[0]