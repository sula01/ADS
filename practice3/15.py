num = int(input('введите натуральное число. Ноль - выйти  '))
max_sum = 0
max_num = 0
while num != 0:
    temp_num = num
    temp_sum = 0
    while num > 0:
        temp_sum += num % 10
        num //= 10
            