from random import randint
from time import sleep
cartela = []
jogos = []
print('---------------------------')
print('     JOGA NA MEGA-SENA     ')
print('---------------------------')
total = 1
quant = int(input('Quantos jogos voce quer que eu sorteie?: '))

for c in range(1, quant+1):
    for numeros in range(0,6):
        num = randint(0,61)

        while num in cartela:
            num = randint(0,60)
        
        cartela.append(num)
    cartela.sort()
    jogos.append(cartela[:])
    cartela.clear()

print('MOSTRANDO RESULTADOS')

for i,l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(0.6)

print('BOA SORTE')
