arquivo = open('Python_Bootcamp_Dio\Manipulação de Arquivo\lorem.txt', 'r')

# Ler todo o conteudo de uma vez so
print(arquivo.read())

# # Traz uma linha por vez
print(arquivo.readline())

# #Lendo e imprimindo todas as linhas do arquivo como uma lista de string e retorna uma lista
print(arquivo.readlines())

# # Melhor maneira de usar o readline()
for linha in arquivo.readlines():
    print(linha)


# # tip
# # Usando um loop while para ler e imprimir todas as linhas do arquivo,
# # enquanto houver linhas para ler (o comprimento de linha não é zero).
while len(linha := arquivo.readline()):
    print(linha)


# # Fechando o arquivo após o uso
arquivo.close()