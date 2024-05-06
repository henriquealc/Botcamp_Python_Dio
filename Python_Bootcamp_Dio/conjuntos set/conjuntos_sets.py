'''
Criando sets - sets é uma coleção que não possui objetos repetidos,
usamos sets para representar conjuntos matemáticos ou eliminar itens
duplicados de um iterável.
NÃO SE PODE CONFIAR NA ORDEM DO SET, ELE RETORNA EM OUTRA ORDEM
'''

'EX de set:'

# numeros = set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
# print(numeros)

# fruta = set('abacaxi') # {'b', 'a', 'c', 'x', 'i'}
# print(fruta)

# carros = set(('palio', 'gol', 'celta', 'palio')) # {'gol', 'celta', 'palio'}
# print(carros)

# linguagens = {'python', 'java', 'python'}
# print(linguagens)


'''
Acessando os dados - Conjuntos em Python não suportam indexação e nem fatiamento,
caso queira acessar os seus valores é necessário converter o conjunto para lista.
'''
'Ex:'

numeros = {1, 2, 3, 2}
numeros = list(numeros) # Transforma o set em uma lista

print(numeros[0])


'''
Iterar conjuntos - A forma mais comum para percorrer os dados de um conjunto
é utilizando o comando 'for'
'''

carros  = {'palio', 'fiat', 'gol'}
for carro in carros:
    print(carros)



'''
Função enumerate- Ás vezes é necessário saber qual o índice do objeto dentro do laço
'for'. Para isso podemos usar a função enumerate.
'''

carros  = {'palio', 'fiat', 'gol', 'audi'}
for i, carro in enumerate(carros):
    print(f'{i+1}- {carro}')
