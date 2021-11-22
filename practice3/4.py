# variant 1
def gcd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b

a,b = map(int,input().split())
print(gcd(a,b))

# variant 2

def gcd2(a,b):
    if b == 0:
        return a
    return gcd2(b, a % b)

a,b = map(int,input().split())
print(gcd2(a,b))

# variant 3

def gcd3(a,b):
    while a != 0:
        a,b = b, a % b
    return a
    
a,b = map(int,input().split())
print(gcd3(a,b))