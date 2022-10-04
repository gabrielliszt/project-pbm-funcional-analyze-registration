# Importando bibliotecas
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dados import importar_dados, cnpjs

# Importando dados
importar_dados()

# Abrindo navegador
driver = webdriver.Chrome()

# Tempo de espera
driver.implicitly_wait(3)

# Maximizando a tela
driver.maximize_window()

# Site que será acessado
url = 'https://www.funcionalacesso.com/NovoCadastro.aspx'

# Abrindo o site
driver.get(url)

# Aceitando os coockies
time.sleep(3)
coockies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
coockies.click()

# Localizando o campo para digitar o CNPJ

mensagens = []
for cnpj in cnpjs:
    time.sleep(3)
    campo_cnpj = driver.find_element(By.XPATH,
                                     '/html/body/form/div[3]/div[8]/div[1]/div[1]/div/div/div[2]/div[1]/div[3]/div[1]/input')
    campo_cnpj.send_keys(cnpj)
    time.sleep(1)
    campo_cnpj.send_keys(Keys.ENTER)
    time.sleep(2)

    span_message = driver.find_element(By.ID, 'ContentPlaceHolder1_lblNaoCnpjInvalido').text

    if span_message == 'Este CNPJ não pode ser cadastrado, pois não pertence à matriz!':
        mensagens.append('NÃO CADASTRADO')
        print(f'{cnpj} não cadastrado.')
    elif span_message == 'Este CNPJ já está cadastrado!':
        mensagens.append('CADASTRADO')
        print(f'{cnpj} cadastrado.')
    else:
        mensagens.append('NÃO CADASTRADO')
        print(f'{cnpj} não cadastrado.')

    driver.refresh()

planilha = {'CNPJ': cnpjs,
            'STATUS': mensagens}
dataframe = pd.DataFrame.from_dict(planilha)
dataframe.to_excel(excel_writer='Relatório.xlsx', sheet_name='Planilha 1', index=False)

# Encerrando navegador
driver.quit()
