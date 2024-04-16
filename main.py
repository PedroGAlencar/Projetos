from palavras import *
import random
from time import sleep

frutas_aleatorias = random.choice(frutas)
comidas_aleatorias = random.choice(comidas)
esportes_aleatorios = random.choice(esportes)
profissoes_aleatorias = random.choice(profissoes)
objetos_aleatorios = random.choice(objetos)

letras_tentadas = []
vidas = 5

print('Carregando menu do jogo da forca...')
sleep(0.7)
print('Bem vindo ao jogo da forca!')
sleep(0.2)
menu = int(input('''
Escolha uma opção:
    [1] Frutas
    [2] Comidas
    [3] Esportes
    [4] Profissões
    [5] Objetos
    [0] Sair do jogo da forca
:'''))
while True:
    if menu == 1:
        letras_certas = [letra for letra in frutas_aleatorias.lower() if letra in letras_tentadas]
        if letras_certas == list(frutas_aleatorias.lower()):
            print(f'Parabéns você venceu! A palavra era {frutas_aleatorias}')
            break
        for letra in frutas_aleatorias:
            if letra.lower() in letras_tentadas:
                print(letra,end=' ')
            else:
                print('_',end = ' ')
        tentativa = input('Escolha uma letra pra advinhar: ')
        print(f'Letras tentadas:{letras_tentadas}')
        if tentativa.lower() not in frutas_aleatorias.lower():
            vidas -= 1
            print(f'Vidas = {vidas}')
            if vidas == 0:
                print('BLEM BLEM BLEM')
                sleep(0.3)
                print('Você Perdeu!!!')
                print(f'A palavra era {frutas_aleatorias}')
                break
        if len(tentativa) == 1:
            letras_tentadas.append(tentativa.lower())
        else:
            print('Só pode digitar uma letra!')
            continue
    elif menu == 2:
        letras_certas = [letra for letra in comidas_aleatorias.lower() if letra in letras_tentadas]
        if letras_certas == list(comidas_aleatorias.lower()):
            print(f'Parabéns você venceu! A palavra era {comidas_aleatorias}')
            break
        for letra in comidas_aleatorias:
            if letra.lower() in letras_tentadas:
                print(letra,end=' ')
            else:
                print('_',end = ' ')
        tentativa = input('Escolha uma letra pra advinhar: ')
        print(f'Letras tentadas:{letras_tentadas}')
        if tentativa.lower() not in comidas_aleatorias.lower():
            vidas -= 1
            print(f'Vidas = {vidas}')
            if vidas == 0:
                print('BLEM BLEM BLEM')
                sleep(0.3)
                print('Você Perdeu!!!')
                print(f'A palavra era {comidas_aleatorias}')
                break
        if len(tentativa) == 1:
            letras_tentadas.append(tentativa.lower())
        else:
            print('Só pode digitar uma letra!')
            continue
    elif menu == 3:
        letras_certas = [letra for letra in esportes_aleatorios.lower() if letra in letras_tentadas]
        if letras_certas == list(esportes_aleatorios.lower()):
            print(f'Parabéns você venceu! A palavra era {esportes_aleatorios}')
            break
        for letra in esportes_aleatorios:
            if letra.lower() in letras_tentadas:
                print(letra,end=' ')
            else:
                print('_',end = ' ')
        tentativa = input('Escolha uma letra pra advinhar: ')
        print(f'Letras tentadas:{letras_tentadas}')
        if tentativa.lower() not in esportes_aleatorios.lower():
            vidas -= 1
            print(f'Vidas = {vidas}')
            if vidas == 0:
                print('BLEM BLEM BLEM')
                sleep(0.3)
                print('Você Perdeu!!!')
                print(f'A palavra era {esportes_aleatorios}')
                break
        if len(tentativa) == 1:
            letras_tentadas.append(tentativa.lower())
        else:
            print('Só pode digitar uma letra!')
            continue
    elif menu == 4:
        letras_certas = [letra for letra in profissoes_aleatorias.lower() if letra in letras_tentadas]
        if letras_certas == list(profissoes_aleatorias.lower()):
            print(f'Parabéns você venceu! A palavra era {profissoes_aleatorias}')
            break
        for letra in profissoes_aleatorias:
            if letra.lower() in letras_tentadas:
                print(letra,end=' ')
            else:
                print('_',end = ' ')
        tentativa = input('Escolha uma letra pra advinhar: ')
        print(f'Letras tentadas:{letras_tentadas}')
        if tentativa.lower() not in profissoes_aleatorias.lower():
            vidas -= 1
            print(f'Vidas= {vidas}')
            if vidas == 0:
                print('BLEM BLEM BLEM')
                sleep(0.3)
                print('Você Perdeu!!!')
                print(f'A palavra era {profissoes_aleatorias}')
                break
        if len(tentativa) == 1:
            letras_tentadas.append(tentativa.lower())
        else:
            print('Só pode digitar uma letra!')
            continue
    elif menu == 5:
        letras_certas = [letra for letra in objetos_aleatorios.lower() if letra in letras_tentadas]
        if letras_certas == list(objetos_aleatorios.lower()):
            print(f'Parabéns você venceu! A palavra era {objetos_aleatorios}')
            break
        for letra in objetos_aleatorios:
            if letra.lower() in letras_tentadas:
                print(letra,end=' ')
            else:
                print('_',end = ' ')
        tentativa = input('Escolha uma letra pra advinhar: ')
        print(f'Letras tentadas:{letras_tentadas}')
        if tentativa.lower() not in objetos_aleatorios.lower():
            vidas -= 1
            print(f'Vidas = {vidas}')
            if vidas == 0:
                print('BLEM BLEM BLEM')
                sleep(0.3)
                print('Você Perdeu!!!')
                print(f'A palavra era {objetos_aleatorios}')
                break
        if len(tentativa) == 1:
            letras_tentadas.append(tentativa.lower())
        else:
            print('Só pode digitar uma letra!')
            continue
    elif menu == 0:
        print('Fechando o jogo...')
        sleep(0.4)
        print('Até a próxima!')
        break
    else:
        print('Número inválido! Tente outro')
        sleep(0.4)