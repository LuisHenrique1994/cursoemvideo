# Tabela do brasileirão / tuplas com times de futebol

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Atlético-PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza',
         'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print('=-=' * 30)
print(f'Lista de times: {times}')
print('=-=' * 30)
print(f'Os 5 primeiros são {times[0:5]}')
print('=-=' * 30)
print(f'Os 4 ultimos são {times[-4:]}')
print('=-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-=' * 30)
print(f'O Corinthians está na {times.index("Corinthians")+1}ª posição.')
print('=-=' * 30)
