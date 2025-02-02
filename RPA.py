from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


#configurando o navegador (Microsoft Edge)
driver = webdriver.Edge()


#acessando o site do Banco Central
url = "https://www.bcb.gov.br/"
driver.get(url)

#aguardando abrir
time.sleep(5)

#encontrando cotação do dolar
cotacao_dolar = driver.find_element(By.XPATH, '//*[@id="home"]/div/div[1]/div[1]/div/cotacao/table[1]/tbody/tr[2]/td[3]').text

#encontrando cotação do euro
cotacao_euro = driver.find_element(By.XPATH, '//*[@id="home"]/div/div[1]/div[1]/div/cotacao/table[2]/tbody/tr[2]/td[3]/span').text

#fechar o navegador
driver.quit()

#criar um dataframe
dados = pd.DataFrame({"Moeda":["Dólar", "Euro"], "Cotação": [cotacao_dolar, cotacao_euro]})

# salvando em execel(xlsx)
dados.to_excel("cotacoes.xlsx", index=False)

print("Relatório gerado!")