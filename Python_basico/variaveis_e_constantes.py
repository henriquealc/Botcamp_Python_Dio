'''
Variáveis = Podem mudar de valor durante a execução do programa.
Constantes = Representam valores fixos. Deve sempre está declarada em nome maiusculo
'''

age = 23 
name = 'Gil'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

# Outra forma
# Posso definir tudo em uma mesma linha
# Os parenteses são opcionais
age, name = (23, 'Rodri') # ou 23, 'Rodri'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')




# snake case - maneira mais correta de declarar uma variavel
# Sempre deixar claro oq a variavel faz
limite_diario_saque = 1000 


#EX de constantes
BRAZILIAN_STATES = ['SP', 'RJ', 'SC', 'RS']
print(BRAZILIAN_STATES)