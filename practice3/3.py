import sys

sys.setrecursionlimit(3000) #увеличиваем размер 

def akk(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))

m,n = map(int, input().split())
print(akk(m,n))