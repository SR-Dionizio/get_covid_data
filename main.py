import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&gl=BR&ceid=BR%3Apt-419&state=1'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

tabela_covid19 = soup.find('table', class_='pH8O4c')

linhas = tabela_covid19.find_all('tr')


for linha in linhas:
    estados = linha.find('th').get_text()
    
    casos = linha.find('td')
    if casos is not None:
        casos_formatado = casos.string
        if casos_formatado:
            
            '''print(estados, texto_formatado)'''

    mortes = linha.find_all('td')
    if len(mortes) >= 5:
        mortes_formatado = mortes[4]
        print(mortes_formatado.get_text())