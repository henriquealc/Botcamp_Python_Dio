# : Crie uma Função: recomendar_plano para receber o consumo médio mensal:

def recomendar_plano(consumo):
# : Crie uma Estrutura Condicional para verifica o consumo médio mensal
  if consumo <= 10:
    return 'Plano Essencial Fibra - 50 Mbps'
  elif consumo <= 20:
    return 'Plano Prata Fibra - 100 Mbps'
  else:
    return 'Plano Premium Fibra - 300 Mbps'


# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input('Insira o consumo mendio mensal de dados: '))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))