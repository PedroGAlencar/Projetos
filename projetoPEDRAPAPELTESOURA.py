import random

jogada = input('Escolha entre pedra,papel ou tesoura: ').lower()

jogada_cpu = ('pedra','papel','tesoura')
escolha = random.choice(jogada_cpu)

if jogada == 'pedra':
    if escolha == 'pedra':
        print(f'A CPU escolheu {escolha}')
        print('O jogo empatou')
    elif escolha == 'papel':
        print(f'A CPU escolheu {escolha}')
        print('A CPU ganhou')
    else:
        print(f'A CPU escolheu {escolha}')
        print('Você ganhou')
elif jogada == 'papel':
    if escolha == 'pedra':
        print(f'A CPU escolheu {escolha}')
        print('Você ganhou!')
    elif escolha == 'papel':
        print(f'A CPU escolheu {escolha}')
        print('O jogo empatou')
    else:
        print(f'A CPU escolheu {escolha}')
        print('A CPU ganhou')
else:
    if escolha == 'pedra':
        print(f'A CPU escolheu {escolha}')
        print('A CPU  ganhou')
    elif escolha == 'papel':
        print(f'A CPU escolheu {escolha}')
        print('Você ganhou!')
    else:
        print(f'A CPU escolheu {escolha}')
        print('O jogo empatou')