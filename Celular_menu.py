from time import sleep as atrasar
bloquear = 3
vida = 3

print(' Loading...')
atrasar(2)
while True:
    menu = '''
        Digite a opção desejada:
        1 - Cadastrar senha
        2 - Entrar
        0 - Sair do programa
'''
    print(menu)
    opcao = int(input(':'))
    if opcao == 1:
        senha = int(input('Digite a senha do seu celular(6 digitos) :'))
        if len(str(senha)) > 6:
            print('Passou da quantidade de dígitos')
            continue
        confirmar = int(input('Digite a senha do seu celular novamente:'))
        if len(str(confirmar)) > 6:
            print('Passou da quantidade de dígitos')
            continue
        elif senha == confirmar :
            print(f'Senha cadastrada!!!')
            continue
        else:
            print('As senhas estão diferentes')
    elif opcao == 2:
        for tentativa in range(3):
            tentativa = int(input('Digite sua senha:'))
            if tentativa == senha:
                print('Seja bem vindo!')
                break
            elif tentativa != senha:
                vida -= 1
                print(f'Voce tem mais {vida} chances')
                if vida == 0:
                    print('Seu celular ta bloqueado por 30 segundos')
                    for contagem in range(30,0,-1):
                        atrasar(1)
                        print(contagem)
    elif opcao == 0:
        print('Saindo do programa...')
        break

    
   
    
    
