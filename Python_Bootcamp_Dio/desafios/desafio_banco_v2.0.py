# Bug esta passando direto nas condições

import textwrap

def menu():
    menu= '''
    ========== MENU ==========
    [1]\tDepsitar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair

    '''
    return int(input(textwrap.dedent(menu)))


def depositar(saldo, valor, extrato, /): # Usando o positional only    
    if valor <= 0: # Condição feita para evitar que o usuario informe valor negativo
        print('Informe um valor positivo.')
    else:
        saldo += valor # Soma os valores inseridos pelo usuario
        saldo == valor # Transferi o valor digitado para o saldo 
        extrato += f'Deposito: R$ {valor:.2f}\n' 
        return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    if numero_saques > LIMITE_SAQUES:
        print('Falha na tentiva de saque! Você excerdeu o número de saques permitidos')
    elif saldo < valor:
       print('Falha na tentativa de saque! Você não contém esse valor em conta.')
    elif valor > limite:
        print('O valor solicitado excede o limite.')
        
    elif valor > 0: # Condição feita para evitar que o valor de saque seja negativo
        saldo -= valor # Subtrai o valor de saque da conta do usuario
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1 # Conta o número de saques 
        print('===== SAQUE EFETUADO COM SUCESSO! =====')
    else:
         print('Operação falhou! O valor informado é inválido.')    
    return saldo, extrato
    
def exibir_extrato(saldo,/, *, extrato):
    print('=' * 20 + 'EXTRATO' + '=' * 20) 
    if saldo == 0:
        print('Não foram realizadas movimentações.')
    else:
        print(f'Saldo: R$ {saldo:.2f}')
    print('=' * 47)
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input('Informe seu cpf: (somente números)')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário com esse CPF!')
        return

    nome = str(input('Informe seu nome: ')).capitalize()
    data_nascimento = input('Data de nascimento: ')
    endereco = input('Informe o seu endereço (rua, nu - bairro - cidade/sigla estado): ')
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'cpf': cpf})
    
    print('==== Usúario cadastrado com sucesso! ====')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n Usuário nçao encontrado, fluxo de criação de conta encerrado!')

def listas_contas(contas):
    for conta in contas:
        linha = f'''\n
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():  
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    sacar = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input('Informe o valor de deposito: R$ '))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input('Informe o valor de saque: R$ '))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                LIMITE_SAQUES = LIMITE_SAQUES,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            numero_conta = len(contas) +1
            conta = criar_usuario(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 5:
            contas(contas)
        
        elif opcao == 6:
            criar_usuario(usuarios)
        
        elif opcao == 7:
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()