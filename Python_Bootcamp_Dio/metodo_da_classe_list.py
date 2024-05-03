'''Link Úteis: https://github.com/digitalinnovationone/trilha-python-dio'''
'''https://academiapme-my.sharepoint.com/:p:/g/personal/nubia_dio_me/EVPXb3r8bPBEryfuvxp2uhABKXdIyWyufNXAjxQuOzabdQ?e=MDo5cY'''


'''append'''
# lista = []

# lista.append(1)
# lista.append('Python')
# lista.append([40, 30, 20])

# print(lista) # [1, 'Python', [40, 30, 20]]


'''clear - Usado para quando quero limpar a minha lista'''

# lista = [1, 'Python', [40, 30, 20]]

# print(lista) # [1, 'Python', [40, 30, 20]]

# lista.clear()

# print(lista) # []


'''copy - Cria uma copia da lista e não altera os valores da lista principal'''

# lista = [1, 'Python', [40, 30, 20]]

# l2 = lista.copy()

# print(lista)
# print(l2)



'''count - conta quantas vezes um determinado objeto tem dentro da lista'''

# cores = ['vermelho', 'azul', 'verde', 'azul']

# print(cores.count('vermelho')) # 1
# print(cores.count('azul')) # 2
# print(cores.count('verde')) # 1


'''extend - Junta uma lista com outra, não elimina os valores duplicados'''

# linguanges = ['python', 'js', 'c']

# print(linguanges) # ['python', 'js', 'c']

# linguanges.extend(['java', 'csharp'])
# print(linguanges) # ['python', 'js', 'c', 'java', 'csharp']


'''index - Mostra onde ocorre a PRIMEIRA ocorrencia do item'''
'''Só retorna 1 ocorrencia'''
# linguages = ['python', 'js', 'c', 'java', 'csharp']

# print(linguages.index("java")) # 3
# print(linguages.index('python')) # 0


'''pop - Remove o ultimo elemento que foi adicionado, mas pode passa pro pop o índice que quero remover'''

# linguagens = ['python', 'js', 'c', 'java', 'csharp']

# linguagens.pop() # csharp
# linguagens.pop() # java
# linguagens.pop() # c
# linguagens.pop(0) #pyhon
# print(linguagens)


'''remove - Segunda formar de retirar o indice de uma lista'''
'''remove apenas a PRIMEIRA ocorrencia'''
# linguagens = ['python', 'js', 'c', 'java', 'csharp']

# linguagens.remove('c')

# print(linguagens)


'''reverse - Espelha a lista de tras para frente'''

# linguagens = ['python', 'js', 'c', 'java', 'csharp']

# linguagens.reverse()

# print(linguagens) # ['csharp', 'java', 's', 'js', 'python']


'''sort - ordena a lista em oredem alfabetica como padrão'''

# linguagens = ['python', 'js', 'c', 'java', 'csharp']

# linguagens.sort() # Ordena em ordem alfabetica

# linguagens.sort(reverse=True) # Ordena em ordem alfabetica so que alcontrario (de trás pra frente)

# linguagens.sort(key=lambda x: len(x)) # Ordena pelo número de letras que tem nas frase (ordem crescente)

# linguagens.sort(key= lambda x: len(x), reverse=True) # Ordena pelo número de letras nas frases (ordem decrescente)


'''len - Usado para contar quantos itens tem na lista'''

# linguagens = ['python', 'js', 'c', 'java', 'csharp']

# print(len(linguagens)) # 5


'''sorted - Serve também para ordenar'''

# linguagens = ['python', 'js', 'c', 'java', 'csharp']

# print(sorted(linguagens, key=lambda x: len(x))) # Ordena as frases pela quantidade de letras

# print(sorted(linguagens, key=lambda x: len(x), reverse= True)) # Ordena as frases pela quantidade de letras de forma descrescente

# print(sorted(linguagens)) # Ordena por ordem alfabetica