cont = 0
print('Numeros Primos')
primo = int(input('Digite o numero: '))

for c in range(1,primo+1):
    if primo %c == 0:
        cont += 1
        print(f'\33[32m' , end=' ')
    else:
        print(f'\33[31m' , end=' ')


print('\033[37m',end='')
print(f'\nO numero foi divisivel {cont} vezes')
if cont == 2:
    print('o numero é primo')
else:
    print('o numero NÃO é primo')