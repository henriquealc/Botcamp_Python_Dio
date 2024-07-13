import sqlite3
from pathlib import Path

# Define o caminho para o arquivo do banco de dados
ROOT_PATH = Path(__file__).parent

# Conecta ao banco de dados SQLite usando o caminho especificado
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

# Cria um cursor para executar comandos SQL no banco de dados
cursor = conexao.cursor()

# Define o modo de fábrica de linha para sqlite3.Row, permitindo acessar colunas por nome
cursor.row_factory = sqlite3.Row

try:
    # Tenta inserir um novo cliente na tabela 'clientes' com nome 'Teste 3' e email 'teste3@gmail.com'
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)', ('Teste 3', 'teste3@gmail.com'))
    
    # Tenta inserir outro cliente na tabela 'clientes' com ID 2, nome 'Teste 4' e email 'teste4@gmail.com'
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?,?,?)', (2, 'Teste 4', 'teste4@gmail.com'))
    conexao.commit()
# Se ocorrer qualquer exceção durante as operações acima, captura o erro
except Exception as exc:

    # Imprime uma mensagem de erro indicando qual exceção ocorreu
    print(f'Ops! um erro ocorreu! {exc}')

    # Desfaz quaisquer alterações não confirmadas no banco de dados
    conexao.rollback()