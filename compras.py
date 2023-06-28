nome = decisao = nomebarato =''
valor = total = mais1k = barato = acumulador = contador = 0

print('=========================================')
print('             lista de compras            ')
print('=========================================')

while True:
    nome = str(input('Nome do produto: '))
    valor = int(input('Valor do produto: R$'))
    acumulador += valor
    contador += 1

    if valor > 1000:
        mais1k += 1
    
    elif contador == 1:
        barato = valor
        nomebarato = nome
    
    elif valor < barato:
        barato = valor
        nomebarato = nome


    decisao = str(input('Quer continuar?[S/N]: ')).strip().upper()
    
    if decisao != 'S':
        break

print('========= Nota Fiscal =========')
print(f'O total da compra foi {acumulador}')
print(f'Temos {mais1k} produtos valendo mais que R$1000')
print(f'O produto mais barato foi {nomebarato} que custa R${barato}')




