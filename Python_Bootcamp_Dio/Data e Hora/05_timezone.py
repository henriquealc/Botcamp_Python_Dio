from datetime import datetime, timezone, timedelta


# Obtém a data e hora atual no fuso horário de Oslo (UTC+2)
data_oslo = datetime.now(timezone(timedelta(hours=2)))


# Obtém a data e hora atual no fuso horário de São Paulo (UTC-3)
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))


# Imprime as datas e horas obtidas
print(data_oslo)
print(data_sao_paulo)