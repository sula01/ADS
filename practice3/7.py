while True:
    print('enter 0 if you want end program')
    s = input("enter (+, -, *, /, 0): ")
    if s == '0':
        break
    if s in {'+', '-', '*', '/'}:
        x = float(input("x = "))
        y = float(input("y = "))
        if s == '+':
            print(f'{x + y:.2f}')
        elif s == '-':
            print(f'{x - y:.2f}')
        elif s == '*':
            print(f'{x * y:.2f}')
        elif s == '/':
            if y != 0:
                print(f'{x / y:.2f}')
            else:
                print("delenie na 0!")
    else:
        print("error")