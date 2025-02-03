"""
  *****
   ***
    *
   ***
  *****
"""
n = int(input())
i = n
s = 0
while i >= 1:
    print(" "*s + "*"*i)
    i -= 2
    s += 1
s -= 2
i += 4
while i <= n:
    print(" "*s + "*"*i)
    i += 2
    s -= 1