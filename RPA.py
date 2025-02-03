from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


#configurando o navegador (Microsoft Edge)
driver = webdriver.Edge()


#acessando o site do Banco Central
url = "https://www.bcb.gov.br/"
driver.get(url)

try:
    
    #encontrando cotação do dolar
    cotacao_dolar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="home"]/div/div[1]/div[1]/div/cotacao/table[1]/tbody/tr[2]/td[2]/span'))).text

    #encontrando cotação do euro
    cotacao_euro = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="home"]/div/div[1]/div[1]/div/cotacao/table[2]/tbody/tr[2]/td[2]/span'))).text

    #criar um dataframe
    dados = pd.DataFrame({"Moeda":["Dólar", "Euro"], "Cotação": [cotacao_dolar, cotacao_euro]})

    # salvando em execel(xlsx)
    dados.to_excel("cotacoes.xlsx", index=False)

    print("Relatório gerado!")
    
except Exception as e:
    print(f"Erro ao buscar cotações: {e}")
    
finally:
    driver.quit()


    