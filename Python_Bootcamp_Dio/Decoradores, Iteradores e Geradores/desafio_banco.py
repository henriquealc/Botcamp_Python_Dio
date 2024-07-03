import textwrap  # Importa o módulo textwrap para formatação de texto
from abc import ABC, abstractclassmethod, abstractproperty  # Importa classes ABC, abstractclassmethod, abstractproperty do módulo abc
from datetime import datetime  # Importa a classe datetime do módulo datetime


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas  # Inicializa o iterador com uma lista de contas
        self._index = 0  # Inicializa o índice do iterador

    def __iter__(self):
        return self  # Retorna o próprio objeto como iterador

    def __next__(self):
        try:
            conta = self.contas[self._index]  # Obtém a conta atual
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration  # Lança StopIteration quando não há mais itens
        finally:
            self._index += 1  # Incrementa o índice para o próximo item


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco  # Inicializa o cliente com um endereço
        self.contas = []  # Inicializa a lista de contas do cliente
        self.indice_conta = 0  # Inicializa o índice da conta (não utilizado no código atualmente)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)  # Realiza uma transação em uma conta específica

    def adicionar_conta(self, conta):
        self.contas.append(conta)  # Adiciona uma nova conta à lista de contas do cliente


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Chama o construtor da classe pai (Cliente)
        self.nome = nome  # Inicializa o nome da pessoa física
        self.data_nascimento = data_nascimento  # Inicializa a data de nascimento da pessoa física
        self.cpf = cpf  # Inicializa o CPF da pessoa física


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0  # Inicializa o saldo da conta
        self._numero = numero  # Define o número da conta
        self._agencia = "0001"  # Define a agência da conta
        self._cliente = cliente  # Define o cliente associado à conta
        self._historico = Historico()  # Inicializa o histórico de transações da conta

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)  # Cria uma nova conta para o cliente especificado

    @property
    def saldo(self):
        return self._saldo  # Retorna o saldo da conta

    @property
    def numero(self):
        return self._numero  # Retorna o número da conta

    @property
    def agencia(self):
        return self._agencia  # Retorna a agência da conta

    @property
    def cliente(self):
        return self._cliente  # Retorna o cliente associado à conta

    @property
    def historico(self):
        return self._historico  # Retorna o histórico de transações da conta

    def sacar(self, valor):
        saldo = self.saldo  # Obtém o saldo atual da conta
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo disponível

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")  # Mensagem de erro se o saldo for insuficiente

        elif valor > 0:
            self._saldo -= valor  # Deduz o valor do saque do saldo da conta
            print("\n=== Saque realizado com sucesso! ===")  # Mensagem de sucesso

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  # Mensagem de erro se o valor do saque for inválido

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor  # Adiciona o valor do depósito ao saldo da conta
            print("\n=== Depósito realizado com sucesso! ===")  # Mensagem de sucesso ao depositar
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  # Mensagem de erro se o valor do depósito for inválido

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Chama o construtor da classe pai (Conta)
        self._limite = limite  # Define o limite da conta corrente
        self._limite_saques = limite_saques  # Define o limite de saques da conta corrente

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )  # Calcula o número de saques realizados

        excedeu_limite = valor > self._limite  # Verifica se o valor do saque excede o limite da conta
        excedeu_saques = numero_saques >= self._limite_saques  # Verifica se excedeu o número máximo de saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")  # Mensagem de erro se o valor do saque exceder o limite

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")  # Mensagem de erro se exceder o número máximo de saques

        else:
            return super().sacar(valor)  # Chama o método sacar da classe pai (Conta)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []  # Inicializa a lista de transações no histórico

    @property
    def transacoes(self):
        return self._transacoes  # Retorna a lista de transações

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Adiciona o tipo da transação (nome da classe)
                "valor": transacao.valor,  # Adiciona o valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),  # Adiciona a data e hora da transação
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao  # Gera as transações filtradas pelo tipo especificado


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Inicializa o valor do saque

    @property
    def valor(self):
        return self._valor  # Retorna o valor do saque

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)  # Tenta realizar o saque na conta

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona a transação ao histórico da conta


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Inicializa o valor do depósito

    @property
    def valor(self):
        return self._valor  # Retorna o valor do depósito

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)  # Tenta realizar o depósito na conta

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona a transação ao histórico da conta


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)  # Executa a função decorada
        print(f"{datetime.now()}: {func.__name__.upper()}")  # Registra o log da transação com data e hora
        return resultado

    return envelope


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """  # Define o menu principal da aplicação
    return input(textwrap.dedent(menu))  # Retorna a opção escolhida pelo usuário


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]  # Filtra clientes pelo CPF
    return clientes_filtrados[0] if clientes_filtrados else None  # Retorna o primeiro cliente encontrado ou None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")  # Mensagem se o cliente não tiver conta
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]  # Retorna a primeira conta do cliente (não implementado o fluxo de escolher a conta)


@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Filtra o cliente pelo CPF

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")  # Mensagem se o cliente não for encontrado
        return

    valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito
    transacao = Deposito(valor)  # Cria uma transação de depósito com o valor informado

    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)  # Realiza a transação de depósito


@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Filtra o cliente pelo CPF

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")  # Mensagem se o cliente não for encontrado
        return

    valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque
    transacao = Saque(valor)  # Cria uma transação de saque com o valor informado

    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)  # Realiza a transação de saque


@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Filtra o cliente pelo CPF

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")  # Mensagem se o cliente não for encontrado
        return

    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio(tipo_transacao="saque"):
        tem_transacao = True
        extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    print(extrato)  # Exibe o extrato da conta
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")  # Exibe o saldo da conta
    print("==========================================")


@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Filtra o cliente pelo CPF

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")  # Mensagem se já existir cliente com o CPF informado
        return

    nome = input("Informe o nome completo: ")  # Solicita o nome completo do cliente
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")  # Solicita a data de nascimento do cliente
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")  # Solicita o endereço do cliente

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)  # Cria um novo cliente

    clientes.append(cliente)  # Adiciona o cliente à lista de clientes

    print("\n=== Cliente criado com sucesso! ===")  # Mensagem de sucesso ao criar o cliente


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Filtra o cliente pelo CPF

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")  # Mensagem se o cliente não for encontrado
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)  # Cria uma nova conta corrente para o cliente
    contas.append(conta)  # Adiciona a conta à lista de contas
    cliente.contas.append(conta)  # Adiciona a conta à lista de contas do cliente

    print("\n=== Conta criada com sucesso! ===")  # Mensagem de sucesso ao criar a conta


def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))  # Lista todas as contas existentes


def main():
    clientes = []  # Inicializa a lista de clientes
    contas = []  # Inicializa a lista de contas

    while True:
        opcao = menu()  # Exibe o menu e obtém a opção escolhida pelo usuário

        if opcao == "d":
            depositar(clientes)  # Chama a função de depósito

        elif opcao == "s":
            sacar(clientes)  # Chama a função de saque

        elif opcao == "e":
            exibir_extrato(clientes)  # Chama a função de exibir extrato

        elif opcao == "nu":
            criar_cliente(clientes)  # Chama a função de criar novo cliente

        elif opcao == "nc":
            numero_conta = len(contas) + 1  # Define o número da nova conta
            criar_conta(numero_conta, clientes, contas)  # Chama a função de criar nova conta

        elif opcao == "lc":
            listar_contas(contas)  # Chama a função de listar contas

        elif opcao == "q":
            break  # Encerra o loop se a opção for 'q' (sair)

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")  # Mensagem se a opção for inválida


main()  # Chama a função principal para iniciar a aplicação
