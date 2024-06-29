class Pessoa:
    def __init__(self, nome= None, idade= None):
       # Método inicializador (construtor) da classe Pessoa
        self.nome = nome # Atributo de instância: nome da pessoa
        self.idade = idade # Atributo de instância: idade da pessoa

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
         # Método de classe para criar uma instância de Pessoa a partir de data de nascimento
        idade = 2024 - ano  # Calcula a idade com base no ano de nascimento fornecido
        return cls(nome, idade)  # Retorna uma nova instância de Pessoa com o nome e a idade calculada
    
    @staticmethod
    def e_maior_idade(idade):    
        # Método estático para verificar se uma pessoa é maior de idade
        return idade >= 18  # Retorna True se a idade fornecida for maior ou igual a 18, caso contrário False


# Criando uma instância de Pessoa usando o método de classe criar_de_data_nascimento
p = Pessoa.criar_de_data_nascimento(2001, 11, 27, "Henrique")
print('Nome:', p.nome, '- Idade:', p.idade) # Imprime o nome e a idade da pessoa criada

print()

# Chamando o método estático e_maior_idade para verificar se uma idade é maior de 18 anos
print(Pessoa.e_maior_idade(18)) # Deve imprimir True, pois 18 é maior ou igual a 18
print(Pessoa.e_maior_idade(8)) # Deve imprimir False, pois 8 não é maior ou igual a 18

