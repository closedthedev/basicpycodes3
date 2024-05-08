#primeiro exercicio de funções, criando uma calculadora 

def soma(a , b):
    soma = a + b
    print(f'Você escolheu somar os números, a soma entre {a} e {b} é {soma}')

def subtração(a , b):
    subtração = a - b
    print(f'Você escolheu subtrair os números, a subtração entre {a} e {b} é {subtração}')

def multiplicação(a , b):
    multiplicação = a * b
    print(f'Você escolheu multiplicar os números, a multiplicação entre {a} e {b} é {multiplicação}')

def divisão(a , b):
    divisão = a / b
    print(f'Você escolheu dividir os números, a divisão entre {a} e {b} é {divisão}')


print('SEJA BEM-VINDO A CALCULADORA DO CLOSEDTHEDEV, PRIMEIRO DIGITE OS DOIS NÚMEROS QUE QUEIRA OPERAR E DEPOIS DIGITE O CÓDIGO REFERENTE A OPERAÇÃO DESEJADA!')

while True:

    print('[1] SOMA')
    print('[2] SUBTRAÇÃO')
    print('[3] MULTIPLICAÇÃO')
    print('[4] DIVISÃO')

    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    escolha_usuário = int(input('Digite o código referente a operação matemática que queira realizar: '))

    if escolha_usuário == 1:
        soma(a, b)

    if escolha_usuário == 2:
        subtração(a , b) 

    if escolha_usuário == 3:
        multiplicação(a , b)

    if escolha_usuário == 4:
        divisão(a , b) 

    continuar = int(input('Quer continuar com números diferentes e/ou operações diferentes? Digite 1 para fazer outra operação com os mesmos números, 2 para digitar outros números e 3 para sair. '))
    
    if continuar == 3:
            break
    if continuar == 1:

        print('[1] SOMA')
        print('[2] SUBTRAÇÃO')
        print('[3] MULTIPLICAÇÃO')
        print('[4] DIVISÃO')

        escolha_usuário = int(input('Digite o código referente a operação matemática que queira realizar: '))

        if escolha_usuário == 1:
            soma(a, b)

        if escolha_usuário == 2:
            subtração(a , b) 

        if escolha_usuário == 3:
            multiplicação(a , b)

        if escolha_usuário == 4:
            divisão(a , b)

        continuar = int(input('Quer continuar com números diferentes e/ou operações diferentes? Digite 1 para fazer outra operação com os mesmos números, 2 para digitar outros números e 3 para sair. '))

        if continuar == 3:
            break


