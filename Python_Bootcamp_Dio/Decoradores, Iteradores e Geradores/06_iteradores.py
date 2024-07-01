# Definindo a classe MeuIterador
class MeuIterador:
    # Método inicializador (__init__) que recebe uma lista de números como argumento
    def __init__(self, numeros: list[int]):
        self.numeros = numeros  # Atributo para armazenar a lista de números
        self.contador = 0 # Atributo para manter o controle do índice atual

    # Método especial __iter__ que retorna o próprio objeto (iterador)
    def __iter__(self):
        return self
    
    # Método especial __next__ que define o comportamento para obter o próximo elemento no iterador
    def __next__(self):
        try:
            # Obtém o próximo número da lista e o multiplica por 2
            numero = self.numeros[self.contador] * 2
            self.contador += 1 # Incrementa o contador para apontar para o próximo número
            return numero * 2 # Retorna o número multiplicado por 2 novamente
        except IndexError:
            # Se alcançarmos o final da lista, levantamos StopIteration para indicar o término do iterador
            raise StopIteration

# Criando uma instância da classe MeuIterador com uma lista de números
# A iteração ocorrerá automaticamente devido à implementação dos métodos __iter__ e __next__
for i in MeuIterador(numeros = [12,44,77,22]):
    print(i)# Imprime cada elemento produzido pelo iterador