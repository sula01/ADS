#v1 
num = int(input('введите количество чисел: '))
digit = int(input('какую цифру подсчитать: '))
count = 0
for i in range(1,num + 1):
    m = int(input(f'введите число {i}: '))
    while m > 0:
        if m % 10 == digit:
            count += 1
        m = m // 10
        
print(f'было введено {count} цифр {digit}')

#v2
num = int(input("введите количество чисел: "))
digit = input('какую цифру подсчитать: ')
count = 0
for i in range(1, num + 1):
    ans = input(f'введите число {i}: ')
    count += ans.count(digit)
    
print(f'было введенол {count} цифр {digit}')