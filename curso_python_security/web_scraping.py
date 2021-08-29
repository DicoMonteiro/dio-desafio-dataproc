from bs4 import BeautifulSoup

import requests

# Objeto site está recebendo o conteúdo da requisição http do site...
site = requests.get('https://www.climatempo.com.br/').content
# Objeto soup está baixando do site o html...
soup = BeautifulSoup(site, 'html.parser')
# transformando html em string e o print vai exibir o html
# print(soup.prettify())

# temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
temperatura = soup.find("div", class_="card _flex _relative ")

# print(temperatura.string)
# print(soup.title.string)
print(soup.a)
print(soup.p)