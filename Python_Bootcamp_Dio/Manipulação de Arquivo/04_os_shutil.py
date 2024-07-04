import os
import shutil
from pathlib import Path

# Obtendo o diretório atual do script Python
ROOT_PATCH = Path(__file__).parent


# Criando um novo diretório chamado 'novo-diretorio' no diretório atual
os.mkdir(ROOT_PATCH / 'novo-diretorio')


# Criando um novo arquivo chamado 'olamundo.txt' no diretório atual
arquivo = open (ROOT_PATCH / 'olamundo.txt', 'w')
arquivo.close() # Fechando o arquivo após a criação


# Renomeando o arquivo 'novo.txt' para 'alterado.txt' no diretório atual
os.rename(ROOT_PATCH / 'novo.txt', ROOT_PATCH / 'alterado.txt')


# Removendo o arquivo 'olamundo.txt' do diretório atual
os.remove(ROOT_PATCH / 'olamundo.txt')


# Movendo o arquivo 'alterado.txt' para o diretório 'novo-diretorio'
shutil.move(ROOT_PATCH / 'alterado.txt', ROOT_PATCH / 'novo-diretorio' / 'alterado.txt')