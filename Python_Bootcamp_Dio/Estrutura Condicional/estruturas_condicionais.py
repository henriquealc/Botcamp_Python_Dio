'''
Estrutura condicionais:
A estrutura condicional permite o desvio de fluxo de controle,
quando determinadas expressões lógicas são atendidas.
* if/ if-else/elif

'''
'Ex: Usando apenas o "if"'
# saldo = 2000
# saque = float(input('Informe o valor do saque: '))

# if saldo >= saque:
#     print('Realizando saque!')

# if saldo < saque:
#     print('Saldo insuficiente!')


'Ex: Usando "if" e "else"'
# if saldo >= saque:
#     print('Saque realizado!')
# else:
#     print('Saldo insuficiente!')


'Ex: Usando "if", "elif" e "else"'
# import sys
# opcao = int(input('Informe uma opção: [1] Sacar [2] Extrato: '))

# if opcao == 1:
#     valor = float(input('Informe a quantia para o saque: '))
#     print('Saque em andamento...')
# elif opcao == 2:
#     print("Exibindo o extrato...")
# else:
#     sys.exit('Opção inválida')


'Outro exemplo do uso do "if" e "else"'
# MAIOR_IDADE = 18

# idade = int(input('Informe a sua idade: '))

# if idade >= 18:
#     print('Pode tirar a CNH.')
# else:
#     print('Ainda não pode tirar a CNH.')

