'''if ternário: Permite escrever uma condição em uma única linha.
Ela é composto por três partes, a primeira parte é o retorno caso a
expressão retorne verdadeiro, a segunda parte é a expressão lógica e a
terceira parte é o retorno caso a expressão seja atendida.'''


saldo = 2000
saque = 2500
# Tudo que esta no começo sera se expressão for VERDADEIRO
status = 'Sucesso' if saldo >= saque else 'Falha'
print(f'{status} ao realazar o saque.')