import requests, json

def dolar():
# endereço da api
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    # request vai pegar os dados no formato json
    dados = requests.get(url, timeout=10).content

    #json.loads vai transformar em um dicionario python
    cotacao = json.loads(dados)

    return cotacao['USDBRL']['ask']



print(dolar())







