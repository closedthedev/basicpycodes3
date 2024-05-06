#praticando dicionários

pessoas = []
mulheres = []
idosos = []
qnt_pessoas = 0
idade = 0
while True:

    pessoa = {}

    pessoa['nome'] = input('Nome do pessoa: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo: M/F ')).strip() .upper()
    qnt_pessoas += 1 
    idade += pessoa['idade']
    pessoas.append(pessoa)

    continuar = str(input('Quer continuar? S/N ')).strip() .upper()
    if pessoa['idade'] >= 50:
        idosos.append(pessoa)

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa)

    if continuar == 'N':
        break
média_idade = idade / qnt_pessoas

print(f'Você forneceu o dado de {qnt_pessoas} pessoas, e a média de idade é de {média_idade}.')

if mulheres:
    nomes_mulheres = ", ".join([mulher['nome'] for mulher in mulheres])
    print(f'As mulheres cadastradas foram: {nomes_mulheres}')
else:
    print('Não há mulheres cadastradas.')