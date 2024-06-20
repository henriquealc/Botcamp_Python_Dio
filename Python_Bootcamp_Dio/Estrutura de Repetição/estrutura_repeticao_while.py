'''While - Usado para repetir um bloco de código
várias vezes. Faz sentido usar while quando não sabemos o número exato
de vezes que nosso bloco de código deve ser executado.'''

# opcao = -1

# while opcao != 0:
#     opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair: "))
#     if opcao == 1:
#         print("Sacando...")
#         print()
#     elif opcao == 2:
#         print('Extrato...')
#         print()
# else:
#     print('Obrigado por usar nosso sistema bancário, até logo!')





'''Uso do "break"'''

# while True:
#     numero = int(input("Informe um número: "))
#     if numero == 10:
#         print('Programa encerrado!')
#         break
#     print(numero)



'''Uso do break com for'''

# for numero in range(100):
#     if numero == 10: # quando não quero exibir o numero 10
#         continue
#     elif numero == 50:
#         break
#     print(numero, end=' ')





'''Usando o "continue" para mostrar os números pares IMPARES'''
for numero in range(100): 
    if numero % 2 == 0:
        continue
    print(numero, end=' ')