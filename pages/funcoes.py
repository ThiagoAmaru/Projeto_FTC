import pandas as pd
import plotly.express as px

# importa os dados
df = pd.read_csv("dataset/zomato.csv")

# criando cópia para preservaar o dataset original
df1 = df.copy()

###### LIMPEZA DOS DADOS ######

# Coloca os codigos dos paises como chave de um dicionario e os nomes como os valores
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

# Função que recebe o valor do codigo do país, vai até o dicionario COUNTRIES e retorna o nome do pais(valor) a partir do codigo(chave)
def country_name(country_id):
    return COUNTRIES[country_id]


# Metodo para atualizar a coluna, de modo que ela apresente apenas o primeiro valor
# Os inputs são o nome do datafrime e da coluna que sofrerá a alteracão
def apenas_primeiro_valor( dataframe, coluna):
    dataframe[coluna] = dataframe.loc[:, coluna].apply(lambda x: x.split(",")[0] if isinstance(x, str) == True else str(x).split(",")[0])
    return None

# Mostra a maior quantidade de um de agrupamentos
# Data Frame, int da quantidade de elementos que deseja, coluna por qual será agrupada, coluna que será agrupada
# Essa função retornará um gráfico de barras

def mostra_maior_quantidade(dataframe, n_var, nome_coluna_x, nome_coluna_y):
    
    # Agrupa as colunas pelo codigo do pais, ver a quantidade de elementos dentro "Country Code", reseta o index
    aux = dataframe.loc[: , [nome_coluna_x, nome_coluna_y]].groupby(nome_coluna_x).nunique().reset_index()
    
    if  aux.shape[0] < n_var:
        n_var = aux.shape[0]
        
    # Ordena os Valores por Cidade, o ascending = False organiza em ordem decrescente, head tras os primeiros elementosva
    if nome_coluna_x == "Country Code":
        var = aux.sort_values(nome_coluna_y, ascending= False).head(n_var)
        lista_aux1 = []
        for i in range (n_var):
            j = country_name(var.iloc[i, 0])
            lista_aux1.append(j)
    else:
        var = aux.sort_values(nome_coluna_y, ascending= False).head(n_var)
        lista_aux1 = []
        for i in range (n_var):
            j = var.iloc[i, 0]
            lista_aux1.append(j)

    lista_aux2 = []
    for i in range (n_var):
        j = var.iloc[i, 1]
        lista_aux2.append(j)


    # Adicionar as barras
    fig = px.bar(df1, x= lista_aux1, y =lista_aux2)
    return fig

def mostra_menor_quantidade(dataframe, n_var, nome_coluna_x, nome_coluna_y):
    
    # Agrupa as colunas pelo codigo do pais, ver a quantidade de elementos dentro "Country Code", reseta o index
    aux = dataframe.loc[: , [nome_coluna_x, nome_coluna_y]].groupby(nome_coluna_x).nunique().reset_index()
    
    if  aux.shape[0] < n_var:
        n_var = aux.shape[0]
        
    # Ordena os Valores por Cidade, o ascending = False organiza em ordem decrescente, head tras os primeiros elementosva
    if nome_coluna_x == "Country Code":
        var = aux.sort_values(nome_coluna_y, ascending= True).head(n_var)
        lista_aux1 = []
        for i in range (n_var):
            j = country_name(var.iloc[i, 0])
            lista_aux1.append(j)
    else:
        var = aux.sort_values(nome_coluna_y, ascending= True).head(n_var)
        lista_aux1 = []
        for i in range (n_var):
            j = var.iloc[i, 0]
            lista_aux1.append(j)

    lista_aux2 = []
    for i in range (n_var):
        j = var.iloc[i, 1]
        lista_aux2.append(j)

    #fig, ax = plt.subplots()

    # Adicionar as barras
    fig = px.bar(df1, x= lista_aux1, y =lista_aux2)
    return fig