listagem = 'Alcatra' , 25.08 , 'Contra-Filé' , 34.77 , 'Picanha' , 38.55 , 'Costela' , 21.22
print('--'* 5 , 'PREÇO DO KG DAS CARNES', '--'*5)
for i in listagem:
    if type(i) is str: #se o tipo do item na tupla for string, ou seja, o nome do produto, vai colocar ele para a esquerda.
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}') #como os valores são float, vão ser adicionados na direita. 
print('--'*20)

print('ESCOLHA SUA CARNE DE PREFERÊNCIA')
print('[1] ALCATRA')
print('[2] CONTRA-FILÉ')
print('[3] PICANHA')
print('[4] COSTELA')

escolha_usuário = int(input('Digite qual carne você quer: '))

if escolha_usuário >= 1 and escolha_usuário <= 4:
    print(f'Você escolheu comprar 1KG de {listagem[escolha_usuário + 2 ]}')

else: print('Infelizmente, nós só temos essas carnes hoje.')