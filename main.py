from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&gl=BR&ceid=BR%3Apt-419&state=1'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

tabela_covid19 = soup.find('table', class_='pH8O4c')

linhas = tabela_covid19.find_all('tr')

lista_estados = []
lista_casos = []
lista_casos_dia = []
casos_um_milhao = []
lista_mortes = []

for linha in linhas:
    estados = linha.find('th').get_text()
    lista_estados.append(estados)

    casos = linha.find('td')
    if casos is not None:
        casos_formatado = casos.string
        if casos_formatado:
            lista_casos.append(casos_formatado)

    casos_dia = linha.find_all('td')
    if len(casos_dia) >= 2:
        casos_dia_formatado = casos_dia[1]
        lista_casos_dia.append(casos_dia_formatado.text)

    mortes = linha.find_all('td')
    if len(mortes) >= 5:
        mortes_formatado = mortes[4]
        lista_mortes.append(mortes_formatado.text)

lista_estados.pop(0)
df = pd.DataFrame({'Estados': lista_estados, 'Casos': lista_casos, 'Novos Casos (1 dia)':lista_casos_dia, 'Mortes': lista_mortes})
df.drop([0, 1], inplace=True)
df = df.sort_values('Estados')
print(df)


'''df.to_csv('covid19.csv', mode='a', header=True, index=False, sep=';')'''

