n = contador = 0
print('Super tabuada')
while True:
    n = int(input('Digite um numero para ver a tabuada: '))
    if n < 0:
        break
    for x in range(1, 11):
        print(f'{n} x {x} = {n*x}')
print('Programa finalizado')