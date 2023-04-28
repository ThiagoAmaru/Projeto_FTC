import pandas as pd

import streamlit as st


st.header("Fome Zero")

# importa os dados
df = pd.read_csv("../dataset/zomato.csv")

# criando cópia para preservaar o dataset original
df1 = df.copy()

# 1. Qual o nome do restaurante que possui a maior quantidade de avaliações?

filtro = df1['Votes'].max()

aux = df1.loc[df1['Votes'] == filtro].reset_index()

aux[["Restaurant Name", "Votes"]]

# 2. Qual o nome do restaurante com a maior nota média?

col = ['Restaurant Name' , 'Aggregate rating']

df1[col].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = False).head(5)

#São muitos, mais de 5

# 3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
# pessoas?


col = ['Restaurant Name' , 'Average Cost for two']

df1[col].groupby('Restaurant Name').max().reset_index().sort_values('Average Cost for two', ascending = False).head(1)


# 4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
# média de avaliação?


col = ['Restaurant Name' , 'Aggregate rating']

filtro = df1.loc[(df1['Cuisines'] == 'Brazilian'), col]

filtro.groupby("Restaurant Name").mean().reset_index().sort_values('Aggregate rating', ascending = False).head(3)


# Verificar o ID mais antigo



# 5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
# possui a maior média de avaliação?

col = ['Restaurant Name' , 'Aggregate rating']

filtro = df1.loc[(df1['Cuisines'] == 'Brazilian') & (df1['Country Code'] == 30), col]

filtro.groupby("Restaurant Name").mean().reset_index().sort_values('Aggregate rating', ascending = False).head(2)


# 6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?


col = ['Has Online delivery', 'Votes', ]

df1.loc[: , col].groupby("Has Online delivery").count().reset_index()



# 7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
# possuem o maior valor médio de um prato para duas pessoas?

col = ['Has Table booking', 'Aggregate rating', ]

df1.loc[: , col].groupby("Has Table booking").mean().reset_index()


# 8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
# possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

col = ['Average Cost for two', 'Cuisines']

filtro = df1.loc[(df1['Cuisines'] == 'Japanese') & (df1['Country Code'] == 216) | (df1['Cuisines'] == 'BBQ')]

filtro.loc[: , col].groupby("Cuisines").mean().reset_index()
