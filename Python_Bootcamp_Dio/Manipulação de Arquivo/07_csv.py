'''link da documentação CSV: https://docs.python.org/3/library/csv.html'''

import csv
from pathlib import Path

ROOT_PATC = Path(__file__).parent

COLUNA_ID = 0 # Índice da coluna 'id' no arquivo CSV
COLUNA_NOME = 1 # Índice da coluna 'nome' no arquivo CSV


# Escrevendo dados em um arquivo CSV usando csv.writer
try:
    with open(ROOT_PATC / 'usuario.csv', 'w', newline= '', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)  # Cria um objeto escritor de CSV associado ao arquivo
        escritor.writerow(['id', 'nome']) # Escreve uma linha no arquivo com os cabeçalhos 'id' e 'nome'
        escritor.writerow(['1', 'Maria']) # Escreve uma linha no arquivo com os dados '1' e 'Maria'
        escritor.writerow(['2', 'José']) # Escreve uma linha no arquivo com os dados '2' e 'José'
        escritor.writerow(['3', 'Aryell']) # Escreve uma linha no arquivo com os dados '2' e 'José'

except IOError as exc:
    print("Erro ao criar o arquivo", exc)



# Lendo dados de um arquivo CSV usando csv.reader
try:
    with open(ROOT_PATC / 'usuario.csv', 'r', newline= '', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)  # Cria um objeto leitor de CSV associado ao arquivo
        for idx, row in enumerate(leitor): # Itera sobre as linhas do arquivo, começando do índice 0
            if idx == 0: # Ignora o cabeçalho na primeira linha
                continue
            print(f'ID: {row[COLUNA_ID]}') # Exibe o valor da coluna 'id' de cada linha
            print(f'Nome: {row[COLUNA_NOME]}') # Exibe o valor da coluna 'nome' de cada linha
except IOError as exc:
    print("Erro ao criar o arquivo", exc)


# Lendo dados de um arquivo CSV usando csv.DictReader
try:
    with open(ROOT_PATC / 'usuario.csv', newline= '', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile) # Cria um objeto leitor de CSV como dicionário associado ao arquivo
        for row in reader: # Itera sobre as linhas do arquivo
            print(f'ID: {row["id"]}') # Exibe o valor da chave 'id' de cada linha (dicionário)
            print(f'Nome: {row["nome"]}') # Exibe o valor da chave 'nome' de cada linha (dicionário)
except IOError as exc:
    print('Erro ao criar o arquivo.', exc)