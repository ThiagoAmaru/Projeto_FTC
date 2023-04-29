import pandas as pd
#import streamlit as st
from funcoes import country_name

# importa os dados
df = pd.read_csv("dataset/zomato.csv")

# criando cópia para preservaar o dataset original
df1 = df.copy()

# 1. Qual o nome do país que possui mais cidades registradas?


# Agrupa as colunas pelo codigo do pais, ver a quantidade de elementos dentro "Country Code", reseta o index
# Ordena os Valores por Cidade, o ascending = False organiza em ordem decrescente, o metodo head retorna os primeiros elementos
var = df1.loc[: , ['Country Code', 'City']].groupby('Country Code').count().reset_index().sort_values('City', ascending= False).head(1)
#chama a função e localiza o primeiro elemento da primeira coluna, que será o codigo do país e retorna o nome do país
country_name(var.iloc[0, 0])

# 2. Qual o nome do país que possui mais restaurantes registrados?

aux = df1.loc[: , ['Country Code', 'Restaurant ID']].groupby('Country Code').count().reset_index().sort_values('Restaurant ID', ascending= False).head(1)
country_name(var.iloc[0, 0])

#3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?


#localiza as linhas com o "Price range" igual a quatro, as colunas desejadas, reseta o index
pre_four = df1.loc[df1['Price range'] == 4, ['Country Code', 'Restaurant ID']].reset_index()
# Agrupa as colunas pelo codigo do pais, ver a quantidade de elementos dentro "Country Code", reseta o index
aux = pre_four.loc[: , ['Country Code', 'Restaurant ID']].groupby('Country Code').count().reset_index()
# Ordena os Valores por Cidade, o ascending = False organiza em ordem decrescente, o metodo head retorna os primeiros elementos
var = aux.sort_values('Restaurant ID', ascending= False).head(1)
country_name(var.iloc[0, 0])

# 4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?


# O metodo nunique realiza a soma dos elementos, considerando apenas os valores únicos
var = df1[['Country Code', 'Cuisines']].groupby(['Country Code'], ).nunique().reset_index().sort_values('Cuisines', ascending = False)
country_name(var.iloc[0, 0])

#5. Qual o nome do país que possui a maior quantidade de avaliações feitas?


# Agrupa as colunas pelo codigo do pais, ver a quantidade de elementos dentro "Country Code", reseta o index
var = df1.loc[: , ['Country Code', 'Votes']].groupby('Country Code').sum().reset_index().sort_values('Votes', ascending= False).head(1)
country_name(var.iloc[0, 0])

#6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?

# Cria um filtro para selecionar quais as restrições
filtro = df1.loc[(df1['Is delivering now'] == 1) | (df1['Has Online delivery'] == 1)]
var = filtro.loc[: , ['Country Code', 'Restaurant ID']].groupby('Country Code').count().reset_index().sort_values('Restaurant ID', ascending= False).head(1)
country_name(var.iloc[0, 0])

#7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?

filtro = df1.loc[df1['Has Table booking'] == 1]
var = filtro.loc[: , ['Country Code', 'Restaurant ID']].groupby('Country Code').count().reset_index().sort_values('Restaurant ID', ascending= False).head(1)
country_name(var.iloc[0, 0])

#8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?

var = df1.loc[: , ['Country Code', 'Votes']].groupby('Country Code').mean().reset_index().sort_values('Votes', ascending= False).head(1)
country_name(var.iloc[0, 0])


#9. Qual o nome do país que possui, na média, a maior nota média registrada?

var = df1.loc[: , ['Country Code', 'Aggregate rating']].groupby('Country Code').mean().reset_index().sort_values('Aggregate rating', ascending= False).head(1)
country_name(var.iloc[0, 0])

#10. Qual o nome do país que possui, na média, a menor nota média registrada?

var = df1.loc[: , ['Country Code', 'Aggregate rating']].groupby('Country Code').mean().reset_index().sort_values('Aggregate rating', ascending= True).head(1)
country_name(var.iloc[0, 0])

#11. Qual a média de preço de um prato para dois por país?

aux = df1.loc[: , ['Average Cost for two', 'Country Code']].groupby('Country Code').mean().reset_index()
aux['Country Code'] = aux['Country Code'].apply(lambda x : country_name(x)) 
aux.sort_values('Average Cost for two', ascending= True)

# Començando a desenvolver o stremlit

#st.header("Será que deu certo?")

#st.sidebar.markdown("# Países")