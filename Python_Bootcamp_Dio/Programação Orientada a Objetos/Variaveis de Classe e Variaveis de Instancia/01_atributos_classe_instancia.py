class Estudante:
    # Variável de classe que armazena o nome da escola (compartilhada por todas as instâncias da classe)
    escola = 'DIO' # Variavel de Classe

    # Método inicializador (construtor) da classe
    def __init__(self, nome, matricula): # nome e matricula são variaveis de instância
        # Atributos de instância: nome e matrícula específicos para cada objeto Estudante
        self.nome = nome
        self.matricula = matricula

    # Método para retornar uma representação em string do objeto
    def __str__(self) -> str:
        # Retorna uma string formatada com nome, matrícula e o nome da escola (variável de classe)
        return f"{self.nome} - {self.matricula} - {self.escola}"

# Função para mostrar os valores dos objetos
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# Criando e imprimindo objetos da classe Estudante
# Cada objeto é inicializado com um nome e uma matrícula específicos   
aluno_1 = Estudante(nome = 'Henrique', matricula=54893)
aluno_2 = Estudante('Jose', 48965)
mostrar_valores(aluno_1, aluno_2)

print('=' * 30)

# Alterando o valor da variável de classe escola para 'Python'
Estudante.escola = 'Python'

# Criando um novo objeto Estudante com a nova escola
aluno_3 = Estudante('Isabella', 45678)
mostrar_valores(aluno_1, aluno_2, aluno_3)

