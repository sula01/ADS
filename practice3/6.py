def binary(n):
    s = ''
    while n > 0:
        s = f'{n % 2}{s}'
        n //= 2
    return s

while True:
    n = int(input('enter num: '))
    if n != 0:
        print(binary(n))
    else:
        break