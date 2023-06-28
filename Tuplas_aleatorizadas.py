from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10) )

print(f'os numeros sortiados foram {numeros}')
print(f'o maior numero sortiado foi {max(numeros)}')
print(f'o menor numero sortiado foi {min(numeros)}')






#numeros = (0,1,2,3,4,5,6,7,8,9)
#maior = menor = aleatorio = 0
#for numero in range(0,5):
#    aleatorio = randint(0,9)
#    n = numeros[aleatorio]
#    print(n, end=' ')
#
#    if numero == 1:
#        menor = n
#        maior = n
#    else:
#        if n > maior:
#            maior = n
#        elif n < menor:
#            menor = n
#print()
#print(f'o maior valor foi: {maior} e o menor foi {menor}')
