#criando uma lista no python que o usuário vai adicionando número nela, mas ela nao aceita números repetidos.

lista_de_números = list()
números = 0
while True:
    n = int(input('Digite um número: '))
    if n not in lista_de_números:
        números += 1
        lista_de_números.append(n)
    r = str(input('Você quer continuar? S/N')) .strip() .upper()
    if r in 'N':
        break

print(f'Você adicionou {números} números na lista, sendo assim, a lista ficou desse jeito: {lista_de_números}')
lista_de_números.sort()
print(f'Essa lista, ordenada em ordem crescente fica: {lista_de_números}')