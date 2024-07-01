# class Foo:
#     def __init__(self, x= None):
#         self._x = x # Inicializa o atributo privado _x com o valor passado como argumento

#     @property
#     def x(self):
#         return self._x or 0 # Getter da propriedade x, retorna o valor de _x se não for None, caso contrário retorna 0
    
#     @x.setter
#     def x(self, value):
#         self._x += value # Setter da propriedade x, incrementa o valor de _x com o valor passado como argumento

#     @x.deleter
#     def x(self):
#         self._x = -1 # Deleter da propriedade x, define o valor de _x como -1 quando a propriedade é deletada

# # Criando uma instância da classe Foo com x inicializado como 10
# foo = Foo(10)
# print(foo.x) # Acessando o valor de x através da propriedade x

# print()

# # Modificando o valor de x através da propriedade x
# foo.x=10
# print(foo.x)  # Saída: 20 (10 + 10)

# print()

# del foo.x # Deletando o valor de x utilizando o deleter da propriedade x
# print(foo.x) # Saída: -1 (valor definido pelo deleter)

# TODO: Crie uma classe UsuarioTelefone.  
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
      self._nome = nome
      self._numero = numero
      self._plano = plano
    
        
    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    @property
    def nome(self):
      return self._nome
    
    @property 
    def numero(self):
      return self._numero
    
    @property
    def plano(self):
      return self._plano

    
    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = str(input())  
numero = str(input())  
plano = str(input())  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)