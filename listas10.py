#praticando listas compostas 


qnt_pessoas = int(input('Quantas pessoas você quer analisar? '))

lista = []
pessoas_pesadas = []
pessoas_leves = []

for i in range(qnt_pessoas):
    print('--' * 10, f'{i+1}ª PESSOA', '--' * 10)
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoa = [nome, peso]  # criando uma lista com os dados da pessoa, e jogando para a lista principal logo em seguida
    lista.append(pessoa)
    
    if peso >= 100:
        pessoas_pesadas.append(pessoa)

    else: 
       pessoas_leves.append(pessoa)

print(f'Você nos passou o dado de {qnt_pessoas} pessoas. São essas as pessoas, nome e peso respectivamente: {lista}')
print(f'Entre essas pessoas, as que tem 100kg ou mais são: {pessoas_pesadas}')
print(f'E as que têm menos de 100kg são: {pessoas_leves}')
       

   
    

