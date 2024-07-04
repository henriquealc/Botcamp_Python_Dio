# Exemplos de abertura e fechamento de arquivos

# Para ler o arquivo
file = open('example.txt', 'r')
#.... Fazemos algo com o arquivo ...
file.close() # Fecha o arquivo, todo arquivo que for aberto deve ser fechado

# Para escrever em um arquivo
file = open('example.txt', 'w')

# Para anexar contéudo a um arquivo existente
file = open('example.txt', 'a')