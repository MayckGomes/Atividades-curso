pessoas = list()
dados = list()
maxpeso = minpeso = 0
decisao = ''

while decisao != 'N':
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    decisao = str(input('Quer continuar?[S/N]: ')).upper()

print('=-'*30)
print(f'ao todo temos {len(pessoas)} pessoas cadastradas')

for dado in pessoas:
    peso = dado[1]
    if maxpeso == 0 and minpeso == 0:
        maxpeso = peso
        minpeso = peso
    else:
        if peso > maxpeso:
            maxpeso = peso
        elif peso < maxpeso:
            minpeso = peso

print(f'o maior peso foi de {maxpeso}kg, peso de ',end='')

for nomemax in pessoas:
    if maxpeso == nomemax[1]:
        print(f'[{nomemax[0]}]',end='')

print(f'\no menor peso foi de {minpeso}kg, peso de ',end='')

for nomemin in pessoas:
    if minpeso == nomemin[1]:
        print(f'[{nomemin[0]}]', end='')