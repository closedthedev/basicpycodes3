#praticando tuplas 

qnt_comidas= int(input('Quantos pratos você quer comer hoje? '))

comidas = tuple(str(input('Diga o nome dos pratos que quer comer: '))for c in range(1, qnt_comidas + 1))

print(f'Hoje você pediu {qnt_comidas} pratos. São eles: {comidas}')