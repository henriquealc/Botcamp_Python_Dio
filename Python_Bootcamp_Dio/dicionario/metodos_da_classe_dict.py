'''link: https://awari.com.br/metodos-de-dicionario-em-python-aprenda-a-manipular-dados-de-forma-eficiente/'''

'''
clear - Apaga todos os valores do dicionário
'''
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com': {'nome': 'Chappei', 'telefone': '3344-9871'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'},
}
print(contatos)

contatos.clear()
print(contatos) # {}


'''
copy - Faz uma copia do dicionário
'''
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

# Faz um copia e altera o nome 
copia = contatos.copy()
copia['guilherme@gmail.com'] = {'nome': 'Gui'}

# Retorna os dados sem alteração
print(contatos['guilherme@gmail.com']) # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(copia)



'''
fromkeys - Cria uma chave pra vc, em 2 situaçõs quando vc quer criar as chaves sem valor
ou quando vc quer criar um conjunto de chaves e quer colocar um valor padrão.
'''

dict.fromkeys(['nome', 'telefone']) # {'nome': None, 'telefone': None}

dict.fromkeys(['nome', 'telefone'], 'vazio') # {'nome':'vazio', 'telefone': 'vazio'}


'''
get - Usado para obter o valor de uma chave especifica em um dicionário. Ele retorna o valor
correspondente à chave fornecida ou um valor padrão(None) se a chave não existir.
'''

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

# contatos['chave'] # KeyError


print(contatos.get('chave'))  # None
print(contatos.get('chave', {})) # {}  - Chave inexistente, por isso retornou {}/None
print(contatos.get("guilherme@gmail.com", {})) # {'nome': 'Guilherme', 'telefone': '3333-2221'}



'''
items - Retorna uma lista de tuplas, Podemos percorrer essa lista usando um loop for para acessar cada par individualmente.
'''
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

print(contatos.items())

for chave, valor in contatos.items():
    print(chave, valor)



'''
keys - retorna uma lista contendo todas as chaves presentes no dicionário. 
Podemos percorrer essa lista usando um loop for para acessar cada chave individualmente.
'''


contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'joyce@gmail.com': {'nome': 'Joyce', 'telefone': '8898-0000'}
}

print(contatos.keys()) # dict_keys(['gilherme@gmail.com'])

for chave in contatos.keys():
    print(chave)



'''
pop - É usado para remover um elemento de um dicionário com base em sua chave. Ele também retorna o valor do elemento removido.
'''
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

print(contatos.pop('guilherme@gmail.com')) # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(contatos.pop('guilherme@gmail.com', 'chave não encontrada')) # {} - Se a chave não existir ele retorna a chave padrão



'''
popitem - Não informa a chave e ele vai retirando os itens na sequencia
'''
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}
}

print(contatos.popitem()) # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
# contatos.popitem () # KeyError - Retorna quando não tem mais itens para ele retirar



'''
setdefault - retorna o valor de uma chave (se a chave estiver no dicionário). Do contrário, 
ele insere uma chave com um valor no dicionário

link com mais ex: https://www.programiz.com/python-programming/methods/dictionary/setdefault
'''
contatos = {
    'nome': 'Guilherme', 'telefone': '3333-2221'
}

contatos.setdefault('nome', 'giovanna') # Guilherme, pois a chave ja existe no dicionário
print(contatos)
print()
contatos.setdefault('idade', 28) # Se a chava não existir ela sera adicionada no dicionário
print(contatos)



''''
Update - É utilizado para adicionar elementos de um dicionário em outro dicionário. Ele recebe
como parâmetro outro dicionário e adiciona seus elementos ao diconário atual.
'''
contatos = {
    'guilherme@gmail.com':{'nome': 'Guilherme', 'telefone': '3333-2221'}
}

# Atualiza a chave ja existente
contatos.update({'guilherme@gmail.com': {'nome': 'Gui'}})
print(contatos) # {'guilherme@gmail.com': {'nome': 'Gui'}}

# Se as chaves não existir ele vai adicionar no dicionário
contatos.update({'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}})
print(contatos) # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}



'''
values - retorna uma lista contendo todos os valores presentes no dicionário.
Podemos percorrer essa lista usando um loop for para acessar cada valor individualmente
'''
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com': {'nome': 'Chappei', 'telefone': '3344-9871'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'},
}

valores_dicionario = contatos.values()
print(valores_dicionario) # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'},
# {'nome': 'Chappei', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])
print()
for valor in contatos.values():
    print(valor)



'''
in - Metodo de verficação
'''

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com': {'nome': 'Chappei', 'telefone': '3344-9871'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'},
}
 
resultado = 'guilherme@gmail.com' in contatos # True
print(resultado)

resultado = 'megui@gmail.com' in contatos # False
print(resultado)

resultado = 'idade' in contatos ['guilherme@gmail.com'] # False
print(resultado)

resultado = 'telefone' in contatos['giovanna@gmail.com'] # True
print(resultado)



'''
del - Usado para tirar um valor do dicionário
'''

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com': {'nome': 'Chappei', 'telefone': '3344-9871'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'},
}

del contatos ['guilherme@gmail.com']['telefone'] # Removendo o telefone
del contatos ['chappie@gmail.com'] # Remove TODA a chave

print(contatos) # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}