# # Definição da função geradora 'meu_gerador', que recebe uma lista de inteiros 'numeros' como argumento
# def meu_gerador(numeros: list[int]):
#     # Itera sobre cada elemento da lista 'numeros'
#     for numero in numeros:
#        # Yield é usado para retornar o valor do número multiplicado por 2
#         yield numero * 2

# # Itera sobre os valores gerados pela função geradora 'meu_gerador' com a lista [1, 2, 3] como entrada
# for i in meu_gerador(numeros=[1, 2, 3]):
#     print(i) # Imprime cada valor gerado pelo gerador




'''Outro exemplo de como usar gerador'''
import requests # Importa o módulo requests, que permite fazer requisições HTTP em Python

# Definição da função geradora 'fetch_products', que recebe uma URL da API e um número máximo de páginas para buscar produtos
def fetch_products(api_url, max_pages= 100):
    page = 1# Inicializa a variável 'page' para começar da página 1
    while page <= max_pages:# Loop while para iterar até o número máximo de páginas especificado
        # Faz uma requisição GET para a API com a URL da página atual
        response = requests.get(f'{api_url}?page={page}')
        data = response.json() # Converte a resposta da API para JSON
        for product in data['products']: # Itera sobre cada produto encontrado na resposta da API
            yield product # Utiliza 'yield' para retornar cada produto como resultado da função geradora
        if 'next_page' not in data: # Verifica se há uma próxima página na resposta da API
            break # Se não houver próxima página, interrompe o loop
        page += 1 # Incrementa o número da página para buscar a próxima página de produtos

# Uso do gerador 'fetch_products' para obter e imprimir o nome de cada produto
for product in fetch_products('http://api.example.com/products'):
    print(product['name']) # Imprime o nome de cada produto obtido através do gerador