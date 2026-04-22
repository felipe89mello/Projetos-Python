sexo = str(input("Digite seu sexo? [M/F] ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("\33[31mDados inválidos.\33[m Por favor digite seu sexo? [M/F] ")).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

