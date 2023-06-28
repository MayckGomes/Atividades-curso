ps = int(input('Digite o primeiro segmento: '))
ss = int(input('Digite o segundo segmento: '))
ts = int(input('Digite o terceiro segmento: '))

tipo = ''

if ps < ss + ts or ss < ps + ts or ts < ps + ss:
    if ps == ss == ts:
        tipo = "EQUILATERO"
    elif ps == ss or ps == ts or ss == ts:
        tipo = "ISOCELES"
    elif ps != ss != ts:
        tipo = 'ESCALENO'
    print(f'esse triangulo é possivel e ele é {tipo}')
else:
    print('esse triangulo nao é possivel')