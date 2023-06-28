lista = []
numero = 0

#meu

for x in range(1,6):

    numero = int(input('Digite um numero: '))
    
    if len(lista) == 0:
        lista.append(numero)
        print('foi adicionado no final da lista')
    
    else:
        if numero < lista[0]:
            lista.insert(0,numero)
            print('o numero foi colocado na posicao 0')
        elif numero > lista[-1]:
            lista.append(numero)
            print('o numero foi colocado no final da lista')

        else:
            for i,v in enumerate(lista):
                if numero > lista[i] and numero < lista[i+1]:
                    lista.insert(i+1,numero)
                    print(f'valor colocado na posicao {i}') 

print('~'*25)
print(f'a lista ficou {lista}')

#resposta do video

# for c in range(0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#         print('Adicionado no final da lista')
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos,n)
#                 print(f'adicionado na posicao {pos}')
#                 break
#         pos += 1
# print('-='*20)
# print(f'os valores digitados foram {lista}')





