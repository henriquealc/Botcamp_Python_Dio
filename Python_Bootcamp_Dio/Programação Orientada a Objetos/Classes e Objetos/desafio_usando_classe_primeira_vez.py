'Ex do uso de Orientação objeto'

# class cachorro:
#     def __init__(self, nome, cor, acordado=True):
#         self.nome = nome
#         self.cor = cor
#         self.acordado = acordado

#     def latir(self):
#         print('Auau')

#     def dormir(self):
#         self.acordado = False
#         print('Zzzzz...')

# cao_1 = cachorro('Chappie', 'amarelo', False)
# cao_2 = cachorro('Aladim', 'branco e preto')

# cao_1.latir() 

# # print(cao_1.acordado)

# print(cao_2.acordado)
# cao_2.dormir() # Zzzzz...
# print(cao_2.acordado)


# Desafio proposto pelo professor

class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    
    def buzinar(self):
        print('Bibi...')
    
    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada!')

    def correr(self):
        print('Vrummm...')

    # def __str__(self):
    #     return f'Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}'

    # Faz a mesma coisa que o código acima, porem é o mais recomendado
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = bicicleta('azul', 'caloi', 1998, 500)

b1.buzinar()
b1.correr()
b1.parar()
print()
#  Como exibir os atributos da classe
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bicicleta('vermelha', 'monark', 2000, 189)
b2.buzinar() # ou bicicleta.buzinar(b2)
print(b2.cor)
print(b2) # Exibindo os valores que estão dentro da classe bicicleta
