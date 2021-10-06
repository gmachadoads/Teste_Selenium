"""
Código de teste de automação com Selenium.
Abrir navegador Google Chrome, buscar "brasileirão 2021 wikipédia" no campo de busca, entrar no link do Wikipédia,
extrair a tabela do Campeonato Brasileiro em um dataframe e exportar a tabela para uma planilha do Excel.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

# Importando drivers Path do navegador
options = webdriver.ChromeOptions()

# Determinando navegador Google Chrome
navegador = webdriver.Chrome()

# Abrindo a primeira URL
url = navegador.get('https://www.google.com.br/')
sleep(1)

# Apontando o caminho através do Xpath da página
# (botão direito/Inspecionar/setinha/clica no elemento/botão direito na TAG/copy/xpath)
html = navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# Enviando texto
html.send_keys('brasileirão 2021 wikipedia')
# Comando para ENTER
html.send_keys(Keys.ENTER)
sleep(1)

# Clicar no link para abrir a página
html = navegador.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')
# Comando para clique
html.click()

# Selecionando tabela na posição 8 (caso tenham várias tabelas) do site
# Utilizando pd.read_html, precisa informar a url. Retornará todas as tabelas disponíveis na página.
df = pd.read_html('https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2021_-_S%C3%A9rie_A')[8]

# Transformando a tabela retirada em DataFrame
df = pd.DataFrame(df)
# Exportando tabela para planílha Excel
df.to_excel(excel_writer='Campeonato.xlsx')

# Fechando navegador
navegador.quit()

print(df)
