import time

def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        return 'Erro! Divisão por zero.'
    else:
        return a / b

while True:
    print('Olá! Bem vindo a sua calculadora virtual!!!!')
    time.sleep(0.5)

    menu = int(input(''' Escolha sua opção...
                     (0)Para sair da calculadora
                     (1)Para iniciar a calculadora
                     
                     :'''))
    if menu == 0:
        break
    elif menu != 0 and menu != 1:
        print('ERROR ' * 20)
        time.sleep(0.3)
        print('loading'+'...')
        time.sleep(1)
        continue
    else:
      while True:
        opcao = int(input('''Escolha a operação:
                          (0)Voltar ao menu
                          (1)Soma
                          (2)Subtração
                          (3)Multiplicação
                          (4)Divisão
                          :'''))
        if opcao > 4 :
            print('Número inválido!')
            time.sleep(0.5)
            continue
        elif opcao == 0:
            break
        a = int(input('Digite um número:'))
        b = int(input('Digite outro número:'))
        if opcao == 1:
            resultado = somar(a, b)
            print('O resultado da soma é:', resultado)
        elif opcao == 2:
            resultado = subtrair(a, b)
            print('O resultado da subtração é:', resultado)
        elif opcao == 3:
            resultado = multiplicar(a, b)
            print('O resultado da multiplicação é:', resultado)
        elif opcao == 4:
            resultado = dividir(a, b)
            print('O resultado da divisão é:', resultado)
        