import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&gl=BR&ceid=BR%3Apt-419&state=1'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

estatistica_covid19 = soup.find('table', class_='pH8O4c')
por_estados = estatistica_covid19.find_all('th', class_= 'l3HOY')
total_casos = estatistica_covid19.find_all('tr')

covid19 = []

for estatistica1, estatistica2 in zip(por_estados, total_casos):
    estatistica1 = estatistica1.get_text()
    covid19.append(estatistica1)



    casos = estatistica2.find('td')
    if casos is not None:
        texto_formatado = casos.string
        if texto_formatado:
            covid19.append(texto_formatado)
print(covid19)