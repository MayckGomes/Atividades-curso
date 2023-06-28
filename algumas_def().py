def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} equivale a {a:.2f}m²')
    

def escreva(txt):
    s = int(len(txt)+4)

    print('~'* s)
    print(f'  {txt}')
    print('~' * s)


def contagem(ini:int ,fim: int,pas: int):
    print('=-'* 25)
    if pas == 0:
            pas = 1
    elif pas <= -1:
        pas *= -1
    print(f'contagem de {ini} ate {fim} de {pas} em {pas}')
    cont = 0
    con = ini

    while True: 
        print(con,end=' ')
        
        if fim > ini:
            con += pas
        else:
            con -= pas
    

        cont += pas

        if con >= fim:
            break
    print()


def fatorial(num:int,show=False):
    """
    num -> numero no qual quer o fatorial
    show -> decisao se quer que apareça a conta ou não
    """
    f = 1
    contador = 0
    print('-'*25)
    print(f'o resultado do fatorial de {num} é: ',end='')
    
    for x in range(num,0,-1):
        f*=x
        contador += 1
        if show == True:
            print(f'{x} x 'if contador < num else '1 = ',end='')
    
    print(f'{f}',end='\n')


def ficha(nome='<desconhecido>',gols=0):
    print(f'o jogador {nome} fez {gols} gol(s)')

ficha()