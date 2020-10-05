menor160 = maior180 = entre160e180 = 0

for calc in range(3):
    altura = float(input(f'Digite a altura da {calc + 1}º pessoa: '))

    if altura < 1.6:
        menor160 += 1
    elif altura > 1.8:
        maior180 += 1
    elif 1.6 <= altura <= 1.80:
        entre160e180 += 1

print("-----------------------------------------")
print(f'Menores a 1.60 foram {menor160}')
print(f'Maiores a 1.80 foram {maior180}')
print(f'Entre 1.60 e 1.80 foram {entre160e180}')
print("-----------------------------------------")
