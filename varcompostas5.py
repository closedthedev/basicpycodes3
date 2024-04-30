#praticando tuplas, dessa vez adicionando valores nela de acordo com a escolha do usuário

qnt_num = int(input('Quantos números você quer adicionar na tupla? '))



valores = tuple(int(input('Digite valores '))for c in range(1, qnt_num + 1))
print(f'Você escolheu digitar {qnt_num} números, e esses números são: {valores}. O maior valor entre eles é  o {max(valores)} e o menor é o {min(valores)}')