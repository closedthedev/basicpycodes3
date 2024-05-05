import datetime

pessoa = {}
pessoa_idade = 0
ano_atual = ano_atual = datetime.date.today().year
while True:
    pessoa['NOME'] = str(input('NOME: ')) .strip() .upper()
    pessoa_idade = int(input('ANO DE NASCIMENTO: '))
    pessoa['CTPS'] = int(input('CTPS: '))
    pessoa['IDADE'] = abs(pessoa_idade - ano_atual)
    print(pessoa['IDADE'])

    if pessoa['CTPS'] != 0:
        pessoa['SALÁRIO'] = float(input('SALÁRIO: '))
        pessoa['CONTRATAÇÃ0'] = int(input('ANO DA CONTRATAÇÃO: '))
        pessoa['APOSENTADORIA'] =  pessoa['CONTRATAÇÃ0'] + 30
        print(pessoa)
        break
    else:
        print('Você ainda não trabalha, então só irá se aposentar 30 anos após a primeira contratação!')
        break