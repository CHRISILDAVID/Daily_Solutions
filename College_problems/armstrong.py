def isarmstrong(n):
    s = 0
    a = n
    while a > 0:
        r = a % 10
        s += r ** 3
        a //= 10
    if s == n:
        return True
    else:
        return False

n = int(input())
if isarmstrong(n):
    print("True")
else:
    print("False")