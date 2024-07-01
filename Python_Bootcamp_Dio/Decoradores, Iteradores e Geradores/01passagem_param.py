# Definindo a primeira função 'mensagem'
def mensagem(nome):
    print('executando nome') # Imprime uma mensagem indicando que a função está sendo executada
    return f'Oi {nome}' # Retorna uma mensagem de cumprimento usando o nome fornecido

# Definindo a segunda função 'mensagem_longa'
def mensagem_longa(nome):
    print('executando mensagem longa') # Imprime uma mensagem indicando que a função está sendo executada
    return f'Olá tudo bem com você {nome}?' # Retorna uma mensagem de cumprimento mais longa usando o nome fornecido

# Definindo a função 'executar' que recebe outra função 'funcao' como entrada junto com 'nome'
def executar(funcao, nome):
    print('executando executar') # Imprime uma mensagem indicando que a função está sendo executada
    return funcao(nome) # Chama a função fornecida 'funcao' com o 'nome' fornecido e retorna o resultado

# Chamando 'executar' com a função 'mensagem' e 'José' como argumento de nome
print(executar(mensagem, 'Josè')) # Saída: Oi José
print('=-' * 25)

# Chamando 'executar' com a função 'mensagem_longa' e 'José' como argumento de nome
print(executar(mensagem_longa, 'Josè')) # Saída: Olá tudo bem com você, José?
