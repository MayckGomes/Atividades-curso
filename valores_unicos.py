num = []
decisao = ''
numero = 0
while decisao != 'n':
    numero = int(input('Digite um numero: '))
    if numero in num:
        print('valor duplicado, nao sera adicionado')
    else:
        num.append(numero)
        print('numero coletado com sucesso')
    num.sort()

    decisao = str(input('Quer continuar?[S/N]: ')).lower()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'você digitou os valores: {num}')