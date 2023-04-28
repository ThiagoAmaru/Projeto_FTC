import pandas as pd

# importa os dados
df = pd.read_csv("dataset/zomato.csv")

# criando cópia para preservaar o dataset original
df1 = df.copy()

# 1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
# restaurante com a maior média de avaliação?

filtro = df1.loc[df1["Cuisines"] == "Italian"]
filtro.loc[: , ["Restaurant Name" , 'Aggregate rating']].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = False).head(17)

# 2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
# restaurante com a menor média de avaliação?

filtro = df1.loc[df1["Cuisines"] == "Italian"]
filtro.loc[: , ["Restaurant Name" , 'Aggregate rating']].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = True).head(9)

# 3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
# restaurante com a maior média de avaliação?

filtro = df1.loc[df1["Cuisines"] == 'American']
filtro.loc[: , ["Restaurant Name" , 'Aggregate rating']].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = False).head(17)


# 4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
# restaurante com a menor média de avaliação?

filtro = df1.loc[df1["Cuisines"] == 'American']
filtro.loc[: , ["Restaurant Name" , 'Aggregate rating']].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = True).head(2)

# 5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
# restaurante com a maior média de avaliação?

filtro = df1.loc[df1["Cuisines"] == 'Arabian']
filtro.loc[: , ["Restaurant Name" , 'Aggregate rating']].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = False).head(1)


# 6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
# restaurante com a menor média de avaliação?

filtro = df1.loc[df1["Cuisines"] == 'Arabian']
filtro.loc[: , ["Restaurant Name" , 'Aggregate rating']].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = True).head(1)


# 7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
# restaurante com a maior média de avaliação?

filtro = df1.loc[df1["Cuisines"] == 'Japanese']
filtro.loc[: , ["Restaurant Name" , 'Aggregate rating']].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = False).head()

# 8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
# restaurante com a menor média de avaliação?

filtro = df1.loc[df1["Cuisines"] == 'Japanese']
filtro.loc[: , ["Restaurant Name" , 'Aggregate rating']].groupby('Restaurant Name').mean().reset_index().sort_values('Aggregate rating', ascending = True).head()

# 9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
# restaurante com a maior média de avaliação?

################## IMCOMPLETO #######################


# 10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
# restaurante com a menor média de avaliação?


################## IMCOMPLETO #######################


# 11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
# pessoas?

df1.loc[: , ["Cuisines" , 'Average Cost for two']].groupby('Cuisines').mean().reset_index().sort_values('Average Cost for two', ascending = False).head()

# 12. Qual o tipo de culinária que possui a maior nota média

df1.loc[: , ["Cuisines" , 'Aggregate rating']].groupby('Cuisines').mean().reset_index().sort_values('Aggregate rating', ascending = False).head()


# 13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
# online e fazem entregas?

filtro = df1.loc[df1["Is delivering now"] == 1]
filtro.loc[: , ["Cuisines" , 'Aggregate rating']].groupby('Cuisines').nunique().reset_index().sort_values('Aggregate rating', ascending = False).head()

