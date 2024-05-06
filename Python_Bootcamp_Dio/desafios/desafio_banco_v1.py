menu = '''
Escolha uma das opcões abaixo:
[1] Depsitar
[2] Sacar
[3] Extrato
[4] Sair

'''

saldo = 0
saque = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = int(input(menu)) # Imprimi o menu na tela

    if opcao == 1:
        deposito = float(input('Insira o valor do seu deposito: R$ '))
        
        if deposito <= 0: # Condição feita para evitar que o usuario informe valor negativo
            print('Informe um valor positivo.')
        else:
            saldo += deposito # Soma os valores inseridos pelo usuario
            saldo == deposito # Transferi o valor digitado para o saldo 
            extrato += f'Deposito: R$ {deposito:.2f}\n' 

    elif opcao == 2:
        deposito = float(input('Informe o valor que deseja sacar: R$ ')) # Coleta o valor que o usuario deseja sacar
        
        if numero_saques > LIMITE_SAQUES:
            print('Falha na tentiva de saque! Você excerdeu o número de saques permitidos')
        elif saldo < deposito:
           print('Falha na tentativa de saque! Você não contém esse valor em conta.')
        elif deposito > limite:
            print('O valor solicitado excede o limite.')
        
        elif deposito > 0: # Condição feita para evitar que o valor de saque seja negativo
            saldo -= deposito # Subtrai o valor de saque da conta do usuario
            extrato += f'Saque: R$ {deposito:.2f}\n'
            numero_saques += 1 # Conta o número de saques 
        else:
            print('Operação falhou! O valor informado é inválido.')    
    
    elif opcao == 3:
        print('=' * 20 + 'EXTRATO' + '=' * 20) 
        if saldo == 0:
            print('Não foram realizadas movimentações.')
        else:
            print(f'Saldo: R$ {saldo:.2f}')
        print('=' * 47)
    
    elif opcao == 4: 
        print('Obrigado por usar o nosso banco. Volte sempre!')
        break
    
    else:
        print('Opção inválida, por favor informe uma opção valida.')