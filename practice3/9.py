#v1
n = int(input('enter num: '))
result = 0
while n > 0:
    result = result * 10 + n % 10
    n = n // 10
print(result)

#v2 
n = input('enter num: ')
result = ''
for i in n:
    result = i + result
print(result)

#v3 
n = input('enter num: ')
result = n[::-1]
print(result)