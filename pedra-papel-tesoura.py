from random import randint
from time import sleep
continuar = True
while continuar == True:
    print('''Suas opções são:
[ 1 ]Pedra
[ 2 ]Papel
[ 3 ]Tesoura
''')
    decisao = int(input('Qual sua decisão?'))
    pc = randint(1,4)
    jogada = ''
    jogadapc = ''


    print('PEDRA')
    sleep(0.5)
    print('PAPEL')
    sleep(0.5)
    print('TESOURA')
    sleep(0.5)
    if pc == 1:
        jogadapc = 'pedra'
    elif pc == 2:
        jogadapc = 'papel'
    elif pc == 3:
        jogadapc = 'tesoura'

    if decisao == 1:
        jogada = 'pedra'
    elif decisao == 2:
        jogada = 'papel'
    elif decisao == 3:
        jogada = 'tesoura'

    print(f'Você jogou {jogada} e eu {jogadapc}')

    if decisao == 1 and pc == 3 or decisao == 2 and pc == 1 or decisao == 3 and pc == 2:
        print('você ganhou')
    elif decisao == pc:
        print('Empate')
    else:
        print('Você perdeu')