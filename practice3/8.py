n = int(input('enter num: '))
even, odd = 0, 0
while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print(f'even - {even}, odd - {odd}')


# #varian 2
# n = input('enter num: ')
# even = odd = 0
# for i in n:
#     if i in {'0', '2', '4', '6', '8'}:
#         even += 1
#     else:
#         odd += 1

# print(f'even - {even}, odd - {odd}')