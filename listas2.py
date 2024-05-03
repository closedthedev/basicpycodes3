qnt_números = int(input('Quantos números terão nessa lista? '))

números = []

for i in range(0 , qnt_números):
    n = int(input(f'Digite o {i + 1}ª número:'))
    números.append(n)

maior_num = max(números)
menor_num = min(números)
pos_maior = números.index(maior_num)
pos_menor = números.index(menor_num)

print(f'Você escolheu digitar {qnt_números} números, são eles : {números} ')
print(f'Entre eles, o maior número é o {maior_num} que aparece na posição {pos_maior}')
print(f'Já o menor número, é o {menor_num} que aparece na posição {pos_menor}')