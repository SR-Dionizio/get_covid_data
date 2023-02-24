from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

#Buscando e abrindo a url fonte
url = 'https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&gl=BR&ceid=BR%3Apt-419&state=1'
response = urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

#Procurando a tabela e as linha para o scraping
tabela_covid19 = soup.find('table', class_='pH8O4c')
linhas = tabela_covid19.find_all('tr')

#Criando as lista para armazenar os dados coletados
lista_estados = []
lista_casos = []
lista_casos_dia = []
lista_casos_um_milhao = []
lista_mortes = []

#Iniciando o laço para o scraping
for linha in linhas:
    #Buscando e adicionando a lista os estados
    estados = linha.find('th').get_text()
    lista_estados.append(estados)

    #Buscando e adicionando a lista o número de casos
    casos = linha.find('td')
    if casos is not None:
        casos_formatado = casos.string
        if casos_formatado:
            lista_casos.append(casos_formatado)

    #Buscando e adicionando a lista o número de casos por dia (baseado no dia anterior da ultima atualização do site)
    casos_dia = linha.find_all('td')
    if len(casos_dia) >= 2:
        casos_dia_formatado = casos_dia[1]
        lista_casos_dia.append(casos_dia_formatado.text)

    #Buscando e adicionando a lista o número de casos a cada 1 milhão de pessoas
    casos_um_milhao = linha.find_all('td')
    if len(casos_um_milhao) >= 4:
        casos_um_milhao_formatado = casos_um_milhao[3]
        lista_casos_um_milhao.append(casos_um_milhao_formatado.text)

    #Buscando e adicionando a lista o número de mortes
    mortes = linha.find_all('td')
    if len(mortes) >= 5:
        mortes_formatado = mortes[4]
        lista_mortes.append(mortes_formatado.text)

#removendo a string "local" da lista para não dar erro de len
lista_estados.pop(0)

#Criando o DataFrame com o conteúdo das listas
df = pd.DataFrame({
    'Estados': lista_estados, 
    'Casos': lista_casos, 
    'Novos Casos (1 dia)':lista_casos_dia,
    'casos a cada um milhão de pessoas': lista_casos_um_milhao,
    'Mortes': lista_mortes})

#Dropando os dois primeiros itens do DataFrame que não será usado 
df.drop([0, 1], inplace=True)
#Ordenando o DataFrame por ordem alfabética e printando o DataFrame
df = df.sort_values('Estados')
print(df)


#Coletando a data atual para nomear o arquivo csv a ser criado
data = datetime.today()
dia = data.day
mes = data.month

#criando o arquivo csv e armazenando o DataFrame nele
df.to_csv(f'covid19_{dia}_{mes}.csv', mode='a', header=True, index=False, sep=';')

