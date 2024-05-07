'''
Criando dicionários - É um conjunto não-ordenado de pares
chave: valor, onde as chaves são únicas em uma data instância
do dicionário. Dicionários são delimitados por chaves: {}, e 
contém uma lista de pares chave:valor separada por vírgulas.
'''

'Ex de dicionário'
# pessoa = {'nome': 'Guilherme', 'idade': 28}
# print(pessoa) # Dicionário antes de adicionar o número
# # Outra forma de declarar um dicionário
# pessoa = dict(nome='Guilherme', idade=38)

# pessoa['telefone'] = '3333-1234' # Adiciona o chave(numero):valor(3333-1234) no dicionário
# print(pessoa)



dados = {'nome': 'Guilherme', 'idade': 28, 'telefone': '4444-3124'}

# Acessando os valores
print(dados['nome']) # Guilherme
print(dados['idade']) # 28
print(dados['telefone']) # 4444-3124

# Acessando e substituindo os valores do diconário
dados['nome'] = 'Maria'
dados['idade'] = '18'
dados['telefone'] = '9988-1781'

print(dados)







