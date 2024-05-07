time = []
código = total_gols =0
while True:
    jogador = {}

    jogador['nome'] = input('Nome do jogador: ').title()
    jogador['gols1'] = int(input('Gols na 1ª partida: '))
    jogador['gols2'] = int(input('Gols na 2ª partida: '))
    jogador['gols3'] = int(input('Gols na 3ª partida: '))

    total_gols = jogador['gols1'] + jogador['gols2'] + jogador['gols3']  

    print('COD        NOME        TOTAL DE GOLS')

    print(f'{código}          {jogador['nome']}         {total_gols} ')

    time.append(jogador)
    código += 1

    continuar = input('Quer continuar? S/N ').strip().upper()

    if continuar == 'N':
        break
    
cod1 = int(input(('Digite o código do jogador para ver quantos jogos ele fez em cada partida: ')))

print(f'Você escolheu o código {cod1}, que é referente ao jogador {time[cod1]["nome"]}. ')
print(f'{time[cod1]["nome"]} marcou {time[cod1]["gols1"]} gols na 1ª partida, {time[cod1]["gols2"]} gols na 2ª partida e {time[cod1]["gols3"]} gols na 3ª partida.  ')