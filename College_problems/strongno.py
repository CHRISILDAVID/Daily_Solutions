def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n-1)*n
def strong(n):
    s = 0
    a = n
    while a > 0:
        r = a % 10
        s += fact(r)
        a //= 10
    if s == n:
        return True
    else:
        return False

n = int(input())
if strong(n):
    print("True")
else:
    print("False")