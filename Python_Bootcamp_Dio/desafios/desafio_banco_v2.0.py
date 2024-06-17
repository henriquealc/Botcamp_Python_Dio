import textwrap

def menu():
    menu_text = '''
    ========== MENU ==========
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair

    '''
    return int(input(textwrap.dedent(menu_text)))  # Utiliza textwrap.dedent para formatar o texto do menu corretamente


def depositar(saldo, valor, extrato):
    if valor <= 0:
        print('Informe um valor positivo.')
    else:
        saldo += valor  # Adiciona o valor ao saldo atual
        extrato += f'Depósito: R$ {valor:.2f}\n'  # Adiciona a transação ao extrato
    return saldo, extrato  # Retorna o saldo e o extrato atualizados


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print('Falha na tentativa de saque! Você excedeu o número de saques permitidos.')
    elif saldo < valor:
        print('Falha na tentativa de saque! Saldo insuficiente.')
    elif valor > limite:
        print('O valor solicitado excede o limite de saque.')
    elif valor <= 0:
        print('Operação falhou! O valor informado é inválido.')
    else:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('===== SAQUE EFETUADO COM SUCESSO! =====')
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('=' * 20 + ' EXTRATO ' + '=' * 20)
    if saldo == 0:
        print('Não foram realizadas movimentações.')
    else:
        print(f'Saldo: R$ {saldo:.2f}')
    print('=' * 47)
    return saldo, extrato


def criar_usuario(AGENCIA, numero_conta, usuarios):
    cpf = input('Informe seu CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe um usuário com esse CPF!')
        return

    nome = input('Informe seu nome: ').capitalize()
    data_nascimento = input('Data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (logadouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'cpf': cpf})

    print('==== Usuário cadastrado com sucesso! ====')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    else:
        print('\nUsuário não encontrado. Criação de conta encerrada.')


def listar_contas(contas):
    for conta in contas:
        linha = f'''\
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
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input('Informe o valor de depósito: R$ '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input('Informe o valor de saque: R$ '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_usuario(AGENCIA, len(usuarios) + 1, usuarios)

        elif opcao == 7:
            break

        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")

main()
