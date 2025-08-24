#Tabela dos times do brasileirão

print('-=-' * 20)

times = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Bragantino', 'Botafogo', 'Mirassol','São Paulo',
         'Fluminense', 'Ceará SC', 'Atlético MG', 'Internacional', 'Grêmio', 'Corinthians', 'Santos',
         'Vasco da Gama', 'EC Vitória', 'Juventude', 'Fortaleza', 'Sport Recife')
print(f'Lista dos time do brasileirão: {times}')

print('-=-' * 20)

print(f'Os 5 primeiros times são {times[0:5]}')

print('-=-' * 20)

print(f'Os 4 últimos times são {times[15:20]}')

print('-=-' * 20)

print(f'Os times em ordem alfabética é {sorted(times)}')

print('-=-' * 20)

print(f'O São Paulo está ná {times.index('São Paulo')+1} posição')

