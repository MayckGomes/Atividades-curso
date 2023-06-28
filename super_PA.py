print('=-=-= Termos de um PA =-=-=')
primeiro = int(input('Digite o primero termo da Pa: '))
razao = int(input('Digite a razao: '))
contador = 0
total = primeiro
maximo = 10
qtd = 0

while maximo != 0:

    while contador < maximo:
        print(total, end=' -> ')

        total += razao
        contador += 1
        qtd += 1

        
    print('pausa')
    contador = 0
    maximo = int(input('quantos temos voce quer mais: '))


print(f'Você finalizou sua PA com {qtd} termos, Fim')