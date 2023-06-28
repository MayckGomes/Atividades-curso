decisao = 'S'
numero = contador = total = qtd = media = maior = menor = 0

while decisao in 'S':
    numero = int(input('Digite um numero: '))

    contador += 1
    
    total += numero

    if contador == 1:
        maior = numero
        menor = numero
    
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    decisao = str(input('Quer continuar?[S/N]: ')).upper()

media = total/contador

print(f'Você digitou {contador} numeros e a media deles são {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')