'''
Objetos de primeira classe - Em Python tudo é objeto, dessa forma funções também
são objetos o que as tornam objetos de primeira classe. Com isso podemos atribuir 
funções a variáveis, passá-las como parâmetro para função, usá-las como valores em estruturas
de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma
função (closures).
'''
'Ex:'
# Função feita para somar 2 números 
def soma(a, b):
    return a + b 

def subtrair(a, b):
    return a - b

def test(a, b):
    return a * 2 + b * 3

# Essa função recebe os argumentos 'a' e 'b' e um terceiro argumento que é 'funcao'.
def exibir_resultado (a, b, funcao):
    resultado = funcao(a, b)
    print(f'O rsultado da operação é = {resultado}')


exibir_resultado(10, 10, soma) # Não executa a função soma pois não passa os parenteses desta forma soma().
# O resutado da operação 10 + 10 = 20

exibir_resultado(10, 10, subtrair) # O resultado da operação 10 - 10 = 0
exibir_resultado(10, 10, test) # O resultado da operação 10 - 10 = 0

op = soma 
print(op(1, 23))
