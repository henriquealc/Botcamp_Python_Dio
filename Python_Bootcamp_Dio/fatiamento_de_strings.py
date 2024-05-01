nome = 'Guilherme Arthur de Carvalho'

print(nome[0])
# 'G'
print(nome[-1]) # Pega última letra do nome
# 'o'
print(nome[:9])
# 'Guilherme'

print(nome[10]) # Começa da posição 10 e vai até o final da  string
# 'Arthur de Carvalho'

print(nome[10:16]) # Começa na posição 10 e vai até a 16
# 'Arthur'

print(nome[10:16:2]) # Começa na posição 10 e vai pulando de 2 em 2 até a posição 16
# 'Atu'

print(nome[:]) # Imprimi o nome completo
# 'Guilherme Arthur de Carvalho'

print(nome[::-1]) # Faz o nome ficar inverso (de tras para frente)
# ohlavraC ed ruhtrA emrehliuG