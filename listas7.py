#praticando listas, dessa vez verificando se uma expressão matemática está correta, de acordo com as vezes que o parenteses abriu e fechou

expr = str(input('Digite uma expressão matemática: '))

pilha = []

for símb in expr: #fazendo um for para verificar a expressão do começo ao fim

    if símb == '(':
        pilha.append('(') #quando aparecer a primeira '(' , será adicionada na lista pilha

    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop() # quando aparecer o ')' , se na lista já estiver um ( esperando ele, eles serão 'excluídos'

        else:
            pilha.append(')') #caso nao tenha nenhum ( aguardando o ) para fechar, o ) será adicionado, deixando a lista com valor diferente de zero, o que nos faz descobrir se a expressão está certa ou não.
            break
            
if len(pilha) == 0: # se o comprimento da pilha for 0, nao tiver nenhum valor significa que a expressão está correta, pois sempre que uma parenteses abria e fechava, ela era 'excluida da lista'
        print('A expressão está correta!')
else:
        print(f'A expressão está incorreta')