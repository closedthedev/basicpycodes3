listagem = 'Lápis' , 1.04 , 'Borracha' , 1.25 , 'Estojo' , 3.95 , 'Caderno' , 7.99
print('--'* 5 , 'PRODUTOS ESCOLARES', '--'*5)
for i in listagem:
    if type(i) is str: #se o tipo do item na tupla for string, ou seja, o nome do produto, vai colocar ele para a esquerda.
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}') #como os valores são float, vão ser adicionados na direita. 
print('--'*20)