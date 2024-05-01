nome = 'Adolfo'
idade = 98
profissao = 'Programador'
linguagem = 'Python'
saldo = 45.435

dados = {'nome': 'Ticotico', 'idade': 28}

print('nome: %s idade: %d' % (nome, idade))

print('nome: {} idade: {}'.format(nome, idade))

print('nome: {1} idade: {0}'.format(idade, nome))
print('nome: {1} idade: {0} nome:{1} {1}'.format(idade, nome))

print('Nome: {nome} Idade: {idade}'.format(nome= nome, idade=idade))
print('Nome: {name} Idade: {age} {name} {name} {age}'.format(age=idade, name=nome))
print('Nome: {nome} Idade: {idade}'.format(**dados))


print(f'nome: {nome} idade: {idade}')
print(f'nome: {nome} Idade{idade} Saldo: {saldo:.2f}')
print(f'nome: {nome} Idade{idade} Saldo: {saldo:10.1f}')