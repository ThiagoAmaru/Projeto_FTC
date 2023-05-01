import pandas as pd
import streamlit as st
from funcoes import country_name, mostra_maior_quantidade, mostra_menor_quantidade, mostra_maior_media, mostra_menor_media

# importa os dados
df = pd.read_csv("dataset/zomato.csv")

# criando cópia para preservar o dataset original
df1 = df.copy()



############################### Començando a desenvolver o stremlit ############################### 

#################################### SIDEBAR ######################################################

st.header("Cidades")

st.sidebar.markdown("# Cidades")

#copiando dataframe e botando em outra variavel
df2 = df1.copy()

#Tirando as  colunas que não serão utilizadas e criando um filtro de seleção unica
df2 = df2.drop( columns= ['City', 'Country Code' ,'Address','Locality', 'Locality Verbose', 'Longitude', 'Latitude','Rating color', 'Rating text', 'Currency','Has Table booking', 'Has Online delivery', 'Is delivering now', 'Switch to order menu' ])
seletor_y = st.sidebar.selectbox("Escolha a coluna que será analisada", df2.columns)

seletor_z = st.sidebar.selectbox("Voce deseja os maiores ou menores valores?", ['maiores' , 'menores'])

seletor_x = st.sidebar.selectbox("Tipo de preços", ['sem restição', 'cheap','normal', 'expensive' , 'gourmet' ])

# criando um filtro de seleção multipla

seletor_2 = st.sidebar.multiselect("filtros", ['Has Table booking', 'Has Online delivery', 'Is delivering now', 'Switch to order menu'])

############################################  Criando Tabs ############################################
tab1 , tab2, tab3 = st.tabs(["Primeira Visão" , "Segunda Visão", "Terceira Visão"])

with tab1:
    filtro_seletor1 = df1.copy()

    if ('cheap' in seletor_x) == True:
        filtro_seletor1 = df1.loc[df1['Price range'] == 1].reset_index()

    if ('normal' in seletor_x) == True:
        filtro_seletor1 = df1.loc[df1['Price range'] == 2].reset_index()

    if ('expensive' in seletor_x) == True:
        filtro_seletor1 = df1.loc[df1['Price range'] == 3].reset_index()
    
    if ('gourmet' in seletor_x) == True:
        filtro_seletor1 = df1.loc[df1['Price range'] == 4].reset_index()

 #
    filtro_seletor2 = df1.copy()
    
    if ('Has Table booking' in seletor_2) == True:
        filtro_seletor2 = df1.loc[df1['Has Table booking'] == 1].reset_index()
    if ('Has Online delivery' in seletor_2 )== True:
        filtro_seletor2 = df1.loc[df1['Has Online delivery'] == 1].reset_index()
    if ('Is delivering now' in seletor_2) == True:
        filtro_seletor2 = df1.loc[df1['Is delivering now'] == 1].reset_index()
    if ('Switch to order menu') in seletor_2 == True:
        filtro_seletor2 = df1.loc[df1['Switch to order menu'] == 1].reset_index()

    st.header('Filtros utilizados: ')
    st.markdown(seletor_2)

    st.title("Soma de Valores Unicos")

    if (seletor_z == 'menores') == True:
        figura = mostra_menor_quantidade(pd.merge(filtro_seletor1, filtro_seletor2, how='inner'), 30, "City", seletor_y)
        st.plotly_chart(figura, use_container_width = True)
    else:
        figura = mostra_maior_quantidade(pd.merge(filtro_seletor1, filtro_seletor2, how='inner'), 30, "City", seletor_y)
        st.plotly_chart(figura, use_container_width = True)

    st.title("Médias")

    if (seletor_z == 'menores') == True:
        figura = mostra_menor_media(pd.merge(filtro_seletor1, filtro_seletor2, how='inner'), 30, "City", seletor_y)
        st.plotly_chart(figura, use_container_width = True)
    else:
        figura = mostra_maior_media(pd.merge(filtro_seletor1, filtro_seletor2, how='inner'), 30, "City", seletor_y)
        st.plotly_chart(figura, use_container_width = True)

with tab2:
        st.header('Respondendo perguntas de negócio')
with tab3:
        st.header('mapas')


        