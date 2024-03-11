import random

num_tirados= list()

def dados(num):
    for dados in range(num):
        dados = random.randint(1,6)
        num_tirados.append(dados)
    print(f'O total de dados foi {num} e os números tirados foram {num_tirados}', end = ' ')


num_dados = int(input('Digite a quantidade de dados jogados: '))

dados(num_dados)
