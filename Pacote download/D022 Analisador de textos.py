nc = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nc.upper()))
print('Seu nome em minúscula é {}'.format(nc.lower()))
print('Seu nome tem um total de {} letras'.format(len(nc) - nc.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nc.find(' ')))



