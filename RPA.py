import pandas as pd
import requests


# função para buscar dados da API
def buscar_cotacao(codigo_serie):
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]["valor"]
    else:
        print("Erro ao buscar dados: {response.status_code}")
        return None
    
    
# codigo das series no BC
codigos = {
    "Dolar Compra": 1,
    "Dolar Venda": 10813,
    "Euro Compra": 21619,
    "Euro Venda": 21620       
}

# dicionario para armazenar os valores
cotacoes = {}

# buscando os valores de compra e venda das moedas
for moeda, codigo in codigos.items():
    cotacoes[moeda] = buscar_cotacao(codigo)

#criando dataframe com os dados coletados
df = pd.DataFrame([cotacoes])

#salvando em excel
df.to_excel("cotacoes.xlsx", index=False)

print("Cotações coletadas!")
