import random
num = random.randint(1,20)
palpite = 0
tentativa = 5
while palpite != num :
    palpite = int(input('Tente acertar o número que o computador pensou de 1 a 20:'))
    if palpite == num:
        print(f'Parabéns você acertou é o {num}!')
    elif palpite > num:
        print(f'Você errou o número é mais baixo que {palpite}')
        tentativa -= 1
        print(f'Faltam {tentativa} vidas')
        if tentativa == 0:
            print('Fim de jogo suas vidas chegaram a zero')
            break
    else:
        print(f'Você errou o número é mais alto que {palpite}')
        tentativa -= 1
        print(f'Faltam {tentativa} vidas')
        if tentativa == 0:
            print('Fim de jogo suas vidas chegaram a zero!')
            break