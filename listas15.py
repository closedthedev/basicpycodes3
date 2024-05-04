qnt_alunos = int(input('Digite a quantidade de alunos que quer passas as notas do primeiro e segundo bimestre: '))
alunos = []
aprovado = reprovado = 0
código = 0
for i in range(qnt_alunos):
    print('--' * 10, f'{i+1}ª ALUNO', '--' * 10)
    nome = input('Nome: ') .upper()
    nota1 = float(input('Nota 1º bimestre: '))
    nota2 = float(input('Nota 2º bimestre: '))
    média = (nota1 + nota2) / 2
    aluno = [nome, nota1, nota2 , média]  
    alunos.append(aluno)

    print('CÓD       NOME       MÉDIA')
    print(f'{código}         {nome}       {média}')
    código += 1 

print('--' * 10, f'Qual aluno quer ver as notas? Digite o código dele!', '--' * 10)

while True:
    print('Digite o código do aluno para eu te mostrar as notas dele: ')
    cod = int(input('Código do aluno: '))
    print(f'NOME: {alunos[cod][0]} NOTA 1º BIMESTRE: {alunos[cod][1]}  NOTA 2º BIMESTRE: {alunos[cod][2]}')
    continuar = str(input('Quer continuar? S/N ')) .strip() .upper()

    if continuar == 'N':
        break

    
