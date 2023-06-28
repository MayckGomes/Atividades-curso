times = ('cruzeiro', 'gremio', 'bahia', 'vasco', 'sampaio correia',
          'ituano', 'sport', 'criciuma', 'londrina', 'quarani',
          'crb', 'ponte preta', 'vila nova', 'chapecoense', 'tombense'
          , 'novohorizontino', 'csa', 'brusque', 'operario', 'nautico')

print(f'a tabela do ano de 2022 da Serie B é {times}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Os 5 primeiros times são: {times[0:5]}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Os 5 ultimos times são: {times[-4:]}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Em ordem alfabetica :{sorted(times)}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'A chapecoense esta na {times.index('chapecoense')+1}º posição')