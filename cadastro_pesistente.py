sexo = str(input('Digite um sexo para o cadastro[M/F]: ')).upper().strip()

while sexo not in 'MF':
    sexo = str(input('Dados invalidos! Digite um sexo para o cadastro[M/F]: ')).upper().strip()
print('Dados coletados')