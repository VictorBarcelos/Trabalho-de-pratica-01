nota1 = float(input('digite sua primeira nota:'))
nota2 = float(input('digite sua segunda nota:'))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

print('-+-'*10)
print('Média do aluno: ', media)
print('-+-'*10)