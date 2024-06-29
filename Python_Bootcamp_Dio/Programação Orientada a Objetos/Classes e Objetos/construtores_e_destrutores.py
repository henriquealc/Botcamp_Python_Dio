class cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo a instância da classe.')

    def falar(self):
        print('AUAUA')


def criar_cachorro():
    c = cachorro('Zeus', 'Branco e preto', False)
    print(f'{c.nome}, {c.cor}')


c = cachorro('Charppie', 'amarelo')
c.falar()

c2 = cachorro('Mag', 'branca', True)
c2.falar()

# criar_cachorro() # Executa o metódo

print('Ola mundo!')
del c
# c.falar() # Não funciona mais pos o del deletou
print('Ola mundo!')
print('Ola mundo!')
print('Ola mundo!')