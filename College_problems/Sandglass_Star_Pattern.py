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
    for j in range(s):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    i -= 2
    s += 1
    print()
s -= 1
i += 2
while i <= n:
    for j in range(s):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    i += 2
    s -= 1
    print()