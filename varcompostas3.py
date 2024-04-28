times_brasileirao = (
    "Flamengo", "Palmeiras", "Santos", "São Paulo", "Internacional",
    "Grêmio", "Atlético Mineiro", "Corinthians", "Fluminense", "Botafogo",
    "Vasco", "Bahia", "Athletico Paranaense", "Fortaleza", "Goiás",
    "Sport", "Ceará", "Bragantino", "Atlético Goianiense", "Coritiba"
)

primeiros5_colocados = times_brasileirao[0:4]
últimos4_colocados = times_brasileirao[-4:]
tabela_organizada = sorted(times_brasileirao)
pos_botafogo = times_brasileirao.index("Botafogo") + 1  # Adicionando 1 porque a indexação em Python começa em 0

# Removendo as aspas ao imprimir os nomes dos times
print(f'Os primeiros 5 colocados no campeonato brasileiro de futebol são: {" , ".join(primeiros5_colocados)}') 
print(f'Os 4 últimos colocados no campeonato brasileiro de futebol são: {" , ".join(últimos4_colocados)}')
print(f'A tabela com o nome dos times organizados fica assim: {" , ".join(tabela_organizada)}')
print(f'O time do Botafogo se encontra na {pos_botafogo}ª posicão.')