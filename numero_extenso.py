numeros = ('zero', 'um', 'dois', 'tres' , 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',  'dezenove', 'vinte')
decisao = ''

while True:
    usu = int(input('Digite o numero: '))
    
    if usu > 20 or usu <= -1:
        usu = int(input('Dados invalidos, digite o numero: '))

    print(f'o numero que voce digitou foi {numeros[usu]}')
    
    decisao = str(input('quer continuar?[s/n]: ')).upper()
    
    if decisao != 'S':
        break
print('Programa finalizado')
