jogador = {}
jogador['nome'] = input('NOME: ').strip().upper()
jogador['gols'] = []
jogador['total_gols'] = 0  

for i in range(5):
    gols_partida = int(input(f'QUANTIDADE DE GOLS NA {i + 1}ª partida: '))
    jogador['total_gols'] += gols_partida  # Adicionando gols da partida ao total
    jogador['gols'].append(gols_partida)

print(jogador)