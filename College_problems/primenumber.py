import math
def isprime(n):
    i = 2
    while i < math.sqrt(n): # only iterate till sqrt(n)
        if n % i == 0: # check for factors
            return False
            break
        i += 1
    else:
        return True