def CalculaArea(largura, comprimento):
    área = largura * comprimento
    print(f'A área do terreno é de {área}m²')


larguraUsuário = float(input('Digite a largura do terreno: '))
comprimentoUsuário = float(input('Digite o comprimento do terreno: '))
CalculaArea(larguraUsuário, comprimentoUsuário)