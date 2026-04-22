while True:
    t = int(input('Quer ver a tabuada de qual valor?  '))
    print('-' *12)
    if t < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(t,c ,t*c))
print('-' *12)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')