#praticando dicionários

alunos = []

while True:
    aluno = {}

    aluno['nome'] = input('Nome do aluno: ')
    aluno['média'] = float(input('Média: '))
    
    if aluno['média'] < 6:
        aluno['situação'] = 'REPROVADO'
    else:
        aluno['situação'] = 'APROVADO'

    alunos.append(aluno)

    continuar = input('Quer continuar? S/N ').strip().upper()
    
    if continuar != 'S':
        break

for aluno in alunos:
    print(aluno)
