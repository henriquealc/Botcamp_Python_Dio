# São operadores utilizados para verificar se um
# objeto está presente em uma sequência.

curso = 'Curso de Python'
frutas = ['laranja', 'uva', 'limão']
saques = [1500, 100]

'Python' in curso
# True

'maça' not in frutas
# True

200 in saques
# False

if 'banana' in frutas:
    print('banana está presente')
else:
    print('banana não está presente') 