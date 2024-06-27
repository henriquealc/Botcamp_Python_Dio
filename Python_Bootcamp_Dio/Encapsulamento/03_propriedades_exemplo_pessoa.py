class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome # Atributo privado _nome
        self._ano_nascimento = ano_nascimento # Atributo privado _ano_nascimento

    @property
    def nome(self):
        return self._nome # Getter para atribuit _nome
    
    @property
    def idade(self):
        _ano_atual = 2024 # Ano atual usado para calcular a idade
        return _ano_atual - self._ano_nascimento # Calcula a idade com base no ano_nascimento


# Cria uma instancia da classe pessoa com o nome "Henrique" e ano de nascimento 2001
pessoa = Pessoa("Henrique", 2001)

# Imprimindo o nome e a idade da pessoa
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}')
    