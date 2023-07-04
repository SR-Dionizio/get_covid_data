# COVID-19 Data Scraping

Este é um script em Python que realiza o scraping dos dados de casos de COVID-19 a partir do site do Google Notícias. O objetivo é extrair as informações de casos, novos casos em 24 horas, casos a cada um milhão de pessoas e mortes, para cada estado brasileiro.

## Bibliotecas Utilizadas

- `urlopen` da biblioteca `urllib.request` para abrir a URL e obter o conteúdo HTML.
- `BeautifulSoup` da biblioteca `bs4` para fazer o parsing do HTML e facilitar a extração dos dados.
- `pandas` para criar e manipular o DataFrame com os dados coletados.
- `datetime` para obter a data atual e utilizar no nome do arquivo CSV.

## Funcionamento do Script

O script realiza as seguintes etapas:

1. Abre a URL do site do Google Notícias que contém os dados sobre a COVID-19 no Brasil.
2. Faz o parsing do HTML utilizando a biblioteca BeautifulSoup.
3. Encontra a tabela que contém os dados de casos de COVID-19.
4. Percorre as linhas da tabela e extrai as informações de estados, casos, novos casos em 24 horas, casos a cada um milhão de pessoas e mortes.
5. Armazena os dados extraídos em listas separadas.
6. Cria um DataFrame utilizando as listas de dados coletados.
7. Remove as linhas iniciais que não são relevantes para a análise.
8. Ordena o DataFrame por ordem alfabética dos estados.
9. Imprime o DataFrame com os dados.
10. Cria um arquivo CSV com os dados coletados, utilizando a data atual no nome do arquivo.

## Como Utilizar

1. Certifique-se de ter as bibliotecas mencionadas instaladas em seu ambiente Python.
2. Copie o código para um arquivo Python.
3. Execute o arquivo Python.
4. O script irá imprimir o DataFrame com os dados de casos de COVID-19 por estado.
5. Será criado um arquivo CSV com os dados coletados, utilizando a data atual no nome do arquivo.

## Observações

- Os dados são coletados do site do Google Notícias e estão sujeitos a possíveis alterações na estrutura do HTML. É importante verificar se o script está funcionando corretamente caso ocorram mudanças no site.
- Certifique-se de cumprir os termos de uso do site do Google Notícias ao realizar o scraping dos dados.
