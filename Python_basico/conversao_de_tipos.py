'''inteiro para float'''
print('=-'* 3, 'CONVERSÃO INTEIRO PARA FLOAT', '=-' * 3)
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10/2
print(preco)

'''float para inteiro'''
print('=-'* 3, 'CONVERSÃO FLOAT PARA INTEIRO', '=-' * 3)

preco = 10.30
print(preco)

preco = int(preco)
print(preco)

print('=-'* 3, 'CONVERSÃO PRO DIVISÃO', '=-' * 3)

preco = 10
print(preco)

print(preco / 2)

print(preco // 2)

print('=-'* 3, 'CONVERSÃO STRING PARA NÚMERO', '=-' * 3)

preco = '10.50'
idade = '28'

print(float(preco)) # Converte a string '10.50' para float
print(int(idade)) # Converte a string '28' para inteiro
print(type(100)) # Verifica a classe 


preco_int = float(preco) 
idade_float = int(idade)

print(preco_int + idade_float)