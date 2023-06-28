matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]
num = [0,0]
c = 0
for lin in range(0,3):
    for col in range(0,3):

        c = int(input(f'Digite um numero para a posicão[{lin},{col}]: '))
        matriz[lin][col] = c

        if c %2 == 0:   
            num[0] += c
        elif col == 2:
            num[1] += c

print('-='*25)
print('matriz')

for lin in range(0,3):
    for col in range(0,3):

        print(f'[{matriz[lin][col]: ^5}]',end='')
    
    print()
print('=-'*25)
print(f'o valor de todos os pares foi: {num[0]}')
print(f'o valor da soma da coluna 3 é: {num[1]}')
print(f'o maior valor da 2 linha é: {max(matriz[1])}')