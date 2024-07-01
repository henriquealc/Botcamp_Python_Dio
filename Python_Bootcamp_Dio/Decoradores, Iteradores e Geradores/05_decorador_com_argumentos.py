# Definição do decorador 'meu_decorador', que recebe uma função 'funcao' como argumento
def meu_decorador(funcao):
    # Definição da função interna 'envelope', que será retornada como decorador
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar') # Imprime uma mensagem antes de executar a função decorada
        funcao(*args, *kwargs) # Chama a função original que foi decorada, passando argumentos posicionais e nomeados
        print('Faz algo antes de executar') # Imprime uma mensagem após executar a função decorada
    return envelope # Retorna a função interna 'envelope' como o decorador

# Usando o decorador '@meu_decorador' para decorar a função 'ola_mundo'
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f'ola_mundo {nome}!') # Mensagem da função 'ola_mundo'

# Chamando a função decorada 'ola_mundo', que agora possui o comportamento do decorador 'meu_decorador'
ola_mundo('José', 555)
