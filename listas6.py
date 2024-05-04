lista_completa = []
lista_pares = []
lista_ímpares = []
números = 0
while True:
    n = int(input('Digite um número: '))
    lista_completa.append(n) 
    números += 1

    if n % 2 == 0:
        lista_pares.append(n)

    else: 
        lista_ímpares.append(n)

    resposta = str(input('Quer continuar? S/N ')) .strip() .upper()
    if resposta == 'N':
        break

print(f'Você escolheu digitar {números} números, são eles: {lista_completa}')
print(f'Os números pares foram divididos em uma lista, são eles: {lista_pares}')
print(f'Os números ímpares foram divididos em uma lista, são eles: {lista_ímpares}')
    
    