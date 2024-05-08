'''
Argumentos nomeados - Funções também podem ser chamadas usando argumentos
nomeados da forma chave= valor.
'''

def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca},{modelo}, {ano}, {placa}')


salvar_carro('fiat', 'palio', 1999, 'ABC-1234')
salvar_carro(marca= 'fiat', modelo= 'palio', ano= 1999, placa='ABC-1234') # melhor forma
salvar_carro(**{'marca': 'fiat', 'modelo': 'palio', 'ano': 1999, 'placa': 'ABC-1234'}) # Um diconario, vai converte com algo parecido com o de cima

