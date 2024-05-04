lista = []

qnt_números = int(input('Quantos números você quer adicionar na lista: '))

for c in range(0 , qnt_números):
    n = int(input('Digite um número: '))
    lista.append(n)

lista_decrescente = sorted(lista , reverse = True)
print(f'Você escolheu adicionar {qnt_números} números na lista, são eles: {lista}')

if 5 in lista:
    print('O número 5 está na lista.')
else: print('O número 5 não está na lista.')

print(f'A lista em ordem decrescente fica: {lista_decrescente}')