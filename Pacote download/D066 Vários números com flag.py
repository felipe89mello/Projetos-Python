n = s = c = 0
while True:
    n = int(input('Digite um número: [Digite 999 para parar] '))
    if n == 999:
        break
    c += 1
    s += n
print(f'No total foram digitados {c} e a soma entre eles foi {s}')