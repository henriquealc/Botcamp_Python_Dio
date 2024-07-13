import sqlite3
from pathlib import Path

# Define o caminho para o arquivo do banco de dados
ROOT_PATH = Path(__file__).parent

# Conecta ao banco de dados SQLite usando o caminho especificado
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

# Imprime o objeto de conexão para verificar se a conexão foi estabelecida corretamente
# print(conexao)


cursor = conexao.cursor()

# cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')


'''Exemplo que devemos sempre evitar'''
# Maneira perigoso que pode vazar dadosx
# id = 1
# cursor.execute('SELECT * FROM minha_tabela WHERE id =' + str(id))

'''Exemplo indicado que deve ser seguido'''
# id = 1
# cursor.execute('SELECT * FROM minha_tabela WHERE id = ?', (id,))



# Inseri usuarios no banco de dados
# data = ('José', 'jose@gmail.com')
# cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data)
# conexao.commit()


# Atualiza o usuario passado abaixo
# data = ('Joyce', 'joyce@gmail.com', 2)
# cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
# conexao.commit()


# Removendo registros
# def excluir_registro(conexao, cursor, id):
#     data = (id,)
#     cursor.execute('DELETE FROM clientes WHERE id=?;', data)
#     conexao.commit()

# excluir_registro(conexao, cursor, 2)



# Inserindo varios dados
# def inserir_muitos(conexao, cursor, dados):
#     cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', dados)
#     conexao.commit()

# dados = [
#     ('Henrique', 'henrique@gmail.com'),
#     ('Raysa', 'raysa@gmail.com'),
#     ('Andre', 'andre@gmail.com'),
#     ('Lary', 'lary@gmail.com'),

# ]

# inserir_muitos(conexao, cursor, dados)


# def recuperar_cliente(cursor, id):
#     # Esta função recebe dois parâmetros: cursor e id.
    
#     # A linha abaixo executa uma consulta SQL para selecionar todos os campos da tabela 'clientes'
#     # onde o campo 'id' seja igual ao ID fornecido como parâmetro.
#     cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
#     # O método fetchone() recupera a próxima linha do resultado da consulta.
#     # Neste caso, ele retornará um único registro que corresponde ao ID fornecido.
#     return cursor.fetchone() 


#    # Aqui estamos chamando a função 'recuperar_cliente' com dois parâmetros:
#    # - cursor: o cursor do banco de dados que será usado para executar a consulta
#    # - 1: o ID do cliente que queremos recuperar
# cliente = recuperar_cliente(cursor, 1)

# # Finalmente, estamos imprimindo o cliente recuperado.
# print(cliente)



# Traz a lista com todos os clientes 
def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes;')
    # return cursor.execute('SELECT * FROM clientes ORDER BY nome;') # Ordena pelo nome

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)
