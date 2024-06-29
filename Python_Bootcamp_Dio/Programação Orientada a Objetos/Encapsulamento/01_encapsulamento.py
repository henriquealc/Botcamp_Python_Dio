class Conta:
    def __init__(self,nro_agencia, saldo = 0):
        self._saldo = saldo # Com o underline na frente vira uma variavel PRIVADA
        self.nro_agencia = nro_agencia # Atributo público

    def depositar(self, valor):
        # Método para depositar dinheiro na conta
        self._saldo += valor

    def sacar(self, valor):
        # Método para sacar dinheiro na conta
        self._saldo -= valor

    def mostra_saldo(self):
        # Método para retornar o saldo atual da conta
        return self._saldo

# Criando uma instancia da classe Conta
conta = Conta('0001', 1000)
# print(conta._saldo) # NÃO É INDICADO FAZER DESTA MANEIRA

# Exemplo de uso dos métodos da Classe
conta.depositar(2000)
conta.sacar(500)

# Acessando atributos públicos
print("Número da Agência: ", conta.nro_agencia)

# Acessando o saldo através de um método público
print("Saldo atual: ", conta.mostra_saldo())