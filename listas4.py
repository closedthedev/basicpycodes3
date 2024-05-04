#organizando uma lista sem usar o comando sort

lista = []
print('ADICIONE 4 NÚMEROS NA LISTA')
for c in range(0,4):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]: 
        lista.append(n)
        print('Adicionado no final da lista...')
    else: 
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos , n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1 

print(f'Os números digitados, na ordem crescente são: {lista}')
        