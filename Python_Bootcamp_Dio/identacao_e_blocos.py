def sacar (valor):
    saldo = 500
    if saldo >= valor:
        print('Valor sacado!')
        print('Retire seu dinheiro na boca do caixa!')
        print('Obrigado por ser nosso cliente, tenha um bom dia!')
    else:
        print('Você não contém o valor inserido!')
        print(f'Seu saldo é R$ {saldo}')

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(float(input('Valor que deseja sacar: R$ ')))
