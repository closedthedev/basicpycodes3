#praticando listas compostas

lista1 = []
lista2 = []
lista3 = []

for i in range(3):
    n = int(input('Digite um valor: '))
    lista1.append(n)

for i in range(3):
    n = int(input('Digite um valor: '))
    lista2.append(n)

for i in range(3):
    n = int(input('Digite um valor: '))
    lista3.append(n)

print("Lista 1:", "[" + "] [".join(map(str, lista1)) + "]")
print("Lista 2:", "[" + "] [".join(map(str, lista2)) + "]")
print("Lista 3:", "[" + "] [".join(map(str, lista3)) + "]")

