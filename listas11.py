#praticando listas compostas 

qnt_numeros = int(input('Quantos números você quer digitar: '))

lista = []
lista_par = []
lista_impar = []

for _ in range(qnt_numeros):
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

lista_par.sort()
lista_impar.sort()

print(f'Você escolheu digitar {qnt_numeros} números, eles juntos em uma lista são: {lista}')
print(f'Entre esses números, os pares separados em ordem crescente são: {lista_par}')
print(f'E os ímpares, também em ordem crescente são: {lista_impar}')