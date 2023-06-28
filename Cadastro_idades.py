idade = contadorid = contadorsex = contadorF = 0
decisao = sexo = ''

while True:
    print('~~~~~~~~~~~~~~~~~~~')
    print('Cadastre uma pessoa')
    print('~~~~~~~~~~~~~~~~~~~')
    idade = int(input('Digite a idade: '))

    if idade >= 18:
        contadorid += 1

    sexo = str(input('Digite o Sexo[F/M]: ')).upper().strip()

    if sexo == 'M':
        contadorsex += 1

    elif sexo == 'F' and idade >= 20:
        contadorF += 1

    decisao = input('Quer continuar[S/N]: ').upper().strip()

    if decisao != 'S':
        break

print(f'Total de pessoas com mais de 18 anos :{contadorid} ')
print(f'ao todo foram {contadorsex} homens cadastrados')
print(f'Foram  cadastradas {contadorF} mulheres com 20 anos ou mais')

