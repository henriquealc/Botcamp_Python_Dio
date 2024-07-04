from pathlib import Path


# Obtendo o diretório atual do script Python
ROOT_PATH = Path(__file__).parent


try:
    # Tentando abrir o arquivo 'alterado.txt' no diretório 'novo-diretorio' para leitura ('r')
    arquivo = open(ROOT_PATH / 'novo-diretorio' / 'alterado.txt', 'r')

except FileNotFoundError as exc: 
    # Se ocorrer um FileNotFoundError (arquivo não encontrado), exibir uma mensagem específica
    print('arquivo não encontrado!')
    print(exc) # Exibi os detalhes da exeção

except IsADirectoryError as exc:
    # Se ocorrer um IsADirectoryError (tentativa de abrir um diretório como arquivo), exibir uma mensagem específica
    print(f'Não foi possivel abrir o arquivo: {exc}')

except IOError as exc:
    # Se ocorrer um IOError (erro genérico de E/S), exibir uma mensagem específica
    print(f'Erro ao abrir o arquivo: {exc}')

except Exception as exc:
    # Se ocorrer qualquer outra exceção não tratada, exibir uma mensagem genérica
    print(f'Algum problema ocorreu ao tentar abir o arquivo.')



# O código abaixo está comentado, mas parece que estava destinado a tentar abrir o diretório 'novo-diretorio'.
# No entanto, diretórios não podem ser abertos da mesma forma que arquivos.
# Se esse trecho fosse descomentado, provavelmente geraria um IsADirectoryError.
# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")