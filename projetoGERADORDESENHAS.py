import random

letras_minusculas = 'abcdefghijklmnopqrstuvwyxzç'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWYXZÇ'
numeros = '0123456789'
caracteres_especiais = '@!#$%&?'
senha = ''

senha_aleatoria = input('Você quer uma senha aleatórias?(S ou N)').upper()
if senha_aleatoria == 'S':
        aleatorio = random.randint(1,4)
        if aleatorio == 1:
            for digito in range(2):
                aleatorio1 = random.choice(letras_maiusculas)
                senha += aleatorio1
            for digito in range(2):
                aleatorio1 = random.choice(letras_minusculas)
                senha += aleatorio1
            for digito in range(2):
                aleatorio2 = random.choice(numeros)
                senha += aleatorio2
            for digito in range(2):
                aleatorio3 = random.choice(caracteres_especiais)
                senha += aleatorio3
        elif aleatorio == 2:
            for digito in range(2):
                 aleatorio3 = random.choice(caracteres_especiais)
                 senha += aleatorio3
            for digito in range(2):
                 aleatorio2 = random.choice(numeros)
                 senha += aleatorio2
            for digito in range(2):
                 aleatorio1 = random.choice(letras_maiusculas)
                 senha += aleatorio1
            for digito in range(2):
                 aleatorio1 = random.choice(letras_minusculas)
                 senha += aleatorio1
        elif aleatorio == 3:
            for digito in range(2):
                 aleatorio2 = random.choice(numeros)
                 senha += aleatorio2
            for digito in range(2):
                 aleatorio1 = random.choice(letras_maiusculas)
                 senha += aleatorio1
            for digito in range(2):
                 aleatorio3 = random.choice(caracteres_especiais)
                 senha += aleatorio3
            for digito in range(2):
                 aleatorio1 = random.choice(letras_minusculas)
                 senha += aleatorio1
        else:
            for digito in range(2):
                  aleatorio1 = random.choice(letras_minusculas)
                  senha += aleatorio1
            for digito in range(2):
                  aleatorio3 = random.choice(caracteres_especiais)
                  senha += aleatorio3
            for digito in range(2):
                 aleatorio1 = random.choice(letras_maiusculas)
                 senha += aleatorio1
            for digito in range(2):
                 aleatorio2 = random.choice(numeros)
                 senha += aleatorio2 
        print(f'A sua senha aleatória é {senha}')
if senha_aleatoria == 'N':
     print('Até a próxima!!!!')
    