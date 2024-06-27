# Definição da classe base Passaro
class Passaro:
    def voar(self):
        print('Voando...') # Método voar da classe base que imprime 'Voando...'


# Definição da classe Pardal que herda de Passaro
class Pardal(Passaro):
    def voar(self):
        # super().voar() # Pega o print da class Passaro e imprimi 'Voando...'
        print('Pardal pode voar') # Sobrescreve o método voar para imprimir 'Pardal pode voar'


# Definição da classe Avestruz que herda de Passaro
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar') # Sobrescreve o método voar para imprimir 'Avestruz não pode voar'


# FIXME: exemplo ruim do uso de herança para "ganhar" o método voar
# Definição da classe Aviao que herda de Passaro (exemplo ruim de uso de herança)
class Aviao(Passaro):
    def voar(self):
        print('Avião decolando...')


# Exemplo de Polimorfismo
# Função que demonstra polimorfismo ao chamar o método voar de diferentes objetos
def plano_voo(obj):
    obj.voar()


# Exemplos de uso da função plano_voo com diferentes tipos de passaros (e um avião)
plano_voo(Pardal()) # Chama voar() de Pardal, imprime 'Pardal pode voar'
plano_voo(Avestruz()) # Chama voar() de Avestruz, imprime 'Avestruz não pode voar'
plano_voo(Aviao()) # Chama voar() de Aviao, imprime 'Avião decolando...'