from random import randint
sort = (randint(0, 60) ,randint(0, 60) ,randint(0, 60),
        randint(0, 60), randint(0, 60))
print(f'Os números sorteados são: {sort}')
print(f'O maior número sorteado foi: {max(sort)}')
print(f'O menor número sorteado foi: {min(sort)}')

