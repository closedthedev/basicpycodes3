#praticando listas compostas 

família = [[], [], [], [], []]

for i in range(5):
    print('--' * 10, f'{i+1}ª PESSOA', '--' * 10)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    família[i].append(nome)
    família[i].append(idade)

print(família)