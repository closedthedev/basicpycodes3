qnt_valores = int(input('Quantos valores você deseja adicionar na tupla: '))

valores = tuple(int(input('Digite valores: ')) for c in range(0, qnt_valores))

print(f'Você digitou os números: {" , ".join(map(str, valores))}')
print(f'Você digitou o número 9 {valores.count(9)} vezes')

if 3 in valores:
    print(f'O número 3 apareceu pela primeira vez na {valores.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição!')

print('Os números pares digitados foram:', end='')
for num in valores:
    if num % 2 == 0:
        print(',', num, end=' ')