
qnt_valores = int(input('Quantos números você quer adicionar na tupla: '))
valores = tuple(int(input('Digite valores: ')) for c in range(0, qnt_valores))

print(f'Você escolheu digitar {qnt_valores} são eles: {" , ".join(map(str, valores))}')
print(f'O número 3 apareceu {valores.count(3)} vezes.')
print(f'O maior número armazenado é o: {max(valores)}')
print(f'O menor valor armazenado é o: {min(valores)}')

print('Os números pares digitados foram:', end='')
for num in valores:
    if num % 2 == 0:
        print(',', num, end=' ')
print('\nOs números ímpares digitados foram:', end='')
for num in valores:
    if num % 2 != 0:
        print(',', num, end=' ')