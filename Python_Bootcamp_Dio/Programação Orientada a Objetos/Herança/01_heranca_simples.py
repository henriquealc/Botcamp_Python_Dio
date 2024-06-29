# Definição da classe base Veiculo
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor # Atributo para armazenar a cor do veículo
        self.placa = placa # Atributo para armazenar a placa do veículo
        self.numero_rodas = numero_rodas # Atributo para armazenar o número de rodas do veículo

    def ligar_motor(self):
        print("Ligando motor") # Método para ligar o motor do veículo

    # Método especial para retornar uma representação em string do objeto
    # Retorna o nome da classe e todos os atributos do objeto formatados como chave=valor
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    
# Classe motocicleta é filha de veiculo
class Motocicleta(Veiculo):
    pass # herda todos os atributos e métodos de Veiculo sem adicionar nada novo


# Classe Carro é filha de Veiculo
class Carro(Veiculo):
    pass # herda todos os atributos e métodos de Veiculo sem adicionar nada novo


# Classe Caminhao é filha de Veiculo
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        # Método inicializador de Caminhao, que recebe os parâmetros da classe base Veiculo e um novo parâmetro carregado
        super().__init__(cor, placa, numero_rodas) # Chama o inicializador da classe base Veiculo
        self.carregado = carregado # Atributo adicional para indicar se o caminhão está carregado ou não


    def esta_carregado(self):
        # Método específico de Caminhao para imprimir se o caminhão está carregado ou não
        print(f'{"Sim" if self.carregado else "Não estou carregado"}')


moto = Motocicleta("Preta", "ABC-1234", 2) # Instância de Motocicleta com cor, placa e número de rodas
# moto.ligar_motor()
# print(moto)

carro = Carro("Azul", "PFG-5547", 4) # Instância de Carro com cor, placa e número de rodas
# carro.ligar_motor()
# print(carro)

caminhao = Caminhao("Verde", "KKP-8756", 4, True) # Instância de Caminhao com cor, placa, número de rodas e estado de carregado
# caminhao.ligar_motor()
# caminhao.esta_carregado()

# Exemplos de uso dos métodos e impressão dos objetos
print(carro) # Imprime a representação em string do objeto Carro
print()
print(moto) # Imprime a representação em string do objeto moto
print()
print(caminhao) # Imprime a representação em string do objeto caminhao