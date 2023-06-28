time = []
jogador = {}
gols = []
des = ''
his =  0
while des != 'N':
    jogador['nome'] = str(input('Digite o nome do jogador: ')).title()
    partidas = int(input(f'Digite quantas partidas {jogador["nome"]} fez: '))
    
    for p in range(0, partidas):
        gols.append(int(input(f'Digite quantos gols {jogador["nome"]} fez na partida {p+1}: ')))
    
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    
    gols.clear()
    time.append(jogador.copy())

    des = str(input('quer continuar?[S/N]: ')).upper()

    while des not in 'SN':
        des = str(input('ERRO!, Apenas digite S ou N: '))
    
print('-='*30)
print(time)
print('cod nome        gols        total')
print('-----------------------------------')
for i,l in enumerate(time):
    print(f'{i:>3} {time[i]["nome"]:<10} {str(time[i]["gols"]):<8} {time[i]["total"]}')

while True:
    his = int(input('Digite o codigo do jogador que quer ver os gols(999 para parar): '))
    if his == 999:
        break
    else:
        print(f'os gols de {time[his]["nome"]} foram: ')
        for x,y in enumerate(time[his]['gols']):
            print(f' --> na {x} partida fez {y} gols')

print('   <<< PROGRAMA ENCERRADO >>>')