import random
import time

qnt_jogos = int(input('Quantos jogos da mega-sena você quer que eu sorteie?  '))
jogos = []
intervalo = 0.5


for i in range(qnt_jogos):
    print('--' * 10, f'{i+1}ª jogo', '--' * 10)

    números = random.sample(range(1, 61), 6)

    print (números)

    jogo = [números]  
    jogos.append(jogo)
    
    time.sleep(intervalo)
