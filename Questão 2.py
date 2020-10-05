vitoria=int(input('Vitórias:'))
empate=int(input('Empates:'))
derrotas=int(input("Derrotas:"))
pontos_totais=vitoria*3+empate
n_de_jogos=vitoria+empate+derrotas
print('Quantidade de Jogos:',n_de_jogos)
print('Pontos Obtidos:',pontos_totais)