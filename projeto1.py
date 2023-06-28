#modulos
from Modulos.projeto1 import *
import time
import datetime

#variaveis
usu = 0
des = filename = item = quantidade = pegarlinha = ''
main = 'arquivos.txt'

#programa principal

while True:
    #verificar main

    arquivo = encontrarArquivo(main)
    if arquivo == False:
        criarArquivo(main,'Cod  Nome               Data\n')

    print('Carregando...')
    time.sleep(1)
    try:
        menu(topicos=['Nova lista','Carregar Lista','excluir lista','encerrar progama'])    
        usu = int(input('Digite a opção: '))
    
    except:
    
        print(f'{cor(1)}Erro!, é apenas aceito números{cor(0)}')
    
    else:
        if usu == 1:
            #nova lista
            while True:
                filename = input('Digite o nome da lista: ').strip()

                if '.txt' not in filename:
                        filename = filename + '.txt'
                    
                #verificar se existe outro arquivo com o mesmo nome para nao dar conflito
                procurar = encontrarArquivo(filename)
                if procurar:

                    print(f'{cor(1)}ja existe um arquivo com esse nome!{cor(0)}')
                    continue
                
                else:

                    escreverArquivo(main,f'{filename}',datetime.datetime.now())
                    criarArquivo(filename)
                    break

            while True:
                menu(1,f'Editando {filename}',['Colocar um novo item na lista','mostrar lista','fechar lista'])
                try:
                    usu = int(input('Digite sua opcão: '))
                except:
                    leiaint('Digite sua opcão: ')
                else:
                    #adicionar item na lista
                    if usu == 1:
                        while True:
                            item = input('Nome do item(fim para finalizar): ').title()
                            
                            if item in 'Fim':
                                break

                            quantidade = input('Digite a quantidade: ')

                            escreverArquivo(filename,item,quantidade)
                            print('=' * 15)

                    elif usu == 2:
                        #mostrar o arquivo de texto
                        menu(2,'Mostrando lista')
                        listmos = lerArquivo(filename)
                        print(listmos.read())
                        time.sleep(1.5)
                    
                    elif usu == 3:
                        #fechar edicao
                        break

                        
        elif usu == 2:                          
            menu(2,'Mostrando listas')
            txtmain = lerArquivo(main)#leu o arquivo

            for i,listas in enumerate(txtmain):
                print(f'{i} - {listas}'if i != 0 else listas)#mostrou a lista com o seu codigo
            
            txtmain = open(main)#o reabriu
            codigotxt = int(input('Digite o codigo da lista: '))#pegou o codigo da lista

            for ind,linha in enumerate(txtmain):
                if codigotxt == ind:
                    print(f'foi carregado a lista {linha.split()[0]}')#pegou o nome do arquivo da lista
                    filename = linha.split()[0]
                    lerArquivo(filename)# abriu o arquivo
                    time.sleep(0.5)
                    print('=' * 15)
            
            # mesmo codigo da segunda opção
            while True:
                titulo = filename
                titulo.replace('.',' ')

                menu(1,f'Editando {titulo.split()[0]}',['Colocar um novo item na lista','mostrar lista','fechar lista'])
                try:
                    usu = int(input('Digite sua opcão: '))
                except:
                    print(f'{cor(1)}Erro!, é apenas aceito números{cor(0)}')
                    continue
                else:
                    if usu == 1:
                        while True:
                            item = input('Digite o nome do item("fim" para finalizar): ').title().strip()
                            
                            if item in 'Fim':
                                break
                            else:
                                quantidade = input('Digite a quantidade: ')

                                escreverArquivo(filename,item,quantidade)
                                print('=' * 15)
                            
                    elif usu == 2:
                        menu(2,'Mostrando lista')
                        listmos = lerArquivo(filename)
                        print(listmos.read())
                        time.sleep(1.5)
                    
                    elif usu == 3:
                        break
        

        elif usu == 3:
            menu('em ') 
            # txtmain = lerArquivo(main)#leu o arquivo

            # for i,listas in enumerate(txtmain):
            #     print(f'{i} - {listas}'if i != 0 else listas)#mostrou a lista com o seu codigo
            
            # txtmain = open(main)#o reabriu
            # codigotxt = int(input('Digite o codigo da lista: '))#pegou o codigo da lista

            # for ind,linha in enumerate(txtmain):
            #     if codigotxt == ind:
            #         print(f'foi carregado a lista {linha.split()[0]}')#pegou o nome do arquivo da lista
            #         filename = linha.split()[0]
            #         linha.pop(ind)
                    
            # print(f'O arquivo {filename} foi excluido com sucesso!')# e o excluiu
            # excluirArquivo(filename)
            # time.sleep(0.5)


        elif usu == 4:
            menu(2,'encerrado o programa...')
            break


        elif usu > 4 or usu <= 0:
            print(f'{cor(1)}indice invalido{cor(0)}')


