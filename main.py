import pandas as pd

# importa os dados
df = pd.read_csv("dataset/zomato.csv")

###### LIMPEZA DOS DADOS ######

#Coloca os codigos dos paises como chave de um dicionario e os nomes como os valores
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

#Função que recebe o valor do codigo do país, vai até o dicionario COUNTRIES e retorna o nome do pais(valor) a partir do codigo(chave)
def country_name(country_id):
    return COUNTRIES[country_id]