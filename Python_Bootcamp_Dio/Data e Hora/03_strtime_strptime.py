from datetime import datetime

# Obtém a data e hora atuais
data_hora_atual = datetime.now()

# Define uma string contendo uma data e hora específicas
data_hora_str = '2023-10-20 10:35'

mascara_ptbr = '%d/%m/%Y %a' # Formato brasileiro: dia/mês/ano dia_da_semana
mascara_en = '%Y-%m-%d %H:%M' # Formato inglês: ano-mês-dia hora:minuto



# Imprime a data atual formatada no formato brasileiro definido pela máscara_ptbr
print(data_hora_atual.strftime(mascara_ptbr)) # Retorna o data em formato do Brasil


# Converte a string data_hora_str para o formato datetime usando a máscara_en
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
# print(data_convertida.strftime('%Y')) # Informa só o ano da data convertida

# Imprime o tipo da variável data_convertida (deve ser datetime)
print(type(data_convertida))