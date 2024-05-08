'''
Parâmetros especiais - Por padrão, argumentos podem ser passados para uma função
Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade
e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados,
assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se 
os itens são passados por posição, por posição e nome, ou por nome.

link util - https://www.dio.me/articles/parametros-especiais-de-funcoes-em-python-de-forma-mais-simples
'''

# def criar_carro (modelo, ano, placa, /, marca, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)

# print(criar_carro('Palio', 1999, 'ABC-1234', marca ='Fiat', motor= '1.0', combustivel='Gasolina')) # Válido

# Invalida pq ja começa passando o nomeado, antes da barra '/' é obrigado ser so por posição
# criar_carro(modelo='Palio',  ano= 1999, placa= 'ABC-1234', marca ='Fiat', motor= '1.0', combustivel='Gasolina') # Inválido



'''
Keyeord only - Definindo parâmetros especiais somente por nome
'''

# def criar_carro (*, modelo, ano, placa, marca, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)

# criar_carro(modelo='palio', ano= 1999, placa= 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina') # Válido

# criar_carro('palio', 1999, 'ABC-1234', 'marca=fiat', motor='1.0', combustivel='Gasolina') # inválido


'''
Keyword and positional only 
'''
# def criar_carro (modelo, ano, placa, /, *, marca, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)

# criar_carro('Palio', 1999, 'ABC - 1234', marca= 'Fiat', motor='1.0', combustivel='Gasolina') # válido

# criar_carro(modelo= 'Palio', ano= 1999, placa= 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina') # inválido


# Mais uma variação do hibrido, quando o  argumento estiver '/' e '*' ele vira opcional
def criar_carro (modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio', 1999, 'ABC-1234', 'fiat', motor='1.0', combustivel='Gasolina') # valido
criar_carro('Palio', 1999, 'ABC-1234', marca='fiat', motor='1.0', combustivel='Gasolina') # valido

# criar_carro(modelo = 'Palio', ano=1999, placa='ABC-1234', marca='fiat', motor='1.0', combustivel='Gasolina') # invalido

