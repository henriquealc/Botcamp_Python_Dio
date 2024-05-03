frutas = ['laranja', 'maça', 'uva']
print(frutas)

frutas = []

letras = list("Python") # Retorna uma lista separando letra por letra
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Ferrari', 'F8', 42000, 2020, 2900, 'São Paulo', True]
print(carro)

'''Exemplo de acesso a listas'''

frutas = ['maça', 'laranja', 'uva', 'pera']
frutas[0] # Maça
frutas[2] # Uva

'''Indices negativos'''
frutas[-1] # Pera
frutas[-3] # Laranja


'''Exemplo de lista aninhadas'''

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0]) # [1, 'a', 2]
print(matriz[0][0]) # 1
print(matriz[0][-1]) # 2
print(matriz[-1][-1]) # 'C'


'''Exemplo de Fatiamento'''

lista = ['p', 'y', 't', 'h', 'o', 'n']

lista[2:] # ['t', 'h', 'o', 'n']
lista[:2] # ['p', 'y']
lista[1:3] # ['y', 't']
lista[0:3:2] # ['p', 't']
lista[::] # ['p', 'y', 't', 'h', 'o', 'n']
lista[::-1] # ['n', 'o', 'h', 't', 'y', 'p']


'''Exemplo de Iterar lista'''

carros = ['gol', 'celta', 'palio']
for ind, carro in enumerate(carros):
    print(f'{ind} {carro}')


'Exemplo de Compreensão de listas'
'''list compreension'''
numeros = [1, 30, 21, 2, 9, 65, 34]

pares = [numero for numero in numeros if numero % 2 == 0] # Pega os números pares e adiciona na lista 'pares'
print(pares)

quadrado = [num ** 2 for num in numeros] # Pega todos os números e eleva ao quadrado
print(quadrado)