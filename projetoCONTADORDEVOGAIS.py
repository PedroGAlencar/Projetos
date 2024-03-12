vogais = ['a','e','i','o','u']
num_vogais = 0

palavra = input('Digite uma palavra: ').lower()

for l in palavra:
    if l in vogais:
        num_vogais += 1
print(f'O número de vogais na palavra {palavra} é {num_vogais}')
