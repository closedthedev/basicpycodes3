import random

tupla_numeros_aleatorios = tuple(random.sample(range(101), 5))  # Gerando 5 números aleatórios e convertendo em uma tupla


numeros_aleatorios_str = [str(numero) for numero in tupla_numeros_aleatorios] #convertendo os números inteiros em strings para poder usar join()


menor_valor = min(tupla_numeros_aleatorios)
maior_valor = max(tupla_numeros_aleatorios)


print(f'Os números sorteados foram: {' , '.join(numeros_aleatorios_str)}')
print(f'O menor número entre os sorteados foi o número: {menor_valor}')
print(f'O maior número entre os sorteados foi o número: {maior_valor}')