import random
from operator import itemgetter

jogadores = []

# Pedir os nomes dos jogadores e atribuir números aleatórios aos dados
for i in range(4):
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ')
    jogador['num_dado'] = random.randint(1, 6)
    jogadores.append(jogador)

# Classificar os jogadores com base no número tirado no dado (em ordem decrescente)
jogadores.sort(key=itemgetter('num_dado'), reverse=True)

print(jogadores)