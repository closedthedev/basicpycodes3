def mostraLinha(titulo):
    print('-'*40)
    print(' '*2,titulo)
    print()

def contagem():
    mostraLinha('Contagem de 1 a 10, de 1 em 1:')
    for n in range(1, 11):
        print(n, ' ', end='')
    
    print()  
    
    mostraLinha('Contagem de 1 a 10, de 2 em 2:')
    for n in range(1, 11, 2):
        print(n, ' ', end='')
    
    print()  
    print()
    mostraLinha('Contagem personalizada:')
    inicio = int(input('Digite o número inicial: '))
    final = int(input('Digite o número final: '))
    passo = int(input('Digite o passo: '))
    
    print()  
  
    for n in range(inicio, final + 1, passo):
        print(n, ' ', end='')
        
    print('\n', '-'*40)

contagem()

