numero = int(input('Digite o numero para calcular o fatorial: '))
numeros = numero
total = 1

while numeros > 0:
    print(numeros, end=' ')
    print('x' if numeros > 1  else '=', end=' ')
    total *= numeros
    numeros -= 1
print(total)