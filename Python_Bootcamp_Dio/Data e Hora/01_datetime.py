# import datetime
from datetime import date, datetime, time # Forma mais usada

# data = datetime.date(2023, 7, 10)
data = date(2023, 7, 10)
print(data)

print(date.today()) # Retorna a data que foi passada '10-07-2023'


# Exemplo feito por mim, so funciona se descomentar o 'import datetime'
# data_hora_atual = datetime.datetime.now()
# data_hora = data_hora_atual.strftime('%A %D %B %Y %I:%M') # Formata e imprimi o dia da semana, data, mês e minutos
# print(data_hora)


data_hora = datetime(2023, 7, 10) # Nesse formato hora e minutos ficam zerados, hora e minutos são opcionais
data_hora = datetime(2023, 7, 10, 12, 15, 25) 
print(data_hora)
print(datetime.today()) # Retorna a data, hora, minutos e segundos atual


# Retorna a hora
hora = time(10, 20, 58)
print(hora)
