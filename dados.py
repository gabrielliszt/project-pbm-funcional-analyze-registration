# Importando bibliotecas
import pandas as pd

cnpjs = []


def importar_dados():
    # Atribuindo a base de dados em uma variável
    arquivo = pd.read_excel('C:\\Users\\pbm\\Meu Drive\\Planilhas\\!ATENDIMENTOS - Gabriel.xlsx', dtype=str)

    # Identificando apenas as lojas que precisam ser verificadas e atribuindo em outra variável
    funcional_verificar = arquivo.loc[arquivo['FUNCIONAL'] == 'VERIFICAR']

    # Obtendo a lista de CNPJs que serão verificados
    for valor in funcional_verificar['CNPJ']:
        cnpjs.append(valor)
