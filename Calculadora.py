from time import sleep
resultado = 0
def soma(a, b):
    global resultado
    resultado = a + b
    return resultado
    
def subtrair(a, b):
    global resultado
    resultado = a - b
    return resultado
    
def multiplicar(a, b):
    global resultado
    resultado = a * b
    return resultado

def dividir(a, b):
    global resultado
    if b == 0:
        return 'ERRO: NÃO É POSSÍVEL DIVISÃO POR ZERO!'
    resultado = a / b
    return resultado

print('-=' * 10)
print(f'{'\033[35m'}{'CALCULADORA':^20}{'\033[m'}')
print('-' * 20)
while True: 
    n1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
    n2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
    print('[ \033[32m+\033[m ] SOMA\n[ \033[31m-\033[m ] SUBTRAÇÃO\n[ \033[36m*\033[m ] MULTIPLICAÇÃO\n[ \033[33m/\033[m ] DIVISÃO')
    operador = str(input('SUA RESPOSTA: ')).upper().strip()
    if operador == '+' or operador == 'SOMA' or operador == 'ADIÇÃO':
        print(f'O RESULTADO É: {soma(n1, n2)}')
    if operador == '-' or operador == 'DIMINUIR' or operador == 'SUBTRAÇÃO':
        print(f'O RESULTADO É: {subtrair(n1, n2)}')
    if operador == '*' or operador == 'MULTIPLICAR' or operador == 'MULTIPLICAÇÃO':
        print(f'O RESULTADO É: {multiplicar(n1, n2)}')
    if operador == '/' or operador == 'DIVIDIR' or operador == 'DIVISÃO':
        print(f'O RESULTADO É: {dividir(n1, n2)}')
    print('-' * 10)
    print('CURIOSIDADES SOBRE O RESULTADO:')
    if resultado > 0:
        if resultado != int(resultado):
            print('é um número DECIMAL')
        else:
            print('- Ele é um número INTEIRO')
        print('- é um número POSITIVO')
        if resultado % 2 == 0:
            print('- é um número PAR')
        else: 
            print('- é um número IMPAR')
    elif resultado <= -1:
        if resultado != int(resultado):
            print('é um número DECIMAL')
        else:
            print('- Ele é um número INTEIRO')
        print('- Ele é um número NEGATIVO')
        if resultado % 2 == 0:
            print('- é um número PAR')
        else:
            print('é um número IMPAR')
    voltar = str(input('Quer fazer outro cálculo[S/N]? ')).upper().strip()[0]
    if voltar == 'N':
        break
print('ENCERRANDO PROGRAMA...')
sleep(2)
