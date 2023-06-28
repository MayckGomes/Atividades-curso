palavras = ('programador', 'mayck','estudante', 'antony'
            , 'recepcionista', 'julliane', 'mecanico', 'alex')

vogais = 'a','e','i','o','u'
acumulador = ''

#meu jeito

#for nomes in palavras:
#    print(f'na palavra {nomes} tem as vogais ', end='')
#    for letras in vogais:
#        if letras in nomes:
#            acumulador = letras
#            print(acumulador, end='')
#    print('\n')

#jeito certo

for nomes in palavras:
    print(f'\nna palavra {nomes} tem as vogais ', end='')
    for letras in nomes:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')