saldo = 1000
saque = 200
limite = 100

saldo >= saque
# True
saque <= limite
# False

# Usando o operador 'and'
# Precisa que todas as partes sejam verdadeiras
saldo >= saque and saque <= limite
# False


# Operador 'or' precisa que pelo menos uma expresão seja verdadeira
saldo >= saque or saque <= limite
# True

# Operador de negação
contatos_emergencia = []

not 1000 > 1500
# True

not contatos_emergencia
# True

not 'saque 1500;'
# False

not ''
# True


'''Parênteses'''
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Expressão mais dificil de ler e menos recomendada
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)# True

# Expresão recomendada
exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)# True


conta_normal_com_saldo = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo or conta_especial_com_saldo_suficiente
print(exp_3)





# AND - para ser True tudo tem que ser True
# OR  - para ser True apenas um tem que ser True
print(True and True) #True
print(True and False) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or False) # False