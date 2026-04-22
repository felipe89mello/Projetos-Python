dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
print('-='*30)
print(f'Nome é igual a {dados["Nome"]}')
print(f'Média é igual a {dados["Média"]}')
if dados["Média"] >= 7:
    dados ['situação'] = 'Aprovado'
elif dados["Média"] >= 5:
    dados ['situação'] = 'Recuperação'
else:
    dados ['situação'] = 'Reprovado'
print(f'Situação igual a {dados["situação"]}')


