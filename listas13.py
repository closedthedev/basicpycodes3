#praticando listas compostas

lista1 = []
lista2 = []
lista3 = []
pares = 0
ímpares = 0

for i in range(3):
    n = int(input('Digite um valor para a primeira linha: '))
    lista1.append(n)

    if n % 2 == 0:
        pares += n
    else:
        ímpares += n

for i in range(3):
    n = int(input('Digite um valor para a segunda linha: '))
    lista2.append(n)

    if n % 2 == 0:
        pares += n
    else:
        ímpares += n

    if i == 0 or n > maior_segunda_linha:
        maior_segunda_linha = n

for i in range(3):
    n = int(input('Digite um valor para a terceira linha: '))
    lista3.append(n)
    
    if n % 2 == 0:
        pares += n
    else:
        ímpares += n

soma_terceira_coluna = lista1[2] + lista2[2] + lista3[2]

print("Lista 1:", "[" + "] [".join(map(str, lista1)) + "]")
print("Lista 2:", "[" + "] [".join(map(str, lista2)) + "]")
print("Lista 3:", "[" + "] [".join(map(str, lista3)) + "]")

print(f'Entre todos esses números, a soma dos pares deu {pares} e dos ímpares deu {ímpares}')
print(f'A soma dos valores da terceira coluna deu: {soma_terceira_coluna} ')
print(f'O maior número da segunda linha é o: {maior_segunda_linha}')