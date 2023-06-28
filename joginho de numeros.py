from random import randint

acumulador = 0
continuar = True
pc = randint(0,11)
resposta = 0

while continuar == True:
    resposta = int(input('Chute um número:'))
    if resposta > pc:
        print('É menor')
        acumulador += 1
    elif resposta < pc:
        print('É maior')
        acumulador += 1
    elif resposta == pc:
        print(f'Você acertou, depois de {acumulador} vezes chutando')
        continuar = False