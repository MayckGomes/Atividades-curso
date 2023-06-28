#modulos
from random import randint
from time import sleep

#variaveis
continuar = True
decisao = ''
f = ''

#codigo
while True:
    print("-=-=-=-=-= PAR OU IMPAR -=-=-=-=-=")
    decisao = str(input('impar ou par?: ')).strip().upper()
    user = int(input('Digite seu palpite: '))
    print("")
    print('Processando...')
    print("")   
    pc = randint(1,6)
    sleep(0.5)
    resultado = user + pc

    if resultado %2 == 0:
        f = 'PAR'
    else:
        f = 'IMPAR'

    if decisao == 'PAR' and resultado %2 == 0 or decisao == 'IMPAR' and resultado %2 != 0:
        print(f'voce ganhou ,o pc jogou {pc} e voce jogou {user} e o resultado deu {f}')
    
    
    else:
        print(f'voce perdeu ,o pc jogou {pc} e voce jogou {user} e o resultado deu {f}')
        break   