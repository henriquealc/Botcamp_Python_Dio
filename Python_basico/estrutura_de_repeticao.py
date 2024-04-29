'''Estrutura de repetição: São estruturas ultilizadas para repetir um
trecho de código um determinado número de vezes. Esse número pode ser
conhecido previamente ou determinado através de um expressão lógica.'''

'EX: Sem repetição'
#Receba um número do teclado e exiba os 2 números seguintes
# a = int(input('Informe um número inteiro: '))
# print(a)

# a+= 1
# print(a)

# a+= 1
# print(a)

'Estrutura "for"'
# texto = input('Informe um texto: ')
# VOGAIS = 'AEIOU'

# Exemplo usando um iterável
# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end='')

# print() # Adicona um quebra de linha


'''FOR/ELSE'''
texto_2 = ''
VOGAIS2 = 'AEIOU'

for letra in texto_2:
    if letra.upper() in VOGAIS2:
        print(letra, end='')
else:
    print()
    print('Executa no final do laço.')