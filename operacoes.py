operacao = str(input('Digite uma expressão: '))
pilha = list()

for sinb in operacao:
    if sinb == '(':
        pilha.append('(')
    elif sinb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
        break
if len(pilha) == 0:
    print('a expressao esta correta')
else:
    print('a expressão esta incorreta')
    print(pilha)