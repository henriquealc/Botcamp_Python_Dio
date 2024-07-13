import sqlite3
from pathlib import Path

# Obtém o diretório pai do arquivo atual
ROOT_PATH = Path(__file__).parent


# Conecta ao banco de dados SQLite
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

# Cria um cursor para executar comandos SQL no banco de dados
cursor = conexao.cursor()

# Define o modo de fábrica de linha para sqlite3.Row, que permite acessar as colunas por nome
cursor.row_factory = sqlite3.Row

# Solicita ao usuário que informe o ID do cliente
id_cliente = input('Informe o id do cliente: ')


# Maneira ERRADA de fazer que pode ocasionar vazamento de dados
# cursor.execute(f'SELECT * FROM clientes WHERE id={id_cliente}')


# Maneira CORRETA de se fazer, SEMPRE UTILIZAR DESSA FORMA
cursor.execute('SELECT * FROM clientes WHERE id=?', (id_cliente,))


# Obtém todos os clientes retornados pela consulta
clientes = cursor.fetchall()

# Itera sobre os clientes e imprime cada um como um dicionário
for cliente in clientes:
    print(dict(cliente))