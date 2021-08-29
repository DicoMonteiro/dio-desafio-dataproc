import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

# print(resposta)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
region = dados['region']
pais = dados['country']
cep = dados['postal']


print('Detalhes do IP Externo\n')
print('IP: {5}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.: {0}\nCEP: {4}\n'.format(org, region, pais, city, cep, ip))