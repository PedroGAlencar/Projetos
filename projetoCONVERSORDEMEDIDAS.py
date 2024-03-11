def conversor_km_pra_milhas():
    km = int(input('Digite a distância em km: '))
    milhas = km / 1.6
    print(f'A distância em milhas é {milhas}')


def conversor_celsius_pra_fahrenheit():
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = celsius * 1.8 + 32
    print(f'A temperatura em Fahrenheit é {fahrenheit}')


def conversor_fahrenheit_pra_celsius():
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = (fahrenheit - 32) / 1.8
    print(f'A temperatura em Celsius é {celsius}')


def conversor_milhas_pra_km():
    milhas = int(input('Digite em milhasa distância: '))
    km = milhas * 1.6
    print(f'A distância em Km é {km}')


def conversor_ms_pra_kmh():
    ms = float(input('Digite a velocidade em m/s: '))
    kmh = ms * 3.6
    print(f'A velocidade em km/h é {kmh:.2f}')


def conversor_kmh_pra_ms():
    kmh = float(input('Digite a velocidade em km/h: '))
    ms = kmh / 3.6
    print(f'A velocidade em m/s é {ms:.2f}')


menu = int(input('''Digite a opção desejada:
                 (1)Celsius --> Fahrenheit
                 (2)Fahrenheit --> Celsius
                 (3)Km --> Milhas
                 (4)Milhas --> Km
                 (5)M/S --> KM/H
                 (6)KM/H --> M/S
                 :'''))

if menu == 1:
    conversor_celsius_pra_fahrenheit()
elif menu == 2:
    conversor_fahrenheit_pra_celsius()
elif menu == 3:
    conversor_km_pra_milhas()
elif menu == 4:
    conversor_milhas_pra_km()
elif menu == 5:
    conversor_ms_pra_kmh()
else:
    conversor_kmh_pra_ms()