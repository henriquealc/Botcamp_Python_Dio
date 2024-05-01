'''Eliminando os espaços'''
print("ELIMINANDO OS ESPAÇOS")
curso ='  Python'
print(curso.strip()) # Elimina os espaços 

print(curso.lstrip()) # Elimina os espaços do lado esquerdo

print(curso.rstrip()) # Elimina os espaços do lado direito
print('-=' * 30)



'''Junções e centralização'''
print('JUNÇÕES E CENTRALIZAÇÃO')
curso = 'Python'

print(curso.center(10, '#'))  # Centraliza automaticamento. Se não passar nada fica um espaço em branco
print('.'.join(curso)) # Coloca um '.' depois de cada letra da variavel curso
print('-=' * 30)

nome = 'José'

print(nome.upper()) # Maiunsculo
print(nome.lower()) # Minusculo
print(nome.title()) # Primeira letra maiunscula
print('-=' * 30)


menu = 'Olá Mundo'
print('###' + menu + '###')
print(menu.center(14))
print(menu.center(20, '#'))
print('P-y-t-h-o-n')
print('-'.join(menu)) # Coloca '-' apos cada letra da variavel menu
print()