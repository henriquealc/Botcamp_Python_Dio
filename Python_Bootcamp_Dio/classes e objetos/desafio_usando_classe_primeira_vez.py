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

b1 = bicicleta('azul', 'caloi', 1998, 500)

b1.buzinar()
b1.correr()
b1.parar()
print()
#  Como exibir os atributos da classe
print(b1.cor, b1.modelo, b1.ano, b1.valor)