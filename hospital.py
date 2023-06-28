from Modulos.dado import *
from time import sleep
usu = 0
arq = 'pessoas.txt'

while True:
    menu(topicos=['Ver pessoas cadastradas','Cadastrar uma nova pessoa','sair do programa'])
    try:
        usu = int(input('digite sua opção: '))
    except ValueError:

        print(f'{cor(1)}ERRO!, é apenas aceito números{cor(0)}')
        usu = leiaint('digite sua opção: ')

    if usu == 1:
        menu(tipo=2,topicos=['Pessoas cadastradas'])
        lerArquivo('pessoas.txt','nome                    idade\n')
        
        sleep(1)

    elif usu == 2:
        menu(tipo=2,topicos=['Novo cadastro'])
        nome = str(input('Digite o nome: ')).title()
        idade = leiaint(f'Digite a idade de {nome}: ')
        escreverArquivo(arq,nome,idade)

        sleep(1)

    elif usu == 3:
        menu(tipo=2,topicos=['Encerrando o programa...'])
        sleep(1)
        break

    elif usu > 3 or usu < 1:
        print(f'{cor(1)}ERRO! opção invalida{cor(0)}')
        