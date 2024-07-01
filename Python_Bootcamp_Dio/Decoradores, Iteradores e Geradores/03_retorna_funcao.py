def calculadora(operacao):
    def soma(a,b):
        return a + b

    def sub (a,b):
        return a - b
    
    def multi (a,b):
        return a * b
    
    def div (a,b):
        return a / b
    
    # Outra forma de condição
    match operacao:
        case '+':
            return soma
        case '*':
            return multi
        case '-':
            return sub   
        case '/':
            return div

# print(calculadora('+')(5, 5))
# print(calculadora('-')(5, 5))
# print(calculadora('*')(5, 5))
# print(calculadora('/')(5, 5))

# Outra maneira
op = calculadora('+')
print('soma:',op(2, 2))
op = calculadora('-')
print('subtração:',op(2, 2))
op = calculadora('*')
print('multiplicação:',op(2, 2))
op = calculadora('/')
print('divisão:',op(2, 2))