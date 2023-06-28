lista = [int(input('Digite 1 valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais 1 valor: ')),
        int(input('Digite mais outro valor: ')),
        int(input('Digite o ultimo valor: '))]
maior = max(lista)
menor = min(lista)
print('=-=-=-=-=-=--=-=-==-=-=-=-=-=-===-')


print(f'o maior valor é o {max(lista)} que aparece na posicao : ', end='')

for maximo,num in enumerate(lista):
    if maior == num:
        print(maximo, end='... ')

print(f'\no menor valor é o {min(lista)} que aparece na posicao : ', end='')

for minimo,num in enumerate(lista):
    if menor == num:
        print(minimo, end='... ')

