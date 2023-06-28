pv = int(input('Digite o 1 valor: '))
sv = int(input('Digite o 2 valor: '))

continuar = True
decisao = 0

while decisao != 5:
    print('''
Menu:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] sair do programa
''')
    decisao = int(input('Escreva sua decisão: '))

    if decisao == 1:
        soma = pv + sv 
        print(f'A soma de {pv} + {sv} = {soma}')
        print('=-'*15)

    elif decisao == 2:
        mult = pv * sv 
        print(f'A multplicação de {pv} x {sv} = {mult}')
        print('=-'*15)

    elif decisao == 3:
        if pv > sv:
            print(f'{pv} É maior que {sv}')
            print('=-'*15)
        elif pv == sv:
            print(f'Os dois são iguais')
            print('=-'*15)
        else:
            print(f'{pv} é menor que {sv}')
            print('=-'*15)

    elif decisao == 4:
        pv = int(input('Digite um novo 1 valor: '))
        sv = int(input('Digite um novo 2 valor: '))

    elif decisao == 5:
        print('Obrigado por usar o nosso programa')
        continuar = False