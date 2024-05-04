qnt_pessoas = int(input('Digite a quantidade de pessoas que tem na sua família: '))
familia = []

for i in range(qnt_pessoas):
    print('--' * 10, f'{i+1}ª PESSOA', '--' * 10)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    pessoa = [nome, idade]  # criando uma lista com os dados da pessoa, e jogando para a lista principal logo em seguida
    familia.append(pessoa)

print(familia)