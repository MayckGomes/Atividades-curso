lista = []
decisao = ''

while decisao != 'n':
    lista.append(int(input('Digite um valor: ')))
    decisao = str(input('quer continuar?[S/N]: ')).lower()

lista.sort(reverse=True)
print('^'*20)
print(f'Foram digitados {len(lista)} numeros na lista')
print(f'a lista em ordem decresente é {lista}')
if 5 in lista:
    print('tem o numero 5 na lista')
else:
    print('nao tem 5 na lista')


