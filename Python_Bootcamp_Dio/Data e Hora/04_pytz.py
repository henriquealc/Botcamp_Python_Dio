# pip install pytz # tem que instalar a biblioteca pelo prompt
import pytz
from datetime import datetime

# Obtém a data e hora atual no fuso horário do local informado
d = datetime.now(pytz.timezone("Europe/Madrid"))
d2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

# Formata a data e hora para uma string legível
data_formatada = d.strftime('%Y-%m-%d %H:%M:%S %Z%z')
data_formatada_2 = d2.strftime('%H:%M:%S %Z%z') # Exibi apenas o horario


print(d) # Imprimi o horario sem ta formatado
print(data_formatada)
print(data_formatada_2)