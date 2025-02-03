a = int(input())
b = int(input())
c = int(input())
def big(a, b, c):
    if a > b:
        if b > c:
            return a
        else:
            if c > a:
                return c
            else:
                return a
    else:
        if a > c:
            return b
        else:
            if c > b:
                return c
            else:
                return b
print(big(a, b, c))