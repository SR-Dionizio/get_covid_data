from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&gl=BR&ceid=BR%3Apt-419&state=1'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

estatistica_covid19 = soup.find('table', class_='pH8O4c')
por_estados = estatistica_covid19.find_all('th', class_= 'l3HOY')

for estatistica in por_estados:
    estados = estatistica.find('div', class_ = 'pcAJd').get_text()

    print(estados)