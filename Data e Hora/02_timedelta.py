# Importa as classes datetime e timedelta do módulo datetime
from datetime import datetime, timedelta, date


# Define o tipo de carro como 'P' (pequeno), convertido para maiúsculas com .upper()
tipo_carro = 'p'.upper() # P - pequeno, M - médio, G - grande


# Define os tempos estimados em minutos para cada tipo de carro
tempo_pequeno = 30 
tempo_medio = 2245
tempo_grande = 60

# Obtém a data e hora atuais
data_atual = datetime.now() # Retorna data e hora atual


# Verifica o tipo de carro e calcula a data estimada de conclusão
if tipo_carro == 'P':
    # Se o tipo de carro é 'P' (pequeno), adiciona tempo_pequeno dias à data atual
    # data_estimada = data_atual + timedelta(days=tempo_pequeno) # alterando para dias o tempo estimado
    
    # Se o tipo de carro é 'P' (pequeno), adiciona tempo_pequeno minutos à data atual
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou as {data_atual} e ficará pronto ás {data_estimada}')
elif tipo_carro == 'M':
    # Se o tipo de carro é 'M' (pequeno), adiciona tempo_pequeno minutos à data atual
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou as {data_atual} e ficará pronto ás {data_estimada}')
else:
    # Se o tipo de carro é 'G' (pequeno), adiciona tempo_pequeno minutos à data atual
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou as {data_atual} e ficará pronto ás {data_estimada}')


# Exemplo de decrementação
# Decrementa apenas 1 dia do dia atual
print(date.today() - timedelta(days=1))


# Decrementa 1 hora da data e horario que foi passado
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time()) # Pega apenas a parte de horas


# Pega apenas a parte da data atual
print(datetime.now().date())