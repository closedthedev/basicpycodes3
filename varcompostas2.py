números =  "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"

while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num < 0 or num > 20:
        print('Eu pedi um número de 0 a 20, tente novamente!')
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {números[num]}!')
        break

