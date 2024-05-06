'''
Tuplas:
São estruturas de dados muito parecidos com as listas, 
a principal diferença é que tuplas são imutáveis enquanto listas são mútaveis.
Podemos criar tuplas através de classe 'tuple',
ou colocando valores separados por vírgula de parenteses.
'''


'''Exemplos de tuplas'''

# frutas = ('maça', 'laranja', 'pera', 'uva',)
# frutas[0] # maça
# frutas[1] # pera
# frutas[-1] # uva
# frutas[-3] # laranja

# letras = tuple('python')

# numeros = tuple([1, 2, 3, 4])

# pais = ('Brasil',)


'''
Tuplas aninhadas:
Podem armazenar todos os tipos de objetos Python;
portanto podemos ter tuplas que armazenam outras tupla.
Com isso podemos criar estruturas bidimensionais (tabelas), e
acessar informando os índices de linha e coluna.
'''

# matriz = (
#     (1, 'a', 2),
#     ('b', 3, 4),
#     (6, 5, 'c'),
# )

# matriz[0] # (1, 'a', 2)
# matriz[0][0] # 1
# matriz[0][-1] # 2
# matriz[-1][-1] # c



'''Fatiamento mesma coisa de listas'''

# tupla = ('p', 'y', 't', 'h', 'o', 'n')

# tupla[2:] # ['t', 'h', 'o', 'n']
# tupla[:2] # ['p', 'y']
# tupla[1:3] # ['y', 't']
# tupla[0:3:2] # ['p', 't']
# tupla[::] # ['p', 'y', 't', 'h', 'o', 'n']
# tupla[::-1] # ['n', 'o', 'h', 't', 'y', 'p']



'''Iterar'''
# tupla = (1, 2, 'a')
# for i, num in enumerate(tupla):
#     print(f'{i}- {num}')


'''Métodos da classe tuple'''

'''count'''
# cores = ('vermelho', 'azul', 'verde', 'azul', )
# cores.count('vemelho') # 1
# cores.count('azul') # 2
# cores.count('verde') # 1


'''index- Retorna em que posição está o objeto'''
# linguagens = ('python', 'js', 'c', 'java', 'csharp')

# linguagens.index('java') # 3
# linguagens.index('python') # 0


'''len'''
linguagens = ('python', 'js', 'c', 'java', 'csharp')
print(len(linguagens)) # 5