'''
Função - É um bloco de código identificado por um nome e pode
receber uma lista de parâmetros, podem ou não ter valores padrões.
Usar funçôes torna o código mais legível e possibilita o reaproveitamento 
de còdigo. Programar baseado em funções, é o mesmo que dizer que estamos
programando de maneira estruturada.
'''

def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem2(nome):
    print(f'Seja bem vinda {nome}!')

def exibir_mensagem3(nome='Anônimo'):
    print(f'Seja bem vindo {nome}!')

exibir_mensagem()
exibir_mensagem2(nome='Guilherme') # Se não passar o valor retornara um error
exibir_mensagem3()
exibir_mensagem3(nome='Chappie')

