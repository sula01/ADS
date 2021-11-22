import random

num = random.randint(0,100)
print('отгадайте число от 0 до 100 за 10 попыток')
for i in range(1,11):
    answer = int(input(f'попытка {i}: '))
    if num < answer:
        print('число меньше')
    elif num > answer:
        print('число больше')
    else:
        print(f'вы угадали с {i}-й попытки')
        break
else: 
    print(f'поражение :( было загадно {num}')