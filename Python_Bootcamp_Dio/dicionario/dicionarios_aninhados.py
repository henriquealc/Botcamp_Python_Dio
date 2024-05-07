'''
Dicionários aninhados - Podem armazenar qualquer tipo de objeto Python
como valor, desde que a chave para esse valor seja um objeto imutável
como (string e números).
'''

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com': {'nome': 'Chappei', 'telefone': '3344-9871'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766', 'extra': {'a': 1}},
}

print(contatos['giovanna@gmail.com']['telefone']) # 3443-2121
print(contatos['chappie@gmail.com'])

telefone = contatos['melaine@gmail.com']['telefone'] # 3333-7766
print(telefone)

extra = contatos['melaine@gmail.com']['extra']['a']
print(extra)


