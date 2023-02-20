from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&gl=BR&ceid=BR%3Apt-419&state=1'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

estado = soup.find('div', class_='pcAJd').get_text()

print(estado)