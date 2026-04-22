from datetime import datetime
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = datetime.now().year - nascimento
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((trabalhador['Contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
