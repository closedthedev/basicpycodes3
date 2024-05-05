#primeiro uso de dicionário

filmes= [{'título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'} ,{'título': 'Vingadores', 'ano': 2012, 'diretor': 'Joss Whedon'} ,
         {'título': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]

print(filmes[0]['título'])
contador = 0

for t in filmes:
    print(f'O filme selecionado foi o: {filmes[contador]['título']}')
    contador += 1