from abc import ABC, abstractmethod, abstractproperty

# Definição da classe abstrata ControleRemoto que herda de ABC (Abstract Base Class)
class ControleRemoto(ABC):
 
    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def ligar(self):
        pass

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod # Obriga ter este metodo em todas as classes herança
    def desligar(self):
        pass

    # Método não abstrato (pode ser sobrescrito ou herdado)
    def mudar_canal(self):
        pass

    # Propriedade abstrata que deve ser implementada pelas subclasses
    @property
    @abstractmethod
    def marca(self):
        pass

# Classe que herda de ControleRemoto, implementando seus métodos abstratos
class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando TV...')
        print('Ligada!')

    def desligar(self):
        print('Desligando AR...')
        print('AR Desligado!')
    
    def mudar_canal(self):
        print('Mundando Canal...')
        print('Canal alterado!')

    # Implementação da propriedade marca
    @property
    def marca(Self):
        return 'SAMSUNG'

# Classe que herda de ControleRemoto, implementando seus métodos abstratos
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o AR...')
        print('AR Ligado!')

    def desligar(self):
        print('Desligando AR...')
        print('AR Desligado!')

    # Implementação da propriedade marca
    @property
    def marca(self):
        return 'LG'
    

# Instanciando um ControleTV e testando seus métodos
controle = ControleTV()
controle.ligar()
controle.desligar()
controle.mudar_canal()
print(controle.marca)

print()

# Instanciando um ControleArCondicionado e testando seus métodos
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)