lista = []
par = []
impar = []
decisao = ''

while decisao != 'n':
    lista.append(int(input('Digite um valor: ')))
    decisao = str(input('Quer continuar?[s/n]: ')).lower()

for x in lista:
    if x %2 == 0:
        par.append(x)
    else:
        impar.append(x)
print('-='*25)
print(f'a lista completa é {lista}')
print(f'a lista de pares é {par}')
print(f'a lista de impares é {impar}')