import math
def isprime(n):
    i = 2
    while i < math.sqrt(n):
        if n % i == 0:
            return False
            break
        i += 1
    else:
        return True