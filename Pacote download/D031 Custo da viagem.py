from time import sleep
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de {}Km.'.format(distância))
sleep(2)
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem é de R${:.2f}.'.format(preço))
