
import numpy as np
import pandas as pd
import os


def trocarEspacos(nome):
    return nome.replace(' ', '')

def main():
    dados = pd.read_excel(io="Tarefas.xlsx", header=2, converters={'Analista': trocarEspacos})
    dadosFiltrados = dados.loc[dados['Analista'] == 'GabrielJardim' ]
    dadosFiltrados.to_excel("Tarefas_filtrado.xlsx")
    os.system('start excel.exe Tarefas_filtrado.xlsx')

if __name__ == '__main__':
    main()