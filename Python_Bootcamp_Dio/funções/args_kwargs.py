'''
Args e Kwargs - Podemos combinar parâmetros obrigatórios com args e
kwargs. Quando esses são definidos (*args e **kwargs), o método recebe
os valores como tupla e dicionário respectivamente.
'''

def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n {texto}\n\n{meta_dados}'
    print(mensagem)


exibir_poema('Quarta-feira, 08 mai 24 ','Zen of Python', 'Beautuful is better than ungly.', autor='Tim Peters', ano = 1999)