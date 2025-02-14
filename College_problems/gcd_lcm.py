def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    lcm = (x*y)//gcd(x,y)
    return lcm

x = 15
y = 20
print(gcd(x, y))
print(hcf(x, y))