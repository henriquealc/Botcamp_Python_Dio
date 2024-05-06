'link: https://www.homehost.com.br/blog/pythondjango/set-python/#:~:text=Set%20em%20Python%20podem%20ser,forma%20mais%20concisa%20e%20f%C3%A1cil.'

'''
Union - Une um conjunto ao outro, retorna um novo 
conjunto contendo todos os elementos de ambos os conjuntos
'''

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b)) # {1, 2, 3, 4}



'''
intersection - retorna um novo conjunto contendo todos os elementos 
comuns aos dois conjuntos
'''

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b)) # {2, 3}


'''
difference - retorna um novo conjunto contendo todos os elementos comuns
aos dois conjuntos
'''

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}



'''
symmetric_difference - Todos os elemntos que nao estao na intersection
'''

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}



'''
issubset - Significa que todos os elemento do conjunto_a pertencerm a 'conjunto_b'
'''

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b)) # True
print(conjunto_b.issubset(conjunto_a)) # False



'''
issuperset - É ao contrario de issubset, retorna True se todos os elemntos de b estiverem em a
'''

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_b.issuperset(conjunto_a)) # True


'''
isdisjoint - Retorna True se os conjuntos NÃO tiverem nenhum elemento em comum.
'''

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # True
print(conjunto_a.isdisjoint(conjunto_c)) # False


'''
add - Adiciona um elemento ao conjunto. 
Se passar um elemento que ja exite ele sera ignorado
'''
print()

sorteio = {1, 23}

print(sorteio)
sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

print(sorteio)


'''clear - Remove todos os elementos do conjunto'''
sorteio = {1, 23}
print(sorteio)
sorteio.clear()
print(sorteio)


'''copy - Gera uma copia do conjunto'''
sorteio = {1, 23}
sorteio # {1, 23}
sorteio.copy()
print(sorteio) # {1, 23} 



'''discard - Discarta um valor, remove e retorna um elemento do conjunto'''
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, Elimina os números repetidos. 
numeros.discard(1)
numeros.discard(2)
numeros.discard(45) # Não existe 45 no set, mas não retorna um erro
print(numeros) 


'''
pop - Remove e retorna o último elemento adicionado ao conjunto (se houver).
'''
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# NESTE CASO O POP SEMPRE VAI TIRAR O VALOR DA FRENTE
print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} Remove os números duplicados
numeros.pop() # 0
numeros.pop() # 1
print(numeros) # {2, 3, 4, 5, 6, 7, 8, 9}



'''
remove - remove um elemento do conjunto
SE O ELEMENTO NÃO EXISTE VAI RETORNAR ERROR
USANDO O DISCARD ELE NÃO DA ERRO SE O ELEMENTO NÃO EXISTIR
'''
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} Remove os duplicados
numeros.remove(0) # Remove o valor 0
# numeros.remove(45) # VAI DA ERROR, POIS O ELEMENTO NÃO EXISTE NO SET
numeros.remove(8)
print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9}



'''len - mostra o tamanho do conjunto'''
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(len(numeros)) # 10


'''in - Verifica se o valor esta no set'''
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros) # True
print(10 in numeros) # False
