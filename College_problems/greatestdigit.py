def bigdig(n):
    m = float("-inf")
    while n > 0:
        r = n % 10
        n = n // 10
        m = max(m, r)
    return m

n = int(input())
print(bigdig(n))