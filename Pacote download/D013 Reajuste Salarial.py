salario = float(input('Qual é o seu salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('O funcionário que ganhava R$ {:.2f}, vai passar a ganhar R$ {:.2f}'.format(salario, novo))
