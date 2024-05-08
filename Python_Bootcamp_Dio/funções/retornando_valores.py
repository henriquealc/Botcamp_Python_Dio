'''
Retornando Valores - Para retornar um valor, utilizamos a palavra reservada 'return'.
Todas funções Python retorna 'None' por padrão. Diferente de outras linguagens de programação,
em Python uma função pode retornar mais de um valor.
'''

def calcular_total(numeros):
    return sum(numeros) # Soma todos os numeros

def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

def fun_3():
    # print('Olá mundo!') # Se usar o print para retorna ira retorna None
    return 'Olá mundo!'

print(calcular_total([10, 20, 34])) # 64
print(antecessor_sucessor(10)) # (9, 11)
print(fun_3())
