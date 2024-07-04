from pathlib import Path


# Obtendo o diretório atual do script Python
ROOT_PATH = Path(__file__).parent


# Abrindo o arquivo 'lorem.txt' em modo de leitura ('r') e fechando manualmente com close()
arquivo = open(ROOT_PATH / 'lorem.txt', 'r')
print(arquivo.read()) # Mostra o conteúdo do arquivo
arquivo.close() # Usando o 'close' para fechar o arquivo manualmente



# Verificando se o arquivo foi aberto corretamente antes de
# executar operações de leitura ou gravação nele.
try:    
    with open(ROOT_PATH / 'lorem.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo {exc}')



# Abrindo o arquivo 'lorem.txt' usando 'with' para garantir que seja fechado automaticamente
with open(ROOT_PATH / 'lorem.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


# Tentando escrever em um arquivo novo ('arquivo-utf-8.txt') com encoding UTF-8
try:
    with open(ROOT_PATH / 'arquivo-utf-8.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Aprendendo a manipular arquivos utilizando Python.')
except IOError as exc:
    print(f'Erro ao abrir o arquivo {exc}')



# Tentando ler um arquivo ('arquivo-utf-8.txt') com encoding ASCII, que causará UnicodeDecodeError
try:
    with open(ROOT_PATH / 'arquivo-utf-8.txt', 'r', encoding='ascii') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo {exc}')
except UnicodeDecodeError as exc:
    print(exc)