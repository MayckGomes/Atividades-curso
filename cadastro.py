idademv = 0 #idade do mais velho
nomeidade = ''
contador = 0
acumulador = 0

for x in range(1,5):
    print(f'=== {x}º pessoa ===')
    nome = str(input(f'Digite o nome da {x} pessoa: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo[F/M]: '))[0].upper().strip()

    acumulador += idade

    media = acumulador / 4
    
    if idade > idademv:
        idademv = idade
        nomeidade = nome
    elif idade < 20 and sexo == 'F':
        contador += 1

print(f'A media das idades é {media}')
print(f'O homem mais velho se chama {nomeidade} e ele tem {idademv} anos')
print(f'E tem {contador} mulheres mais velhas que 20 anos')