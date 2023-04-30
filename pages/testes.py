import pandas as pd
import matplotlib.pyplot as plt
from funcoes import country_name

# importa os dados
df = pd.read_csv("dataset/zomato.csv")

# criando cópia para preservaar o dataset original
df1 = df.copy()

testando_codigo = ['Has Table booking', 'Has Online delivery', 'Is delivering now', 'Switch to order menu']

h = "Has Table book" in testando_codigo

print(h)

#aux = df1.loc[: , ["Country Code", "City"]].groupby('Country Code').agg({ "City" : ['nunique' , 'count'] }).reset_index()


#print(aux)

"""

def mostra(dataframe, n_var, nome_coluna_x, nome_coluna_y):
    
    
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

    fig, ax = plt.subplots()

    # Adicionar as barras
    ax.bar(lista_aux1, lista_aux2)

    # Rotacionar os rótulos do eixo x em 90 graus
    plt.xticks(rotation=90)

    # Adicionar legendas e título / Atualizar essa parte
    ax.set_xlabel('Chaves')
    ax.set_ylabel('O que o grafico quer quantitativamente')
    ax.set_title(' Titulo do Grafico')
    return plt.show()

mostra(df1, 7, "Country Code", "City")

"""