tupla = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),int(input('Digite um numero: ')))

contador = 0

print(f'Você digitou os numeros {tupla}')
print(f'o numero 9 apareceu {tupla.count(9)} vezes' if tupla.count(9) > 0 else 'o numero nove nao foi digitado')

if 3 in tupla:
    print(f'o 3 apareceu na posição {tupla.index(3)+1}'if tupla.index(3) > 0 else 'O 3 nao foi digitado')
else:
    print('O numero 3 nao foi digitado')

print(f'numeros pares digitados foi: ', end='')
for par in tupla:
    if par %2 == 0:
        contador = par
        print(f'{contador}', end=' ')
