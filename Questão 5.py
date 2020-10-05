menor_q_160 = entre_160_e_180 = maior_q_180 = 0

for cont in range(3):
    altura = float(input('Digite sua altura: '))

    if altura < 1.60:
        menor_q_160 =+ 1

    elif 1.80 >= altura >= 1.60:
        entre_160_e_180 =+ 1

    else:
        maior_q_180 =+ 1

print("--------------------------------------------")
print("Menores que 1.60m:",menor_q_160)
print("Entre 1.60m e 1.80m:",entre_160_e_180)
print("Maiores que 1.80m:",maior_q_180)
print("--------------------------------------------")
