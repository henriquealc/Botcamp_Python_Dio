def principal():
    print('Executando a função principal')

    def funcao_internar():
        print('Executando á função interna')

    def funcao_2():
        print('Executando a função 2')

    funcao_internar()
    funcao_2

principal()