# Abrindo (ou criando, se não existir) o arquivo 'teste.txt' em modo de escrita ('w')
arquivo = open('Python_Bootcamp_Dio\Manipulação de Arquivo/teste.txt', 'w')

# Escrevendo uma string no arquivo
arquivo.write('Escrevendo dados em um novo arquivo.')

# Escrevendo várias linhas no arquivo usando writelines()
# Cada string na lista será escrita como uma linha separada no arquivo
arquivo.writelines(['\n', 'escrevendo', '\num', '\nnovo', '\ntexto'])

# Fechando o arquivo após a escrita
arquivo.close()