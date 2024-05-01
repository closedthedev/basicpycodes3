#praticando tuplas

carnes = 'Picanha' , 'Contra-Filé' , 'Costela' , 'Alcatra'

print('ESCOLHA SUA CARNE DE PREFERÊNCIA')
print('[1] PICANHA')
print('[2] CONTRA-FILÉ')
print('[3] COSTELA')
print('[4] ALCATRA')

escolha_usuário = int(input('Digite o número de acordo com a carne que você quer: '))

print(f'Você escolheu o corte {carnes[escolha_usuário - 1]} para comer hoje, tenha um bom apetite.')