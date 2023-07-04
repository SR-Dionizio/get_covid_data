# Documentação - COVID-19 Data Scraping

Esta documentação descreve o funcionamento e a utilização do script de scraping de dados de COVID-19 a partir do site do Google Notícias. O script é desenvolvido em Python e tem como objetivo extrair informações sobre casos de COVID-19 por estado brasileiro.

## Funcionamento

O script realiza as seguintes etapas:

1. Abertura da URL: O script abre a URL do site do Google Notícias, onde estão disponíveis os dados sobre a COVID-19.

2. Parsing do HTML: Utilizando a biblioteca BeautifulSoup, o script faz o parsing do HTML da página e organiza a estrutura do documento para facilitar a extração dos dados.

3. Extração dos dados: O script busca a tabela que contém os dados de casos de COVID-19 e percorre as linhas dessa tabela. Para cada linha, são extraídas as informações de estado, casos, novos casos em 24 horas, casos a cada um milhão de pessoas e mortes. Esses dados são armazenados em listas separadas.

4. Criação do DataFrame: Utilizando a biblioteca pandas, o script cria um DataFrame para armazenar os dados coletados. As listas de dados são convertidas em colunas do DataFrame.

5. Manipulação do DataFrame: O script remove as linhas iniciais que não são relevantes para a análise e ordena o DataFrame por ordem alfabética dos estados.

6. Impressão dos dados: O script imprime na tela o DataFrame com os dados de casos de COVID-19 por estado.

7. Criação do arquivo CSV: O script utiliza a biblioteca datetime para obter a data atual e utiliza essa informação no nome do arquivo CSV a ser criado. O DataFrame é exportado para o arquivo CSV, separando os valores por ponto e vírgula (;).

## Utilização

Para utilizar o script de scraping de dados de COVID-19, siga as instruções abaixo:

1. Certifique-se de ter as seguintes bibliotecas instaladas em seu ambiente Python:
   - urllib
   - BeautifulSoup
   - pandas
   - datetime

2. Copie o código do script para um arquivo Python com a extensão `.py`.

3. Execute o arquivo Python em seu ambiente Python.

4. Aguarde até que o script finalize a execução.

5. Após a execução, o script imprimirá na tela o DataFrame com os dados de casos de COVID-19 por estado.

6. Além disso, um arquivo CSV será criado com os dados coletados, utilizando a data atual no nome do arquivo. O arquivo CSV conterá as seguintes colunas: "Estados", "Casos", "Novos Casos (1 dia)", "Casos a cada um milhão de pessoas" e "Mortes".

## Observações

- É importante garantir que o ambiente Python tenha acesso à internet para que o script possa acessar a URL e coletar os dados do site do Google Notícias.

- O script foi desenvolvido com base na estrutura atual do site do Google Notícias. Caso ocorram alterações na estrutura do site, é possível que o script deixe de funcionar corretamente. Nesse caso, será necessário fazer ajustes no código para adaptá-lo às mudanças.

- É importante respeitar os termos de uso do site do Google Notícias ao utilizar o script de scraping. Certifique-se de que a coleta de dados esteja em conformidade com as
