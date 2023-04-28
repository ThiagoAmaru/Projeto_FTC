import pandas as pd

import streamlit as st


st.header("Fome Zero")

# importa os dados
df = pd.read_csv("../dataset/zomato.csv")

# criando cópia para preservar o dataset original
df1 = df.copy()

# 1. Qual o nome da cidade que possui mais restaurantes registrados?

#Localiza as colunas, agrupa pelas cidades, soma a quantidade de restaurantes desonsiderando valores repetidos, reseta o index e ordena em ordem decrescente 
aux = df1.loc[:,['City', 'Restaurant ID']].groupby('City').nunique().reset_index().sort_values('Restaurant ID', ascending = False).head(1)
aux['City']

# 2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?

# filtra as restrições
filtro = df1.loc[df1['Aggregate rating'] > 4]
aux = filtro.loc[: , [ 'City', 'Aggregate rating']].groupby('City').mean().reset_index().sort_values('Aggregate rating', ascending = False).head(1)
aux['City']


# 3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?

filtro = df1.loc[df1['Aggregate rating'] < 2.5]
aux = filtro.loc[: , [ 'City', 'Aggregate rating']].groupby('City').mean().reset_index().sort_values('Aggregate rating', ascending = False).head(1)
aux['City']


# 4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?

aux = df1.loc[: , ['Aggregate rating', 'City']].groupby("City").mean().reset_index().sort_values("Aggregate rating", ascending = False).head(1)
aux['City']


# 5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?

aux = df1.loc[: , ['Cuisines', 'City']].groupby("City").nunique().reset_index().sort_values("Cuisines", ascending = False).head(1)
aux['City']


# 6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?


filtro = df1.loc[df1['Has Table booking'] == 1]
aux = filtro.loc[: , ['City', 'Restaurant ID']].groupby('City').count().reset_index().sort_values('Restaurant ID', ascending= False).head(1)
aux['City']

# 7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?

filtro = df1.loc[(df1['Is delivering now'] == 1) | (df1['Has Online delivery'] == 1)]
aux = filtro.loc[: , ['City' , 'Restaurant ID' ]].groupby('City').count().reset_index().sort_values('Restaurant ID', ascending= False).head(1)
aux['City']


# 8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

filtro = df1.loc[(df1['Has Online delivery'] == 1)]
aux = filtro.loc[: , ['City' , 'Restaurant ID' ]].groupby('City').count().reset_index().sort_values('Restaurant ID', ascending= False).head(1)
aux['City']