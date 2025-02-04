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

XPATH_DOLAR_COMPRA = '//*[@id="home"]/div/div[1]/div[1]/div/cotacao/table[1]/tbody/tr[2]/td[2]/span'
XPATH_DOLAR_VENDA = '//*[@id="home"]/div/div[1]/div[1]/div/cotacao/table[1]/tbody/tr[2]/td[3]/span'
XPATH_EURO_COMPRA = '//*[@id="home"]/div/div[1]/div[1]/div/cotacao/table[2]/tbody/tr[2]/td[2]/span'
XPATH_EURO_VEMDA = '//*[@id="home"]/div/div[1]/div[1]/div/cotacao/table[2]/tbody/tr[2]/td[3]/span'


# def para formatar a cotação para float
def formatar_cotacao(valor):
    return float(valor.replace(",", "."))

try:
    #encontrando cotação do dolar
    cotacao_dolar_compra = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, XPATH_DOLAR_COMPRA))).text
    cotacao_dolar_venda = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, XPATH_DOLAR_VENDA))).text

    #encontrando cotação do euro
    cotacao_euro_compra = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, XPATH_EURO_COMPRA))).text
    cotacao_euro_venda = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, XPATH_EURO_VEMDA))).text

    #criar um dataframe
    dados = pd.DataFrame({
        "Moeda": ["Dólar", "Euro"],
        "Compra": [formatar_cotacao(cotacao_dolar_compra), formatar_cotacao(cotacao_euro_compra)],
        "Venda": [formatar_cotacao(cotacao_dolar_venda), formatar_cotacao(cotacao_euro_venda)]
    })

    #salvando em execel(xlsx)
    dados.to_excel("cotacoes.xlsx", index=False)

    print("Relatório gerado!")
    
except Exception as e:
    print(f"Erro ao buscar cotações: {e}")
    
finally:
    if 'driver' in locals():
        driver.quit


    